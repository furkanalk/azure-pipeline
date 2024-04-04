from functions import write_file, create_dir_if_not_exists

def generate_http_log_config(workspace_name):
    global_plugins_dir = f"{workspace_name}/global-plugins"
    create_dir_if_not_exists(global_plugins_dir)
    content = """plugins:
- name: http-log
  config:
    content_type: application/json
    custom_fields_by_lua: {}
    flush_timeout: 2
    headers: {}
    http_endpoint: http://logstash-logstash:8080
    keepalive: 60000
    method: POST
    queue:
      initial_retry_delay: 0.01
      max_batch_size: 1
      max_bytes: null
      max_coalescing_delay: 1
      max_entries: 10000
      max_retry_delay: 60
      max_retry_time: 60
    queue_size: 1
    retry_count: 10
    timeout: 10000
  enabled: false
  instance_name: http-log
  protocols:
  - grpc
  - grpcs
  - http
  - https"""
    write_file(f"{global_plugins_dir}/http-log.yaml", content)
