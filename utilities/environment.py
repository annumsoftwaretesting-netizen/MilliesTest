import os

from utilities.config_reader import ConfigReader


class Environment:

    @staticmethod
    def get_authenticated_url():

        config = ConfigReader.get_config()

        username = os.environ.get(
            "UAT_USERNAME",
            config.get("username", "")
        )

        password = os.environ.get(
            "UAT_PASSWORD",
            config.get("password", "")
        )

        if not username or not password:
            raise RuntimeError(
                "UAT credentials not set. Export UAT_USERNAME "
                "and UAT_PASSWORD environment variables."
            )

        return (
            f"https://{username}:"
            f"{password}@"
            f"{config['uat_url']}"
        )
