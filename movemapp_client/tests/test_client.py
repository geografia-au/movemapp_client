# This is the test_client.py module for movemapp_client package

import unittest
from movemapp_client import MovemappClient
from dotenv import load_dotenv
import os
# load test fixtures
from .fixtures import fixtures

# from unittest import assert


class MovemappClientTest(unittest.TestCase):
    # setup before all tests
    @classmethod
    def setUpClass(cls):
        load_dotenv(dotenv_path="./movemapp_client/tests/.env.test")
        cls.geodb_master_api_key = os.getenv("GEODB_MASTER_API_KEY")
        cls.geodb_url = os.getenv("GEODB_URL")
        cls.test_token = os.getenv("TEST_TOKEN")
        if cls.geodb_master_api_key is None:
            raise ValueError("GEODB_MASTER_API_KEY is not set")
        if cls.geodb_url is None:
            raise ValueError("GEODB_URL is not set")
        if cls.test_token is None:
            raise ValueError("TEST_TOKEN is not set")

    def setUp(self):
        # load the .env.test into the environment
        pass

    def test_api_key(self):
        client = MovemappClient(
            geodb_master_api_key=self.geodb_master_api_key,
            geodb_url=self.geodb_url,
            lga_number="00000"
        )
        result = client.get("datasets")
        api_key = client.get("api_key")
        schema = client.schema

        self.assertEqual(result, fixtures["lga_00000"]["tables"])
        self.assertEqual(api_key, {
            'token': self.test_token,
            'name': 'mvmp_00000_ro'
        })
        self.assertEqual(schema, "test4movemapp")

    def test_create_api_key(self):
        lga_number = 99999
        client = MovemappClient(
            geodb_master_api_key=self.geodb_master_api_key,
            geodb_url=self.geodb_url,
            lga_number=lga_number
        )

        # create the api key
        api_key = client.get("api_key")
        # assert that the api key is created and matches the expected dict:
        token = api_key["token"]
        # must be a string of length 22
        self.assertEqual(len(token), 22)

        self.assertEqual(api_key, {
            'token': token,
            'name': f'mvmp_{lga_number}_ro'
        })

        result = client.get("datasets")
        self.assertEqual(result, fixtures["lga_99999"]["tables"])

    def test_delete_api_key(self):

        lga_number = 99999
        client = MovemappClient(
            geodb_master_api_key=self.geodb_master_api_key,
            geodb_url=self.geodb_url,
            lga_number=lga_number
        )

        # create the api key
        api_key = client.get("api_key")
        # assert that the api key is created and matches the expected dict:
        token = api_key["token"]
        # must be a string of length 22
        self.assertEqual(len(token), 22)

        client.delete("api_key")
        # assert that the api key is deleted
        api_key = client.get("api_key")
        # assert that the new api key token is different from the old one
        self.assertNotEqual(api_key["token"], token)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
