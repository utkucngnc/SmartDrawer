import yaml

def read_yaml(config_path: str) -> dict:
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config

def write_yaml(config: dict, config_path: str) -> None:
    with open(config_path, "w") as file:
        yaml.dump(config, file)