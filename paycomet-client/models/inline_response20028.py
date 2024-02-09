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

class InlineResponse20028(object):
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
        'order': 'str',
        'submerchant': 'InlineResponse20028Submerchant'
    }

    attribute_map = {
        'error_code': 'errorCode',
        'order': 'order',
        'submerchant': 'submerchant'
    }

    def __init__(self, error_code=None, order=None, submerchant=None):  # noqa: E501
        """InlineResponse20028 - a model defined in Swagger"""  # noqa: E501
        self._error_code = None
        self._order = None
        self._submerchant = None
        self.discriminator = None
        if error_code is not None:
            self.error_code = error_code
        if order is not None:
            self.order = order
        if submerchant is not None:
            self.submerchant = submerchant

    @property
    def error_code(self):
        """Gets the error_code of this InlineResponse20028.  # noqa: E501


        :return: The error_code of this InlineResponse20028.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this InlineResponse20028.


        :param error_code: The error_code of this InlineResponse20028.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def order(self):
        """Gets the order of this InlineResponse20028.  # noqa: E501


        :return: The order of this InlineResponse20028.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this InlineResponse20028.


        :param order: The order of this InlineResponse20028.  # noqa: E501
        :type: str
        """

        self._order = order

    @property
    def submerchant(self):
        """Gets the submerchant of this InlineResponse20028.  # noqa: E501


        :return: The submerchant of this InlineResponse20028.  # noqa: E501
        :rtype: InlineResponse20028Submerchant
        """
        return self._submerchant

    @submerchant.setter
    def submerchant(self, submerchant):
        """Sets the submerchant of this InlineResponse20028.


        :param submerchant: The submerchant of this InlineResponse20028.  # noqa: E501
        :type: InlineResponse20028Submerchant
        """

        self._submerchant = submerchant

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
        if issubclass(InlineResponse20028, dict):
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
        if not isinstance(other, InlineResponse20028):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other