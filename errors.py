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

CUSTOM_ERRORS = {
    "NameEmptyError": {
        "message" : "Name cannot be empty.",
        "status" : 400,
    },
    "InvalidPhoneNumberError": {
        "message": "Phone number doesn't contain 10 digits. Please verify and re-enter!",
        "status": 400,
    },
    "EmailEmptyError": {
        "message": "Email cannot be empty. Please fill it up.",
        "status": 400,
    },
    "DBInsertError": {
        "message": "Unable to insert into database.",
        "status": 409,
    },
    "DBQueryError": {
        "message": "Unable to query user from database",
        "status": 404,
    },
}
