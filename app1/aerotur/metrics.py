import os
from prometheus_client import start_http_server
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.instrumentation.django import DjangoInstrumentor

def start_metrics():
    try:
        port = int(os.getenv("METRICS_PORT", 8006))
        start_http_server(port, addr="0.0.0.0")
        print(f"[METRICS] Servidor Prometheus iniciado na porta {port}")
    except OSError as e:
        print(f"[METRICS ERROR] Porta já está em uso: {e}")
        return
    except Exception as e:
        print(f"[METRICS ERROR] Erro inesperado: {e}")
        return

    reader = PrometheusMetricReader()
    provider = MeterProvider(metric_readers=[reader])
    metrics.set_meter_provider(provider)

    DjangoInstrumentor().instrument()
    print("[METRICS] OpenTelemetry configurado com Prometheus")
