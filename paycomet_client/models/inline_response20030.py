# coding: utf-8

"""
    PAYCOMET REST API

    PAYCOMET API REST for customers.  # noqa: E501

    OpenAPI spec version: 2.99.0
    Contact: tecnico@paycomet.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse20030(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'error_code': 'int',
        'merchant_customer_id': 'str',
        'link': 'str'
    }

    attribute_map = {
        'error_code': 'errorCode',
        'merchant_customer_id': 'merchantCustomerId',
        'link': 'link'
    }

    def __init__(self, error_code=None, merchant_customer_id=None, link=None):  # noqa: E501
        """InlineResponse20030 - a model defined in Swagger"""  # noqa: E501
        self._error_code = None
        self._merchant_customer_id = None
        self._link = None
        self.discriminator = None
        if error_code is not None:
            self.error_code = error_code
        if merchant_customer_id is not None:
            self.merchant_customer_id = merchant_customer_id
        if link is not None:
            self.link = link

    @property
    def error_code(self):
        """Gets the error_code of this InlineResponse20030.  # noqa: E501


        :return: The error_code of this InlineResponse20030.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this InlineResponse20030.


        :param error_code: The error_code of this InlineResponse20030.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def merchant_customer_id(self):
        """Gets the merchant_customer_id of this InlineResponse20030.  # noqa: E501

        Unique identifier of the client of the supplier.  # noqa: E501

        :return: The merchant_customer_id of this InlineResponse20030.  # noqa: E501
        :rtype: str
        """
        return self._merchant_customer_id

    @merchant_customer_id.setter
    def merchant_customer_id(self, merchant_customer_id):
        """Sets the merchant_customer_id of this InlineResponse20030.

        Unique identifier of the client of the supplier.  # noqa: E501

        :param merchant_customer_id: The merchant_customer_id of this InlineResponse20030.  # noqa: E501
        :type: str
        """

        self._merchant_customer_id = merchant_customer_id

    @property
    def link(self):
        """Gets the link of this InlineResponse20030.  # noqa: E501

        Link to redirect the customer to check the bank account  # noqa: E501

        :return: The link of this InlineResponse20030.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this InlineResponse20030.

        Link to redirect the customer to check the bank account  # noqa: E501

        :param link: The link of this InlineResponse20030.  # noqa: E501
        :type: str
        """

        self._link = link

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse20030, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse20030):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
