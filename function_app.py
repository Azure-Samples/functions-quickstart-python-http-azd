import azure.functions as func
import logging
import time

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_get")
def main(req: func.HttpRequest) -> func.HttpResponse:
    user = req.params.get("user")
    return f"Hello, {user}!"

@app.route(route="http_post")
def main(req: func.HttpRequest) -> func.HttpResponse:
    req_body = req.get_json()
    name = req_body.get('name')
    return func.HttpResponse(f"Hello, {name}!")
