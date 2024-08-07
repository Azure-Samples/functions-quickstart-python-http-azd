---
name: "Azure Functions Python HTTP Trigger using AZD"
description: This repository contains a Azure Functions HTTP trigger quickstart written in Python and deployed to Azure using Azure Developer CLI (AZD). This sample uses manaaged identity and a virtual network to insure it is secure by default.
page_type: sample
languages:
- Python
products:
- azure
- azure-functions
- entra-id
urlFragment: functions-quickstart-python-azd
---

# Azure Functions Python HTTP Trigger using AZD

This repository contains a Azure Functions HTTP trigger quickstart written in Python and deployed to Azure using Azure Developer CLI (AZD). This sample uses manaaged identity and a virtual network to insure it is secure by default. 

## Getting Started

### Prerequisites

1) [Python 3.11](https://www.python.org/) 
2) [Azure Functions Core Tools](https://learn.microsoft.com/azure/azure-functions/functions-run-local?tabs=v4%2Cmacos%2Ccsharp%2Cportal%2Cbash#install-the-azure-functions-core-tools)
3) [Azure Developer CLI (AZD)](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd)
4) [Visual Studio Code](https://code.visualstudio.com/) - Only required if using VS Code to run locally

### Get repo on your local machine
Run the following GIT command to clone this repository to your local machine.
```bash
git clone https://github.com/Azure-Samples/functions-quickstart-python-azd.git
```

## Run on your local environment

### Prepare your local environment
1) Add a file named local.settings.json file to the root of the project with the following contents. This will allow you to run your function locally.
```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python"
  }
}
```

### Using Functions CLI
1) Open this folder in a new terminal and run the following commands:

```bash
npm install
func start
```

2) Test the HTTP GET trigger using the browser to open http://localhost:7071/api/httpGetFunction

3) Test the HTTP POST trigger in a new terminal window:
```bash
curl -i -X POST http://localhost:7071/api/http_post -H "Content-Type: text/json" --data-binary "@src/functions/testdata.json"
```

### Using Visual Studio Code
1) Open this folder in a new terminal
2) Open VS Code by entering `code .` in the terminal
3) Press Run/Debug (F5) to run in the debugger (select "Debug anyway" if prompted about local emulater not running) 
4) Insure your favorite REST clientextension is installed (e.g. [RestClient in VS Code](https://marketplace.visualstudio.com/items?itemName=humao.rest-client), PostMan, etc.)
5) Open the file src/functions/test/ which contains a GET and POST test
6) Click the "Send Request" link for each and see the results in the right-hand pane that opens

## Source Code

The key code that makes tthese functions work is in `function_app.py`.  The function is identified as an Azure Function by use of the `@azure/functions` library. This code shows a HTTP GET triggered function.  

```python
@app.route(route="http_get", methods=["GET"])
def http_get(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name")
    
    logging.info(f"Processing GET request. Name: {name}")

    if name:
        return func.HttpResponse(f"Hello, {name}!")
    else:
        return func.HttpResponse(
            "Please pass a 'name' parameter in the query string",
            status_code=400
        )
```
This code shows a HTTP POST triggered function.

```python
@app.route(route="http_post", methods=["POST"])
def http_post(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        name = req_body.get('name')
        
        logging.info(f"Processing POST request. Name: {name}")

        if name:
            return func.HttpResponse(f"Hello, {name}!")
        else:
            return func.HttpResponse(
                "Please pass a 'name' in the request body",
                status_code=400
            )
    except ValueError:
        return func.HttpResponse(
            "Invalid JSON in request body",
            status_code=400
        )
```

## Deploy to Azure

To provision the dependent resources and deploy the Function app run the following command:
```bash
azd up
```
You will be prompted for an environment name (this is a friendly name for storing AZD parameters), a Azure subscription, and an Aure location.
