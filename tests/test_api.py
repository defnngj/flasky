import unittest
import requests


# About system API test demo
class APIPostsTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:5000/api/v1.0/posts/"
        self.auth = ('testingwtb@126.com', '111111')

    def test_posts_all(self):
        r = requests.get(self.base_url, auth=self.auth)
        result = r.json()
        self.assertEqual(result['count'], 3)

    def test_posts_one(self):
        r = requests.get(self.base_url+"1", auth=self.auth)
        result = r.json()
        self.assertEqual(len(result), 7)


class APITokenTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:5000/api/v1.0/token"
        self.auth = ('testingwtb@126.com', '111111')


    def test_token(self):
        r = requests.get(self.base_url, auth=self.auth)
        result = r.json()
        self.assertEqual(result['expiration'], 3600)



if __name__ == '__main__':
    unittest.main()