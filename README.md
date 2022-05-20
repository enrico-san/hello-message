# hello-message

## Prerequisites
* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

```bash
pip install -r hello_world/requirements.txt --user
pip install -r tests/requirements.txt --user
```

### Start an MySQL container

Note: this MySQL stuff is a quick&dirty setup meant to spare time. Not to be used in real projects


```bash
docker run --name=acube \
  --restart on-failure \
  --env MYSQL_ALLOW_EMPTY_PASSWORD=true \
  -p 3307:3306 \
  -d mysql/mysql-server:5.7
```


### Setup the database
```bash
docker exec -it acube mysql -uroot
```

From the `mysql>` prompt, paste:
```
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

```

Find the container's address:
```bash
docker inspect acube  | grep IPAddress
```

and put it in `hello_world/mysql_helper.py >> HOST variable`


## Build and local run
Build the application.

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
Tests are defined in the `tests` folder in this project.

```bash
./scripts/run_local  # if not running
./scripts/test       # on a different terminal
```



