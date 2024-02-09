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
from paycomet-client.api.susbcriptions_api import SusbcriptionsApi  # noqa: E501
from paycomet-client.rest import ApiException


class TestSusbcriptionsApi(unittest.TestCase):
    """SusbcriptionsApi unit test stubs"""

    def setUp(self):
        self.api = SusbcriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_subscription(self):
        """Test case for create_subscription

        Create susbcription payment  # noqa: E501
        """
        pass

    def test_edit_subscription(self):
        """Test case for edit_subscription

        Edit susbcription payment.  # noqa: E501
        """
        pass

    def test_info_subscription(self):
        """Test case for info_subscription

        Gets susbcription info. If the susbscription is not a card subscription only the idUser is need. TokenUser is just for card subscriptions.  # noqa: E501
        """
        pass

    def test_remove_subscription(self):
        """Test case for remove_subscription

        Remove susbcription payment. If the susbscription is not a card subscription only the idUser is need. TokenUser is just for card subscriptions.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
