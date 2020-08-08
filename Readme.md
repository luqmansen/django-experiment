# django-experiment

Experiment with some techstack in Django

#### Currently Available
- Instrumented with [Prometheus](https://prometheus.io/)
- Health checks (readiness and liveness)
- opentracing with Jaeger


#### Web API
- `GET /metrics` return prometheus metrics
- `GET /healthz` for Kubernetes liveness probe
- `GET /readyz` for Kubernetes readiness probe

#### Issues
- Jaeger client for python is so buggy, sometimes the local agent reporter doesn't work
