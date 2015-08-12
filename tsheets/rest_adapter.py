import requests
import error
import logging
import logger

class RestAdapter(object):
    def __init__(self):
        self.logger = logging.getLogger('tsheets_logger')

    def get(self, url, params, headers):
        self.logger.debug("GET {} {} {}".format(url, params, headers))
        response = None
        try:
            response = requests.get(url, params=params, headers=headers)
            print response.content
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise error.TSheetsError(e, response)

    def post(self, url, data, options):
        self.logger.debug("GET {} {} {}".format(url, data, options))
        try:
            response = requests.post(url, body=data, headers = options)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise error.TSheetsError(e)

    def put(self, url, data, options):
        self.logger.debug("GET {} {} {}".format(url, data, options))
        try:
            response = requests.put(url, body = data, headers = options)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise error.TSheetsError(e)

    def delete(self, url, data, options):
        self.logger.debug("DELETE {} {} {}".format(url, data, options))
        try:
            response = requests.delete(url, params={ "ids": data['ids'].join(",") }, headers = options)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise error.TSheetsError(e)