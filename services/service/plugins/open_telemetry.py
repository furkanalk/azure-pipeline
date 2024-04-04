from functions import write_file, create_dir_if_not_exists

def generate_open_telemetry(workspace_name, service_name):
    actual_workspace_name = workspace_name.replace('-workspace', '')
    plugins_dir = f"{workspace_name}/services/{service_name.lower()}/plugins"
    create_dir_if_not_exists(plugins_dir)

    content = f"""plugins:
- name: opentelemetry
  instance_name: {actual_workspace_name}-OT
  service: ${{{{ env "DECK_SERVICE_TAG" }}}}
  _config: open-telemetry-${{{{ env "DECK_SERVICE_TAG" }}}}-config
"""
    write_file(f"{plugins_dir}/open-telemetry.yaml", content)
