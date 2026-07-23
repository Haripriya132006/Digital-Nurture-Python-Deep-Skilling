## Three problems waterfall project development can cause to the Course Management API project

* Late defect discovery - the critical bus can be founs only during the end of the project leading to a loss of both time and money 

* Compressed QA cycles - if development gets delayed then testing time is reduced to fit deadline leading to missed test cases and untested endpoints in the final product

* Misalignment on Requirements - if there aint no continuous QA input for the teveopers they might build the app based on their understanding but not fit to the requirements given by the stackeholder

## Role of QA Engineer
### Sprint Planning
collaborate with developers and managers and clarify user stories, define clear, testable acceptance criteria giving idea on what is the key of the project

### Daily Standup
shares testing process, reports critical bugs and highlights blacking issues to achieve the sprint goals 

### Sprint review
participate in the demo testing along stakeholders and validating the newly built user stories meet the functional expectations before shipping to production 

### Retrospective
Drives process improvements by evaluating QA bottlenecks from the sprint, suggests automation enhancements and prevents reccuring bugs 

## Shift left practices
### a. reviewing requirements for testability 
QA reviews user stories before development starts to ensure API specs are unambiguous - verifying mandatory fields - status codes - error messages 

### b. writing test cases before code 
QA/developers weire scenarios of failing unit/integration tests bedire writing production code to ensure correct implementation that satisfies the requirements 

### c. Static code analysis
Autimatic linters and security scanners run directly in CI piplined to catch dead code , errors and security flaws before QA execution 

### d.API contract testing before integration 
tools like Pact verify API schemas upfront allowung frontend and backend teams to develop independently without breaking changes 

## Acceptance critereia for followin stiry in Gherkin format
### As a college admin,I want to create a new course, so that students can enroll in it
#### Scenario 1 - successfull (Happy path)
* admin logged in with valid administrator credentials
* course with code "CS101" doesnt exist in the system already 
* if given the request to create a course with  course code "CS101" name "Data structures" and credits 5 then the systen should successfully create the course
* then return a 201 Created with the new course details 
 
#### Scenario-2 - duplicate course code
* given a course "CS101" already exists in the system
* when the admin submits a request to create a new course with the code "CS101"
* then the system should reject the request 
* then return a 409 conflict with an error message "Course with the course code CS101 already exists"

#### Scenario-3 - Missed Required fields
* given the college admin is on the course creation payload form 
* when the admin submits a request to create a course without providing the required "course name" field 
* then the system should reject the request 
* and return an HTTP statuc code 400 bad request with validation error details for missing fields
(example - course name is missing)

