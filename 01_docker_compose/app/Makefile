run:
	python manage.py runserver
sh:
	./manage.py shell_plus
# Translations
build-locale:
	python manage.py compilemessages -l en -l ru
collect-locale:
	python manage.py makemessages -l en -l ru

# DB content Schema
run-db:
	docker run -d \
		--name postgres \
		-p 5432:5432 \
		-v ~/postgresql/data:/var/lib/postgresql/data \
		-e POSTGRES_PASSWORD=123qwe \
		-e POSTGRES_USER=app \
		-e POSTGRES_DB=movies_db  \
		postgres:13
drop-schema:
	psql -h 127.0.0.1 -U app movies_db -c 'DROP SCHEMA content CASCADE;'
create-schema:
	psql -h 127.0.0.1 -U app -d movies_db -f ../01_schema_design/movies_database.ddl
	echo "Schema has been created."
seed-db:
	psql -h 127.0.0.1 -U app -d movies_db -f ../01_schema_design/seed.sql
	echo "film_work table has been populated."
	python ../01_schema_design/seed.py
	echo "Persons has been created."
reset-schema: drop-schema create-schema

# Django
new-admin:
	# Skip initial migration since we already have the DB schema
	python manage.py migrate --fake movies
	python manage.py migrate
	python manage.py createsuperuser --username admin --email amiskov@ya.ru

# Database itself
drop-db:
	dropdb -h 127.0.0.1 -U app movies_db
	echo "DB has been dropped."
create-db:
	createdb -h 127.0.0.1 -U app movies_db
	echo "DB has been created."
