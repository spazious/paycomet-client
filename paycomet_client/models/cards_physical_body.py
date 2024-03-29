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

class CardsPhysicalBody(object):
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
        'device_ksn': 'str',
        'device_dukpt': 'str',
        'cof_identifier': 'str',
        'original_ip': 'str'
    }

    attribute_map = {
        'terminal': 'terminal',
        'provider_id': 'providerId',
        'merchant_id': 'merchantId',
        'terminal_id': 'terminalId',
        'device_ksn': 'deviceKsn',
        'device_dukpt': 'deviceDukpt',
        'cof_identifier': 'cofIdentifier',
        'original_ip': 'originalIp'
    }

    def __init__(self, terminal=None, provider_id=None, merchant_id=None, terminal_id=None, device_ksn=None, device_dukpt=None, cof_identifier=None, original_ip=None):  # noqa: E501
        """CardsPhysicalBody - a model defined in Swagger"""  # noqa: E501
        self._terminal = None
        self._provider_id = None
        self._merchant_id = None
        self._terminal_id = None
        self._device_ksn = None
        self._device_dukpt = None
        self._cof_identifier = None
        self._original_ip = None
        self.discriminator = None
        self.terminal = terminal
        self.provider_id = provider_id
        self.merchant_id = merchant_id
        self.terminal_id = terminal_id
        self.device_ksn = device_ksn
        self.device_dukpt = device_dukpt
        if cof_identifier is not None:
            self.cof_identifier = cof_identifier
        self.original_ip = original_ip

    @property
    def terminal(self):
        """Gets the terminal of this CardsPhysicalBody.  # noqa: E501

        Product or terminal Id.  # noqa: E501

        :return: The terminal of this CardsPhysicalBody.  # noqa: E501
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this CardsPhysicalBody.

        Product or terminal Id.  # noqa: E501

        :param terminal: The terminal of this CardsPhysicalBody.  # noqa: E501
        :type: int
        """
        if terminal is None:
            raise ValueError("Invalid value for `terminal`, must not be `None`")  # noqa: E501

        self._terminal = terminal

    @property
    def provider_id(self):
        """Gets the provider_id of this CardsPhysicalBody.  # noqa: E501

        Provider identifier for physical operations given by PAYCOMET  # noqa: E501

        :return: The provider_id of this CardsPhysicalBody.  # noqa: E501
        :rtype: int
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this CardsPhysicalBody.

        Provider identifier for physical operations given by PAYCOMET  # noqa: E501

        :param provider_id: The provider_id of this CardsPhysicalBody.  # noqa: E501
        :type: int
        """
        if provider_id is None:
            raise ValueError("Invalid value for `provider_id`, must not be `None`")  # noqa: E501

        self._provider_id = provider_id

    @property
    def merchant_id(self):
        """Gets the merchant_id of this CardsPhysicalBody.  # noqa: E501

        Merchant identifier code for physical operations given by PAYCOMET  # noqa: E501

        :return: The merchant_id of this CardsPhysicalBody.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this CardsPhysicalBody.

        Merchant identifier code for physical operations given by PAYCOMET  # noqa: E501

        :param merchant_id: The merchant_id of this CardsPhysicalBody.  # noqa: E501
        :type: str
        """
        if merchant_id is None:
            raise ValueError("Invalid value for `merchant_id`, must not be `None`")  # noqa: E501

        self._merchant_id = merchant_id

    @property
    def terminal_id(self):
        """Gets the terminal_id of this CardsPhysicalBody.  # noqa: E501

        Terminal identifier  # noqa: E501

        :return: The terminal_id of this CardsPhysicalBody.  # noqa: E501
        :rtype: str
        """
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, terminal_id):
        """Sets the terminal_id of this CardsPhysicalBody.

        Terminal identifier  # noqa: E501

        :param terminal_id: The terminal_id of this CardsPhysicalBody.  # noqa: E501
        :type: str
        """
        if terminal_id is None:
            raise ValueError("Invalid value for `terminal_id`, must not be `None`")  # noqa: E501

        self._terminal_id = terminal_id

    @property
    def device_ksn(self):
        """Gets the device_ksn of this CardsPhysicalBody.  # noqa: E501

        Card KSN info  # noqa: E501

        :return: The device_ksn of this CardsPhysicalBody.  # noqa: E501
        :rtype: str
        """
        return self._device_ksn

    @device_ksn.setter
    def device_ksn(self, device_ksn):
        """Sets the device_ksn of this CardsPhysicalBody.

        Card KSN info  # noqa: E501

        :param device_ksn: The device_ksn of this CardsPhysicalBody.  # noqa: E501
        :type: str
        """
        if device_ksn is None:
            raise ValueError("Invalid value for `device_ksn`, must not be `None`")  # noqa: E501

        self._device_ksn = device_ksn

    @property
    def device_dukpt(self):
        """Gets the device_dukpt of this CardsPhysicalBody.  # noqa: E501

        Card DUKPT info  # noqa: E501

        :return: The device_dukpt of this CardsPhysicalBody.  # noqa: E501
        :rtype: str
        """
        return self._device_dukpt

    @device_dukpt.setter
    def device_dukpt(self, device_dukpt):
        """Sets the device_dukpt of this CardsPhysicalBody.

        Card DUKPT info  # noqa: E501

        :param device_dukpt: The device_dukpt of this CardsPhysicalBody.  # noqa: E501
        :type: str
        """
        if device_dukpt is None:
            raise ValueError("Invalid value for `device_dukpt`, must not be `None`")  # noqa: E501

        self._device_dukpt = device_dukpt

    @property
    def cof_identifier(self):
        """Gets the cof_identifier of this CardsPhysicalBody.  # noqa: E501

        Processor COF identifier  # noqa: E501

        :return: The cof_identifier of this CardsPhysicalBody.  # noqa: E501
        :rtype: str
        """
        return self._cof_identifier

    @cof_identifier.setter
    def cof_identifier(self, cof_identifier):
        """Sets the cof_identifier of this CardsPhysicalBody.

        Processor COF identifier  # noqa: E501

        :param cof_identifier: The cof_identifier of this CardsPhysicalBody.  # noqa: E501
        :type: str
        """

        self._cof_identifier = cof_identifier

    @property
    def original_ip(self):
        """Gets the original_ip of this CardsPhysicalBody.  # noqa: E501

        IP Address of the customer  # noqa: E501

        :return: The original_ip of this CardsPhysicalBody.  # noqa: E501
        :rtype: str
        """
        return self._original_ip

    @original_ip.setter
    def original_ip(self, original_ip):
        """Sets the original_ip of this CardsPhysicalBody.

        IP Address of the customer  # noqa: E501

        :param original_ip: The original_ip of this CardsPhysicalBody.  # noqa: E501
        :type: str
        """
        if original_ip is None:
            raise ValueError("Invalid value for `original_ip`, must not be `None`")  # noqa: E501

        self._original_ip = original_ip

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
        if issubclass(CardsPhysicalBody, dict):
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
        if not isinstance(other, CardsPhysicalBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
