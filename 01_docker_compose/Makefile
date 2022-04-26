docker-up:
	docker-compose up -d --build
docker-down:
	docker-compose down -v
docker-fill:
	docker-compose exec db psql --username=movies_db --dbname=movies_db -c 'CREATE SCHEMA IF NOT EXISTS content;'
	docker-compose exec backend sh -c " \
		echo 'Applying migrations...' ; \
		./manage.py migrate --noinput ; \
		echo 'Collecting static files...' ; \
		./manage.py collectstatic --no-input --clear ; \
		echo 'Filling the DataBase with test data...' ; \
		./manage.py loaddata db.json ; \
		echo 'All done! Check http://localhost:8000/admin (use admin/admin to log in)'"
docker-logs:
	docker-compose logs -f
swagger-run:
	docker run --rm -p 8080:8080 --name swagger \
		-v $(realpath ./openapi.yml):/swagger.yml \
		-e SWAGGER_JSON=/swagger.yml \
		swaggerapi/swagger-ui
