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

class V1paymentsorderdccconfirmPayment(object):
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
        'order': 'str',
        'amount': 'str',
        'currency': 'str',
        'method_id': 'str',
        'original_ip': 'str',
        'secure': 'str',
        'id_user': 'str',
        'token_user': 'str',
        'scoring': 'str',
        'product_description': 'str',
        'merchant_descriptor': 'str',
        'user_interaction': 'int',
        'trx_type': 'str',
        'sca_exception': 'str',
        'url_ok': 'str',
        'url_ko': 'str',
        'notify_direct_payment': 'int',
        'merchant_data': 'V1paymentspreauthPaymentMerchantData'
    }

    attribute_map = {
        'terminal': 'terminal',
        'order': 'order',
        'amount': 'amount',
        'currency': 'currency',
        'method_id': 'methodId',
        'original_ip': 'originalIp',
        'secure': 'secure',
        'id_user': 'idUser',
        'token_user': 'tokenUser',
        'scoring': 'scoring',
        'product_description': 'productDescription',
        'merchant_descriptor': 'merchantDescriptor',
        'user_interaction': 'userInteraction',
        'trx_type': 'trxType',
        'sca_exception': 'scaException',
        'url_ok': 'urlOk',
        'url_ko': 'urlKo',
        'notify_direct_payment': 'notifyDirectPayment',
        'merchant_data': 'merchantData'
    }

    def __init__(self, terminal=None, order=None, amount=None, currency=None, method_id=None, original_ip=None, secure=None, id_user=None, token_user=None, scoring=None, product_description=None, merchant_descriptor=None, user_interaction=None, trx_type=None, sca_exception=None, url_ok=None, url_ko=None, notify_direct_payment=None, merchant_data=None):  # noqa: E501
        """V1paymentsorderdccconfirmPayment - a model defined in Swagger"""  # noqa: E501
        self._terminal = None
        self._order = None
        self._amount = None
        self._currency = None
        self._method_id = None
        self._original_ip = None
        self._secure = None
        self._id_user = None
        self._token_user = None
        self._scoring = None
        self._product_description = None
        self._merchant_descriptor = None
        self._user_interaction = None
        self._trx_type = None
        self._sca_exception = None
        self._url_ok = None
        self._url_ko = None
        self._notify_direct_payment = None
        self._merchant_data = None
        self.discriminator = None
        if terminal is not None:
            self.terminal = terminal
        if order is not None:
            self.order = order
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if method_id is not None:
            self.method_id = method_id
        if original_ip is not None:
            self.original_ip = original_ip
        if secure is not None:
            self.secure = secure
        if id_user is not None:
            self.id_user = id_user
        if token_user is not None:
            self.token_user = token_user
        if scoring is not None:
            self.scoring = scoring
        if product_description is not None:
            self.product_description = product_description
        if merchant_descriptor is not None:
            self.merchant_descriptor = merchant_descriptor
        if user_interaction is not None:
            self.user_interaction = user_interaction
        if trx_type is not None:
            self.trx_type = trx_type
        if sca_exception is not None:
            self.sca_exception = sca_exception
        if url_ok is not None:
            self.url_ok = url_ok
        if url_ko is not None:
            self.url_ko = url_ko
        if notify_direct_payment is not None:
            self.notify_direct_payment = notify_direct_payment
        if merchant_data is not None:
            self.merchant_data = merchant_data

    @property
    def terminal(self):
        """Gets the terminal of this V1paymentsorderdccconfirmPayment.  # noqa: E501

        Product or terminal Id.  # noqa: E501

        :return: The terminal of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this V1paymentsorderdccconfirmPayment.

        Product or terminal Id.  # noqa: E501

        :param terminal: The terminal of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :type: int
        """

        self._terminal = terminal

    @property
    def order(self):
        """Gets the order of this V1paymentsorderdccconfirmPayment.  # noqa: E501

        Unique reference for merchant's purchase  # noqa: E501

        :return: The order of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this V1paymentsorderdccconfirmPayment.

        Unique reference for merchant's purchase  # noqa: E501

        :param order: The order of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :type: str
        """

        self._order = order

    @property
    def amount(self):
        """Gets the amount of this V1paymentsorderdccconfirmPayment.  # noqa: E501

        Amount of the operation in number format. 1.00 EURO = 100, 4.50 EUROS = 450...  # noqa: E501

        :return: The amount of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this V1paymentsorderdccconfirmPayment.

        Amount of the operation in number format. 1.00 EURO = 100, 4.50 EUROS = 450...  # noqa: E501

        :param amount: The amount of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this V1paymentsorderdccconfirmPayment.  # noqa: E501

        Currency of the transaction.   # noqa: E501

        :return: The currency of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this V1paymentsorderdccconfirmPayment.

        Currency of the transaction.   # noqa: E501

        :param currency: The currency of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def method_id(self):
        """Gets the method_id of this V1paymentsorderdccconfirmPayment.  # noqa: E501

        PAYCOMET payment method ID. 1 is for card.  # noqa: E501

        :return: The method_id of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :rtype: str
        """
        return self._method_id

    @method_id.setter
    def method_id(self, method_id):
        """Sets the method_id of this V1paymentsorderdccconfirmPayment.

        PAYCOMET payment method ID. 1 is for card.  # noqa: E501

        :param method_id: The method_id of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :type: str
        """

        self._method_id = method_id

    @property
    def original_ip(self):
        """Gets the original_ip of this V1paymentsorderdccconfirmPayment.  # noqa: E501

        IP Address of the customer that initiated the payment transaction  # noqa: E501

        :return: The original_ip of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :rtype: str
        """
        return self._original_ip

    @original_ip.setter
    def original_ip(self, original_ip):
        """Sets the original_ip of this V1paymentsorderdccconfirmPayment.

        IP Address of the customer that initiated the payment transaction  # noqa: E501

        :param original_ip: The original_ip of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :type: str
        """

        self._original_ip = original_ip

    @property
    def secure(self):
        """Gets the secure of this V1paymentsorderdccconfirmPayment.  # noqa: E501

        0 or 1. Indicates if the transaction is secure.  # noqa: E501

        :return: The secure of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :rtype: str
        """
        return self._secure

    @secure.setter
    def secure(self, secure):
        """Sets the secure of this V1paymentsorderdccconfirmPayment.

        0 or 1. Indicates if the transaction is secure.  # noqa: E501

        :param secure: The secure of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :type: str
        """

        self._secure = secure

    @property
    def id_user(self):
        """Gets the id_user of this V1paymentsorderdccconfirmPayment.  # noqa: E501

        Identification of user card given by PAYCOMET. Mandatory if is a card payment.  # noqa: E501

        :return: The id_user of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :rtype: str
        """
        return self._id_user

    @id_user.setter
    def id_user(self, id_user):
        """Sets the id_user of this V1paymentsorderdccconfirmPayment.

        Identification of user card given by PAYCOMET. Mandatory if is a card payment.  # noqa: E501

        :param id_user: The id_user of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :type: str
        """

        self._id_user = id_user

    @property
    def token_user(self):
        """Gets the token_user of this V1paymentsorderdccconfirmPayment.  # noqa: E501

        Identification of user card given by PAYCOMET. Mandatory if is a card payment.  # noqa: E501

        :return: The token_user of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :rtype: str
        """
        return self._token_user

    @token_user.setter
    def token_user(self, token_user):
        """Sets the token_user of this V1paymentsorderdccconfirmPayment.

        Identification of user card given by PAYCOMET. Mandatory if is a card payment.  # noqa: E501

        :param token_user: The token_user of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :type: str
        """

        self._token_user = token_user

    @property
    def scoring(self):
        """Gets the scoring of this V1paymentsorderdccconfirmPayment.  # noqa: E501

        Risk scoring value from 0 to 100.  # noqa: E501

        :return: The scoring of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :rtype: str
        """
        return self._scoring

    @scoring.setter
    def scoring(self, scoring):
        """Sets the scoring of this V1paymentsorderdccconfirmPayment.

        Risk scoring value from 0 to 100.  # noqa: E501

        :param scoring: The scoring of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :type: str
        """

        self._scoring = scoring

    @property
    def product_description(self):
        """Gets the product_description of this V1paymentsorderdccconfirmPayment.  # noqa: E501

        Description of the product sold.  # noqa: E501

        :return: The product_description of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :rtype: str
        """
        return self._product_description

    @product_description.setter
    def product_description(self, product_description):
        """Sets the product_description of this V1paymentsorderdccconfirmPayment.

        Description of the product sold.  # noqa: E501

        :param product_description: The product_description of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :type: str
        """

        self._product_description = product_description

    @property
    def merchant_descriptor(self):
        """Gets the merchant_descriptor of this V1paymentsorderdccconfirmPayment.  # noqa: E501

        Allows the business to send a text up to 25 characters that will be printed on the customer invoice. Limited to simple characters, no accents or special characters.  # noqa: E501

        :return: The merchant_descriptor of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :rtype: str
        """
        return self._merchant_descriptor

    @merchant_descriptor.setter
    def merchant_descriptor(self, merchant_descriptor):
        """Sets the merchant_descriptor of this V1paymentsorderdccconfirmPayment.

        Allows the business to send a text up to 25 characters that will be printed on the customer invoice. Limited to simple characters, no accents or special characters.  # noqa: E501

        :param merchant_descriptor: The merchant_descriptor of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :type: str
        """

        self._merchant_descriptor = merchant_descriptor

    @property
    def user_interaction(self):
        """Gets the user_interaction of this V1paymentsorderdccconfirmPayment.  # noqa: E501

        Indicates wether the business can interact with the customer  # noqa: E501

        :return: The user_interaction of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :rtype: int
        """
        return self._user_interaction

    @user_interaction.setter
    def user_interaction(self, user_interaction):
        """Sets the user_interaction of this V1paymentsorderdccconfirmPayment.

        Indicates wether the business can interact with the customer  # noqa: E501

        :param user_interaction: The user_interaction of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :type: int
        """

        self._user_interaction = user_interaction

    @property
    def trx_type(self):
        """Gets the trx_type of this V1paymentsorderdccconfirmPayment.  # noqa: E501

        Obligatory only if an MIT exception has been selected in scaException  # noqa: E501

        :return: The trx_type of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :rtype: str
        """
        return self._trx_type

    @trx_type.setter
    def trx_type(self, trx_type):
        """Sets the trx_type of this V1paymentsorderdccconfirmPayment.

        Obligatory only if an MIT exception has been selected in scaException  # noqa: E501

        :param trx_type: The trx_type of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :type: str
        """

        self._trx_type = trx_type

    @property
    def sca_exception(self):
        """Gets the sca_exception of this V1paymentsorderdccconfirmPayment.  # noqa: E501

        TYPE OF EXCEPTION TO THE SECURE PAYMENT. If not specified, PAYCOMET will try to assign it the most appropriate possible  # noqa: E501

        :return: The sca_exception of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :rtype: str
        """
        return self._sca_exception

    @sca_exception.setter
    def sca_exception(self, sca_exception):
        """Sets the sca_exception of this V1paymentsorderdccconfirmPayment.

        TYPE OF EXCEPTION TO THE SECURE PAYMENT. If not specified, PAYCOMET will try to assign it the most appropriate possible  # noqa: E501

        :param sca_exception: The sca_exception of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :type: str
        """

        self._sca_exception = sca_exception

    @property
    def url_ok(self):
        """Gets the url_ok of this V1paymentsorderdccconfirmPayment.  # noqa: E501

        Url where the customer will be redirected after finishing a correct transaction. (Max 255 characters)  # noqa: E501

        :return: The url_ok of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :rtype: str
        """
        return self._url_ok

    @url_ok.setter
    def url_ok(self, url_ok):
        """Sets the url_ok of this V1paymentsorderdccconfirmPayment.

        Url where the customer will be redirected after finishing a correct transaction. (Max 255 characters)  # noqa: E501

        :param url_ok: The url_ok of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :type: str
        """

        self._url_ok = url_ok

    @property
    def url_ko(self):
        """Gets the url_ko of this V1paymentsorderdccconfirmPayment.  # noqa: E501

        Url where the customer will be redirected after finishing a failed transaction. (Max 255 characters)  # noqa: E501

        :return: The url_ko of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :rtype: str
        """
        return self._url_ko

    @url_ko.setter
    def url_ko(self, url_ko):
        """Sets the url_ko of this V1paymentsorderdccconfirmPayment.

        Url where the customer will be redirected after finishing a failed transaction. (Max 255 characters)  # noqa: E501

        :param url_ko: The url_ko of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :type: str
        """

        self._url_ko = url_ko

    @property
    def notify_direct_payment(self):
        """Gets the notify_direct_payment of this V1paymentsorderdccconfirmPayment.  # noqa: E501

        Configurate POST notification of the operation result in frictionless payment (possible values: 1 - force notify, 2 - not notify). It will notify if is not informed  # noqa: E501

        :return: The notify_direct_payment of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :rtype: int
        """
        return self._notify_direct_payment

    @notify_direct_payment.setter
    def notify_direct_payment(self, notify_direct_payment):
        """Sets the notify_direct_payment of this V1paymentsorderdccconfirmPayment.

        Configurate POST notification of the operation result in frictionless payment (possible values: 1 - force notify, 2 - not notify). It will notify if is not informed  # noqa: E501

        :param notify_direct_payment: The notify_direct_payment of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :type: int
        """

        self._notify_direct_payment = notify_direct_payment

    @property
    def merchant_data(self):
        """Gets the merchant_data of this V1paymentsorderdccconfirmPayment.  # noqa: E501


        :return: The merchant_data of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :rtype: V1paymentspreauthPaymentMerchantData
        """
        return self._merchant_data

    @merchant_data.setter
    def merchant_data(self, merchant_data):
        """Sets the merchant_data of this V1paymentsorderdccconfirmPayment.


        :param merchant_data: The merchant_data of this V1paymentsorderdccconfirmPayment.  # noqa: E501
        :type: V1paymentspreauthPaymentMerchantData
        """

        self._merchant_data = merchant_data

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
        if issubclass(V1paymentsorderdccconfirmPayment, dict):
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
        if not isinstance(other, V1paymentsorderdccconfirmPayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
