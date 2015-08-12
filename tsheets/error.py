
class TSheetsError(Exception):
    """Exception Class to handle the failure of the request."""

    def __init__(self, base_exception=None, response=None):
        print response.content
        self.base_exception = base_exception
        self.response = response

    def __str__(self):
        error_msg = ""

        if self.base_exception:
            error_msg = str(self.base_exception)
        if self.response.status_code == 417:
            try:
                r = self.response.json()
                error = r.get("error", {})
                msg = error.get("message", None)
                error_msg = msg
            except:
                pass
        return str(error_msg)


class FilterInvalidValueError(TSheetsError):
    pass