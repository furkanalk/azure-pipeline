from functions import write_file, create_dir_if_not_exists

def generate_prometheus_config(workspace_name):
    global_plugins_dir = f"{workspace_name}/global-plugins"
    create_dir_if_not_exists(global_plugins_dir)

    content = """plugins:
- name: prometheus
  config:
    bandwidth_metrics: true
    latency_metrics: true
    per_consumer: true
    status_code_metrics: true
    upstream_health_metrics: true
  enabled: false
  instance_name: Prometheus
  protocols:
  - grpc
  - grpcs
  - http
  - https
"""
    write_file(f"{global_plugins_dir}/prometheus.yaml", content)
