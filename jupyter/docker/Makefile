USER=$$(id -un)
JUPYTER_VOLUME=/Users/${USER}/Workspace/jupyter

up:
	export USER=${USER} && \
	export JUPYTER_VOLUME=${JUPYTER_VOLUME} && \
		docker compose up jupyter -d 

up-all:
	export USER=${USER} && \
	export JUPYTER_VOLUME=${JUPYTER_VOLUME} && \
		docker compose up -d

down:
	docker compose down -v