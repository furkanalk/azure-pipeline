from functions import load_config_from_yaml
from global_plugins.http_log import generate_http_log_config
from global_plugins.meta import generate_meta_config
from global_plugins.prometheus import generate_prometheus_config
from global_plugins.pre_function_analytics import generate_pre_function_analytics_config

def run():
    # Load configuration
    config = load_config_from_yaml('config.yaml')
    workspace_name = config['workspace'] + '-workspace'

    # Generate configurations for global plugins
    generate_http_log_config(workspace_name)
    generate_meta_config(workspace_name)
    generate_prometheus_config(workspace_name)
    generate_pre_function_analytics_config(workspace_name)

if __name__ == "__main__":
    run()
