import azure.functions as func
import logging
import time

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.function_name(name="http_get")
@app.route(route="http_get")
def main(req: func.HttpRequest) -> func.HttpResponse:
    user = req.params.get("user")
    return f"Hello, {user}!"

@app.function_name(name="http_post")
@app.route(route="http_post")
def main(req: func.HttpRequest) -> func.HttpResponse:
    req_body = req.get_json()
    name = req_body.get('name')
    return func.HttpResponse(f"Hello, {name}!")
