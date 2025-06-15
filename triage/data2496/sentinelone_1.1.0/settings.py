import logging
from management.mgmtsdk_v2_1.endpoints import *
from management.mgmtsdk_v2.services.settings import Settings as Settings_v2
from management.mgmtsdk_v2.exceptions import raise_from_response


logger = logging.getLogger('Settings_2.1')


class Settings(Settings_v2):
    """Users service"""

    def __init__(self, client):
        self.client = client
        super(Settings_v2, self).__init__()

    def get_user_preferences(self):
        """
        Get current user preferences (for the logged in user). Returns an empty object if preferences were never saved before.

        :rtype: ManagementResponse
        """
        res = self.client.get(endpoint=USER_PREFERENCES)
        if res.status_code != 200:
            logger.warning("Failed to get user preferences, response_code: {}".format(res.json))
            raise_from_response(res)
        return res

    def set_user_preferences(self, preferences):
        """
        Set user preferences (for the logged in user). "data" attribute should contain a valid JSON object.

        :rtype: ManagementResponse
        """
        res = self.client.put(endpoint=USER_PREFERENCES, data=preferences.to_json())
        if res.status_code != 200:
            logger.warning("Failed to set user preferences, response_code: {}".format(res.status_code))
            raise_from_response(res)
        return res
