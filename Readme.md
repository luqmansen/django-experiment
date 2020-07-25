# django-pod

Django-pod is simple Django application that shows some 
example of best practice to running Django app on Kubernetes,
this repo inspired by [stefanprodan/podinfo](https://github.com/stefanprodan/podinfo), but in Django

Also going to be added some of commons Django production ready feature eg: Connection pooling, Caching, Oauth, etc.

#### Currently Available
- Instrumented with [Prometheus](https://prometheus.io/)
- Health checks (readiness and liveness)


#### Web API
- `GET /metrics` return prometheus metrics
- `GET /healthz` for Kubernetes liveness probe
- `GET /readyz` for Kubernetes readiness probe

