install:
	@[ -f '.env' ] || cp .env.example .env
	@pipenv install -d

build:
	@pipenv lock -r > requirements.txt
	@pipenv lock -d -r > requirements-dev.txt
	@docker-compose build app

up: build
	@docker-compose up -d app
	@docker-compose logs -f app

cron:
	@pipenv lock -r > requirements.txt
	@pipenv lock -d -r > requirements-dev.txt
	@docker-compose up --build cron
	@docker-compose logs -f cron

#clear-log:
#ifdef worker_name
##	@rm *.pid *.
#	@echo ^.*worker_name.*$
#else
#	@echo 'no toto around'
#endif

stop:
	@docker-compose stop

test: build
	@docker-compose run app pytest
	@open ./.tmp/reports/pytest/index.html

migrations: up-data
	@pipenv run python manage.py makemigrations

# additional commands

up-data:
	@docker-compose up -d data cache storage
	@bash ./scripts/wait-data.sh

clean:
	@docker ps -aq -f status=exited | xargs docker rm
	@docker images -q -f dangling=true | xargs docker rmi
	@find . -name "__pycache__" | xargs rm -rf

clean-data:
	@rm -rf ./.tmp/data

clean-all: clean clean-data

lint: build
	@docker-compose run app pylint myproject myapp
