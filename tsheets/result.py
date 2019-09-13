class Result(object):

    def __init__(self, code, body):
        self.code = code
        self.body = body

    def is_success(self):
        return self.code == 200 and self._get_status_code() == 200

    def _get_status_code(self):
        try:
            status_code = list(self.body['results'].values())[0].values()[0]['_status_code']
            return status_code
        except:
            return 0

    def message(self):
        try:
            message = list(self.body['results'].values())[0].values()[0]['_status_extra']
            return "Unexpected API response - inspect result body. Exception Message: {}".format(message)
        except:
            return ""