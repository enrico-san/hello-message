# hello-message

## Prerequisites
* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

```bash
pip install -r hello_world/requirements.txt --user
pip install -r tests/requirements.txt --user
```

## Build and local run
Build the application: the SAM CLI installs dependencies defined in `hello_world/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

```bash
./scripts/build
```

Build and run in local with SAM. The application will respond on http://localhost:3000/

```bash
./scripts/run_local
```

Remember to run `./scripts/build` if you make changes to the code.
SAM doesn't do it for you

## view logs
```bash
tail -f logfile.txt
```


## Tests
Tests are defined in the `tests` folder in this project. Use PIP to install the test dependencies and run tests.

```bash
pip install -r hello_world/requirements.txt --user
pip install -r tests/requirements.txt --user

# unit test
./scripts/test

# integration test (local)
./scripts/integration_test
```



docker run --name=acube \
  --restart on-failure \
  --env MYSQL_ALLOW_EMPTY_PASSWORD=true \
  -p 3307:3306 \
  -d mysql/mysql-server:5.7


setup mysql container
- docker run
- docker exec -it acube mysql -uroot
- paste:
use mysql;
select host from user where user='root';
update user set host = '%' where user ='root';
flush privileges;
DROP DATABASE IF EXISTS acube;
CREATE DATABASE acube;
use acube;
CREATE TABLE IF NOT EXISTS stats(
  id INT AUTO_INCREMENT PRIMARY KEY,
  customer_id INT NOT NULL,
  type_id VARCHAR(255) NOT NULL,
  count INT,
  amount DECIMAL(10,3),
  UNIQUE KEY my_uniq_id (customer_id, type_id)
);
exit

find container's address:
- docker inspect conduxDB  | grep IPAddress
and put it in template.yaml