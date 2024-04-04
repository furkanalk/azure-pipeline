from functions import write_file, create_dir_if_not_exists
from urllib.parse import urlparse

def generate_request_transformer_config(service_name, route_names, endpoints, workspace_name):
    plugin_conf_dir = f"{workspace_name}/services/{service_name.lower()}/plugin-conf"
    create_dir_if_not_exists(plugin_conf_dir)
    
    for route_name, endpoint in zip(route_names, endpoints):
        path = urlparse(endpoint).path
        content = f"""_plugin_configs:
  request-transformer-{route_name}-config:
    replace:
      body: [ ]
      headers: [ ]
      querystring: [ ]
      uri: {path}
"""
        write_file(f"{plugin_conf_dir}/request-transformer-{route_name}-config.yaml", content)
