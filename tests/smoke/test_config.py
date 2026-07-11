from utilities.config_reader import ConfigReader
 
 
def test_config():
 
    config = ConfigReader.get_config()
 
    print(config)
 
    assert config["uat_url"] != ""