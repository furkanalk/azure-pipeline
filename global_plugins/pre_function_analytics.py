from functions import write_file, create_dir_if_not_exists

def generate_pre_function_analytics_config(workspace_name):
    global_plugins_dir = f"{workspace_name}/global-plugins"
    create_dir_if_not_exists(global_plugins_dir)

    content = """plugins:
- name: pre-function
  config:
    access:
      - kong.log.set_serialize_value("request.body", kong.request.get_raw_body())
      - kong.service.request.enable_buffering()
    body_filter:
      - kong.log.set_serialize_value("response.body", kong.response.get_raw_body())
    certificate: []
    header_filter: []
    log: []
    rewrite: []
    ws_client_frame: []
    ws_close: []
    ws_handshake: []
    ws_upstream_frame: []
  enabled: false
  instance_name: Requestbody-prefunction
  protocols:
  - grpc
  - grpcs
  - http
  - https
"""
    write_file(f"{global_plugins_dir}/pre-function-analytics.yaml", content)
