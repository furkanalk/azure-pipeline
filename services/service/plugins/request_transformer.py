from functions import write_file, extract_path_portion
import os

def generate_request_transformer(routes, endpoints, plugin_conf_dir):
    content_lines = ["plugins:"]
    for route_name, endpoint in zip(routes, endpoints):
        extract_path_portion(endpoint)  
        content_lines.append(f"""- name: request-transformer
  instance_name: {route_name}-RT
  route: {route_name}
  _config: request-transformer-{route_name}-config\n""")

    content = "\n".join(content_lines).strip()
    write_file(os.path.join(plugin_conf_dir, 'request-transformer.yaml'), content)
