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

class MarketplaceTransferBody(object):
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
        'submerchant': 'V1marketplacesplittransferSubmerchant',
        'payment': 'V1marketplacetransferPayment'
    }

    attribute_map = {
        'submerchant': 'submerchant',
        'payment': 'payment'
    }

    def __init__(self, submerchant=None, payment=None):  # noqa: E501
        """MarketplaceTransferBody - a model defined in Swagger"""  # noqa: E501
        self._submerchant = None
        self._payment = None
        self.discriminator = None
        self.submerchant = submerchant
        self.payment = payment

    @property
    def submerchant(self):
        """Gets the submerchant of this MarketplaceTransferBody.  # noqa: E501


        :return: The submerchant of this MarketplaceTransferBody.  # noqa: E501
        :rtype: V1marketplacesplittransferSubmerchant
        """
        return self._submerchant

    @submerchant.setter
    def submerchant(self, submerchant):
        """Sets the submerchant of this MarketplaceTransferBody.


        :param submerchant: The submerchant of this MarketplaceTransferBody.  # noqa: E501
        :type: V1marketplacesplittransferSubmerchant
        """
        if submerchant is None:
            raise ValueError("Invalid value for `submerchant`, must not be `None`")  # noqa: E501

        self._submerchant = submerchant

    @property
    def payment(self):
        """Gets the payment of this MarketplaceTransferBody.  # noqa: E501


        :return: The payment of this MarketplaceTransferBody.  # noqa: E501
        :rtype: V1marketplacetransferPayment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this MarketplaceTransferBody.


        :param payment: The payment of this MarketplaceTransferBody.  # noqa: E501
        :type: V1marketplacetransferPayment
        """
        if payment is None:
            raise ValueError("Invalid value for `payment`, must not be `None`")  # noqa: E501

        self._payment = payment

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
        if issubclass(MarketplaceTransferBody, dict):
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
        if not isinstance(other, MarketplaceTransferBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
