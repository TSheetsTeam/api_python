import requests
from requests import HTTPError
from models.user import User

class TSheets:
    def __init__(self, access_token):
        self.base_url = 'https://rest.tsheets.com/api/v1/'
        self._access_token = access_token
        self.auth_options = {'Authorization': "Bearer {}".format(access_token)}

        self.session = requests.Session()
        self.session.headers.update(self.auth_options)
        url = self.base_url + 'users'

        try:
            response = self.session.get(url)
            response.raise_for_status()
        except HTTPError as e:
            print e

    def _get(self, model_class, **kwargs):
        url = self.base_url + model_class.endpoint
        params = {}
        result = []
        params.update(**kwargs)

        try:
            response = self.session.get(url, params = params)
            if response.status_code == 200:
               json_output = response.json()['results'][model_class.endpoint]

               if hasattr(json_output, 'values'):
                   objects = json_output.values()
               else:
                   objects = json_output

               for item in objects:
                   print item
                   instance = model_class(api=self, **item)
                   result.append(instance)
               return result
            else:
                raise Exception("Status Code is not 200!")
        except Exception as e:
            print e

    def list_users(self, **kwargs):
        """
        Retrieves the list of users associated with your company
        """
        return self._get(User)

    def list_timesheets(self, **kwargs):
        """
        Retrieves the list of timesheets associated with your company
        """
        pass
