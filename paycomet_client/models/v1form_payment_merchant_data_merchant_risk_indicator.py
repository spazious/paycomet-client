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

class V1formPaymentMerchantDataMerchantRiskIndicator(object):
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
        'delivery_email_address': 'str',
        'delivery_timeframe': 'str',
        'gift_card_amount': 'str',
        'gift_card_count': 'int',
        'gift_card_curr': 'str',
        'pre_order_date': 'str',
        'pre_order_purchase_ind': 'str',
        'reorder_items_ind': 'str',
        'ship_indicator': 'str'
    }

    attribute_map = {
        'delivery_email_address': 'deliveryEmailAddress',
        'delivery_timeframe': 'deliveryTimeframe',
        'gift_card_amount': 'giftCardAmount',
        'gift_card_count': 'giftCardCount',
        'gift_card_curr': 'giftCardCurr',
        'pre_order_date': 'preOrderDate',
        'pre_order_purchase_ind': 'preOrderPurchaseInd',
        'reorder_items_ind': 'reorderItemsInd',
        'ship_indicator': 'shipIndicator'
    }

    def __init__(self, delivery_email_address=None, delivery_timeframe=None, gift_card_amount=None, gift_card_count=None, gift_card_curr=None, pre_order_date=None, pre_order_purchase_ind=None, reorder_items_ind=None, ship_indicator=None):  # noqa: E501
        """V1formPaymentMerchantDataMerchantRiskIndicator - a model defined in Swagger"""  # noqa: E501
        self._delivery_email_address = None
        self._delivery_timeframe = None
        self._gift_card_amount = None
        self._gift_card_count = None
        self._gift_card_curr = None
        self._pre_order_date = None
        self._pre_order_purchase_ind = None
        self._reorder_items_ind = None
        self._ship_indicator = None
        self.discriminator = None
        if delivery_email_address is not None:
            self.delivery_email_address = delivery_email_address
        if delivery_timeframe is not None:
            self.delivery_timeframe = delivery_timeframe
        if gift_card_amount is not None:
            self.gift_card_amount = gift_card_amount
        if gift_card_count is not None:
            self.gift_card_count = gift_card_count
        if gift_card_curr is not None:
            self.gift_card_curr = gift_card_curr
        if pre_order_date is not None:
            self.pre_order_date = pre_order_date
        if pre_order_purchase_ind is not None:
            self.pre_order_purchase_ind = pre_order_purchase_ind
        if reorder_items_ind is not None:
            self.reorder_items_ind = reorder_items_ind
        if ship_indicator is not None:
            self.ship_indicator = ship_indicator

    @property
    def delivery_email_address(self):
        """Gets the delivery_email_address of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501

        For electronic delivery, the email address to which the goods were delivered  # noqa: E501

        :return: The delivery_email_address of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501
        :rtype: str
        """
        return self._delivery_email_address

    @delivery_email_address.setter
    def delivery_email_address(self, delivery_email_address):
        """Sets the delivery_email_address of this V1formPaymentMerchantDataMerchantRiskIndicator.

        For electronic delivery, the email address to which the goods were delivered  # noqa: E501

        :param delivery_email_address: The delivery_email_address of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501
        :type: str
        """

        self._delivery_email_address = delivery_email_address

    @property
    def delivery_timeframe(self):
        """Gets the delivery_timeframe of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501

        Indicates the delivery period of the goods. Accepted values: 01 = Electronic delivery, 02 = Delivery on the same day, 03 = 24 hour delivery, 04 = Delivery in 2 days or more  # noqa: E501

        :return: The delivery_timeframe of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501
        :rtype: str
        """
        return self._delivery_timeframe

    @delivery_timeframe.setter
    def delivery_timeframe(self, delivery_timeframe):
        """Sets the delivery_timeframe of this V1formPaymentMerchantDataMerchantRiskIndicator.

        Indicates the delivery period of the goods. Accepted values: 01 = Electronic delivery, 02 = Delivery on the same day, 03 = 24 hour delivery, 04 = Delivery in 2 days or more  # noqa: E501

        :param delivery_timeframe: The delivery_timeframe of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501
        :type: str
        """

        self._delivery_timeframe = delivery_timeframe

    @property
    def gift_card_amount(self):
        """Gets the gift_card_amount of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501

        For purchases from prepaid cards or gift cards, the total amount of the purchase in major units (for example, USD 123.45 is 123)  # noqa: E501

        :return: The gift_card_amount of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501
        :rtype: str
        """
        return self._gift_card_amount

    @gift_card_amount.setter
    def gift_card_amount(self, gift_card_amount):
        """Sets the gift_card_amount of this V1formPaymentMerchantDataMerchantRiskIndicator.

        For purchases from prepaid cards or gift cards, the total amount of the purchase in major units (for example, USD 123.45 is 123)  # noqa: E501

        :param gift_card_amount: The gift_card_amount of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501
        :type: str
        """

        self._gift_card_amount = gift_card_amount

    @property
    def gift_card_count(self):
        """Gets the gift_card_count of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501

        For purchases from prepaid cards or gift cards, total count of prepaid cards or gift cards/gift codes purchased  # noqa: E501

        :return: The gift_card_count of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501
        :rtype: int
        """
        return self._gift_card_count

    @gift_card_count.setter
    def gift_card_count(self, gift_card_count):
        """Sets the gift_card_count of this V1formPaymentMerchantDataMerchantRiskIndicator.

        For purchases from prepaid cards or gift cards, total count of prepaid cards or gift cards/gift codes purchased  # noqa: E501

        :param gift_card_count: The gift_card_count of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501
        :type: int
        """

        self._gift_card_count = gift_card_count

    @property
    def gift_card_curr(self):
        """Gets the gift_card_curr of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501

        For the purchase of prepaid/gift cards, code ISO-4217 of currency of the card  # noqa: E501

        :return: The gift_card_curr of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501
        :rtype: str
        """
        return self._gift_card_curr

    @gift_card_curr.setter
    def gift_card_curr(self, gift_card_curr):
        """Sets the gift_card_curr of this V1formPaymentMerchantDataMerchantRiskIndicator.

        For the purchase of prepaid/gift cards, code ISO-4217 of currency of the card  # noqa: E501

        :param gift_card_curr: The gift_card_curr of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501
        :type: str
        """

        self._gift_card_curr = gift_card_curr

    @property
    def pre_order_date(self):
        """Gets the pre_order_date of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501

        For a pre-ordered purchase, the forecast availability date of the goods. Date format: YYYYMMDD  # noqa: E501

        :return: The pre_order_date of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501
        :rtype: str
        """
        return self._pre_order_date

    @pre_order_date.setter
    def pre_order_date(self, pre_order_date):
        """Sets the pre_order_date of this V1formPaymentMerchantDataMerchantRiskIndicator.

        For a pre-ordered purchase, the forecast availability date of the goods. Date format: YYYYMMDD  # noqa: E501

        :param pre_order_date: The pre_order_date of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501
        :type: str
        """

        self._pre_order_date = pre_order_date

    @property
    def pre_order_purchase_ind(self):
        """Gets the pre_order_purchase_ind of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501

        Indicates whether the customer makes an order with availability or future launch date. Accepted values: 01 = Goods available, 02 = Future availability  # noqa: E501

        :return: The pre_order_purchase_ind of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501
        :rtype: str
        """
        return self._pre_order_purchase_ind

    @pre_order_purchase_ind.setter
    def pre_order_purchase_ind(self, pre_order_purchase_ind):
        """Sets the pre_order_purchase_ind of this V1formPaymentMerchantDataMerchantRiskIndicator.

        Indicates whether the customer makes an order with availability or future launch date. Accepted values: 01 = Goods available, 02 = Future availability  # noqa: E501

        :param pre_order_purchase_ind: The pre_order_purchase_ind of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501
        :type: str
        """

        self._pre_order_purchase_ind = pre_order_purchase_ind

    @property
    def reorder_items_ind(self):
        """Gets the reorder_items_ind of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501

        Indicates whether the card is reordering previously purchased goods. Accepted values: 01 = First time purchased, 02 = Previously purchased  # noqa: E501

        :return: The reorder_items_ind of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501
        :rtype: str
        """
        return self._reorder_items_ind

    @reorder_items_ind.setter
    def reorder_items_ind(self, reorder_items_ind):
        """Sets the reorder_items_ind of this V1formPaymentMerchantDataMerchantRiskIndicator.

        Indicates whether the card is reordering previously purchased goods. Accepted values: 01 = First time purchased, 02 = Previously purchased  # noqa: E501

        :param reorder_items_ind: The reorder_items_ind of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501
        :type: str
        """

        self._reorder_items_ind = reorder_items_ind

    @property
    def ship_indicator(self):
        """Gets the ship_indicator of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501

        Indicates the delivery method selected for the transaction. Businesses must select the delivery indicator code which more precisely describes the specific transaction of the payment user, not their general commercial activity. If one or more items are included in the sale, use the delivery Indicator code for physical goods, or if all products are digital, use the delivery Indicator code which describes the most expensive item. Accepted values: 01 = Delivery to the invoice address of the customer, 02 = Delivery to another verified address of the client, 03 = Delivery to an address other than that of the customer’s invoice address, 04 = Delivery to the store or collection at premises (the address of the store will be stored in the delivery address fields), 05 = Digital goods (includes online services, electronic gift cards and discount coupons), 06 = Tickets for events and trips, without delivery, 07 = Other (for example, games, digital services without delivery, subscriptions to online services, etc.)  # noqa: E501

        :return: The ship_indicator of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501
        :rtype: str
        """
        return self._ship_indicator

    @ship_indicator.setter
    def ship_indicator(self, ship_indicator):
        """Sets the ship_indicator of this V1formPaymentMerchantDataMerchantRiskIndicator.

        Indicates the delivery method selected for the transaction. Businesses must select the delivery indicator code which more precisely describes the specific transaction of the payment user, not their general commercial activity. If one or more items are included in the sale, use the delivery Indicator code for physical goods, or if all products are digital, use the delivery Indicator code which describes the most expensive item. Accepted values: 01 = Delivery to the invoice address of the customer, 02 = Delivery to another verified address of the client, 03 = Delivery to an address other than that of the customer’s invoice address, 04 = Delivery to the store or collection at premises (the address of the store will be stored in the delivery address fields), 05 = Digital goods (includes online services, electronic gift cards and discount coupons), 06 = Tickets for events and trips, without delivery, 07 = Other (for example, games, digital services without delivery, subscriptions to online services, etc.)  # noqa: E501

        :param ship_indicator: The ship_indicator of this V1formPaymentMerchantDataMerchantRiskIndicator.  # noqa: E501
        :type: str
        """

        self._ship_indicator = ship_indicator

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
        if issubclass(V1formPaymentMerchantDataMerchantRiskIndicator, dict):
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
        if not isinstance(other, V1formPaymentMerchantDataMerchantRiskIndicator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
