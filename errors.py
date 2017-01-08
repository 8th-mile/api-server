from flask_restful import HTTPException

class InvalidPhoneNumberError(HTTPException):
    pass
class NameEmptyError(HTTPException):
    pass
class EmailEmptyError(HTTPException):
    pass
class DBInsertError(HTTPException):
    pass
class DBQueryError(HTTPException):
    pass
class UserNotFound(HTTPException):
    pass

CUSTOM_ERRORS = {
    "NameEmptyError": {
        "message" : "Name cannot be empty.",
        "success" : "false",
        "status" : 401,
    },
    "InvalidPhoneNumberError": {
        "message": "Phone number doesn't contain 10 digits. Please verify and re-enter!",
        "success" : "false",
        "status": 401,
    },
    "EmailEmptyError": {
        "message": "Email cannot be empty. Please fill it up.",
        "success" : "false",
        "status": 401,
    },
    "DBInsertError": {
        "message": "Unable to insert into database.",
        "success" : "false",
        "status": 402,
    },
    "DBQueryError": {
        "message": "Unable to query user from database",
        "success" : "false",
        "status": 402,
    },
    "UserNotFound": {
        "message": "Specified User entry and registered phone number not found in database. Try the Signup option to register the same.",
        "success" : "false",
        "status": 403,
    },
}