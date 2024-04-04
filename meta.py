import os
from functions import write_file, create_dir_if_not_exists, load_config_from_yaml

def generate_meta(workspace_dir):
    content = """_format_version: "3.0"
_workspace: ${{ env "DECK_WORKSPACE" }}

_info:
  defaults:
    service:
      connect_timeout: 60000
      read_timeout: 60000
      write_timeout: 60000
      retries: 5
    route:
      https_redirect_status_code: 426
      preserve_host: false
      path_handling: v0
      regex_priority: 0
      request_buffering: true
      response_buffering: true
      strip_path: true
      protocols:
      - http
      - https
  select_tags:
  - ${{ env "DECK_SERVICE_TAG" }}-svc
  - ${{ env "DECK_ENV_NAME" }}
"""
    write_file(os.path.join(workspace_dir, 'meta.yaml'), content)


if __name__ == "__main__":
    config = load_config_from_yaml('config.yaml')
    workspace_name = config['workspace'] + '-workspace'
    workspace_dir = f"{workspace_name}/"
    create_dir_if_not_exists(workspace_dir)
    generate_meta(workspace_dir)
