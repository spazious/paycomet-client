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

class InlineResponse2006(object):
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
        '_global': 'str',
        'available': 'str',
        'deposit': 'str',
        'error_code': 'int'
    }

    attribute_map = {
        '_global': 'global',
        'available': 'available',
        'deposit': 'deposit',
        'error_code': 'errorCode'
    }

    def __init__(self, _global=None, available=None, deposit=None, error_code=None):  # noqa: E501
        """InlineResponse2006 - a model defined in Swagger"""  # noqa: E501
        self.__global = None
        self._available = None
        self._deposit = None
        self._error_code = None
        self.discriminator = None
        if _global is not None:
            self._global = _global
        if available is not None:
            self.available = available
        if deposit is not None:
            self.deposit = deposit
        if error_code is not None:
            self.error_code = error_code

    @property
    def _global(self):
        """Gets the _global of this InlineResponse2006.  # noqa: E501

        Total balance in the account  # noqa: E501

        :return: The _global of this InlineResponse2006.  # noqa: E501
        :rtype: str
        """
        return self.__global

    @_global.setter
    def _global(self, _global):
        """Sets the _global of this InlineResponse2006.

        Total balance in the account  # noqa: E501

        :param _global: The _global of this InlineResponse2006.  # noqa: E501
        :type: str
        """

        self.__global = _global

    @property
    def available(self):
        """Gets the available of this InlineResponse2006.  # noqa: E501

        Available balance in the account  # noqa: E501

        :return: The available of this InlineResponse2006.  # noqa: E501
        :rtype: str
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this InlineResponse2006.

        Available balance in the account  # noqa: E501

        :param available: The available of this InlineResponse2006.  # noqa: E501
        :type: str
        """

        self._available = available

    @property
    def deposit(self):
        """Gets the deposit of this InlineResponse2006.  # noqa: E501

        Balance withheld in account  # noqa: E501

        :return: The deposit of this InlineResponse2006.  # noqa: E501
        :rtype: str
        """
        return self._deposit

    @deposit.setter
    def deposit(self, deposit):
        """Sets the deposit of this InlineResponse2006.

        Balance withheld in account  # noqa: E501

        :param deposit: The deposit of this InlineResponse2006.  # noqa: E501
        :type: str
        """

        self._deposit = deposit

    @property
    def error_code(self):
        """Gets the error_code of this InlineResponse2006.  # noqa: E501


        :return: The error_code of this InlineResponse2006.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this InlineResponse2006.


        :param error_code: The error_code of this InlineResponse2006.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

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
        if issubclass(InlineResponse2006, dict):
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
        if not isinstance(other, InlineResponse2006):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
