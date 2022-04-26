docker-up:
	docker-compose up -d --build
docker-down:
	docker-compose down -v
docker-fill:
	docker-compose exec db psql --username=movies_db --dbname=movies_db -c 'CREATE SCHEMA IF NOT EXISTS content;'
	docker-compose exec backend \
		python manage.py migrate --noinput
		&& python manage.py collectstatic --no-input --clear
		&& python manage.py createsuperuser --noinput
docker-logs:
	docker-compose logs -f
swagger-run:
	docker run --rm -p 8080:8080 --name swagger \
		-v $(realpath ./openapi.yml):/swagger.yml \
		-e SWAGGER_JSON=/swagger.yml \
		swaggerapi/swagger-ui
