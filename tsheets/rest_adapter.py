import requests
import error
import logging
import logger
import json


class RestAdapter(object):
    def __init__(self):
        self.logger = logging.getLogger('tsheets_logger')

    def get(self, url, params, headers):
        self.logger.debug("GET {} {} {}".format(url, params, headers))
        response = None
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            if response is not None:
                if response.status_code == 417:
                    raise error.TSheetsExpectedError(e, response)
            raise error.TSheetsError(e)

    def post(self, url, data, options):
        self.logger.debug("POST {} {} {}".format(url, data, options))
        response = None
        try:
            print json.dumps(data)
            options.update({'Content-type': 'application/json'})
            response = requests.post(url, json=data, headers=options)
            response.raise_for_status()
            print response.content
            return response
        except requests.exceptions.RequestException as e:
            if response is not None:
                if response.status_code == 417:
                    raise error.TSheetsExpectedError(e, response)
            raise error.TSheetsError(e)

    def put(self, url, data, options):
        self.logger.debug("PUT {} {} {}".format(url, data, options))
        response = None
        try:
            print json.dumps(data)
            options.update({'Content-type': 'application/json'})
            response = requests.put(url, json=data, headers=options)
            response.raise_for_status()
            print response.content
            return response
        except requests.exceptions.RequestException as e:
            if response is not None:
                if response.status_code == 417:
                    raise error.TSheetsExpectedError(e, response)
            raise error.TSheetsError(e)

    def delete(self, url, data, options):
        self.logger.debug("DELETE {} {} {}".format(url, data, options))
        try:
            ids_to_delete = ','.join(str(id) for id in data['ids'])
            print ids_to_delete
            response = requests.delete(url, params={"ids":ids_to_delete }, headers=options)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise error.TSheetsError(e)