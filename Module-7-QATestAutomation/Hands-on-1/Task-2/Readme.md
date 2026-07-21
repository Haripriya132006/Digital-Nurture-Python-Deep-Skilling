## 1. Complete defect lifecycle flow

```
new|-> assigned  |-> open -> Fixed -> retest -> verified->closed 
   |-> rejected<-|
   |-> deffered
```

* new - tester logs a newly bug in the defect tracking system
* assigned - the QA lead evaluates the bug and assigns it to a developer
* open - the dev starts analyzing and working to fix the bug
* fixed - the developer finishes the code and deploys the change to the test environment .
* retest - the bug is tested again and using the original steps 
* verified - the QA confirms the fix works properly without inroducing new issues
* closed - QA marks the ticket as competed or resolved

* rejected - the developer or lead rejects the bug because its not valid bug, works as designed or cannot be reporoduced
* deffered - the bug is recognized as valid but will be fixed in the future release and hence given low priority 

## 2. severityy of bugs
### a. `POST /api/courses/` return 500 internal server error for all requests 
* severity - critical - a core api is broken and it affect the whole website's fucnction
*priority - P1 - must be fixed immediately because it affect the whole website

### b. course names longer than 1500 characters are silently truncated without an error
* data trunctation leads to data integrity issues - but the core functionality still works 
* priority P2/P3 - needs to be adressed to protect data but doesnt cause a system failure

### c. the `/docs` swagger page has a typ in the API description 
* minor cosmetic issue - doesnt affect system perfomance
* priority P4 - can be fixed whenever convinient in future

### d. Login with correct credentials occasionally return 401 on the first attempt
* intermittent failure disrupts user authentication and indicated underlying system instability.
* priority P1/P2 - intermittent authentication flaws reduced user trust and mask deeper session bugs making quick fix essential 

## 3.
| Field | Details |
| :--- | :--- |
| **Defect ID** | `DEF-2026-001` |
| **Title** | `POST /api/courses/` fails with 500 Internal Server Error on valid payloads |
| **Environment** | Staging / QA Environment (`http://staging-api.college.edu`) |
| **Build Version** | v1.4.2-beta |
| **Severity** | Critical |
| **Priority** | P1 |
| **Preconditions** | API Gateway is running; Admin user has valid JWT token. |
| **Steps to Reproduce** | 1. Open API client (Postman/cURL).<br>2. Set Headers: `Content-Type: application/json`, `Authorization: Bearer <valid_token>`.<br>3. Send `POST` to `/api/courses/` with body:<br>`{"title": "Computer Networks", "credits": 3, "code": "CS-301"}`<br>4. Observe response status code. |
| **Expected Result** | HTTP `201 Created` with created course payload. |
| **Actual Result** | HTTP `500 Internal Server Error` returned with empty response body. |
| **Attachments** | `screenshot_of_500_error.png` |

## severity vs priority 
* severity -> refers to technical impact of the bug on the system - system crash , data loss vs. minor alignment issue
* refers to how quick the bug has to resolved 

### real work eample -> high severity , low priority 

* senario - a core feature cause a memory leak or 505 error whenever executed
* severity - high - the crash brings down the application 
* priority - it affects a deprecated module with zero active users access. Fixing it can wait while developers focus on critical user workflows.