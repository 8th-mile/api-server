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
4. Event-add (/event/add)
  * Request
  ```json
  {"eventid":"12","type_id":"10","event_name":"hack59","date":"10/01/2017","price":"500"}
  ```
  * Response
  ```json
 { "msg":"successfully added or failed","success":"true or false", "statuscode":"200 or 400 etc."}
 ```
 
 5. Event-get (/event)
  * Request
  ```json
  {"type_id":"10","event_id":"12"}
  ```
  * Response
  ```json
 {"results":"list of all the events","success":"true or false", "statuscode":"200 or 400 etc."}
 ```
 
 6.Event-Register (/event/register)
  * Request
  ```json
  {"userid":"10","event_id":"12"}
  ```
  * Response
  ```json
 {"link":"Qrcode","success":"true or false", "statuscode":"200 or 400 etc."}
 ```
 
 7.Sponsor-add (/sponsor/add)
  * Request
  ```json
  {"name":"paytm","logo":"logo of particular sponsor","event_id":"12"}
  ```
  * Response
  ```json
 {"msg":"successfully added or failed", "success":"true or false", "statuscode":"200 or 400 etc."}
 ```
 
 8.Sponsor-get (/sponsor)
  * Request
  ```request
  (get)
  ```
  * Response
  ```json
 {"result":"list of all the sponsors", "success":"true or false", "statuscode":"200 or 400 etc."}
 ```
 
 9.User-wishlist (/user/wishlist)
  * Request
  ```json
  {"userid":"12","event_id":"10"}
  ```
  * Response
  ```json
 {"msg":"successfully added or failed", "success":"true or false", "statuscode":"200 or 400 etc."}
 ```
 
 10.User-wishlist-get (/user/wishlist)
  * Request
  ```json
  {"userid":"12"}
  ```
  * Response
  ```json
 {"result":"list of events", "success":"true or false", "statuscode":"200 or 400 etc."}
 ```
 
  
  
  
 
  
  
  
 
