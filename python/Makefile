pkg:=$(shell python setup.py --fullname)

.PHONY: lock build deploy clean

Pipfile.lock: Pipfile
	pipenv lock
	pipenv lock --requirements > requirements.txt
	pipenv lock --requirements --dev > requirements-dev.txt

lock: Pipfile.lock

build:
	docker-compose run --rm build --target /var/task --no-deps --upgrade .
	docker-compose run --rm build --target /opt/python --upgrade --requirement requirements.txt

dist:
	mkdir -p dist
	docker-compose run --rm -T dist > dist/$(pkg).lambda.zip
	docker-compose run --rm -T --workdir /opt dist > dist/$(pkg).layer.zip

# create a new bucket "hello-message" before this command
deploy:
	docker-compose run --rm -T dist | aws s3 cp - s3://hello-message/$(pkg).lambda.zip
	docker-compose run --rm -T --workdir /opt dist | aws s3 cp - s3://hello-message/$(pkg).layer.zip

clean:
	rm -rf dist
	docker-compose down --volumes

test:
	docker-compose run --rm test message_digest/index.handler '{"body": {"body": {"customerId": 2,"type": "B","amount": "0.012","uuid": "a596b362-08be-419f-8070-9c3055566e7c"}}}'

# shell into the container
dev:
	docker-compose run --rm dev

db:
	docker-compose run --rm mysql

sam:
	docker-compose run --rm sam

update-env:
	aws lambda update-function-configuration --function-name aws-node-express-api-dev-api \
    --environment "Variables={BUCKET=s3://hello-message}"