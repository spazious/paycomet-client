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

class PreauthCancelBody(object):
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
        'payment': 'V1paymentsorderpreauthcancelPayment'
    }

    attribute_map = {
        'payment': 'payment'
    }

    def __init__(self, payment=None):  # noqa: E501
        """PreauthCancelBody - a model defined in Swagger"""  # noqa: E501
        self._payment = None
        self.discriminator = None
        if payment is not None:
            self.payment = payment

    @property
    def payment(self):
        """Gets the payment of this PreauthCancelBody.  # noqa: E501


        :return: The payment of this PreauthCancelBody.  # noqa: E501
        :rtype: V1paymentsorderpreauthcancelPayment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this PreauthCancelBody.


        :param payment: The payment of this PreauthCancelBody.  # noqa: E501
        :type: V1paymentsorderpreauthcancelPayment
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
        if issubclass(PreauthCancelBody, dict):
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
        if not isinstance(other, PreauthCancelBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
