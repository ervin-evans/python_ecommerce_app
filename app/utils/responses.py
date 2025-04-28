

def success_response(message: str, data=None, status_code=200):
    response = {
        "success": True,
        "message": message
    }
    if data is not None:
        response["data"] = data
    return response, status_code


def error_response(message: str, errors=None, status_code=400):
    response = {
        "success": False,
        "message": message
    }
    if errors:
        response["errors"] = errors
    return response, status_code
