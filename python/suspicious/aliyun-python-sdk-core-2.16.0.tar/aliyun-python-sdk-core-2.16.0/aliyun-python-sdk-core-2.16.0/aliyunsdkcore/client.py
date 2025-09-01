class AcsClient:
    LOG_FORMAT = '%(thread)d %(asctime)s %(name)s %(levelname)s %(message)s'

    def __init__(
            self,
            ak=None,
            secret=None,
            region_id="cn-hangzhou",
            auto_retry=True,
            max_retry_time=None,
            user_agent=None,
            port=80,
            connect_timeout=None,
            timeout=None,
            public_key_id=None,
            private_key=None,
            session_period=3600,
            credential=None,
            debug=False,
            verify=None,
            pool_size=10,
            proxy=None
    ):
        """
        constructor for AcsClient
        :param ak: String, access key id
        :param secret: String, access key secret
        :param region_id: String, region id
        :param auto_retry: Boolean
        :param max_retry_time: Number
        :param pool_size:
            In a multithreaded environment,
            you should set the maxsize of the pool to a higher number,
            such as the number of threads.
        :return:
        """

        self._max_retry_num = max_retry_time
        self._auto_retry = auto_retry
        self._ak = ak
        self._secret = secret
        self._region_id = region_id
        self._user_agent = user_agent
        self._port = port
        self._connect_timeout = connect_timeout
        self._read_timeout = timeout
        self._extra_user_agent = {}
        self._verify = verify
        credential = {
            'ak': ak,
            'secret': secret,
            'public_key_id': public_key_id,
            'private_key': private_key,
            'session_period': session_period,
            'credential': credential,
        }
        self._signer = SignerFactory.get_signer(
            credential, region_id, self._implementation_of_do_action, debug)
        self._endpoint_resolver = DefaultEndpointResolver(self)

        self.session = Session()
        self.session.mount('https://', HTTPAdapter(DEFAULT_POOL_CONNECTIONS, pool_size))
        self.session.mount('http://', HTTPAdapter(DEFAULT_POOL_CONNECTIONS, pool_size))

        if self._auto_retry:
            self._retry_policy = retry_policy.get_default_retry_policy(
                max_retry_times=self._max_retry_num)
        else:
            self._retry_policy = retry_policy.NO_RETRY_POLICY

        self.proxy = proxy

    def get_region_id(self):
        return self._region_id

    def get_access_key(self):
        return self._ak

    def get_access_secret(self):
        return self._secret

    def is_auto_retry(self):
        return self._auto_retry

    def get_max_retry_num(self):
        return self._max_retry_num

    def get_user_agent(self):
        return self._user_agent

    def get_verify(self):
        return self._verify

    def set_region_id(self, region):
        self._region_id = region

    def set_max_retry_num(self, num):
        self._max_retry_num = num

    def set_auto_retry(self, flag):
        """
        set whether or not the client perform auto-retry
        :param flag: Booleans
        :return: None
        """
        self._auto_retry = flag

    def set_user_agent(self, agent):
        """
        User agent set to client will overwrite the request setting.
        :param agent:
        :return:
        """
        self._user_agent = agent

    def set_verify(self, verify):
        self._verify = verify

    def append_user_agent(self, key, value):
        self._extra_user_agent.update({key: value})

    @staticmethod
    def user_agent_header():
        base = '%s (%s %s;%s)' \
               % ('AlibabaCloud',
                  platform.system(),
                  platform.release(),
                  platform.machine()
                  )
        return base

    @staticmethod
    def default_user_agent():
        default_agent = OrderedDict()
        default_agent['Python'] = platform.python_version()
        default_agent['Core'] = __import__('aliyunsdkcore').__version__
        default_agent['python-requests'] = __import__(
            'aliyunsdkcore.vendored.requests.__version__', globals(), locals(),
            ['vendored', 'requests', '__version__'], 0).__version__

        return CaseInsensitiveDict(default_agent)

    def client_user_agent(self):
        client_user_agent = {}
        if self.get_user_agent() is not None:
            client_user_agent.update({'client': self.get_user_agent()})
        else:
            client_user_agent.update(self._extra_user_agent)

        return CaseInsensitiveDict(client_user_agent)

    def get_port(self):
        return self._port

    def get_location_service(self):
        return None

    @staticmethod
    def merge_user_agent(default_agent, extra_agent):
        if default_agent is None:
            return extra_agent

        if extra_agent is None:
            return default_agent
        user_agent = default_agent.copy()
        for key, value in extra_agent.items():
            if key not in default_agent:
                user_agent[key] = value
        return user_agent

    def __del__(self):
        if self.session:
            self.session.close()

    def handle_extra_agent(self, request):
        client_agent = self.client_user_agent()
        request_agent = request.request_user_agent()

        if client_agent is None:
            return request_agent

        if request_agent is None:
            return client_agent
        for key in request_agent:
            if key in client_agent:
                client_agent.pop(key)
        client_agent.update(request_agent)
        return client_agent

    def _make_http_response(self, endpoint, request, read_timeout, connect_timeout,
                            specific_signer=None):
        body_params = request.get_body_params()
        if body_params:
            content_type = request.get_headers().get('Content-Type')
            if content_type and format_type.APPLICATION_JSON in content_type:
                body = json.dumps(body_params)
                request.set_content(body)
            elif content_type and format_type.APPLICATION_XML in content_type:
                body = aliyunsdkcore.utils.parameter_helper.to_xml(body_params)
                request.set_content(body)
            else:
                body = urlencode(body_params)
                request.set_content(body)
                request.set_content_type(format_type.APPLICATION_FORM)
        elif request.get_content() and "Content-Type" not in request.get_headers():
            request.set_content_type(format_type.APPLICATION_OCTET_STREAM)
        method = request.get_method()

        if isinstance(request, CommonRequest):
            request.trans_to_acs_request()

        signer = self._signer if specific_signer is None else specific_signer
        header = request.get_headers()
        signed_header, url = signer.sign(self._region_id, request)
        header.update(signed_header)

        base = self.user_agent_header()

        extra_agent = self.handle_extra_agent(request)
        default_agent = self.default_user_agent()
        user_agent = self.merge_user_agent(default_agent, extra_agent)

        for key, value in user_agent.items():
            base += ' %s/%s' % (key, value)
        header['User-Agent'] = base

        header['x-sdk-client'] = 'python/2.0.0'

        protocol = request.get_protocol_type()
        response = HttpResponse(
            endpoint,
            url,
            method,
            header,
            protocol,
            request.get_content(),
            self._port,
            read_timeout=read_timeout,
            connect_timeout=connect_timeout,
            verify=self.get_verify(),
            session=self.session,
            proxy=self.proxy
        )
        if body_params:
            response.set_content(body, "utf-8", request.get_headers().get('Content-Type'))
        return response

    def _implementation_of_do_action(self, request, signer=None):
        if not isinstance(request, AcsRequest):
            raise ClientException(
                error_code.SDK_INVALID_REQUEST,
                error_msg.get_msg('SDK_INVALID_REQUEST'))

        # modify Accept-Encoding
        request.add_header('Accept-Encoding', 'identity')

        if request.endpoint:
            endpoint = request.endpoint
        else:
            endpoint = self._resolve_endpoint(request)

        return self._handle_retry_and_timeout(endpoint, request, signer)

    def implementation_of_do_action(self, request, signer=None):
        # keep compatible
        warnings.warn(
            "implementation_of_do_action() method is deprecated",
            DeprecationWarning)

        status, headers, body, exception = self._implementation_of_do_action(request, signer)
        return status, headers, body

    def _add_request_client_token(self, request):
        if hasattr(request, "set_ClientToken") and hasattr(request, "get_ClientToken"):
            client_token = request.get_ClientToken()
            if not client_token:
                # ClientToken has not been set
                client_token = aliyunsdkcore.utils.parameter_helper.get_uuid()  # up to 60 chars
                request.set_ClientToken(client_token)