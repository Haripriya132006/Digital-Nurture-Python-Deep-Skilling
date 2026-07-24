## Comparison of 5 automation framework types
### linear automation framework - record and playback
* Description - test scripts are executed sequentiallywithout modularization and abstraction  - each test script contains all locators test data and user actions embedded in a sing flow
* Advantage - requires minimal coding knowledge and allows rapid initila script creation
* Disadvantage - high maintenance overhead - UI or locator changes require manually editing or re-recording every affected script
* Course Management system example - Quickly recording a one-off smoke test to verify that the home page loads after a server patch 

### modular testing framework 
* Description - divides the application into individual modules or page components - individual scripts or fuunctions are created for each module - then called by main test script 
* Advantage - High code reusability and reduced duplication making test maintanace significantly easier
* Disadvantage - Test data is still hard coded inside modular scripts restricting dynamic testing across multiple data sets 
* Course Management system example - creating a reusable login_page.py module that handles user login and can be called at the start of student , instructor and admin workflow tests

### Data-Driven framework 
* Description - seperates login from test input data - test scripts read dynamic input parameter sets and expected results from external sources - CSV or excel or json 
* Advantages - Enables running a single test logic across hundreds of different data combinations without duplicating code 
* Disadvantages : Requires additional utility code to parse external data files manage data binding 
* Course Management system example : parameterizing a single test_course_creation script to iterate through 50 rows of different course names, codes, and capacities stored in Excel sheet 

### Keyword driven framework
* Description - seperates application actions into predefined keywords (clickElement, typeText, verifyText)
* Advantage - enables non-technical team members to design test cases using readable keywords without writting code 
* Disadvantage - igh initial setup complexity and development cost to build and maintain the underlying keyword library and driver script 
* Course Management system example - writing test steps in excel like LOGIN, CREATE_COURSE, and LOGOUT for non-technical QA members to execute API and UI tests

### Hybrid framework 
* Description - Integrates the strengths of two or more frameworks - typically combining modular, data driven , keyword driven approaches into a unified architecture 
* Advantage - offers maximum flexiblity, scalablity, high reusability 
* Disadvantage - complex architecture that requires advanced technical expertise to build maintain and structure effectively 
* Course Management system example - building a page object model (modular) suite that fetches test user credentials from external json files
(data-driven) and supports Cucumber gherkin steps (keyword driven).

## Recommended framework for the situation
### Hybrid framework (modular + data-driven + keyword/BDD)
#### Justification
* testing login with 50 combination -> data driven component
* reusing login steps across 20 test cases -> Modular component 
* suporting technical and non technical members -> keyword / BDD component

## folder structure for hybrid structure 
```
course-management-tests/
│
├── config/                         # Environment & execution configurations
│   ├── config.py                   # URLs, timeouts, browser settings
│   └── test_env.json               # Environment details (dev, staging, prod)
│
├── test_data/                      # External test data files (Data-Driven)
│   ├── users_50_credentials.csv    # 50 login combinations
│   └── course_payloads.json        # Dynamic course creation data
│
├── pages/                          # Page Object Model files (Modular)
│   ├── base_page.py                # Wrapper for common Selenium actions
│   ├── login_page.py               # Locators & methods for Login screen
│   └── course_page.py              # Locators & methods for Course Management
│
├── features/                       # BDD / Keyword Feature Files (For non-technical members)
│   ├── login.feature               # Gherkin feature specs for login scenarios
│   └── course_management.feature   # Gherkin feature specs for course creation
│
├── step_definitions/               # Bindings between Gherkin steps and Python/Selenium
│   ├── login_steps.py
│   └── course_steps.py
│
├── utils/                          # Common utility and helper scripts
│   ├── driver_factory.py          # Selenium WebDriver setup & cleanup
│   ├── excel_reader.py            # Utility to parse CSV / Excel test data
│   └── reporter.py                 # Custom HTML report configuration
│
├── tests/                          # Automated PyTest execution files
│   ├── test_login.py
│   └── test_courses.py
│
├── reports/                        # Auto-generated execution reports & screenshots
│   ├── html_report.html
│   └── screenshots/                # Failure screenshots captured dynamically
│
├── pytest.ini                      # Pytest execution parameters & markers
└── requirements.txt                # Project dependencies (selenium, pytest, behave, etc.)
```