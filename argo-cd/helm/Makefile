CHART_NAME=argo-cd


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