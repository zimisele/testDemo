import unittest
import json
from app import app

class TestGitHubAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_get_user_gists(self):
        """Test the API response for a valid GitHub user."""
        response = self.client.get('/octocat')
        self.assertEqual(response.status_code, 200)
        
        gists = json.loads(response.data)
        self.assertIsInstance(gists, list)
    
    def test_user_not_found(self):
        """Test the API response when a user is not found."""
        response = self.client.get('/nonexistentuser')
        self.assertEqual(response.status_code, 400)
        
        error_message = json.loads(response.data)
        self.assertEqual(error_message['error'], 'Unable to fetch gists for the specified user')

if __name__ == '__main__':
    unittest.main()
