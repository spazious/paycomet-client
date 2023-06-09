# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import paycomet_client
from paycomet_client.paths.v1_cards_physical import post  # noqa: E501
from paycomet_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1CardsPhysical(ApiTestMixin, unittest.TestCase):
    """
    V1CardsPhysical unit test stubs
        Tokenize a card by physical encrypted data  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
