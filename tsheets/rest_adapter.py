import requests
import error

class RestAdapter(object):

    def get(self, url, params, headers):
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise error.TSheetsError(e)

    def post(self, url, data, options):
        # print "POST #{url} (#{options.inspect}) - #{data.inspect}" if Typhoeus::Config.verbose
        try:
            response = requests.post(url, body = data, headers = options)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise error.TSheetsError(e)

    def put(self, url, data, options):
        # print "PUT #{url} (#{options.inspect}) - #{data.inspect}" if Typhoeus::Config.verbose
        try:
            response = requests.put(url, body = data, headers = options)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise error.TSheetsError(e)

    def delete(self, url, data, options):
        # print "DELETE #{url} (#{options.inspect}) - #{data.inspect}" if Typhoeus::Config.verbose
        try:
            response = requests.delete(url, params={ "ids": data['ids'].join(",") }, headers = options)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise error.TSheetsError(e)