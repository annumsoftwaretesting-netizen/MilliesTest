import json
 
 
class ConfigReader:
 
    @staticmethod
    def get_config():
 
        with open(
            "testdata/config.json",
            "r"
        ) as file:
 
            return json.load(file)