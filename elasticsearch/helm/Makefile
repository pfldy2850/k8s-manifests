CHART_NAME=helm-es
CLUSTER_NAME=es
NAMESPACE=elastic

# update dependencies
# - install treafik chart
dependency.update:
	helm dependency update


# deploy helm chart
deploy: dependency.update
	helm upgrade --install \
		${CHART_NAME} \
		. \
		-f values.yaml \
		--namespace $(NAMESPACE)

port-fowrad:
	kubectl port-forward svc/$(CLUSTER_NAME)-master 9200 --namespace $(NAMESPACE)