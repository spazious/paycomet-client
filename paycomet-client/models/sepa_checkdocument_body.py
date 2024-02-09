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

class SepaCheckdocumentBody(object):
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
        'sepa_provider_id': 'int',
        'merchant_code': 'str',
        'merchant_customer_id': 'str',
        'merchant_customer_iban': 'str',
        'document_type': 'int'
    }

    attribute_map = {
        'terminal': 'terminal',
        'sepa_provider_id': 'sepaProviderId',
        'merchant_code': 'merchantCode',
        'merchant_customer_id': 'merchantCustomerId',
        'merchant_customer_iban': 'merchantCustomerIban',
        'document_type': 'documentType'
    }

    def __init__(self, terminal=None, sepa_provider_id=None, merchant_code=None, merchant_customer_id=None, merchant_customer_iban=None, document_type=None):  # noqa: E501
        """SepaCheckdocumentBody - a model defined in Swagger"""  # noqa: E501
        self._terminal = None
        self._sepa_provider_id = None
        self._merchant_code = None
        self._merchant_customer_id = None
        self._merchant_customer_iban = None
        self._document_type = None
        self.discriminator = None
        self.terminal = terminal
        self.sepa_provider_id = sepa_provider_id
        self.merchant_code = merchant_code
        self.merchant_customer_id = merchant_customer_id
        self.merchant_customer_iban = merchant_customer_iban
        self.document_type = document_type

    @property
    def terminal(self):
        """Gets the terminal of this SepaCheckdocumentBody.  # noqa: E501

        Product or terminal Id.  # noqa: E501

        :return: The terminal of this SepaCheckdocumentBody.  # noqa: E501
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this SepaCheckdocumentBody.

        Product or terminal Id.  # noqa: E501

        :param terminal: The terminal of this SepaCheckdocumentBody.  # noqa: E501
        :type: int
        """
        if terminal is None:
            raise ValueError("Invalid value for `terminal`, must not be `None`")  # noqa: E501

        self._terminal = terminal

    @property
    def sepa_provider_id(self):
        """Gets the sepa_provider_id of this SepaCheckdocumentBody.  # noqa: E501

        Unique identifier assigned by PAYCOMET for the supplier sending SEPA operations. Available on the client control panel.  # noqa: E501

        :return: The sepa_provider_id of this SepaCheckdocumentBody.  # noqa: E501
        :rtype: int
        """
        return self._sepa_provider_id

    @sepa_provider_id.setter
    def sepa_provider_id(self, sepa_provider_id):
        """Sets the sepa_provider_id of this SepaCheckdocumentBody.

        Unique identifier assigned by PAYCOMET for the supplier sending SEPA operations. Available on the client control panel.  # noqa: E501

        :param sepa_provider_id: The sepa_provider_id of this SepaCheckdocumentBody.  # noqa: E501
        :type: int
        """
        if sepa_provider_id is None:
            raise ValueError("Invalid value for `sepa_provider_id`, must not be `None`")  # noqa: E501

        self._sepa_provider_id = sepa_provider_id

    @property
    def merchant_code(self):
        """Gets the merchant_code of this SepaCheckdocumentBody.  # noqa: E501

        Unique identifier as PAYCOMET account. Available on the client control panel.  # noqa: E501

        :return: The merchant_code of this SepaCheckdocumentBody.  # noqa: E501
        :rtype: str
        """
        return self._merchant_code

    @merchant_code.setter
    def merchant_code(self, merchant_code):
        """Sets the merchant_code of this SepaCheckdocumentBody.

        Unique identifier as PAYCOMET account. Available on the client control panel.  # noqa: E501

        :param merchant_code: The merchant_code of this SepaCheckdocumentBody.  # noqa: E501
        :type: str
        """
        if merchant_code is None:
            raise ValueError("Invalid value for `merchant_code`, must not be `None`")  # noqa: E501

        self._merchant_code = merchant_code

    @property
    def merchant_customer_id(self):
        """Gets the merchant_customer_id of this SepaCheckdocumentBody.  # noqa: E501

        Unique identifier of the client of the supplier.  # noqa: E501

        :return: The merchant_customer_id of this SepaCheckdocumentBody.  # noqa: E501
        :rtype: str
        """
        return self._merchant_customer_id

    @merchant_customer_id.setter
    def merchant_customer_id(self, merchant_customer_id):
        """Sets the merchant_customer_id of this SepaCheckdocumentBody.

        Unique identifier of the client of the supplier.  # noqa: E501

        :param merchant_customer_id: The merchant_customer_id of this SepaCheckdocumentBody.  # noqa: E501
        :type: str
        """
        if merchant_customer_id is None:
            raise ValueError("Invalid value for `merchant_customer_id`, must not be `None`")  # noqa: E501

        self._merchant_customer_id = merchant_customer_id

    @property
    def merchant_customer_iban(self):
        """Gets the merchant_customer_iban of this SepaCheckdocumentBody.  # noqa: E501

        Account number of the client in IBAN format.  # noqa: E501

        :return: The merchant_customer_iban of this SepaCheckdocumentBody.  # noqa: E501
        :rtype: str
        """
        return self._merchant_customer_iban

    @merchant_customer_iban.setter
    def merchant_customer_iban(self, merchant_customer_iban):
        """Sets the merchant_customer_iban of this SepaCheckdocumentBody.

        Account number of the client in IBAN format.  # noqa: E501

        :param merchant_customer_iban: The merchant_customer_iban of this SepaCheckdocumentBody.  # noqa: E501
        :type: str
        """
        if merchant_customer_iban is None:
            raise ValueError("Invalid value for `merchant_customer_iban`, must not be `None`")  # noqa: E501

        self._merchant_customer_iban = merchant_customer_iban

    @property
    def document_type(self):
        """Gets the document_type of this SepaCheckdocumentBody.  # noqa: E501

        Identifier of the type of document on PAYCOMET.  # noqa: E501

        :return: The document_type of this SepaCheckdocumentBody.  # noqa: E501
        :rtype: int
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this SepaCheckdocumentBody.

        Identifier of the type of document on PAYCOMET.  # noqa: E501

        :param document_type: The document_type of this SepaCheckdocumentBody.  # noqa: E501
        :type: int
        """
        if document_type is None:
            raise ValueError("Invalid value for `document_type`, must not be `None`")  # noqa: E501

        self._document_type = document_type

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
        if issubclass(SepaCheckdocumentBody, dict):
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
        if not isinstance(other, SepaCheckdocumentBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
