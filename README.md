# api-server
8th mile apis


1. User-signup (/user/signup)
  * Request
 ```json
 {"name": "8mile", "password": "1234", "phone": "123456789"}
 ```
  * Response
  ```json
  {"otp":"53634 or error", "success":"true or false", "statuscode":"200 or 400 etc."}
  ```
  
2. User-verify (/verify)
  * Request
  ```json
  {"otp":"23463"}
  ```
  * Response
  ```json
  {"msg":"Successfully registered or failed", "success":"true or false", "statuscode":"200 or 400 or etc."}
  ```
 
3. User-login (/user/login)
 * Request
  ```json
  {"phone":"a@cv.com"}
  ```
 * Response
 ```json
 {"token":"it will be a jwt token","statuscode":"200 or 400 or etc."}
 ```
