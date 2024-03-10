import os
import time

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, applications, Query
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
import fastapi_offline_swagger_ui
from os import path
from scripts.my_script.main import create_user
from helper import password_decorator_factory
from pydantic import SecretStr

app = FastAPI()

''' 
This following code block necessary to switch offline cdn files via fastapi_offline_swagger_ui module
'''
assets_path = fastapi_offline_swagger_ui.__path__[0]
print(assets_path)

app.mount("/images", StaticFiles(directory="images"), name="images")
if path.exists(assets_path + "/swagger-ui.css") and path.exists(assets_path + "/swagger-ui-bundle.js"):
    app.mount("/assets", StaticFiles(directory=assets_path), name="static")
    def swagger_monkey_patch(*args, **kwargs):
        return get_swagger_ui_html(
            *args,
            **kwargs,
            swagger_css_url="/assets/swagger-ui.css",
            swagger_js_url="/assets/swagger-ui-bundle.js",
        )
    applications.get_swagger_ui_html = swagger_monkey_patch


origins = [
    "*",
    "http://localhost:3000",
]

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ALGORITHM = "HS256"


@app.get("/")
async def ping():
    """
    Pings the API.

    Returns:
        dict: A dictionary containing the message.
    """

    return {"message": "Automation API is running successfully"}


@app.post("/create-user")
@password_decorator_factory('Password@2024')
async def create_sla_user(password: SecretStr, name: str, email: str, mobile: str, office: str, existing_user: str, skip_userdb:bool, user_type: str = Query('mspsla', enum=['mspsla', 'mobile', 'sec', 'admin']),):
    try:
        create_user(email, name, user_type)
        return JSONResponse(content={"message": "User created successfully."}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

    



