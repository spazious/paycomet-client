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

import paycomet-client
from paycomet-client.api.mirakl_api import MiraklApi  # noqa: E501
from paycomet-client.rest import ApiException


class TestMiraklApi(unittest.TestCase):
    """MiraklApi unit test stubs"""

    def setUp(self):
        self.api = MiraklApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_mirakl_invoices_search(self):
        """Test case for mirakl_invoices_search

        Search Mirakl invoices  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
