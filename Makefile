
up:
		docker compose -f docker-compose.yaml up --build -d

build:
		docker compose build

up_only:
		docker compose up -d

down:
		docker compose down --remove-orphans

clean:
		docker compose down --remove-orphans --rmi all

fclean: clean
		docker volume ls -q | grep camagru_database | xargs -r docker volume rm

re:		down fclean up

logs:
		docker compose logs

ls:
		docker compose images
		docker compose ps
		docker volume ls

e_enginx:
		docker exec -it nginx_camagru sh
