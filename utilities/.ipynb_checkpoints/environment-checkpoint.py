from utilities.config_reader import ConfigReader
 
 
class Environment:
 
    @staticmethod
    def get_authenticated_url():
 
        config = ConfigReader.get_config()
 
        return (
            f"https://{config['username']}:"
            f"{config['password']}@"
            f"{config['uat_url']}"
        )