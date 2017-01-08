# api-server
8th mile apis

#### Installation
```shell
pip install -r requirements.txt
```

1. User-signup (/user/signup)
  * Request
 ```json
 {"name": "8mile", "phone": "123456789"}
 ```
  * Response
  ```json
  {"success":"true or false", "statuscode":"200 or 400 etc."}
  ```

2. User-verify (/verify)
  * Request
  ```json
  {"phone":"123456789","otp":"23463"}
  ```
  * Response
  ```json
  {"msg":"Successfully registered or failed", "token":"jwt token,in case of signup this should be null", "success":"true or false",     "statuscode":"200 or 400 or etc."}
  ```

3. User-login (/user/login)
 * Request
  ```json
  {"phone":"a@cv.com"}
  ```
 * Response
 ```json
 {"otp":"53634 or error", "success":"true or false", "statuscode":"200 or 400 etc."}
 ```
