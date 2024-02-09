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

class PhysicalEditBody(object):
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
        'provider_id': 'int',
        'merchant_id': 'str',
        'terminal_id': 'str',
        'id_user': 'int',
        'token_user': 'str',
        'cof_identifier': 'str'
    }

    attribute_map = {
        'terminal': 'terminal',
        'provider_id': 'providerId',
        'merchant_id': 'merchantId',
        'terminal_id': 'terminalId',
        'id_user': 'idUser',
        'token_user': 'tokenUser',
        'cof_identifier': 'cofIdentifier'
    }

    def __init__(self, terminal=None, provider_id=None, merchant_id=None, terminal_id=None, id_user=None, token_user=None, cof_identifier=None):  # noqa: E501
        """PhysicalEditBody - a model defined in Swagger"""  # noqa: E501
        self._terminal = None
        self._provider_id = None
        self._merchant_id = None
        self._terminal_id = None
        self._id_user = None
        self._token_user = None
        self._cof_identifier = None
        self.discriminator = None
        self.terminal = terminal
        self.provider_id = provider_id
        self.merchant_id = merchant_id
        self.terminal_id = terminal_id
        self.id_user = id_user
        self.token_user = token_user
        if cof_identifier is not None:
            self.cof_identifier = cof_identifier

    @property
    def terminal(self):
        """Gets the terminal of this PhysicalEditBody.  # noqa: E501

        Product or terminal Id.  # noqa: E501

        :return: The terminal of this PhysicalEditBody.  # noqa: E501
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this PhysicalEditBody.

        Product or terminal Id.  # noqa: E501

        :param terminal: The terminal of this PhysicalEditBody.  # noqa: E501
        :type: int
        """
        if terminal is None:
            raise ValueError("Invalid value for `terminal`, must not be `None`")  # noqa: E501

        self._terminal = terminal

    @property
    def provider_id(self):
        """Gets the provider_id of this PhysicalEditBody.  # noqa: E501

        Provider identifier for physical operations given by PAYCOMET  # noqa: E501

        :return: The provider_id of this PhysicalEditBody.  # noqa: E501
        :rtype: int
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this PhysicalEditBody.

        Provider identifier for physical operations given by PAYCOMET  # noqa: E501

        :param provider_id: The provider_id of this PhysicalEditBody.  # noqa: E501
        :type: int
        """
        if provider_id is None:
            raise ValueError("Invalid value for `provider_id`, must not be `None`")  # noqa: E501

        self._provider_id = provider_id

    @property
    def merchant_id(self):
        """Gets the merchant_id of this PhysicalEditBody.  # noqa: E501

        Merchant identifier code for physical operations given by PAYCOMET  # noqa: E501

        :return: The merchant_id of this PhysicalEditBody.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this PhysicalEditBody.

        Merchant identifier code for physical operations given by PAYCOMET  # noqa: E501

        :param merchant_id: The merchant_id of this PhysicalEditBody.  # noqa: E501
        :type: str
        """
        if merchant_id is None:
            raise ValueError("Invalid value for `merchant_id`, must not be `None`")  # noqa: E501

        self._merchant_id = merchant_id

    @property
    def terminal_id(self):
        """Gets the terminal_id of this PhysicalEditBody.  # noqa: E501

        Terminal identifier  # noqa: E501

        :return: The terminal_id of this PhysicalEditBody.  # noqa: E501
        :rtype: str
        """
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, terminal_id):
        """Sets the terminal_id of this PhysicalEditBody.

        Terminal identifier  # noqa: E501

        :param terminal_id: The terminal_id of this PhysicalEditBody.  # noqa: E501
        :type: str
        """
        if terminal_id is None:
            raise ValueError("Invalid value for `terminal_id`, must not be `None`")  # noqa: E501

        self._terminal_id = terminal_id

    @property
    def id_user(self):
        """Gets the id_user of this PhysicalEditBody.  # noqa: E501

        Identification of user card given by PAYCOMET. Mandatory if is a card payment.  # noqa: E501

        :return: The id_user of this PhysicalEditBody.  # noqa: E501
        :rtype: int
        """
        return self._id_user

    @id_user.setter
    def id_user(self, id_user):
        """Sets the id_user of this PhysicalEditBody.

        Identification of user card given by PAYCOMET. Mandatory if is a card payment.  # noqa: E501

        :param id_user: The id_user of this PhysicalEditBody.  # noqa: E501
        :type: int
        """
        if id_user is None:
            raise ValueError("Invalid value for `id_user`, must not be `None`")  # noqa: E501

        self._id_user = id_user

    @property
    def token_user(self):
        """Gets the token_user of this PhysicalEditBody.  # noqa: E501

        Identification of user card given by PAYCOMET. Mandatory if is a card payment.  # noqa: E501

        :return: The token_user of this PhysicalEditBody.  # noqa: E501
        :rtype: str
        """
        return self._token_user

    @token_user.setter
    def token_user(self, token_user):
        """Sets the token_user of this PhysicalEditBody.

        Identification of user card given by PAYCOMET. Mandatory if is a card payment.  # noqa: E501

        :param token_user: The token_user of this PhysicalEditBody.  # noqa: E501
        :type: str
        """
        if token_user is None:
            raise ValueError("Invalid value for `token_user`, must not be `None`")  # noqa: E501

        self._token_user = token_user

    @property
    def cof_identifier(self):
        """Gets the cof_identifier of this PhysicalEditBody.  # noqa: E501

        Processor COF identifier  # noqa: E501

        :return: The cof_identifier of this PhysicalEditBody.  # noqa: E501
        :rtype: str
        """
        return self._cof_identifier

    @cof_identifier.setter
    def cof_identifier(self, cof_identifier):
        """Sets the cof_identifier of this PhysicalEditBody.

        Processor COF identifier  # noqa: E501

        :param cof_identifier: The cof_identifier of this PhysicalEditBody.  # noqa: E501
        :type: str
        """

        self._cof_identifier = cof_identifier

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
        if issubclass(PhysicalEditBody, dict):
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
        if not isinstance(other, PhysicalEditBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
