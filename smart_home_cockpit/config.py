import yaml


class Config:
    def __init__(self, config_path):
        self.config_path = config_path
        config_yaml = open(config_path)
        self.parsed_config_yaml = yaml.load(config_yaml, Loader=yaml.FullLoader)

    def get_config(self):
        return self.parsed_config_yaml