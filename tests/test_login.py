import requests
from test_base import TestBase

# create a class for the endpoint
class TestLogin(TestBase):

    # positive test case as class method
    def test_login_with_valid_credentials(self):
        endpoint = f'{self.base_url}/login'
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "test"
            }
        
        response = requests.post(endpoint, json=payload)
        data = response.json()

        print(data)

        assert response.status_code == 200

