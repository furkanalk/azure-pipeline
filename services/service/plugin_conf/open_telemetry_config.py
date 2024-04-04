from functions import write_file, create_dir_if_not_exists

def generate_open_telemetry_config(service_name, workspace_name):
    plugin_conf_dir = f"{workspace_name}/services/{service_name.lower()}/plugin-conf"
    create_dir_if_not_exists(plugin_conf_dir)
    
    content = f"""_plugin_configs:
  open-telemetry-{service_name.lower()}-config:
    endpoint: http://jaeger-collector.observability.svc.cluster.local:4318/v1/traces
    header_type: preserve
    resource_attributes:
      service.name: ${{{{ env "DECK_SERVICE_TAG" }}}}
"""
    write_file(f"{plugin_conf_dir}/open-telemetry-{service_name.lower()}-config.yaml", content)

