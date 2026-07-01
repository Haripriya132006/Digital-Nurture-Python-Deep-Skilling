# 1
"""
Browser----------------------------|
   | (GET /api/courses)            |
urls.py                            |
   | seaches for the right view    |
views.py  ---templates(htmlfiles)--|
   | asks data 
models.py
"""

# 2
"""
the middleware sits between the webserver requests to urls.py and views.py 
it takes care of the security and access to the views

CsrfViewMiddleware 
-> takes care of the security and authenticates the user

->AuthenticationMiddleware 
-> It identifies the person accessing the application and validates if 
          they are allowed to enter
"""

# 3 
"""
wsgi (web server gateway Interface)
->synchronous
->request-response traditional web application
->blocks execution until process is complete
->supports Http/1.1

asgi (asynchronous server gateway interface)
->asynchronous 
->supports websockets and Http making it 
          ideal for real time communication
->supports

"""

# 4
"""
M-model  - db connector
V-view  - frontend
C-Controller - businness logic

M-model - db connector
V-view - businness logic
T-templates - frontend
"""


