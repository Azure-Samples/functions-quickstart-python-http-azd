---
name: "Azure Functions Python HTTP Trigger using AZD"
description: This repository contains an Azure Functions HTTP trigger quickstart written in Python and deployed to Azure Functions Flex Consumption using the Azure Developer CLI (AZD). This sample uses managed identity and a virtual network to insure it is secure by default.
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

This repository contains a Azure Functions HTTP trigger quickstart written in Python and deployed to Azure using Azure Developer CLI (AZD). This sample uses managed identity and a virtual network to insure it is secure by default. 

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

### Create a virtual environment
Open the terminal, navigate to the project folder, and run the following commands:

#### bash
```bash
python -m venv .venv
source .venv/scripts/activate
```

#### PowerShell
```powershell
py -m venv .venv
.venv\scripts\activate
```

#### Cmd
```cmd
py -m venv .venv
.venv\scripts\activate
```

### Using Functions CLI

1) Open this folder in a new terminal and run the following commands:

    ```bash
    pip install -r requirements.txt
    func start
    ```

2) Test the HTTP GET trigger using the browser to open http://localhost:7071/api/httpget

3) Test the HTTP POST trigger using your favorite REST client (e.g. [RestClient in VS Code](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)). `test.http` has been provided to run this quickly.
Or in a new terminal run the following:

    ```bash
    curl -i -X POST http://localhost:7071/api/httppost -H "Content-Type: text/json" -d "{\"name\": \"Awesome Developer\", \"age\": \"25\"}"
    ```

### Using Visual Studio Code

1) Open this folder in a new terminal
2) Open VS Code by entering `code .` in the terminal
3) Make sure the [Azure Functions extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) is installed
4) Press Run/Debug (F5) to run in the debugger (select "Debug anyway" if prompted about local emulater not running) 
5) Use same approach above to test using an HTTP REST client

## Source Code

The key code that makes tthese functions work is in `function_app.py`.  The function is identified as an Azure Function by use of the `@azure/functions` library. This code shows a HTTP GET triggered function.  

```python
@app.route(route="http_get", methods=["GET"])
def http_get(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name", "World")

    logging.info(f"Processing GET request. Name: {name}")

    return func.HttpResponse(f"Hello, {name}!")
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
You will be prompted for an environment name (this is a friendly name for storing AZD parameters), a Azure subscription, and an Azure location.
