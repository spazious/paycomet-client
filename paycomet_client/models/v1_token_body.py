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

class V1TokenBody(object):
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
        'terminal': 'int',
        'method_id': 'int',
        'order': 'str',
        'product_description': 'str',
        'language': 'str'
    }

    attribute_map = {
        'terminal': 'terminal',
        'method_id': 'methodId',
        'order': 'order',
        'product_description': 'productDescription',
        'language': 'language'
    }

    def __init__(self, terminal=None, method_id=None, order=None, product_description=None, language='es'):  # noqa: E501
        """V1TokenBody - a model defined in Swagger"""  # noqa: E501
        self._terminal = None
        self._method_id = None
        self._order = None
        self._product_description = None
        self._language = None
        self.discriminator = None
        self.terminal = terminal
        self.method_id = method_id
        self.order = order
        if product_description is not None:
            self.product_description = product_description
        if language is not None:
            self.language = language

    @property
    def terminal(self):
        """Gets the terminal of this V1TokenBody.  # noqa: E501

        Product or terminal Id.  # noqa: E501

        :return: The terminal of this V1TokenBody.  # noqa: E501
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this V1TokenBody.

        Product or terminal Id.  # noqa: E501

        :param terminal: The terminal of this V1TokenBody.  # noqa: E501
        :type: int
        """
        if terminal is None:
            raise ValueError("Invalid value for `terminal`, must not be `None`")  # noqa: E501

        self._terminal = terminal

    @property
    def method_id(self):
        """Gets the method_id of this V1TokenBody.  # noqa: E501

        PAYCOMET payment method ID.  # noqa: E501

        :return: The method_id of this V1TokenBody.  # noqa: E501
        :rtype: int
        """
        return self._method_id

    @method_id.setter
    def method_id(self, method_id):
        """Sets the method_id of this V1TokenBody.

        PAYCOMET payment method ID.  # noqa: E501

        :param method_id: The method_id of this V1TokenBody.  # noqa: E501
        :type: int
        """
        if method_id is None:
            raise ValueError("Invalid value for `method_id`, must not be `None`")  # noqa: E501

        self._method_id = method_id

    @property
    def order(self):
        """Gets the order of this V1TokenBody.  # noqa: E501

        Reference, will be included in callback.  # noqa: E501

        :return: The order of this V1TokenBody.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this V1TokenBody.

        Reference, will be included in callback.  # noqa: E501

        :param order: The order of this V1TokenBody.  # noqa: E501
        :type: str
        """
        if order is None:
            raise ValueError("Invalid value for `order`, must not be `None`")  # noqa: E501

        self._order = order

    @property
    def product_description(self):
        """Gets the product_description of this V1TokenBody.  # noqa: E501

        Concept, will be included in callback.  # noqa: E501

        :return: The product_description of this V1TokenBody.  # noqa: E501
        :rtype: str
        """
        return self._product_description

    @product_description.setter
    def product_description(self, product_description):
        """Sets the product_description of this V1TokenBody.

        Concept, will be included in callback.  # noqa: E501

        :param product_description: The product_description of this V1TokenBody.  # noqa: E501
        :type: str
        """

        self._product_description = product_description

    @property
    def language(self):
        """Gets the language of this V1TokenBody.  # noqa: E501

        Language for callback translation.  # noqa: E501

        :return: The language of this V1TokenBody.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this V1TokenBody.

        Language for callback translation.  # noqa: E501

        :param language: The language of this V1TokenBody.  # noqa: E501
        :type: str
        """

        self._language = language

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
        if issubclass(V1TokenBody, dict):
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
        if not isinstance(other, V1TokenBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
