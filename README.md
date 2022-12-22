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
| BASE_URL/auth/users/me/avatar/ | edit user to add an avatar image | PATCH |
| BASE_URL/calendar/ | list all calendars, create a calendar | GET, POST |
| BASE_URL/calendar/<int:pk>/ | get, edit, or delete a single calendar | GET, PATCH, DELETE |
| BASE_URL/calendar/cover/<int:pk>/ | edit calendar to add cover image | PATCH |
| BASE_URL/journal/ | list all journals, create a journal | GET, POST |
| BASE_URL/journal/<int:pk>/ | get, edit, or delete a single journal | GET, PATCH, DELETE |



## User Authentication Endpoints

### Register a new user:

#### request:
Username and password are required fields. Email is optional.
Token should not be entered or enabled.

POST  <BASE_URL>/auth/users/

```json
{
  "username": "testusername",
  "password": "testpassword"
}
```

#### response:
201 Created

```json
{
  "email": "",
  "username": "testusername",
  "id": 1
}
```

### Log In:

#### request:
Username and password are required fields.
Token should not be entered or enabled.

POST  <BASE_URL>/auth/token/login/

```json
{
  "username": "testusername",
  "password": "testpassword"
}
```

### response:
```json
{
  "auth_token": "c312049c7f034a3d1b52eabc2040b46e094ff34c"
}
```

### Log out

#### request:

Authentication Required.
Must be logged in.

POST  <BASE_URL>/auth/token/logout/


#### response:
```json
"No body returned for response"
```

## Calendar Endpoints

### List all Calendars:

#### request:
Authentication required.

GET  <BASE_URL>/calendar/

#### response:
```json
[
	{
		"id": 1,
		"name": "new cal",
		"journals": [
			{
				"id": 3,
				"date": "2020-10-10",
				"entry": null,
				"event": null,
				"calendar": 1,
				"tags": [
					"momentum",
					"code"
				],
				"journal_images": [
					{
						"id": 1,
						"image": "http://127.0.0.1:8000/media/journal_images/1hector_cwD6hmQ.jpeg"
					},
					{
						"id": 2,
						"image": "http://127.0.0.1:8000/media/journal_images/1hector_QZ6SMMD.jpeg"
					}
				]
			}
		]
	},
	{
		"id": 2,
		"name": "second cal",
		"journals": []
	}
]
```

### Create Calendar:

#### request:
Authentication Required. 
Name is a required field.

POST  <BASE_URL>/calendar/

```json
{
    "name": "third cal"
}
```

#### response:
201 CREATED
```json
{
	"id": 3,
	"name": "third cal",
	"journals": []
}
```

### Get Individual Calendar by PK:

#### request:
Authentication required.

GET <BASE_URL>/calendar/<int:pk>/

#### response:
200 OK
```json
[
	{
		"id": 1,
		"name": null,
		"avatar": null
	},
	{
		"id": 2,
		"name": null,
		"avatar": null
	}
]
```

### Edit Calendar:

#### request:
Authentication Required. 

PATCH  <BASE_URL>/calendar/<int:pk>/

```json
{
    "name": "THIRD calendar"
}
```

#### response:
200 OK
```json
{
	"id": 3,
	"name": "THIRD cal",
	"journals": []
}
```

### Add Calendar Cover Image:

#### request:
Authentication Required. 

PATCH  <BASE_URL>/calendar/<int:pk>/

* Binary File should be selected in first drop down > choose file to upload.
* Headers:
- Content-Type | image/jpeg 
- Content-Disposition | attachment; nameofyourfile.jpeg


#### response:
200 OK
```json
{
	"id": 2,
	"name": "new cal!",
	"cal_image": "https://frostybucket1.s3.amazonaws.com/cal_covers/bernine_82uTsDF.jpg",
	"journals": []
}
```

### Delete Calendar:

#### request:
Authentication Required. 

DELETE  <BASE_URL>/calendar/<int:pk>/

#### response:
204 NO CONTENT
```json
{
"No body returned for response"
}
```