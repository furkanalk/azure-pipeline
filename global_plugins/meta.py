from functions import write_file, create_dir_if_not_exists

def generate_meta_config(workspace_name):
    global_plugins_dir = f"{workspace_name}/global-plugins"
    create_dir_if_not_exists(global_plugins_dir)

    content = """_format_version: "3.0"
_workspace: ${{ env "DECK_WORKSPACE" }}

_info:
  select_tags:
    - global-plugin
    - ${{ env "DECK_ENV_NAME" }}
"""
    write_file(f"{global_plugins_dir}/meta.yaml", content)
