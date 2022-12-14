# Journeyal-BackEnd

# Link to Production Application
https://journeyal-webservice.onrender.com/

**All requests, except registration and log in, require authentication**

Requests to endpoints requiring authentication should set the `Authorization` header to `Token <token>`, where `<token>` is the token received in the login response.

POST requests with a body should set the `Content-Type` header to `application/json`.

# URLS
| URL	| Description | Possible request |
| -----|-----|-----| 
| BASE_URL/auth/users/| register a new user | POST |
| BASE_URL/auth/token/login/ | log in | POST |
| BASE_URL/auth/token/logout/ | log out | POST |
| BASE_URL/user/ | list all users | GET |
| BASE_URL/user/<int:pk>/ | get, edit, or delete a single user | GET, PATCH, DELETE |
| BASE_URL/calendar/ | list all calendars | GET |
| BASE_URL/calendar/<int:pk>/ | get, edit, or delete a single calendar | GET, PATCH, DELETE |
| BASE_URL/journal/ | list all journal | GET |
| BASE_URL/journal/<int:pk>/ | get, edit, or delete a single journal | GET, PATCH, DELETE |
