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
from paycomet_client.api.form_api import FormApi  # noqa: E501
from paycomet_client.rest import ApiException


class TestFormApi(unittest.TestCase):
    """FormApi unit test stubs"""

    def setUp(self):
        self.api = FormApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_form(self):
        """Test case for form

        Create form view for user capture  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
