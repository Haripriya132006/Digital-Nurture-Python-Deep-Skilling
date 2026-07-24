## Automation Decision and test case selection 
### Repetitiveness and execution frequency
* tests that have to run in multiple builds or environments 
* validation of course creation endpoint will be executed repeatedly during regression testing for every deployment making it a prime candidate

### Business criticality / High risk 
* features that support core revenue where the failure is unacceptable
* course creation is a fundamental pillar of the course management API, failure here halts all the downstream processes such as enrollment and academic workflows

### Predictability and determinism :
* tests with stable inputs and consistent , deterministic expected outputs. 
* a valid post request with standard payload predictabily yields a 201 created starus code and a matching json response body 

### Execution speed and efficiency
* tasks that can be validated significantly faster through code than manual execution 
* automating payload validation eliminates manual curl or postman execution verifying functionality in milliseconds

### Data driven potential 
* tests that benefit from running iteratively across multiple datasets
* the endpoint can be easily made to run for different types of situation of valid and invalid course payloads to easily retrive the summary of it 

## Test Case Categorization
### (a) Regression test for all CRUD endpoints after every code change: Automate
* executing CRUD checks manually after every code commit is repetitive, time-consuming, and prone to human oversight. Automation ensures continuous coverage.

### (b) Exploratory testing of a new search feature: Manual
* relies main on human intuition, creativoty and real time learning to predict unexpected edge cases 

### (c) Performance test: 100 concurrent users calling GET /api/courses/: Automate
* as simulating hig concurrency required specalized load-testing tools and cannot be done manually

### (d) UI test for the login form: Automate
* login is critical, repetitive gateway workflow that must function with every release so automating would be the right choice

### (e) Verify the API documentation (Swagger) is accurate: Manual
* assessing documentation requires human judgement to evaluate tone, clariy, grammer, and conceptual alignment with business requirements

### (f) Smoke test: verify the API is reachable after deployment: Automate
* must execute instantly in the cicd pipeline right after a deployment to block faulty builds automatically without manual intervention 

## Test Automation ROI calculation 
* ROI - return of investment  measures efficiency and financial value gained by automating tests compared to executing them manually 
* balances the upfront automation creation costs against ongoing execution and maintanance savings 

### given :
* manual execution- 30 mins - 0.5 hrs
* upfront cutomation cost - 4 hrs
* maintanance overhead 20%  per run after the 10th run

### break-even analysus
* cost of manual execution for n runs = 0.5n hrs
* upto 10 th run the automated cost is at the creational cost of 4 hrs
* setting manual cost equal to automation creational cost
* 0.5n=4 => n=8 runs
* the automation pays for itself at 8 runs because the break even point occurs before the 10 th run the 20% maintanace overheat does not delay the initial break-even threshold

## Flaky test analysis
* it is an automated test that irregularly passes and fails under the exact same code and environment conditions , producing false alarms and destroying team confidence in the test suite
* an ui test that clicks a submit button but fails randomly as the asynchronous API response takes longer than expected triggering an element not found timeout 
### strategies to prevent flaky tests
* replace hardcoded sleeps with explicit waits - WebDriverWait instead time.sleep()
* ensure test isolation and state management - reset database or application state before and after each test so that test execution order or leftover data never cause side effects 
* handle asynchronous network/DOM stability - ensure all background AJAX (asynchronous javascript and xml) calls, animations and DOM re-renders are completetly settled before executing assertions