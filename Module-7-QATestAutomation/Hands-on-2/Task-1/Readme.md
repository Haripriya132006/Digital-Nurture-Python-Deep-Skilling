## V model diagram
Requirement Analysis ----------------> Acceptance Testing
    \                                          /
     System Design -------------------> System Testing
        \                                     /
        Architecture diagram -------> Integration Testing
           \                                 /
          Module design --------------> Unit testing
                \                          /
                 ----------Coding----------

## SDLC - TDLC mapping
Requirement analysis ---------------- Acceptance Testing ---------------- User Acceptance Test & Acceptance Criteria
System Design ---------------- System Testing ---------------- system test plan & end to end test cases
Architecture Design ---------------- Integration Testing ---------------- Integration test plan & API/Integration test cases
Module Design ---------------- Unit Testing ---------------- unit test cases & code coverage criteria

## Entry and exit criteria
### Level 1 - Unit testing 
* Entry criteria - Source code for inidividual module/classes to make sure the code is run withour compilation/syntax errors
* Exit criteria - all unit tests executed with 100% pass rate and code coverage(upto which part of code is executed for a test set)
>= 80%
### Level 2 - Integration testing
* Entry criteria - all constituent modules passing unit testing and api endpoints and sb mock schemas are ready and deployed in staging environment
* Exit criteria - inter-module workflow and calls run witout communication errors and ther are no critical bugs during the integration

### Level 3 - System testing
* Entry criteria - successful completion od integration testing  and fully integrated course Management api application deployed in a staging / test environment
* Exit criteria - 100% of planned functional and non functional test cases executed and total open defects fall below threshold with zero open critical bugs

### Level 4 - Acceptance Testing 
* Entry criteria - system testing successfully signed off by the QA team and production like environment prepared for the mock user/course data
* Exit criteria - All business use cases (course enrollment - roles - grading ) validated by stakeholders and official business sign off obtained for deployment to production

## Early QA engagement points
### Requirements review phase 
* QA participates in reviewing API requirements and user storied (a student cannt enroll before completing its pre requisites)
* uncovers missing edge cases or contradictory specs before code construction begins

### Architecture and API schema design phase:
* QA reviews OpenAPI/swagger specifications data models and HTTP response contract mappings 
* prevents integration mismatches between frontend and backend and ensures testablility of endpoints before implementation
