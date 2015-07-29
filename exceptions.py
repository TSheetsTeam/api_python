from exceptions import Exception


class TsheetsError(Exception):

    def __init__(self, response=None):
        self.status_code = response.code
        self.error_message = response.body

    def __str__(self):
        return '{0}: {1}'.format(self.status_code, self.error_message)


