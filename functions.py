import os

def create_dir_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_file(path, content):
    with open(path, 'w') as file:
        file.write(content)

def extract_path_portion(url):
    return '/' + '/'.join(url.split('/')[3:])

def load_config_from_yaml(filename):
    import yaml
    with open(filename, 'r') as file:
        return yaml.safe_load(file)
