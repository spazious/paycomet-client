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

class InlineResponse20018(object):
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
        'amount': 'str',
        'currency': 'str',
        'method_id': 'int',
        'order': 'str',
        'auth_code': 'str',
        'challenge_url': 'str',
        'id_user': 'int',
        'token_user': 'str',
        'card_country': 'str'
    }

    attribute_map = {
        'error_code': 'errorCode',
        'amount': 'amount',
        'currency': 'currency',
        'method_id': 'methodId',
        'order': 'order',
        'auth_code': 'authCode',
        'challenge_url': 'challengeUrl',
        'id_user': 'idUser',
        'token_user': 'tokenUser',
        'card_country': 'cardCountry'
    }

    def __init__(self, error_code=None, amount=None, currency=None, method_id=None, order=None, auth_code=None, challenge_url=None, id_user=None, token_user=None, card_country=None):  # noqa: E501
        """InlineResponse20018 - a model defined in Swagger"""  # noqa: E501
        self._error_code = None
        self._amount = None
        self._currency = None
        self._method_id = None
        self._order = None
        self._auth_code = None
        self._challenge_url = None
        self._id_user = None
        self._token_user = None
        self._card_country = None
        self.discriminator = None
        if error_code is not None:
            self.error_code = error_code
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if method_id is not None:
            self.method_id = method_id
        if order is not None:
            self.order = order
        if auth_code is not None:
            self.auth_code = auth_code
        if challenge_url is not None:
            self.challenge_url = challenge_url
        if id_user is not None:
            self.id_user = id_user
        if token_user is not None:
            self.token_user = token_user
        if card_country is not None:
            self.card_country = card_country

    @property
    def error_code(self):
        """Gets the error_code of this InlineResponse20018.  # noqa: E501


        :return: The error_code of this InlineResponse20018.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this InlineResponse20018.


        :param error_code: The error_code of this InlineResponse20018.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def amount(self):
        """Gets the amount of this InlineResponse20018.  # noqa: E501


        :return: The amount of this InlineResponse20018.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InlineResponse20018.


        :param amount: The amount of this InlineResponse20018.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this InlineResponse20018.  # noqa: E501


        :return: The currency of this InlineResponse20018.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InlineResponse20018.


        :param currency: The currency of this InlineResponse20018.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def method_id(self):
        """Gets the method_id of this InlineResponse20018.  # noqa: E501


        :return: The method_id of this InlineResponse20018.  # noqa: E501
        :rtype: int
        """
        return self._method_id

    @method_id.setter
    def method_id(self, method_id):
        """Sets the method_id of this InlineResponse20018.


        :param method_id: The method_id of this InlineResponse20018.  # noqa: E501
        :type: int
        """

        self._method_id = method_id

    @property
    def order(self):
        """Gets the order of this InlineResponse20018.  # noqa: E501


        :return: The order of this InlineResponse20018.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this InlineResponse20018.


        :param order: The order of this InlineResponse20018.  # noqa: E501
        :type: str
        """

        self._order = order

    @property
    def auth_code(self):
        """Gets the auth_code of this InlineResponse20018.  # noqa: E501


        :return: The auth_code of this InlineResponse20018.  # noqa: E501
        :rtype: str
        """
        return self._auth_code

    @auth_code.setter
    def auth_code(self, auth_code):
        """Sets the auth_code of this InlineResponse20018.


        :param auth_code: The auth_code of this InlineResponse20018.  # noqa: E501
        :type: str
        """

        self._auth_code = auth_code

    @property
    def challenge_url(self):
        """Gets the challenge_url of this InlineResponse20018.  # noqa: E501


        :return: The challenge_url of this InlineResponse20018.  # noqa: E501
        :rtype: str
        """
        return self._challenge_url

    @challenge_url.setter
    def challenge_url(self, challenge_url):
        """Sets the challenge_url of this InlineResponse20018.


        :param challenge_url: The challenge_url of this InlineResponse20018.  # noqa: E501
        :type: str
        """

        self._challenge_url = challenge_url

    @property
    def id_user(self):
        """Gets the id_user of this InlineResponse20018.  # noqa: E501


        :return: The id_user of this InlineResponse20018.  # noqa: E501
        :rtype: int
        """
        return self._id_user

    @id_user.setter
    def id_user(self, id_user):
        """Sets the id_user of this InlineResponse20018.


        :param id_user: The id_user of this InlineResponse20018.  # noqa: E501
        :type: int
        """

        self._id_user = id_user

    @property
    def token_user(self):
        """Gets the token_user of this InlineResponse20018.  # noqa: E501


        :return: The token_user of this InlineResponse20018.  # noqa: E501
        :rtype: str
        """
        return self._token_user

    @token_user.setter
    def token_user(self, token_user):
        """Sets the token_user of this InlineResponse20018.


        :param token_user: The token_user of this InlineResponse20018.  # noqa: E501
        :type: str
        """

        self._token_user = token_user

    @property
    def card_country(self):
        """Gets the card_country of this InlineResponse20018.  # noqa: E501


        :return: The card_country of this InlineResponse20018.  # noqa: E501
        :rtype: str
        """
        return self._card_country

    @card_country.setter
    def card_country(self, card_country):
        """Sets the card_country of this InlineResponse20018.


        :param card_country: The card_country of this InlineResponse20018.  # noqa: E501
        :type: str
        """

        self._card_country = card_country

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
        if issubclass(InlineResponse20018, dict):
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
        if not isinstance(other, InlineResponse20018):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
