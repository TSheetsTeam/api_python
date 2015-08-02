from models.user import User

class UserRepository(object):

    def __init__(self, client):
        self.client = client
        self.url = "users"
        self.model = User

    def where(self):
        print self.url
        result = self.client.get(self.url)
        result = result['results']['users']['2052270']
        print result
        print type(result)
        result_model = User.from_raw(result)
        return result_model