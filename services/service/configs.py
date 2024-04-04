from functions import write_file, create_dir_if_not_exists
from urllib.parse import urlparse

def generate_configs(workspace_name, service_info):
    for service in service_info:
        service_name = service['name']
        service_dir = f"./{workspace_name}/services/{service_name}"
        workspace_name_formatted = workspace_name.replace('-workspace', '')
        create_dir_if_not_exists(service_dir)

        parsed_url = urlparse(service['endpoints'][0])
        host = parsed_url.hostname
        port = parsed_url.port if parsed_url.port else '443'
        protocol = parsed_url.scheme

        routes_configs = "\n"
        for route_name, method, path in zip(service['route']['names'], service['route']['methods'], service['route']['paths']):
            method_part = "\n    methods:\n    - " + "\n    - ".join(method.split(", ")) if method != "ALL" else ""
            path = urlparse(path).path
            routes_configs += f"""
  # {route_name}
  - name: {route_name}{method_part}
    paths:
    - {path}
"""

        configs_yaml_content = f"""# {workspace_name_formatted} - {service_name} Service
services:
- name: ${{{{ env "DECK_SERVICE_TAG" }}}}
  enabled: true
  host: {host}
  port: {port}
  path: /
  protocol: {protocol}
  routes:{routes_configs}
"""
        write_file(f"{service_dir}/configs.yaml", configs_yaml_content.strip())
