# hello-message

## Prerequisites
* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

## Build and local run

Build the application: the SAM CLI installs dependencies defined in `hello_world/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

```bash
./scripts/build
```

Build and run in local with SAM. The application will respond on http://localhost:3000/

```bash
./scripts/run_local
```

## view logs

```bash
tail -f logfile.txt
```


## Tests

Tests are defined in the `tests` folder in this project. Use PIP to install the test dependencies and run tests.

```bash
pip install -r tests/requirements.txt --user

# unit test
./scripts/test

# integration test (local)
./scripts/integration_test
```
