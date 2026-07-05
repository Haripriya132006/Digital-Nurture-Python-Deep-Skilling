# Bounded Contexts Decomposition

| Service Name | Responsibility | Endpoints it owns | Database it owns |
| :--- | :--- | :--- | :--- |
| **Auth Service** | Handles user registration, credentials verification, and token issuing. | `POST /api/v1/auth/register/`<br>`POST /api/v1/auth/login/` | `auth.db` |
| **Course Service** | Manages departments and course metadata creation, updates, and listings. | `POST /api/v1/courses/`<br>`GET /api/v1/courses/`<br>`GET /api/v1/courses/{id}`<br>`PATCH /api/v1/courses/{id}`<br>`PUT /api/v1/courses/{id}`<br>`DELETE /api/v1/courses/{id}` | `courses.db` |
| **Student Service**| Manages student profiles and handles course catalog enrollment registrations. | `POST /api/v1/students/`<br>`DELETE /api/v1/students/{id}`<br>`POST /api/v1/enrollments` | `students.db` |
| **Notification Service** | Asynchronously dispatches transactional confirmation emails. | Worker consumed (triggered by events/hooks) | No database (Stateless) |

![alt text](<Screenshot 2026-07-05 222305.png>)
![alt text](<Screenshot 2026-07-05 222413.png>)
![alt text](<Screenshot 2026-07-05 223045.png>)

# How to run
```
uvicorn app:app --port 5001
uvicorn app:app --port 5002
```