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

class InlineResponse20032(object):
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
        'operations': 'list[InlineResponse20032Operations]'
    }

    attribute_map = {
        'error_code': 'errorCode',
        'operations': 'operations'
    }

    def __init__(self, error_code=None, operations=None):  # noqa: E501
        """InlineResponse20032 - a model defined in Swagger"""  # noqa: E501
        self._error_code = None
        self._operations = None
        self.discriminator = None
        if error_code is not None:
            self.error_code = error_code
        if operations is not None:
            self.operations = operations

    @property
    def error_code(self):
        """Gets the error_code of this InlineResponse20032.  # noqa: E501


        :return: The error_code of this InlineResponse20032.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this InlineResponse20032.


        :param error_code: The error_code of this InlineResponse20032.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def operations(self):
        """Gets the operations of this InlineResponse20032.  # noqa: E501


        :return: The operations of this InlineResponse20032.  # noqa: E501
        :rtype: list[InlineResponse20032Operations]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this InlineResponse20032.


        :param operations: The operations of this InlineResponse20032.  # noqa: E501
        :type: list[InlineResponse20032Operations]
        """

        self._operations = operations

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
        if issubclass(InlineResponse20032, dict):
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
        if not isinstance(other, InlineResponse20032):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
