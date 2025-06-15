import requests, os, json

class NetUtils():
    def run() -> None:
        print("Test run")
    def env_info() -> dict:
        """
        This method enables automatic detection of a public IP-address.
        and retrieval of supporting information for the address.

        Args:
            None

        Returns:
            ip_info (dict): dictionary with details of a public IP-address
            detected for your active Internet connection.
        """

        cur_path = os.environ.get("PATH", "")

        env_info = {
            "env_path": cur_path,
        }
        print(json.dumps(env_info, indent=4))
        return env_info
