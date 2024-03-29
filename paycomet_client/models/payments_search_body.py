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

class PaymentsSearchBody(object):
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
        'sort_type': 'int',
        'sort_order': 'str',
        'operations': 'list[int]',
        'min_amount': 'int',
        'max_amount': 'int',
        'state': 'int',
        'from_date': 'str',
        'to_date': 'str',
        'currency': 'str',
        'limit': 'int',
        'order': 'str',
        'search_type': 'int'
    }

    attribute_map = {
        'terminal': 'terminal',
        'sort_type': 'sortType',
        'sort_order': 'sortOrder',
        'operations': 'operations',
        'min_amount': 'minAmount',
        'max_amount': 'maxAmount',
        'state': 'state',
        'from_date': 'fromDate',
        'to_date': 'toDate',
        'currency': 'currency',
        'limit': 'limit',
        'order': 'order',
        'search_type': 'searchType'
    }

    def __init__(self, terminal=None, sort_type=None, sort_order=None, operations=None, min_amount=None, max_amount=None, state=None, from_date=None, to_date=None, currency=None, limit=10000, order=None, search_type=None):  # noqa: E501
        """PaymentsSearchBody - a model defined in Swagger"""  # noqa: E501
        self._terminal = None
        self._sort_type = None
        self._sort_order = None
        self._operations = None
        self._min_amount = None
        self._max_amount = None
        self._state = None
        self._from_date = None
        self._to_date = None
        self._currency = None
        self._limit = None
        self._order = None
        self._search_type = None
        self.discriminator = None
        self.terminal = terminal
        self.sort_type = sort_type
        self.sort_order = sort_order
        self.operations = operations
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.state = state
        self.from_date = from_date
        self.to_date = to_date
        self.currency = currency
        if limit is not None:
            self.limit = limit
        if order is not None:
            self.order = order
        if search_type is not None:
            self.search_type = search_type

    @property
    def terminal(self):
        """Gets the terminal of this PaymentsSearchBody.  # noqa: E501

        Product or terminal Id.  # noqa: E501

        :return: The terminal of this PaymentsSearchBody.  # noqa: E501
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this PaymentsSearchBody.

        Product or terminal Id.  # noqa: E501

        :param terminal: The terminal of this PaymentsSearchBody.  # noqa: E501
        :type: int
        """
        if terminal is None:
            raise ValueError("Invalid value for `terminal`, must not be `None`")  # noqa: E501

        self._terminal = terminal

    @property
    def sort_type(self):
        """Gets the sort_type of this PaymentsSearchBody.  # noqa: E501

        Sorting type (0 No sorting, 1 date, 2 order, 3 type, 4 state, 5 terminal, 6 amount, 7 user).  # noqa: E501

        :return: The sort_type of this PaymentsSearchBody.  # noqa: E501
        :rtype: int
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        """Sets the sort_type of this PaymentsSearchBody.

        Sorting type (0 No sorting, 1 date, 2 order, 3 type, 4 state, 5 terminal, 6 amount, 7 user).  # noqa: E501

        :param sort_type: The sort_type of this PaymentsSearchBody.  # noqa: E501
        :type: int
        """
        if sort_type is None:
            raise ValueError("Invalid value for `sort_type`, must not be `None`")  # noqa: E501

        self._sort_type = sort_type

    @property
    def sort_order(self):
        """Gets the sort_order of this PaymentsSearchBody.  # noqa: E501

        Sort results ASC = Ascending, DESC = Descending.  # noqa: E501

        :return: The sort_order of this PaymentsSearchBody.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this PaymentsSearchBody.

        Sort results ASC = Ascending, DESC = Descending.  # noqa: E501

        :param sort_order: The sort_order of this PaymentsSearchBody.  # noqa: E501
        :type: str
        """
        if sort_order is None:
            raise ValueError("Invalid value for `sort_order`, must not be `None`")  # noqa: E501

        self._sort_order = sort_order

    @property
    def operations(self):
        """Gets the operations of this PaymentsSearchBody.  # noqa: E501


        :return: The operations of this PaymentsSearchBody.  # noqa: E501
        :rtype: list[int]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this PaymentsSearchBody.


        :param operations: The operations of this PaymentsSearchBody.  # noqa: E501
        :type: list[int]
        """
        if operations is None:
            raise ValueError("Invalid value for `operations`, must not be `None`")  # noqa: E501

        self._operations = operations

    @property
    def min_amount(self):
        """Gets the min_amount of this PaymentsSearchBody.  # noqa: E501

        Minimum amount of the operation in whole format  # noqa: E501

        :return: The min_amount of this PaymentsSearchBody.  # noqa: E501
        :rtype: int
        """
        return self._min_amount

    @min_amount.setter
    def min_amount(self, min_amount):
        """Sets the min_amount of this PaymentsSearchBody.

        Minimum amount of the operation in whole format  # noqa: E501

        :param min_amount: The min_amount of this PaymentsSearchBody.  # noqa: E501
        :type: int
        """
        if min_amount is None:
            raise ValueError("Invalid value for `min_amount`, must not be `None`")  # noqa: E501

        self._min_amount = min_amount

    @property
    def max_amount(self):
        """Gets the max_amount of this PaymentsSearchBody.  # noqa: E501

        Maximum amount of the operation in whole format  # noqa: E501

        :return: The max_amount of this PaymentsSearchBody.  # noqa: E501
        :rtype: int
        """
        return self._max_amount

    @max_amount.setter
    def max_amount(self, max_amount):
        """Sets the max_amount of this PaymentsSearchBody.

        Maximum amount of the operation in whole format  # noqa: E501

        :param max_amount: The max_amount of this PaymentsSearchBody.  # noqa: E501
        :type: int
        """
        if max_amount is None:
            raise ValueError("Invalid value for `max_amount`, must not be `None`")  # noqa: E501

        self._max_amount = max_amount

    @property
    def state(self):
        """Gets the state of this PaymentsSearchBody.  # noqa: E501

        Result of operation. 0 is operation failed, 1 operation correct and 2 operation unfinished (for pending operations from an SCA or 3DS).  # noqa: E501

        :return: The state of this PaymentsSearchBody.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentsSearchBody.

        Result of operation. 0 is operation failed, 1 operation correct and 2 operation unfinished (for pending operations from an SCA or 3DS).  # noqa: E501

        :param state: The state of this PaymentsSearchBody.  # noqa: E501
        :type: int
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def from_date(self):
        """Gets the from_date of this PaymentsSearchBody.  # noqa: E501

        Start datetime limit (format: YmdHis)  # noqa: E501

        :return: The from_date of this PaymentsSearchBody.  # noqa: E501
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this PaymentsSearchBody.

        Start datetime limit (format: YmdHis)  # noqa: E501

        :param from_date: The from_date of this PaymentsSearchBody.  # noqa: E501
        :type: str
        """
        if from_date is None:
            raise ValueError("Invalid value for `from_date`, must not be `None`")  # noqa: E501

        self._from_date = from_date

    @property
    def to_date(self):
        """Gets the to_date of this PaymentsSearchBody.  # noqa: E501

        Finish datetime limit (format: YmdHis)  # noqa: E501

        :return: The to_date of this PaymentsSearchBody.  # noqa: E501
        :rtype: str
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this PaymentsSearchBody.

        Finish datetime limit (format: YmdHis)  # noqa: E501

        :param to_date: The to_date of this PaymentsSearchBody.  # noqa: E501
        :type: str
        """
        if to_date is None:
            raise ValueError("Invalid value for `to_date`, must not be `None`")  # noqa: E501

        self._to_date = to_date

    @property
    def currency(self):
        """Gets the currency of this PaymentsSearchBody.  # noqa: E501

        Currency of the transaction.   # noqa: E501

        :return: The currency of this PaymentsSearchBody.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PaymentsSearchBody.

        Currency of the transaction.   # noqa: E501

        :param currency: The currency of this PaymentsSearchBody.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def limit(self):
        """Gets the limit of this PaymentsSearchBody.  # noqa: E501

        Results limit.  # noqa: E501

        :return: The limit of this PaymentsSearchBody.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PaymentsSearchBody.

        Results limit.  # noqa: E501

        :param limit: The limit of this PaymentsSearchBody.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def order(self):
        """Gets the order of this PaymentsSearchBody.  # noqa: E501

        Unique reference for merchant's purchase  # noqa: E501

        :return: The order of this PaymentsSearchBody.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this PaymentsSearchBody.

        Unique reference for merchant's purchase  # noqa: E501

        :param order: The order of this PaymentsSearchBody.  # noqa: E501
        :type: str
        """

        self._order = order

    @property
    def search_type(self):
        """Gets the search_type of this PaymentsSearchBody.  # noqa: E501

        Comparison type. 0 LIKE comparison (%xxx%) , 1 exact comparison (=)  # noqa: E501

        :return: The search_type of this PaymentsSearchBody.  # noqa: E501
        :rtype: int
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        """Sets the search_type of this PaymentsSearchBody.

        Comparison type. 0 LIKE comparison (%xxx%) , 1 exact comparison (=)  # noqa: E501

        :param search_type: The search_type of this PaymentsSearchBody.  # noqa: E501
        :type: int
        """

        self._search_type = search_type

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
        if issubclass(PaymentsSearchBody, dict):
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
        if not isinstance(other, PaymentsSearchBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
