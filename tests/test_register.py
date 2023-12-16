import requests
from test_base import TestBase

# create a class for the endpoint
class TestRegister(TestBase):

    # positive test case as class method
    def test_register(self):
        endpoint = f'{self.base_url}/register'
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "test"
            }
        response = requests.post(endpoint, json=payload)
        data = response.json()
        
        print(data)
        assert response.status_code == 200
        assert 'id' in data.keys()
        assert 'token' in data
        assert type(data['token']) == str

    # negative test case
    def test_register_with_missing_password(self):
        endpoint = f'{self.base_url}/register'
        payload = {
            "email": "eve.holt@reqres.in"
            }
        response = requests.post(endpoint, json=payload)
        data = response.json()
        
        print(data)
        assert response.status_code == 400
        assert data['error'] == 'Missing password' 
    