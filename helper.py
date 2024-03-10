from fastapi import UploadFile
from functools import wraps
from fastapi.responses import JSONResponse

async def save_upload_file_tmp(upload_file: UploadFile):
    try:
        tmp_file = f"tmp/{upload_file.filename}"
        with open(tmp_file, "wb") as buffer:
            buffer.write(await upload_file.read())
        return tmp_file
    except Exception as e:
        raise e


def password_decorator_factory(password):
    """This function is a python decorator that is used to protect the endpoints with a password

    Args:
        password: This password is the secret that protects the route

    Returns:
        password_decorator: A decorator that runs the provided function
    """

    def password_decorator(target_function):
        """This function is a python decorator that wraps the inner function and define the execution of the function

        Args:
            target_function: A function that is decorated with the decorator

        Returns:
            wrapper_func: This function actually executes the function.
        """

        @wraps(target_function)
        async def wrapper_func(*args, **kwargs):
            """This function checks that the user provided password matches the password for this function before
            executing the function.

            Args:
                *args: The list of arguments provided
                **kwargs: The dictionary of keyword arguments provided.

            Returns:
                result: This maybe the result returned by the function itself if the password matches otherwise a JSON
                        Response of status 401 which is used for Unauthorized access
            """

            if kwargs['password'] and kwargs['password'].get_secret_value() == password:
                result = await target_function(*args, **kwargs)
            else:
                result = JSONResponse(content={"error": "Invalid Password"}, status_code=401)
            return result
        return wrapper_func
    return password_decorator