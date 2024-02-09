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
from paycomet-client.api.ivr_api import IVRApi  # noqa: E501
from paycomet-client.rest import ApiException


class TestIVRApi(unittest.TestCase):
    """IVRApi unit test stubs"""

    def setUp(self):
        self.api = IVRApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_session(self):
        """Test case for check_session

        Checks an IVR session  # noqa: E501
        """
        pass

    def test_get_session(self):
        """Test case for get_session

        Creates an IVR session  # noqa: E501
        """
        pass

    def test_session_cancel(self):
        """Test case for session_cancel

        Cancel an IVR session  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
