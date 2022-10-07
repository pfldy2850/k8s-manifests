USER=$$(id -un)
JUPYTER_VOLUME=/Users/${USER}/Workspace/jupyter

up:
	export USER=${USER} && \
	export JUPYTER_VOLUME=${JUPYTER_VOLUME} && \
		docker compose up jupyter -d 

down:
	docker compose down -v