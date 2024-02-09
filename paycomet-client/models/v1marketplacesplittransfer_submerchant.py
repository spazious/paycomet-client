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

class V1marketplacesplittransferSubmerchant(object):
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
        'split_id': 'str',
        'amount': 'float',
        'currency': 'str'
    }

    attribute_map = {
        'split_id': 'splitId',
        'amount': 'amount',
        'currency': 'currency'
    }

    def __init__(self, split_id=None, amount=None, currency=None):  # noqa: E501
        """V1marketplacesplittransferSubmerchant - a model defined in Swagger"""  # noqa: E501
        self._split_id = None
        self._amount = None
        self._currency = None
        self.discriminator = None
        self.split_id = split_id
        self.amount = amount
        self.currency = currency

    @property
    def split_id(self):
        """Gets the split_id of this V1marketplacesplittransferSubmerchant.  # noqa: E501

        Identifier for you to receive split payments  # noqa: E501

        :return: The split_id of this V1marketplacesplittransferSubmerchant.  # noqa: E501
        :rtype: str
        """
        return self._split_id

    @split_id.setter
    def split_id(self, split_id):
        """Sets the split_id of this V1marketplacesplittransferSubmerchant.

        Identifier for you to receive split payments  # noqa: E501

        :param split_id: The split_id of this V1marketplacesplittransferSubmerchant.  # noqa: E501
        :type: str
        """
        if split_id is None:
            raise ValueError("Invalid value for `split_id`, must not be `None`")  # noqa: E501

        self._split_id = split_id

    @property
    def amount(self):
        """Gets the amount of this V1marketplacesplittransferSubmerchant.  # noqa: E501

        Amount of the operation  # noqa: E501

        :return: The amount of this V1marketplacesplittransferSubmerchant.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this V1marketplacesplittransferSubmerchant.

        Amount of the operation  # noqa: E501

        :param amount: The amount of this V1marketplacesplittransferSubmerchant.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this V1marketplacesplittransferSubmerchant.  # noqa: E501

        Currency of the transaction  # noqa: E501

        :return: The currency of this V1marketplacesplittransferSubmerchant.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this V1marketplacesplittransferSubmerchant.

        Currency of the transaction  # noqa: E501

        :param currency: The currency of this V1marketplacesplittransferSubmerchant.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

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
        if issubclass(V1marketplacesplittransferSubmerchant, dict):
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
        if not isinstance(other, V1marketplacesplittransferSubmerchant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
