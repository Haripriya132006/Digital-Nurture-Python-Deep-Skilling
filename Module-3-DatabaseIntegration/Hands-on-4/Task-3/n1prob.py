import time
import mysql.connector

# pip install mysql-connector-python
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'vanihari123',
    'database': 'college_db',
    'use_pure':True,
    'connection_timeout': 5  # Prevents hanging forever
}

def run():
    print("Trying to connect to MySQL...", flush=True)
    
    try:
        conn = mysql.connector.connect(**db_config)
        print("Connected successfully!", flush=True)
    except mysql.connector.Error as err:
        print(f"\n❌ COULD NOT CONNECT TO MYSQL: {err}")
        print("--> Check if your MySQL Service/XAMPP is actually started.")
        return

    cursor = conn.cursor(dictionary=True)

    # ---------------------------------------------------------
    # Approach 1: The N+1 Problem (Query inside loop)
    # ---------------------------------------------------------
    start_time = time.perf_counter()
    query_count = 0

    cursor.execute("SELECT * FROM enrollments")
    enrollments = cursor.fetchall()
    query_count += 1

    n1_results = []

    for enrollment in enrollments:
        student_id = enrollment['student_id']
        cursor.execute("SELECT first_name, last_name FROM students WHERE student_id = %s", (student_id,))
        student = cursor.fetchone()
        query_count += 1
        n1_results.append({
            'enrollment_id': enrollment.get('enrollment_id'),
            'student_name': f"{student['first_name']} {student['last_name']}" if student else "Unknown",
            'course_id': enrollment['course_id']
        })

    end_time = time.perf_counter()
    time_taken = end_time - start_time

    print(f"\nV1 (N+1) - Total queries: {query_count} | Time: {time_taken:.4f}s")

    # ---------------------------------------------------------
    # Approach 2: Optimized SQL JOIN (Out of loop)
    # ---------------------------------------------------------
    start_time_join = time.perf_counter()
    query_count_join = 0

    join_query = """
        SELECT e.student_id, e.course_id,
               CONCAT(s.first_name, ' ', s.last_name) AS student_name
        FROM enrollments e
        JOIN students s ON e.student_id = s.student_id
    """

    cursor.execute(join_query)
    join_results = cursor.fetchall()
    query_count_join += 1

    end_time_join = time.perf_counter()
    time_taken_join = end_time_join - start_time_join

    print(f"V2 (JOIN) - Total queries: {query_count_join} | Time: {time_taken_join:.4f}s")

    # Summary
    print("-" * 40)
    print("Queries saved:", (query_count - query_count_join))
    print("Time saved:", f"{(time_taken - time_taken_join):.4f} seconds")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    run()