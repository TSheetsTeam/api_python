import json
import requests
import logging
import exceptions

DEFAULT_API_VERSION = 'v1'
DEFAULT_BASE_URL = 'https://rest.tsheets.com/api/v1/'

class HTTPClient(object):

    def __init__(self, url=DEFAULT_BASE_URL, api_version=DEFAULT_API_VERSION,
                 access_token=None, headers=None, query_params=None):
        self.url = url
        self._access_token = access_token
        self.auth_options = {'Authorization': "Bearer {}".format(self._access_token)}
        self.session = requests.Session()
        self.session.headers.update(self.auth_options)

    def verify_response_status(self, response, expected_code=200):
        if response.status_code != expected_code:
            self._raise_client_error(response)

    def _do_request(self, requests_method, request_url, params, headers, expected_status_code):
        response = requests_method(request_url,
                                   params=params,
                                   headers=headers)

        if response.status_code != expected_status_code:
            raise exceptions.TsheetsError(response)
        print "self.url in _do_request "+self.url
        return response.json()



    def do_request(self,
                   requests_method,
                   url,
                   params=None,
                   headers=None,
                   expected_status_code=None):
        request_url = '{0}{1}'.format(self.url, url)
        print request_url
        print "self.url in do_request "+self.url
        # build headers
        headers = headers or {}

        # build query params
        params = params or {}

        return self._do_request(
            requests_method=requests_method, request_url=request_url,
            params=params, headers=headers, expected_status_code=expected_status_code)

    def get(self, url, params=None, headers=None):
        if not params:
            params = {}
        expected_status_code = 200
        print "self.url in get "+self.url
        print url
        return self.do_request(self.session.get,
                               url,
                               params=params,
                               headers=headers,
                               expected_status_code=expected_status_code)

    @staticmethod
    def _raise_client_error(response, url=None):
        try:
            result = response.json()
        except Exception:
            message = response.content
            if url:
                message = '{0} [{1}]'.format(message, url)
            error_msg = '{0}: {1}'.format(response.status_code, message)
            raise exceptions.TsheetsError(
                error_msg)