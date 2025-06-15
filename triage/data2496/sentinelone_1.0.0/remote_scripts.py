import os
import logging
from contextlib import ExitStack

from management.common.query_filter import QueryFilter
from management.mgmtsdk_v2.entities.task import Task
from management.mgmtsdk_v2.services.task import TaskQueryFilter
from management.mgmtsdk_v2_1.endpoints import *
from management.mgmtsdk_v2.exceptions import raise_from_response
from management.mgmtsdk_v2_1.entities.remote_script import RemoteScript, RemoteScriptsDownloadLink, \
    RemoteScriptsDownloadLinkError

logger = logging.getLogger('RemoteScripts')


class RemoteScriptsQueryFilter(QueryFilter):
    QUERY_ARGS = {
        'ids': ['eq'],
        'osTypes': ['eq'],
        'scriptType': ['eq'],
        'threatContentHash': ['eq'],
        'tenant': ['eq'],
        'accountIds': ['eq'],
        'siteIds': ['eq'],
        'groupIds': ['eq'],
        'query': ['eq'],
        'limit': ['eq'],
        'cursor': ['eq'],
        'skip': ['eq'],
        'skipCount': ['eq'],
        'sortBy': ['eq'],
        'sortOrder': ['eq'],
    }

    def __init__(self):
        super(RemoteScriptsQueryFilter, self).__init__()


class RemoteScripts(object):
    """Remote Scripts Orchestration service"""

    def __init__(self, client):
        self.client = client

    # Remote scripts
    def get(self, query_filter=None, **script_args):
        """
        Get list of ``scripts`` from the console by filters, default filter is empty

        :type query_filter: RemoteScriptsQueryFilter
        :type script_args: dict
        :rtype: ManagementResponse
        """
        query_params = RemoteScriptsQueryFilter.get_query_params(query_filter, script_args)
        res = self.client.get(endpoint=REMOTE_SCRIPTS_GET_SCRIPTS, params=query_params)
        if res.status_code != 200:
            logger.warning(f"Failed to get remote scripts, response_code: {res.status_code}")
            raise_from_response(res)
        res.data = [RemoteScript(**script) for script in res.data]
        return res

    def add(self, script):
        """
        add remote script
        :param script:
        :rtype: ManagementResponse
        """

        files = dict()
        file_path = script.pop("filePath", "script_test.txt")
        if not os.path.exists(file_path):
            if file_path == 'script_test.txt':
                file = open(file_path, "w")
                file.write("#!/bin/bash")
                file.close()
            else:
                raise FileNotFoundError(f'File {file_path} not found')

        package_path = script.pop("packagePath", None)
        if package_path and not os.path.exists(package_path):
            raise FileNotFoundError(f'File {package_path} not found')

        for key in script:
            files[key] = (None, script[key])

        with ExitStack() as files_context:
            script_fh = files_context.enter_context(open(file_path, 'rb'))
            files['file'] = (os.path.basename(file_path), script_fh, 'application/terminal')
            if package_path:
                package_fh = files_context.enter_context(open(package_path, 'rb'))
                files['packageFile'] = (os.path.basename(package_path), package_fh, 'application/terminal')

            res = self.client.post(endpoint=REMOTE_SCRIPTS_ADD_SCRIPT, files=files)

        if res.status_code != 200:
            logger.warning(f"Failed to add remote script, response_code: {res.status_code}")
            raise_from_response(res)
        res.data = RemoteScript(**res.data)
        return res.data

    def execute(self, script, query_filter=None, **script_args):
        """
        Execute remote script
        :param script:
        :param query_filter:
        :param script_args:
        :rtype: ManagementResponse
        """
        query_params = RemoteScriptsQueryFilter.get_query_params(query_filter, script_args)
        res = self.client.post(endpoint=REMOTE_SCRIPTS_EXECUTE_SCRIPT, query_filter=query_params, data=script)
        if res.status_code != 200:
            logger.warning(f"Failed to execute remote script, response_code: {res.status_code}")
            raise_from_response(res)
        res.data = {"affected": int(res.data.get('affected', 0)), "parentTaskId": res.data.get('parentTaskId', '')}
        return res

    def edit(self, script_id, script_name, script_type, os_types, input_example, input_instructions,
             input_required, script_run_timeout, script_description=None, package_endpoint_expiration=None,
             package_endpoint_expiration_seconds=None):
        """
        Edit remote script
        :param script_id:
        :param script_name:
        :param script_type:
        :param os_types:
        :param input_example:
        :param input_instructions:
        :param input_required:
        :param script_run_timeout:
        :param script_description:
        :param package_endpoint_expiration:
        :param package_endpoint_expiration_seconds:
        :rtype: ManagementResponse
        """

        new_data = {
            'scriptName': script_name,
            'scriptType': script_type,
            'osTypes': os_types,
            'inputExample': input_example,
            'inputInstructions': input_instructions,
            'inputRequired': input_required,
            'scriptRuntimeTimeoutSeconds': script_run_timeout
        }
        if script_description is not None:
            new_data['scriptDescription'] = script_description
        if package_endpoint_expiration is not None:
            new_data['packageEndpointExpiration'] = package_endpoint_expiration
        if package_endpoint_expiration_seconds is not None:
            new_data['packageEndpointExpirationSeconds'] = package_endpoint_expiration_seconds

        res = self.client.put(endpoint=REMOTE_SCRIPTS_EDIT_SCRIPT.format(script_id), data=new_data)
        if res.status_code != 200:
            logger.warning(f"Failed to edit remote script, response_code: {res.status_code}")
            raise_from_response(res)
        res.data = [RemoteScript(**script) for script in res.data]
        return res

    def delete(self, query_filter=None, **script_args):
        """
        Delete remote script
        :param query_filter:
        :param script_args:
        :rtype: ManagementResponse
        """
        query_params = RemoteScriptsQueryFilter.get_query_params(query_filter, script_args)
        res = self.client.delete(endpoint=REMOTE_SCRIPTS_DELETE_SCRIPT, query_filter=query_params, data={})
        if res.status_code != 200:
            logger.warning(f"Failed to delete remote script, response_code: {res.status_code}")
            raise_from_response(res)
        res.data = int(res.data['affected'])
        return res

    def status(self, query_filter=None, **task_args):
        """
        Get list of RSO ``Tasks`` from the console by filters, default filter is empty

        :type query_filter: TaskQueryFilter
        :type task_args: dict
        :rtype: ManagementResponse
        """
        query_params = TaskQueryFilter.get_query_params(query_filter, task_args)
        res = self.client.get(endpoint=REMOTE_SCRIPTS_STATUS, params=query_params)
        if res.status_code != 200:
            logger.warning("Failed to get remote scripts tasks, response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = [Task(**task) for task in res.data]
        return res

    def fetch_files(self, task_ids: [str] = None, computer_names: [str] = None):
        """
        Get a list of download links based on a list of task id's or computer names filter
        Can be only one or the other (task ids or computer name)

        :type: task_ids: array[str]
        :type: computer_names: array[str]
        :rtype: ManagementResponse
        """

        task_ids_computer_names_object = dict()
        if task_ids is not None:
            task_ids_computer_names_object['taskIds'] = task_ids
        if computer_names is not None:
            task_ids_computer_names_object['computerNames'] = computer_names

        res = self.client.post(endpoint=REMOTE_SCRIPTS_FETCH_FILES, data=task_ids_computer_names_object)
        if res.status_code != 200:
            logger.warning("Failed to fetch download links. response_code: {}".format(res.status_code))
            raise_from_response(res)
        res.data = {
                        'download_links': [RemoteScriptsDownloadLink(**link) for link in res.data['download_links']],
                        'errors': [RemoteScriptsDownloadLinkError(**err) for err in res.data['errors']]
                   }
        return res
