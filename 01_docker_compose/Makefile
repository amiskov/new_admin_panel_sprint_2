docker-up:
	docker-compose up -d --build
docker-down:
	docker-compose down -v
docker-migrate:
	docker-compose exec db psql --username=movies_db --dbname=movies_db -c 'CREATE SCHEMA IF NOT EXISTS content;'
	docker-compose exec backend ./manage.py migrate --noinput
docker-collectstatic:
	docker-compose exec backend ./manage.py collectstatic --no-input --clear
docker-fill-db:
	docker compose cp app/db.json.zip db:/tmp
	docker-compose exec backend ./manage.py loaddata db.json
docker-fill: docker-migrate docker-collectstatic docker-fill-db
docker-logs:
	docker-compose logs -f
swagger-run:
	docker run --rm -p 8080:8080 --name swagger \
		-v $(realpath ./openapi.yml):/swagger.yml \
		-e SWAGGER_JSON=/swagger.yml \
		swaggerapi/swagger-ui
