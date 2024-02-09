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

class PaymentsPreauthBody(object):
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
        'language': 'str',
        'payment': 'V1paymentspreauthPayment'
    }

    attribute_map = {
        'language': 'language',
        'payment': 'payment'
    }

    def __init__(self, language='es', payment=None):  # noqa: E501
        """PaymentsPreauthBody - a model defined in Swagger"""  # noqa: E501
        self._language = None
        self._payment = None
        self.discriminator = None
        if language is not None:
            self.language = language
        if payment is not None:
            self.payment = payment

    @property
    def language(self):
        """Gets the language of this PaymentsPreauthBody.  # noqa: E501

        ISO2 code of language.  # noqa: E501

        :return: The language of this PaymentsPreauthBody.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this PaymentsPreauthBody.

        ISO2 code of language.  # noqa: E501

        :param language: The language of this PaymentsPreauthBody.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def payment(self):
        """Gets the payment of this PaymentsPreauthBody.  # noqa: E501


        :return: The payment of this PaymentsPreauthBody.  # noqa: E501
        :rtype: V1paymentspreauthPayment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this PaymentsPreauthBody.


        :param payment: The payment of this PaymentsPreauthBody.  # noqa: E501
        :type: V1paymentspreauthPayment
        """

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
        if issubclass(PaymentsPreauthBody, dict):
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
        if not isinstance(other, PaymentsPreauthBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
