JWT LOGIN :
          credentials sent directly to backend
          backend validates
          issues a Access Token back to client
          Highly secure for First-Party applications
          -> YOur react authenticating with your own API backend

OAuth LOGIN:
          client app never sees user credentials
          details sent to dedicated Identity Provider(Google,Auth0)
          these apps exchange short-lived code to generate Access Token to the user
          Essential for 3rd party integrations (Sign in with google etc)

![alt text](<Screenshot 2026-07-05 212553.png>)