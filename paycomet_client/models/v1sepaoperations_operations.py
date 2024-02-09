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

class V1sepaoperationsOperations(object):
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
        'operation_type': 'int',
        'merchant_code': 'str',
        'terminal_id_debtor': 'int',
        'unique_id_creditor': 'str',
        'company_name_creditor': 'str',
        'iban_number_creditor': 'str',
        'swift_code_creditor': 'str',
        'company_type_creditor': 'int',
        'operation_order': 'str',
        'operation_amount': 'int',
        'operation_currency': 'str',
        'operation_datetime': 'date',
        'operation_concept': 'str'
    }

    attribute_map = {
        'operation_type': 'operationType',
        'merchant_code': 'merchantCode',
        'terminal_id_debtor': 'terminalIDDebtor',
        'unique_id_creditor': 'uniqueIdCreditor',
        'company_name_creditor': 'companyNameCreditor',
        'iban_number_creditor': 'ibanNumberCreditor',
        'swift_code_creditor': 'swiftCodeCreditor',
        'company_type_creditor': 'companyTypeCreditor',
        'operation_order': 'operationOrder',
        'operation_amount': 'operationAmount',
        'operation_currency': 'operationCurrency',
        'operation_datetime': 'operationDatetime',
        'operation_concept': 'operationConcept'
    }

    def __init__(self, operation_type=None, merchant_code=None, terminal_id_debtor=None, unique_id_creditor=None, company_name_creditor=None, iban_number_creditor=None, swift_code_creditor=None, company_type_creditor=None, operation_order=None, operation_amount=None, operation_currency=None, operation_datetime=None, operation_concept=None):  # noqa: E501
        """V1sepaoperationsOperations - a model defined in Swagger"""  # noqa: E501
        self._operation_type = None
        self._merchant_code = None
        self._terminal_id_debtor = None
        self._unique_id_creditor = None
        self._company_name_creditor = None
        self._iban_number_creditor = None
        self._swift_code_creditor = None
        self._company_type_creditor = None
        self._operation_order = None
        self._operation_amount = None
        self._operation_currency = None
        self._operation_datetime = None
        self._operation_concept = None
        self.discriminator = None
        self.operation_type = operation_type
        self.merchant_code = merchant_code
        self.terminal_id_debtor = terminal_id_debtor
        self.unique_id_creditor = unique_id_creditor
        self.company_name_creditor = company_name_creditor
        self.iban_number_creditor = iban_number_creditor
        self.swift_code_creditor = swift_code_creditor
        self.company_type_creditor = company_type_creditor
        self.operation_order = operation_order
        self.operation_amount = operation_amount
        self.operation_currency = operation_currency
        self.operation_datetime = operation_datetime
        self.operation_concept = operation_concept

    @property
    def operation_type(self):
        """Gets the operation_type of this V1sepaoperationsOperations.  # noqa: E501

        Type of operation. Identifies whether the operation is a direct debit or a transfer. 1 – Direct Debit (N19) 2 – Transfer (N34)  # noqa: E501

        :return: The operation_type of this V1sepaoperationsOperations.  # noqa: E501
        :rtype: int
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this V1sepaoperationsOperations.

        Type of operation. Identifies whether the operation is a direct debit or a transfer. 1 – Direct Debit (N19) 2 – Transfer (N34)  # noqa: E501

        :param operation_type: The operation_type of this V1sepaoperationsOperations.  # noqa: E501
        :type: int
        """
        if operation_type is None:
            raise ValueError("Invalid value for `operation_type`, must not be `None`")  # noqa: E501

        self._operation_type = operation_type

    @property
    def merchant_code(self):
        """Gets the merchant_code of this V1sepaoperationsOperations.  # noqa: E501

        Unique identifier as PAYCOMET account. Available on the client control panel.  # noqa: E501

        :return: The merchant_code of this V1sepaoperationsOperations.  # noqa: E501
        :rtype: str
        """
        return self._merchant_code

    @merchant_code.setter
    def merchant_code(self, merchant_code):
        """Sets the merchant_code of this V1sepaoperationsOperations.

        Unique identifier as PAYCOMET account. Available on the client control panel.  # noqa: E501

        :param merchant_code: The merchant_code of this V1sepaoperationsOperations.  # noqa: E501
        :type: str
        """
        if merchant_code is None:
            raise ValueError("Invalid value for `merchant_code`, must not be `None`")  # noqa: E501

        self._merchant_code = merchant_code

    @property
    def terminal_id_debtor(self):
        """Gets the terminal_id_debtor of this V1sepaoperationsOperations.  # noqa: E501

        This will be the terminal number assigned to the product. Obtained from the control panel. Identifies the terminal number of the debtor/payer of a SEPA operation. Therefore, it will depend on the type of operation (debit, transfer).  # noqa: E501

        :return: The terminal_id_debtor of this V1sepaoperationsOperations.  # noqa: E501
        :rtype: int
        """
        return self._terminal_id_debtor

    @terminal_id_debtor.setter
    def terminal_id_debtor(self, terminal_id_debtor):
        """Sets the terminal_id_debtor of this V1sepaoperationsOperations.

        This will be the terminal number assigned to the product. Obtained from the control panel. Identifies the terminal number of the debtor/payer of a SEPA operation. Therefore, it will depend on the type of operation (debit, transfer).  # noqa: E501

        :param terminal_id_debtor: The terminal_id_debtor of this V1sepaoperationsOperations.  # noqa: E501
        :type: int
        """
        if terminal_id_debtor is None:
            raise ValueError("Invalid value for `terminal_id_debtor`, must not be `None`")  # noqa: E501

        self._terminal_id_debtor = terminal_id_debtor

    @property
    def unique_id_creditor(self):
        """Gets the unique_id_creditor of this V1sepaoperationsOperations.  # noqa: E501

        This will be the unique identifier of this individual, freelancer, company (recipient) in the client.  # noqa: E501

        :return: The unique_id_creditor of this V1sepaoperationsOperations.  # noqa: E501
        :rtype: str
        """
        return self._unique_id_creditor

    @unique_id_creditor.setter
    def unique_id_creditor(self, unique_id_creditor):
        """Sets the unique_id_creditor of this V1sepaoperationsOperations.

        This will be the unique identifier of this individual, freelancer, company (recipient) in the client.  # noqa: E501

        :param unique_id_creditor: The unique_id_creditor of this V1sepaoperationsOperations.  # noqa: E501
        :type: str
        """
        if unique_id_creditor is None:
            raise ValueError("Invalid value for `unique_id_creditor`, must not be `None`")  # noqa: E501

        self._unique_id_creditor = unique_id_creditor

    @property
    def company_name_creditor(self):
        """Gets the company_name_creditor of this V1sepaoperationsOperations.  # noqa: E501

        Name of the company, individual or freelancer corresponding to the previous indicator.  # noqa: E501

        :return: The company_name_creditor of this V1sepaoperationsOperations.  # noqa: E501
        :rtype: str
        """
        return self._company_name_creditor

    @company_name_creditor.setter
    def company_name_creditor(self, company_name_creditor):
        """Sets the company_name_creditor of this V1sepaoperationsOperations.

        Name of the company, individual or freelancer corresponding to the previous indicator.  # noqa: E501

        :param company_name_creditor: The company_name_creditor of this V1sepaoperationsOperations.  # noqa: E501
        :type: str
        """
        if company_name_creditor is None:
            raise ValueError("Invalid value for `company_name_creditor`, must not be `None`")  # noqa: E501

        self._company_name_creditor = company_name_creditor

    @property
    def iban_number_creditor(self):
        """Gets the iban_number_creditor of this V1sepaoperationsOperations.  # noqa: E501

        IBAN code of the account of the recipient.  # noqa: E501

        :return: The iban_number_creditor of this V1sepaoperationsOperations.  # noqa: E501
        :rtype: str
        """
        return self._iban_number_creditor

    @iban_number_creditor.setter
    def iban_number_creditor(self, iban_number_creditor):
        """Sets the iban_number_creditor of this V1sepaoperationsOperations.

        IBAN code of the account of the recipient.  # noqa: E501

        :param iban_number_creditor: The iban_number_creditor of this V1sepaoperationsOperations.  # noqa: E501
        :type: str
        """
        if iban_number_creditor is None:
            raise ValueError("Invalid value for `iban_number_creditor`, must not be `None`")  # noqa: E501

        self._iban_number_creditor = iban_number_creditor

    @property
    def swift_code_creditor(self):
        """Gets the swift_code_creditor of this V1sepaoperationsOperations.  # noqa: E501

        SWIFT code of the bank account of the recipient. Must be provided when the account IBAN is not Spanish. If the ibanNumberCreditor number belongs to a Spanish account, it must be sent as an empty string.  # noqa: E501

        :return: The swift_code_creditor of this V1sepaoperationsOperations.  # noqa: E501
        :rtype: str
        """
        return self._swift_code_creditor

    @swift_code_creditor.setter
    def swift_code_creditor(self, swift_code_creditor):
        """Sets the swift_code_creditor of this V1sepaoperationsOperations.

        SWIFT code of the bank account of the recipient. Must be provided when the account IBAN is not Spanish. If the ibanNumberCreditor number belongs to a Spanish account, it must be sent as an empty string.  # noqa: E501

        :param swift_code_creditor: The swift_code_creditor of this V1sepaoperationsOperations.  # noqa: E501
        :type: str
        """
        if swift_code_creditor is None:
            raise ValueError("Invalid value for `swift_code_creditor`, must not be `None`")  # noqa: E501

        self._swift_code_creditor = swift_code_creditor

    @property
    def company_type_creditor(self):
        """Gets the company_type_creditor of this V1sepaoperationsOperations.  # noqa: E501

        Identifier of the type of recipient: 1: Individual / 2: Freelancer / 3: Commercial Company.  # noqa: E501

        :return: The company_type_creditor of this V1sepaoperationsOperations.  # noqa: E501
        :rtype: int
        """
        return self._company_type_creditor

    @company_type_creditor.setter
    def company_type_creditor(self, company_type_creditor):
        """Sets the company_type_creditor of this V1sepaoperationsOperations.

        Identifier of the type of recipient: 1: Individual / 2: Freelancer / 3: Commercial Company.  # noqa: E501

        :param company_type_creditor: The company_type_creditor of this V1sepaoperationsOperations.  # noqa: E501
        :type: int
        """
        if company_type_creditor is None:
            raise ValueError("Invalid value for `company_type_creditor`, must not be `None`")  # noqa: E501

        self._company_type_creditor = company_type_creditor

    @property
    def operation_order(self):
        """Gets the operation_order of this V1sepaoperationsOperations.  # noqa: E501

        Unique reference of the operation.  # noqa: E501

        :return: The operation_order of this V1sepaoperationsOperations.  # noqa: E501
        :rtype: str
        """
        return self._operation_order

    @operation_order.setter
    def operation_order(self, operation_order):
        """Sets the operation_order of this V1sepaoperationsOperations.

        Unique reference of the operation.  # noqa: E501

        :param operation_order: The operation_order of this V1sepaoperationsOperations.  # noqa: E501
        :type: str
        """
        if operation_order is None:
            raise ValueError("Invalid value for `operation_order`, must not be `None`")  # noqa: E501

        self._operation_order = operation_order

    @property
    def operation_amount(self):
        """Gets the operation_amount of this V1sepaoperationsOperations.  # noqa: E501

        Amount in the transaction currency with 2 decimals in integer format: (€2.25 = 225).  # noqa: E501

        :return: The operation_amount of this V1sepaoperationsOperations.  # noqa: E501
        :rtype: int
        """
        return self._operation_amount

    @operation_amount.setter
    def operation_amount(self, operation_amount):
        """Sets the operation_amount of this V1sepaoperationsOperations.

        Amount in the transaction currency with 2 decimals in integer format: (€2.25 = 225).  # noqa: E501

        :param operation_amount: The operation_amount of this V1sepaoperationsOperations.  # noqa: E501
        :type: int
        """
        if operation_amount is None:
            raise ValueError("Invalid value for `operation_amount`, must not be `None`")  # noqa: E501

        self._operation_amount = operation_amount

    @property
    def operation_currency(self):
        """Gets the operation_currency of this V1sepaoperationsOperations.  # noqa: E501

        Currency type of the transaction. The only permitted currency is the euro, whose code is EUR.  # noqa: E501

        :return: The operation_currency of this V1sepaoperationsOperations.  # noqa: E501
        :rtype: str
        """
        return self._operation_currency

    @operation_currency.setter
    def operation_currency(self, operation_currency):
        """Sets the operation_currency of this V1sepaoperationsOperations.

        Currency type of the transaction. The only permitted currency is the euro, whose code is EUR.  # noqa: E501

        :param operation_currency: The operation_currency of this V1sepaoperationsOperations.  # noqa: E501
        :type: str
        """
        if operation_currency is None:
            raise ValueError("Invalid value for `operation_currency`, must not be `None`")  # noqa: E501

        self._operation_currency = operation_currency

    @property
    def operation_datetime(self):
        """Gets the operation_datetime of this V1sepaoperationsOperations.  # noqa: E501

        Date desired for sending the SEPA operation / remittance. Always after the current date. Format: yyyymmdd.  # noqa: E501

        :return: The operation_datetime of this V1sepaoperationsOperations.  # noqa: E501
        :rtype: date
        """
        return self._operation_datetime

    @operation_datetime.setter
    def operation_datetime(self, operation_datetime):
        """Sets the operation_datetime of this V1sepaoperationsOperations.

        Date desired for sending the SEPA operation / remittance. Always after the current date. Format: yyyymmdd.  # noqa: E501

        :param operation_datetime: The operation_datetime of this V1sepaoperationsOperations.  # noqa: E501
        :type: date
        """
        if operation_datetime is None:
            raise ValueError("Invalid value for `operation_datetime`, must not be `None`")  # noqa: E501

        self._operation_datetime = operation_datetime

    @property
    def operation_concept(self):
        """Gets the operation_concept of this V1sepaoperationsOperations.  # noqa: E501

        Concept assigned to the operation / remittance. This is the descriptor which will appear in banking entries. Maximum length 100. Although error 1273 specified 140 characters, PAYCOMET reserves 40, the maximum permitted in the input therefore being 100. Allowed charactaers: ([A-Za-z0-9]|[+|?|/|-|:|(|)|.|,|'| ])  # noqa: E501

        :return: The operation_concept of this V1sepaoperationsOperations.  # noqa: E501
        :rtype: str
        """
        return self._operation_concept

    @operation_concept.setter
    def operation_concept(self, operation_concept):
        """Sets the operation_concept of this V1sepaoperationsOperations.

        Concept assigned to the operation / remittance. This is the descriptor which will appear in banking entries. Maximum length 100. Although error 1273 specified 140 characters, PAYCOMET reserves 40, the maximum permitted in the input therefore being 100. Allowed charactaers: ([A-Za-z0-9]|[+|?|/|-|:|(|)|.|,|'| ])  # noqa: E501

        :param operation_concept: The operation_concept of this V1sepaoperationsOperations.  # noqa: E501
        :type: str
        """
        if operation_concept is None:
            raise ValueError("Invalid value for `operation_concept`, must not be `None`")  # noqa: E501

        self._operation_concept = operation_concept

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
        if issubclass(V1sepaoperationsOperations, dict):
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
        if not isinstance(other, V1sepaoperationsOperations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
