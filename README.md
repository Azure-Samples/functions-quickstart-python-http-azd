---
name: "Azure Functions Python HTTP Trigger using AZD"
description: This repository contains an Azure Functions HTTP trigger quickstart written in Python and deployed to Azure Functions Flex Consumption using the Azure Developer CLI (AZD). This sample uses managed identity and a virtual network to insure it's secure by default.
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

This repository contains an Azure Functions HTTP trigger quickstart written in Python and deployed to Azure using Azure Developer CLI (AZD). This sample uses managed identity and a virtual network to insure it's secure by default. 

## Prerequisites

+ [Python 3.11](https://www.python.org/)
+ [Azure Functions Core Tools](https://learn.microsoft.com/azure/azure-functions/functions-run-local#install-the-azure-functions-core-tools)
+ [Azure Developer CLI (AZD)](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd)
+ To use Visual Studio Code to run and debug locally:
  + [Visual Studio Code](https://code.visualstudio.com/) 
  + [Azure Functions extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)

### Get repo on your local machine

You can download this project template in one of these ways:

+ Use this `azd init` command from an empty local (root) folder:

    ```azd
    azd init --template functions-quickstart-python-http-azd
    ```

+ Clone this repository locally using the `git clone` command:

    ```bash
    git clone https://github.com/Azure-Samples/functions-quickstart-python-azd.git
    cd functions-quickstart-python-azd
    ```

+ Fork this repository to your GitHub account and then clone locally using the `git clone` command:

    ```bash
    git clone https://github.com/<YOUR_ACCOUNT>/functions-quickstart-python-azd.git
    cd functions-quickstart-python-azd
    ```

## Prepare your local environment

Add a file named `local.settings.json` in the root of your project with the following contents:

```json
{
    "IsEncrypted": false,
    "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python"
    }
}
```

## Create a virtual environment

The way that you create your virtual environment depends on your operating system.
Open the terminal, navigate to the project folder, and run these commands:

### Linux/macOs

```bash
python -m venv .venv
source .venv/bin/activate
```

#### Windows

```shell
py -m venv .venv
.venv\scripts\activate
```

## Run your app from the terminal

1. Run these commands in the virtual environment:

    ```bash
    pip install -r requirements.txt
    func start
    ```

2. From your HTTP test tool in a new terminal (or from your browser), call the HTTP GET endpoint: <http://localhost:7071/api/httpget>

3. Test the HTTP POST trigger with a payload using your favorite secure HTTP test tool. This is an example that uses the `curl` tool with the `testdata.json` project file:

    ```bash
    curl -i http://localhost:7071/api/httppost -H "Content-Type: text/json" -d @testdata.json
    ```

## Run your app using Visual Studio Code

1. Open the root folder in a new terminal.
1. Run the `code .` code command to open the project in Visual Studio Code.
1. Press **Run/Debug (F5)** to run in the debugger. Select **Debug anyway** if prompted about local emulator not running.
1. Send GET and POST requests to the `httpget` and `httppost` endpoints respectively using your HTTP test tool (or browser for `httpget`). If you have the [RestClient](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) extension installed, you can execute requests directly from the `test.http` project file.

## Source Code

The source code for both functions is in `function_app.py` code file. The function is identified as an Azure Function by use of the `@azure/functions` library. This code shows an HTTP GET triggered function.  

```python
@app.route(route="httpget", methods=["GET"])
def http_get(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name", "World")

    logging.info(f"Processing GET request. Name: {name}")

    return func.HttpResponse(f"Hello, {name}!")
```

This code shows an HTTP POST triggered function.

```python
@app.route(route="httppost", methods=["POST"])
def http_post(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        name = req_body.get('name')
        age = req_body.get('age')
        
        logging.info(f"Processing POST request. Name: {name}")

        if name and isinstance(name, str) and age and isinstance(age, int):
            return func.HttpResponse(f"Hello, {name}! You are {age} years old!")
        else:
            return func.HttpResponse(
                "Please provide both 'name' and 'age' in the request body.",
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

You'll be prompted for an environment name (this is a friendly name for storing AZD parameters), an Azure subscription, and an Azure location.
