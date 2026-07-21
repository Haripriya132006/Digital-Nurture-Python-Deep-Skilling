## 1. Concrete Test cases Across Testing Levels

### Unit Test
* Test the CourseService.enrollCourses() method in isolationusing mock dependencies.
* Ensure if the Enrolled courses are not enrolled again

### Integration Testing
* Test the working of how the course service with the database
* sending a valid request through `/api/courses` and checking if the course got added in the courses table then seeing the response code to be 201 created

### System Testing
* Test the complete end to end flow by sending request theough API gateway
* send a `POST /api/courses/` request with valid request and fetch the courses with the `GET /api/courses`
then update it with `PUT /api/courses/{id}` and verify the results in all parts of the process

### User Acceptance Testing
* Evaluate the whole workflow from the perspective of an admin
* login to the portal , visit the current courses , add courses , update existing courses See if all the actions are done smoothly

## 2.Functional tesing VS Non functional testing

### Functional testing: 
Focus on what the system does - features,funtions, working, rules, responses 
### Non functional testing:
* focus on how well the system perfoms - speed, security, scalability
* testing if the API can handle 100 or 200 simultaneious requests and provide fast response for  most of it without throwing 502 error 

## 3. Black box vs white box testing

### Black box testing :
Testing the functions and woring of the application witthout knowing how to code was made .. they are done by QA testers 

### White box testing :
Testing the internal architectures and code after building it .. it is done by the developers and it is done befor black box testing 

## 4.Formal test cases for `Post /api/courses`

### Testcase -1\

* create a course with valid data
```
payload in json format :

{"title": "database management", "credits": 3, "code": "CS101"}
```

```
expected:
          status code:
                    201 Created
          message:
                    course created successfully
```

* missing fields
```
payload in json format:

{"credits": 3, "code": "IT101"}```
```

```
expected:
          status code:
                    400 Bad Request
          message:
                    missing title
```

* duplicate course code
```
payload in json format:

{"title": "Python", "credits": 4, "code": "CS101"}
```

```
expected:
          status code:
                    409 conflict / 400 bad request
          message:
                    course code must be unique
```
* table format

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC_POST_01** | Create a course with valid data | Admin user is authenticated; API service and DB are running. | 1. Send `POST /api/courses`<br>Payload: `{"title": "Database Management", "credits": 3, "code": "CS101"}`<br>2. Verify response status and payload. | **Status:** `201 Created`<br>**Message:** `Course created successfully` | | |
| **TC_POST_02** | Attempt to create a course with missing required fields | Admin user is authenticated. | 1. Send `POST /api/courses`<br>Payload: `{"credits": 3, "code": "IT101"}` *(missing title)*<br>2. Verify response status. | **Status:** `400 Bad Request`<br>**Message:** `Missing title` | | |
| **TC_POST_03** | Attempt to create a course with a duplicate course code | A course with code `"CS101"` already exists in the database. | 1. Send `POST /api/courses`<br>Payload: `{"title": "Python", "credits": 4, "code": "CS101"}`<br>2. Verify response status. | **Status:** `409 Conflict` (or `400 Bad Request`) <br>**Message:** `Course code must be unique` | | |