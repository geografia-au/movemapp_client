# This is the test_client.py module for movemapp_client package

import unittest
from movemapp_client import MovemappClient
from dotenv import load_dotenv
import os
# load test fixtures
from .fixtures import fixtures

# from unittest import assert


class MovemappClientTest(unittest.TestCase):
    def test_api_key(self):
        # load the .env.test into the environment
        load_dotenv(dotenv_path="./movemapp_client/tests/.env.test")
        # get the API_KEY from the environment
        GEODB_MASTER_API_KEY = os.getenv("GEODB_MASTER_API_KEY")
        GEODB_URL = os.getenv("GEODB_URL")
        TEST_TOKEN = os.getenv("TEST_TOKEN")

        # raise exception if the environment variable is not found
        if GEODB_MASTER_API_KEY is None:
            raise ValueError("GEODB_MASTER_API_KEY is not set")
        if GEODB_URL is None:
            raise ValueError("GEODB_URL is not set")
        if TEST_TOKEN is None:
            raise ValueError("TEST_TOKEN is not set")


        client = MovemappClient(
            geodb_master_api_key=GEODB_MASTER_API_KEY,
            geodb_url=GEODB_URL,
            lga_number="00000"
        )
        result = client.get("datasets")
        api_key = client.get("api_key")
        schema = client.schema

        self.assertEqual(result, fixtures["lga_00000"]["tables"])
        self.assertEqual(api_key, {
            'token': TEST_TOKEN,
            'name': 'mvmp_00000_ro'
        })
        self.assertEqual(schema, "test4movemapp")
