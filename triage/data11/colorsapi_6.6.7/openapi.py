import yaml
import re
from flask import request
from .logger import Logger
from .exceptions import Http406Exception, Http400Exception
from .oasschema import validate


class OpenAPI:
    def __init__(self, appname, endpoint="/openapi.json", openApiFile="conf/openapi.yaml"):
        self.endpoint = endpoint
        self._pattern = re.compile(r"<([^<]*:)?([^<]*)>")
        self._replace = r"{\2}"
        self._doc = dict()

        self.spec = dict()
        self.spec["info"] = dict()
        self.spec["paths"] = dict()

        try:
            with open(openApiFile) as f:
                data = yaml.load(f)
                if data:
                    self.spec.update(data)
                    if "title" not in self.spec["info"]:
                        self.spec["info"]["title"] = "{} API Specifications".format(appname)
                    if "version" not in self.spec["info"]:
                        self.spec["info"]["version"] = "1.0.0"
                Logger.info("'{}' loaded".format(openApiFile))
        except FileNotFoundError:
            pass

        self.spec["openapi"] = "3.0.0"

    def addEndpoint(self, rule, methods, docstring, funcName):
        if docstring:
            clean = re.sub(self._pattern, self._replace, rule)
            self.spec["paths"][clean] = dict()
            common_responses = dict()
            docs = docstring.split("---")

            try:
                once = True
                idx = 0
                for doc in docs:
                    yl = yaml.load(doc)
                    if "responses" in yl:
                        yl["responses"].update(common_responses)
                        self.spec["paths"][clean][methods[idx].lower()] = yl
                        if idx < len(methods) - 1:
                            idx += 1
                    elif once:
                        common_responses = yl.pop('common_responses', dict())
                        self.spec["paths"][clean] = yl
                    once = False
                self._doc[funcName] = self.spec["paths"][clean]
            except:
                Logger.error('"Invalide OpenAPI Spec for endpoint "{}" {}'.format(rule, methods))

    def check(self, funcName, method, *args, **kwargs):
        schemas = self.spec.get("components", {})

        try:
            doc = self._doc[funcName][method.lower()]
        except:
            Logger.error("OpenAPI Specifications not found for {} on route def ''{}()''".format(method, funcName))
            return

        body = doc.get("requestBody", None)
        if body:
            dataRequired = body.get("required", False)

            keys = body["content"].keys()
            if len(keys) > 1:
                Logger.error("OpenAPI Specifications marlformed body content for {} on route def '{}()'".format(method, funcName))
                return
            contentType = list(keys)[0]
            schema = (body["content"][contentType]).get("schema", None)

            if not schema:
                Logger.error("OpenAPI Specifications body content schema missing for {} on route def '{}()'".format(method, funcName))
                return

            # NOTE if contentType != Accept in request.headers, return Http406Exception
            schema["components"] = schemas
            if contentType == "application/json":
                data = request.get_json()
                if (not data and dataRequired) or not validate(data, schema):
                    return Http400Exception

        # print(doc)
        # TODO validate query (/?name=toto) 400
        # TODO validate args (/<args>/) 400 & *args, **kwargs
        # if "parameters" in self._doc[funcName][method.lower()]:
        #    pass

    def fake(self, funcName, method):
        try:
            # TODO parcourir la doc pour trouver une request valide (reponse 200 ou < 300)
            return str(self._doc[funcName][method.lower()]["responses"])
        except:
            # TODO raise error 500 : OpenAPI Specifications not found
            return "Fake data"
