.PHONY: dev exec-backend

LINE=DEPLOYMENT_CONFIG=./deployment/config/.env
FILE=.env

dev:
	grep -qFxs -- "$(LINE)" "$(FILE)" || echo "$(LINE)" >> "$(FILE)"
	docker-compose up --build

exec-backend:
	docker-compose exec backend bash
