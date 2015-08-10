
class TSheetsError(Exception):
    """Exception Class to handle the failure of the request."""

    def __init__(self, base_exception=None):
        self.base_exception = base_exception

    def __str__(self):
        if self.base_exception:
            return str(self.base_exception)

        return "An unknown error occurred."


class FilterInvalidValueError(TSheetsError):
    pass