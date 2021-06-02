import json

import requests

from worlddata.APIExceptions.WorldDataExceptions import WorldDataException


class WorldDataBase:
    API_path = "/api/rest/zdaly/trends/"

    def __init__(
        self,
        auth_token,
        server_url="https://zdaly.com",
        ssl_verify=True,
        proxies=None,
        timeout=60,
        session=None,
        client_certs=None,
    ):
        self.headers = {}
        self.server_url = server_url
        self.proxies = proxies
        self.ssl_verify = ssl_verify
        self.cert = client_certs
        self.timeout = timeout
        self.req = session or requests
        if not auth_token:
            raise WorldDataException("API Key not provided")
        self.headers["api-key"] = auth_token

        self.headers['Content-type'] = 'application/json'
        self.headers['Accept'] = 'application/json'

    @staticmethod
    def __reduce_kwargs(kwargs):
        if "kwargs" in kwargs:
            for arg in kwargs["kwargs"].keys():
                kwargs[arg] = kwargs["kwargs"][arg]

            del kwargs["kwargs"]
        return kwargs

    def call_api_delete(self, method):
        url = self.server_url + self.API_path + method
        response = self.req.delete(
            url,
            headers=self.headers,
            verify=self.ssl_verify,
            cert=self.cert,
            proxies=self.proxies,
            timeout=self.timeout,
        )
        self.parse_response_codes(response)
        json_data = response.json()
        return json_data['responseEntity']

    def call_api_get(self, method, **kwargs):
        args = self.__reduce_kwargs(kwargs)
        url = self.server_url + self.API_path + method
        # convert to key[]=val1&key[]=val2 for args like key=[val1, val2], else key=val
        params = "&".join(
            "&".join(i + "[]=" + j for j in args[i])
            if isinstance(args[i], list)
            else i + "=" + str(args[i])
            for i in args
        )
        response = self.req.get(
            "%s?%s" % (url, params),
            headers=self.headers,
            verify=self.ssl_verify,
            cert=self.cert,
            proxies=self.proxies,
            timeout=self.timeout,
        )
        self.parse_response_codes(response)
        json_data = response.json()
        return json_data['responseEntity']

    def call_api_post(self, method, files=None, use_json=None, **kwargs):
        reduced_args = self.__reduce_kwargs(kwargs)
        response = self.req.post(
            self.server_url + self.API_path + method,
            json=reduced_args,
            files=files,
            headers=self.headers,
            verify=self.ssl_verify,
            cert=self.cert,
            proxies=self.proxies,
            timeout=self.timeout,
        )
        self.parse_response_codes(response)
        json_data = response.json()
        return json_data['responseEntity']

    @staticmethod
    def parse_response_codes(response):
        """Parses the reponse code and raises a APIConnection error if not 200"""
        if response.status_code == 200:
            return

        json_data = response.json()

        if response.status_code == 400:
            raise WorldDataException(json_data['responseMessage'])

        if response.status_code == 401:
            raise WorldDataException(json_data['responseMessage'])

        if response.status_code == 403:
            raise WorldDataException(json_data['responseMessage'])

        if response.status_code == 404:
            raise WorldDataException("The URI requested is invalid or the requested resource does not exist")

        if response.status_code == 429:
            raise WorldDataException("You are making requests too quickly, slow down and try again.")

        if response.status_code == 500:
            raise WorldDataException("Something unexpected occurred.")

        if response.status_code == 502:
            raise WorldDataException("WorlData service is down")

        if response.status_code == 503:
            raise WorldDataException("WorldData service is up but overloaded with requests")

        else:
            raise WorldDataException(json_data['responseMessage'])
