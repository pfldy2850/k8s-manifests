CHART_NAME=traefik


# update dependencies
# - install treafik chart
dependency.update:
	helm dependency update


# deploy helm chart
deploy: dependency.update
	helm upgrade --install \
		${CHART_NAME} \
		. \
		-f values.yaml


# port-foward for dashboard
port-forward:
    kubectl port-forward $(kubectl get pods --selector "app.kubernetes.io/name=traefik" --output=name) 9000:9000
