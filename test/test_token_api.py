# coding: utf-8

"""
    PAYCOMET REST API

    PAYCOMET API REST for customers.  # noqa: E501

    OpenAPI spec version: 2.99.0
    Contact: tecnico@paycomet.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import paycomet_client
from paycomet_client.api.token_api import TokenApi  # noqa: E501
from paycomet_client.rest import ApiException


class TestTokenApi(unittest.TestCase):
    """TokenApi unit test stubs"""

    def setUp(self):
        self.api = TokenApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_token(self):
        """Test case for add_token

        Tokenizes an APM.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
