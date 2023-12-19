import requests
import pytest
from test_base import TestBase

# create a class for the endpoint
class TestUsers(TestBase):

    # positive test case as class method
    # @pytest.mark.smoke
    def test_view_user_by_id(self):
        endpoint = f'{self.base_url}/users/10'
        
        response = requests.get(endpoint)
        data = response.json()
        
        assert response.status_code == 200
        assert data['data']['id'] == 10
        assert 'data' in data.keys()
        assert 'support' in data.keys()
        assert len(data['data']['avatar'])> 0
        assert len(data['data']['avatar'])> 0
        assert 'text' in data['support'].keys()
        assert '@' in data['data']['email']
        assert len(data['data']['first_name']) > 0
        assert len(data['data']['last_name']) > 0
        assert 'support' in data.keys() 
        assert len(data['support']['url']) > 0
        assert 'email' in data['data'].keys()

    # data driven test case
    ids = [1, 2, 5, 8, 10]
    @pytest.mark.parametrize('id', ids)
    def test_view_user_by_multiple_ids(self, id):
        endpoint = f'{self.base_url}/users/{id}'
        response = requests.get(endpoint)
        print(response.url)
        
        data = response.json()
        email = data['data']['email']
        print(email)
        assert 'email' in data['data'].keys()
        assert '@' in email
        assert response.status_code == 200



    # negative test case
    def test_view_non_existent_user(self):
        endpoint = f'{self.base_url}/users/100'
        
        response = requests.get(endpoint)
        
        assert response.status_code == 404


    def test_delete_user(self):
        endpoint = f'{self.base_url}/users/10'
        
        response = requests.delete(endpoint)
        
        assert response.status_code == 204
    

    def test_view_all_pages_with_users(self):
        endpoint = f'{self.base_url}/users'
        # params = {'page': 1}

        current_page = 1
        total_pages = 1

        while current_page <= total_pages:
            params = {'page': current_page}
            response = requests.get(endpoint, params=params)
            print(response.url)

            data = response.json()
            total_pages = data['total_pages']
            
            # list which contains 1 dictionary per user
            users = data['data']
            for user in users:
                print(user['email'])
                assert 'email' in user.keys()
            
            current_page += 1
            
    def test_update_user_info(self):
        endpoint = f'{self.base_url}/users/2'
        
        payload = {
        "name": "morpheus",
        "job": "zion resident"
        }
        
        response = requests.put(endpoint, json = payload)
        data = response.json()
        
        assert response.status_code == 200
        assert data['data']['id'] == 2
       





            

