from functions import load_config_from_yaml
from services.service.plugins.open_telemetry import generate_open_telemetry
from services.service.plugins.request_transformer import generate_request_transformer
from services.service.configs import generate_configs
from services.service.plugin_conf.open_telemetry_config import generate_open_telemetry_config
from services.service.plugin_conf.request_transformer_config import generate_request_transformer_config
import os

def run():
    # Load configuration
    config = load_config_from_yaml('config.yaml')
    workspace_name = config['workspace'] + '-workspace'

    for service in config['service']:
        service_name = service['name']
        service_dir = os.path.join(workspace_name, 'services', service_name.lower())
        plugins_dir = os.path.join(service_dir, 'plugins')

        # Generate open-telemetry.yaml (plugins)
        generate_open_telemetry(workspace_name, service_name)

        # Generate request-transformer.yaml (plugins)
        generate_request_transformer(service['route']['names'], service['endpoints'], plugins_dir)
        
        # Generate configs.yaml (service)
        generate_configs(
        workspace_name=workspace_name,
        service_info=config['service']
        )
        
        # Generate open-telemetry-config (plugin-conf)
        generate_open_telemetry_config(service_name, workspace_name)
        
        # Generate request-transformer-config (plugin-conf)
        generate_request_transformer_config(service_name, service['route']['names'], service['endpoints'], workspace_name)

if __name__ == "__main__":
    run()