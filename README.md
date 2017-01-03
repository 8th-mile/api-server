# api-server
8th mile apis


1. User-signup (/user/signup)
  * Request
 ```json
 {"name": "8mile", "password": "1234", "phone": "123456789"}
 ```
  * Response
  ```json
  {"msg":"successfully registered or failed"}
  ```
2. User-login (/user/login)
 * Request
  ```json
  {"phone or email":"a@cv.com", "password": "1234"}
  ```
 * Response
 ```json
 {"token":"it will be a jwt token"}
 ```
