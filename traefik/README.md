# Traefik

- https://traefik.io/

- helm chart
  - https://github.com/traefik/traefik-helm-chart

## deploy

- deploy chart

```shell
$ make deploy
```

## port-forward

```shell
kubectl port-forward $(kubectl get pods --selector "app.kubernetes.io/name=traefik" --output=name) 9000:9000
```

access to http://localhost:9000/dashboard/
