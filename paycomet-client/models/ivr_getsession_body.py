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

class IvrGetsessionBody(object):
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
        'ivr_provider_id': 'int',
        'ivr_station_id': 'str',
        'ivr_merchant_amount': 'int',
        'ivr_merchant_currency': 'str',
        'ivr_merchant_order': 'str',
        'ivr_merchant_language': 'str',
        'ivr_transaction_type': 'str',
        'ivr_merchant_concept': 'str',
        'ivr_subscription_startdate': 'str',
        'ivr_subscription_enddate': 'str',
        'ivr_subscription_periodicity': 'int',
        'ivr_max_retries': 'int',
        'ivr_session_timeout': 'int',
        'ivr_callback_station_timeout': 'str',
        'ivr_callback_station_ok': 'str',
        'ivr_callback_station_ko': 'str',
        'ivr_caller_phone_number': 'str',
        'ivr_provider_data01': 'str',
        'vr_provider_data02': 'str',
        'ivr_provider_data03': 'str',
        'ivr_provider_data04': 'str',
        'ivr_provider_data05': 'str'
    }

    attribute_map = {
        'terminal': 'terminal',
        'ivr_provider_id': 'ivrProviderId',
        'ivr_station_id': 'ivrStationId',
        'ivr_merchant_amount': 'ivrMerchantAmount',
        'ivr_merchant_currency': 'ivrMerchantCurrency',
        'ivr_merchant_order': 'ivrMerchantOrder',
        'ivr_merchant_language': 'ivrMerchantLanguage',
        'ivr_transaction_type': 'ivrTransactionType',
        'ivr_merchant_concept': 'ivrMerchantConcept',
        'ivr_subscription_startdate': 'ivrSubscriptionStartdate',
        'ivr_subscription_enddate': 'ivrSubscriptionEnddate',
        'ivr_subscription_periodicity': 'ivrSubscriptionPeriodicity',
        'ivr_max_retries': 'ivrMaxRetries',
        'ivr_session_timeout': 'ivrSessionTimeout',
        'ivr_callback_station_timeout': 'ivrCallbackStationTimeout',
        'ivr_callback_station_ok': 'ivrCallbackStationOk',
        'ivr_callback_station_ko': 'ivrCallbackStationKo',
        'ivr_caller_phone_number': 'ivrCallerPhoneNumber',
        'ivr_provider_data01': 'ivrProviderData01',
        'vr_provider_data02': 'vrProviderData02',
        'ivr_provider_data03': 'ivrProviderData03',
        'ivr_provider_data04': 'ivrProviderData04',
        'ivr_provider_data05': 'ivrProviderData05'
    }

    def __init__(self, terminal=None, ivr_provider_id=None, ivr_station_id=None, ivr_merchant_amount=None, ivr_merchant_currency=None, ivr_merchant_order=None, ivr_merchant_language=None, ivr_transaction_type=None, ivr_merchant_concept=None, ivr_subscription_startdate=None, ivr_subscription_enddate=None, ivr_subscription_periodicity=None, ivr_max_retries=None, ivr_session_timeout=None, ivr_callback_station_timeout=None, ivr_callback_station_ok=None, ivr_callback_station_ko=None, ivr_caller_phone_number=None, ivr_provider_data01=None, vr_provider_data02=None, ivr_provider_data03=None, ivr_provider_data04=None, ivr_provider_data05=None):  # noqa: E501
        """IvrGetsessionBody - a model defined in Swagger"""  # noqa: E501
        self._terminal = None
        self._ivr_provider_id = None
        self._ivr_station_id = None
        self._ivr_merchant_amount = None
        self._ivr_merchant_currency = None
        self._ivr_merchant_order = None
        self._ivr_merchant_language = None
        self._ivr_transaction_type = None
        self._ivr_merchant_concept = None
        self._ivr_subscription_startdate = None
        self._ivr_subscription_enddate = None
        self._ivr_subscription_periodicity = None
        self._ivr_max_retries = None
        self._ivr_session_timeout = None
        self._ivr_callback_station_timeout = None
        self._ivr_callback_station_ok = None
        self._ivr_callback_station_ko = None
        self._ivr_caller_phone_number = None
        self._ivr_provider_data01 = None
        self._vr_provider_data02 = None
        self._ivr_provider_data03 = None
        self._ivr_provider_data04 = None
        self._ivr_provider_data05 = None
        self.discriminator = None
        self.terminal = terminal
        self.ivr_provider_id = ivr_provider_id
        self.ivr_station_id = ivr_station_id
        self.ivr_merchant_amount = ivr_merchant_amount
        self.ivr_merchant_currency = ivr_merchant_currency
        self.ivr_merchant_order = ivr_merchant_order
        self.ivr_merchant_language = ivr_merchant_language
        self.ivr_transaction_type = ivr_transaction_type
        if ivr_merchant_concept is not None:
            self.ivr_merchant_concept = ivr_merchant_concept
        if ivr_subscription_startdate is not None:
            self.ivr_subscription_startdate = ivr_subscription_startdate
        if ivr_subscription_enddate is not None:
            self.ivr_subscription_enddate = ivr_subscription_enddate
        if ivr_subscription_periodicity is not None:
            self.ivr_subscription_periodicity = ivr_subscription_periodicity
        if ivr_max_retries is not None:
            self.ivr_max_retries = ivr_max_retries
        if ivr_session_timeout is not None:
            self.ivr_session_timeout = ivr_session_timeout
        if ivr_callback_station_timeout is not None:
            self.ivr_callback_station_timeout = ivr_callback_station_timeout
        if ivr_callback_station_ok is not None:
            self.ivr_callback_station_ok = ivr_callback_station_ok
        if ivr_callback_station_ko is not None:
            self.ivr_callback_station_ko = ivr_callback_station_ko
        if ivr_caller_phone_number is not None:
            self.ivr_caller_phone_number = ivr_caller_phone_number
        if ivr_provider_data01 is not None:
            self.ivr_provider_data01 = ivr_provider_data01
        if vr_provider_data02 is not None:
            self.vr_provider_data02 = vr_provider_data02
        if ivr_provider_data03 is not None:
            self.ivr_provider_data03 = ivr_provider_data03
        if ivr_provider_data04 is not None:
            self.ivr_provider_data04 = ivr_provider_data04
        if ivr_provider_data05 is not None:
            self.ivr_provider_data05 = ivr_provider_data05

    @property
    def terminal(self):
        """Gets the terminal of this IvrGetsessionBody.  # noqa: E501

        Product or terminal Id.  # noqa: E501

        :return: The terminal of this IvrGetsessionBody.  # noqa: E501
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this IvrGetsessionBody.

        Product or terminal Id.  # noqa: E501

        :param terminal: The terminal of this IvrGetsessionBody.  # noqa: E501
        :type: int
        """
        if terminal is None:
            raise ValueError("Invalid value for `terminal`, must not be `None`")  # noqa: E501

        self._terminal = terminal

    @property
    def ivr_provider_id(self):
        """Gets the ivr_provider_id of this IvrGetsessionBody.  # noqa: E501

        Supplier / IVR integrator code.  # noqa: E501

        :return: The ivr_provider_id of this IvrGetsessionBody.  # noqa: E501
        :rtype: int
        """
        return self._ivr_provider_id

    @ivr_provider_id.setter
    def ivr_provider_id(self, ivr_provider_id):
        """Sets the ivr_provider_id of this IvrGetsessionBody.

        Supplier / IVR integrator code.  # noqa: E501

        :param ivr_provider_id: The ivr_provider_id of this IvrGetsessionBody.  # noqa: E501
        :type: int
        """
        if ivr_provider_id is None:
            raise ValueError("Invalid value for `ivr_provider_id`, must not be `None`")  # noqa: E501

        self._ivr_provider_id = ivr_provider_id

    @property
    def ivr_station_id(self):
        """Gets the ivr_station_id of this IvrGetsessionBody.  # noqa: E501

        Location identifier.  # noqa: E501

        :return: The ivr_station_id of this IvrGetsessionBody.  # noqa: E501
        :rtype: str
        """
        return self._ivr_station_id

    @ivr_station_id.setter
    def ivr_station_id(self, ivr_station_id):
        """Sets the ivr_station_id of this IvrGetsessionBody.

        Location identifier.  # noqa: E501

        :param ivr_station_id: The ivr_station_id of this IvrGetsessionBody.  # noqa: E501
        :type: str
        """
        if ivr_station_id is None:
            raise ValueError("Invalid value for `ivr_station_id`, must not be `None`")  # noqa: E501

        self._ivr_station_id = ivr_station_id

    @property
    def ivr_merchant_amount(self):
        """Gets the ivr_merchant_amount of this IvrGetsessionBody.  # noqa: E501

        Amount of the operation in full format. 1,00 EURO = 100, 4,50 EUROS = 450...  # noqa: E501

        :return: The ivr_merchant_amount of this IvrGetsessionBody.  # noqa: E501
        :rtype: int
        """
        return self._ivr_merchant_amount

    @ivr_merchant_amount.setter
    def ivr_merchant_amount(self, ivr_merchant_amount):
        """Sets the ivr_merchant_amount of this IvrGetsessionBody.

        Amount of the operation in full format. 1,00 EURO = 100, 4,50 EUROS = 450...  # noqa: E501

        :param ivr_merchant_amount: The ivr_merchant_amount of this IvrGetsessionBody.  # noqa: E501
        :type: int
        """
        if ivr_merchant_amount is None:
            raise ValueError("Invalid value for `ivr_merchant_amount`, must not be `None`")  # noqa: E501

        self._ivr_merchant_amount = ivr_merchant_amount

    @property
    def ivr_merchant_currency(self):
        """Gets the ivr_merchant_currency of this IvrGetsessionBody.  # noqa: E501

        Transaction currency.  # noqa: E501

        :return: The ivr_merchant_currency of this IvrGetsessionBody.  # noqa: E501
        :rtype: str
        """
        return self._ivr_merchant_currency

    @ivr_merchant_currency.setter
    def ivr_merchant_currency(self, ivr_merchant_currency):
        """Sets the ivr_merchant_currency of this IvrGetsessionBody.

        Transaction currency.  # noqa: E501

        :param ivr_merchant_currency: The ivr_merchant_currency of this IvrGetsessionBody.  # noqa: E501
        :type: str
        """
        if ivr_merchant_currency is None:
            raise ValueError("Invalid value for `ivr_merchant_currency`, must not be `None`")  # noqa: E501

        self._ivr_merchant_currency = ivr_merchant_currency

    @property
    def ivr_merchant_order(self):
        """Gets the ivr_merchant_order of this IvrGetsessionBody.  # noqa: E501

        Operation reference. It must be unique in each valid transaction. IMPORTANT IN CASE OF SUBSCRIPTIONS Do not include the characters “[“ or “]”, they will be used to recognise the business idUser.  # noqa: E501

        :return: The ivr_merchant_order of this IvrGetsessionBody.  # noqa: E501
        :rtype: str
        """
        return self._ivr_merchant_order

    @ivr_merchant_order.setter
    def ivr_merchant_order(self, ivr_merchant_order):
        """Sets the ivr_merchant_order of this IvrGetsessionBody.

        Operation reference. It must be unique in each valid transaction. IMPORTANT IN CASE OF SUBSCRIPTIONS Do not include the characters “[“ or “]”, they will be used to recognise the business idUser.  # noqa: E501

        :param ivr_merchant_order: The ivr_merchant_order of this IvrGetsessionBody.  # noqa: E501
        :type: str
        """
        if ivr_merchant_order is None:
            raise ValueError("Invalid value for `ivr_merchant_order`, must not be `None`")  # noqa: E501

        self._ivr_merchant_order = ivr_merchant_order

    @property
    def ivr_merchant_language(self):
        """Gets the ivr_merchant_language of this IvrGetsessionBody.  # noqa: E501

        Language (iso2) in which the IVR phrases will be sent  # noqa: E501

        :return: The ivr_merchant_language of this IvrGetsessionBody.  # noqa: E501
        :rtype: str
        """
        return self._ivr_merchant_language

    @ivr_merchant_language.setter
    def ivr_merchant_language(self, ivr_merchant_language):
        """Sets the ivr_merchant_language of this IvrGetsessionBody.

        Language (iso2) in which the IVR phrases will be sent  # noqa: E501

        :param ivr_merchant_language: The ivr_merchant_language of this IvrGetsessionBody.  # noqa: E501
        :type: str
        """
        if ivr_merchant_language is None:
            raise ValueError("Invalid value for `ivr_merchant_language`, must not be `None`")  # noqa: E501

        self._ivr_merchant_language = ivr_merchant_language

    @property
    def ivr_transaction_type(self):
        """Gets the ivr_transaction_type of this IvrGetsessionBody.  # noqa: E501

        Possible types 107 Bankstore user registration 1 Authorization 3 Pre-authorization 9 Subscription  # noqa: E501

        :return: The ivr_transaction_type of this IvrGetsessionBody.  # noqa: E501
        :rtype: str
        """
        return self._ivr_transaction_type

    @ivr_transaction_type.setter
    def ivr_transaction_type(self, ivr_transaction_type):
        """Sets the ivr_transaction_type of this IvrGetsessionBody.

        Possible types 107 Bankstore user registration 1 Authorization 3 Pre-authorization 9 Subscription  # noqa: E501

        :param ivr_transaction_type: The ivr_transaction_type of this IvrGetsessionBody.  # noqa: E501
        :type: str
        """
        if ivr_transaction_type is None:
            raise ValueError("Invalid value for `ivr_transaction_type`, must not be `None`")  # noqa: E501

        self._ivr_transaction_type = ivr_transaction_type

    @property
    def ivr_merchant_concept(self):
        """Gets the ivr_merchant_concept of this IvrGetsessionBody.  # noqa: E501

        Operation concept.  # noqa: E501

        :return: The ivr_merchant_concept of this IvrGetsessionBody.  # noqa: E501
        :rtype: str
        """
        return self._ivr_merchant_concept

    @ivr_merchant_concept.setter
    def ivr_merchant_concept(self, ivr_merchant_concept):
        """Sets the ivr_merchant_concept of this IvrGetsessionBody.

        Operation concept.  # noqa: E501

        :param ivr_merchant_concept: The ivr_merchant_concept of this IvrGetsessionBody.  # noqa: E501
        :type: str
        """

        self._ivr_merchant_concept = ivr_merchant_concept

    @property
    def ivr_subscription_startdate(self):
        """Gets the ivr_subscription_startdate of this IvrGetsessionBody.  # noqa: E501

        Mandatory in subscriptions. Subscription start date.  # noqa: E501

        :return: The ivr_subscription_startdate of this IvrGetsessionBody.  # noqa: E501
        :rtype: str
        """
        return self._ivr_subscription_startdate

    @ivr_subscription_startdate.setter
    def ivr_subscription_startdate(self, ivr_subscription_startdate):
        """Sets the ivr_subscription_startdate of this IvrGetsessionBody.

        Mandatory in subscriptions. Subscription start date.  # noqa: E501

        :param ivr_subscription_startdate: The ivr_subscription_startdate of this IvrGetsessionBody.  # noqa: E501
        :type: str
        """

        self._ivr_subscription_startdate = ivr_subscription_startdate

    @property
    def ivr_subscription_enddate(self):
        """Gets the ivr_subscription_enddate of this IvrGetsessionBody.  # noqa: E501

        Mandatory in subscriptions. Subscription end date.  # noqa: E501

        :return: The ivr_subscription_enddate of this IvrGetsessionBody.  # noqa: E501
        :rtype: str
        """
        return self._ivr_subscription_enddate

    @ivr_subscription_enddate.setter
    def ivr_subscription_enddate(self, ivr_subscription_enddate):
        """Sets the ivr_subscription_enddate of this IvrGetsessionBody.

        Mandatory in subscriptions. Subscription end date.  # noqa: E501

        :param ivr_subscription_enddate: The ivr_subscription_enddate of this IvrGetsessionBody.  # noqa: E501
        :type: str
        """

        self._ivr_subscription_enddate = ivr_subscription_enddate

    @property
    def ivr_subscription_periodicity(self):
        """Gets the ivr_subscription_periodicity of this IvrGetsessionBody.  # noqa: E501

        Mandatory in subscriptions. Frequency of the payment from the start date. The number is expressed in Days. It cannot be more than 365 days.  # noqa: E501

        :return: The ivr_subscription_periodicity of this IvrGetsessionBody.  # noqa: E501
        :rtype: int
        """
        return self._ivr_subscription_periodicity

    @ivr_subscription_periodicity.setter
    def ivr_subscription_periodicity(self, ivr_subscription_periodicity):
        """Sets the ivr_subscription_periodicity of this IvrGetsessionBody.

        Mandatory in subscriptions. Frequency of the payment from the start date. The number is expressed in Days. It cannot be more than 365 days.  # noqa: E501

        :param ivr_subscription_periodicity: The ivr_subscription_periodicity of this IvrGetsessionBody.  # noqa: E501
        :type: int
        """

        self._ivr_subscription_periodicity = ivr_subscription_periodicity

    @property
    def ivr_max_retries(self):
        """Gets the ivr_max_retries of this IvrGetsessionBody.  # noqa: E501

        Number of attempts permitted.  # noqa: E501

        :return: The ivr_max_retries of this IvrGetsessionBody.  # noqa: E501
        :rtype: int
        """
        return self._ivr_max_retries

    @ivr_max_retries.setter
    def ivr_max_retries(self, ivr_max_retries):
        """Sets the ivr_max_retries of this IvrGetsessionBody.

        Number of attempts permitted.  # noqa: E501

        :param ivr_max_retries: The ivr_max_retries of this IvrGetsessionBody.  # noqa: E501
        :type: int
        """

        self._ivr_max_retries = ivr_max_retries

    @property
    def ivr_session_timeout(self):
        """Gets the ivr_session_timeout of this IvrGetsessionBody.  # noqa: E501

        Maximum session time. In seconds.  # noqa: E501

        :return: The ivr_session_timeout of this IvrGetsessionBody.  # noqa: E501
        :rtype: int
        """
        return self._ivr_session_timeout

    @ivr_session_timeout.setter
    def ivr_session_timeout(self, ivr_session_timeout):
        """Sets the ivr_session_timeout of this IvrGetsessionBody.

        Maximum session time. In seconds.  # noqa: E501

        :param ivr_session_timeout: The ivr_session_timeout of this IvrGetsessionBody.  # noqa: E501
        :type: int
        """

        self._ivr_session_timeout = ivr_session_timeout

    @property
    def ivr_callback_station_timeout(self):
        """Gets the ivr_callback_station_timeout of this IvrGetsessionBody.  # noqa: E501

        Extension of return in case of timeout.  # noqa: E501

        :return: The ivr_callback_station_timeout of this IvrGetsessionBody.  # noqa: E501
        :rtype: str
        """
        return self._ivr_callback_station_timeout

    @ivr_callback_station_timeout.setter
    def ivr_callback_station_timeout(self, ivr_callback_station_timeout):
        """Sets the ivr_callback_station_timeout of this IvrGetsessionBody.

        Extension of return in case of timeout.  # noqa: E501

        :param ivr_callback_station_timeout: The ivr_callback_station_timeout of this IvrGetsessionBody.  # noqa: E501
        :type: str
        """

        self._ivr_callback_station_timeout = ivr_callback_station_timeout

    @property
    def ivr_callback_station_ok(self):
        """Gets the ivr_callback_station_ok of this IvrGetsessionBody.  # noqa: E501

        Extension of return in case of operation OK.  # noqa: E501

        :return: The ivr_callback_station_ok of this IvrGetsessionBody.  # noqa: E501
        :rtype: str
        """
        return self._ivr_callback_station_ok

    @ivr_callback_station_ok.setter
    def ivr_callback_station_ok(self, ivr_callback_station_ok):
        """Sets the ivr_callback_station_ok of this IvrGetsessionBody.

        Extension of return in case of operation OK.  # noqa: E501

        :param ivr_callback_station_ok: The ivr_callback_station_ok of this IvrGetsessionBody.  # noqa: E501
        :type: str
        """

        self._ivr_callback_station_ok = ivr_callback_station_ok

    @property
    def ivr_callback_station_ko(self):
        """Gets the ivr_callback_station_ko of this IvrGetsessionBody.  # noqa: E501

        Extension of return in case of operation KO.  # noqa: E501

        :return: The ivr_callback_station_ko of this IvrGetsessionBody.  # noqa: E501
        :rtype: str
        """
        return self._ivr_callback_station_ko

    @ivr_callback_station_ko.setter
    def ivr_callback_station_ko(self, ivr_callback_station_ko):
        """Sets the ivr_callback_station_ko of this IvrGetsessionBody.

        Extension of return in case of operation KO.  # noqa: E501

        :param ivr_callback_station_ko: The ivr_callback_station_ko of this IvrGetsessionBody.  # noqa: E501
        :type: str
        """

        self._ivr_callback_station_ko = ivr_callback_station_ko

    @property
    def ivr_caller_phone_number(self):
        """Gets the ivr_caller_phone_number of this IvrGetsessionBody.  # noqa: E501

        Number of incoming call.  # noqa: E501

        :return: The ivr_caller_phone_number of this IvrGetsessionBody.  # noqa: E501
        :rtype: str
        """
        return self._ivr_caller_phone_number

    @ivr_caller_phone_number.setter
    def ivr_caller_phone_number(self, ivr_caller_phone_number):
        """Sets the ivr_caller_phone_number of this IvrGetsessionBody.

        Number of incoming call.  # noqa: E501

        :param ivr_caller_phone_number: The ivr_caller_phone_number of this IvrGetsessionBody.  # noqa: E501
        :type: str
        """

        self._ivr_caller_phone_number = ivr_caller_phone_number

    @property
    def ivr_provider_data01(self):
        """Gets the ivr_provider_data01 of this IvrGetsessionBody.  # noqa: E501

        Optional field.  # noqa: E501

        :return: The ivr_provider_data01 of this IvrGetsessionBody.  # noqa: E501
        :rtype: str
        """
        return self._ivr_provider_data01

    @ivr_provider_data01.setter
    def ivr_provider_data01(self, ivr_provider_data01):
        """Sets the ivr_provider_data01 of this IvrGetsessionBody.

        Optional field.  # noqa: E501

        :param ivr_provider_data01: The ivr_provider_data01 of this IvrGetsessionBody.  # noqa: E501
        :type: str
        """

        self._ivr_provider_data01 = ivr_provider_data01

    @property
    def vr_provider_data02(self):
        """Gets the vr_provider_data02 of this IvrGetsessionBody.  # noqa: E501

        Optional field.  # noqa: E501

        :return: The vr_provider_data02 of this IvrGetsessionBody.  # noqa: E501
        :rtype: str
        """
        return self._vr_provider_data02

    @vr_provider_data02.setter
    def vr_provider_data02(self, vr_provider_data02):
        """Sets the vr_provider_data02 of this IvrGetsessionBody.

        Optional field.  # noqa: E501

        :param vr_provider_data02: The vr_provider_data02 of this IvrGetsessionBody.  # noqa: E501
        :type: str
        """

        self._vr_provider_data02 = vr_provider_data02

    @property
    def ivr_provider_data03(self):
        """Gets the ivr_provider_data03 of this IvrGetsessionBody.  # noqa: E501

        Optional field.  # noqa: E501

        :return: The ivr_provider_data03 of this IvrGetsessionBody.  # noqa: E501
        :rtype: str
        """
        return self._ivr_provider_data03

    @ivr_provider_data03.setter
    def ivr_provider_data03(self, ivr_provider_data03):
        """Sets the ivr_provider_data03 of this IvrGetsessionBody.

        Optional field.  # noqa: E501

        :param ivr_provider_data03: The ivr_provider_data03 of this IvrGetsessionBody.  # noqa: E501
        :type: str
        """

        self._ivr_provider_data03 = ivr_provider_data03

    @property
    def ivr_provider_data04(self):
        """Gets the ivr_provider_data04 of this IvrGetsessionBody.  # noqa: E501

        Optional field.  # noqa: E501

        :return: The ivr_provider_data04 of this IvrGetsessionBody.  # noqa: E501
        :rtype: str
        """
        return self._ivr_provider_data04

    @ivr_provider_data04.setter
    def ivr_provider_data04(self, ivr_provider_data04):
        """Sets the ivr_provider_data04 of this IvrGetsessionBody.

        Optional field.  # noqa: E501

        :param ivr_provider_data04: The ivr_provider_data04 of this IvrGetsessionBody.  # noqa: E501
        :type: str
        """

        self._ivr_provider_data04 = ivr_provider_data04

    @property
    def ivr_provider_data05(self):
        """Gets the ivr_provider_data05 of this IvrGetsessionBody.  # noqa: E501

        Optional field.  # noqa: E501

        :return: The ivr_provider_data05 of this IvrGetsessionBody.  # noqa: E501
        :rtype: str
        """
        return self._ivr_provider_data05

    @ivr_provider_data05.setter
    def ivr_provider_data05(self, ivr_provider_data05):
        """Sets the ivr_provider_data05 of this IvrGetsessionBody.

        Optional field.  # noqa: E501

        :param ivr_provider_data05: The ivr_provider_data05 of this IvrGetsessionBody.  # noqa: E501
        :type: str
        """

        self._ivr_provider_data05 = ivr_provider_data05

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
        if issubclass(IvrGetsessionBody, dict):
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
        if not isinstance(other, IvrGetsessionBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other