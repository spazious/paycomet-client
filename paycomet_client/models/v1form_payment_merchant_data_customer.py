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

class V1formPaymentMerchantDataCustomer(object):
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
        'id': 'str',
        'name': 'str',
        'surname': 'str',
        'email': 'str',
        'home_phone': 'V1formPaymentMerchantDataCustomerHomePhone',
        'mobile_phone': 'V1formPaymentMerchantDataCustomerMobilePhone',
        'work_phone': 'V1formPaymentMerchantDataCustomerWorkPhone',
        'first_buy': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'surname': 'surname',
        'email': 'email',
        'home_phone': 'homePhone',
        'mobile_phone': 'mobilePhone',
        'work_phone': 'workPhone',
        'first_buy': 'firstBuy'
    }

    def __init__(self, id=None, name=None, surname=None, email=None, home_phone=None, mobile_phone=None, work_phone=None, first_buy=None):  # noqa: E501
        """V1formPaymentMerchantDataCustomer - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._surname = None
        self._email = None
        self._home_phone = None
        self._mobile_phone = None
        self._work_phone = None
        self._first_buy = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if surname is not None:
            self.surname = surname
        if email is not None:
            self.email = email
        if home_phone is not None:
            self.home_phone = home_phone
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone
        if work_phone is not None:
            self.work_phone = work_phone
        if first_buy is not None:
            self.first_buy = first_buy

    @property
    def id(self):
        """Gets the id of this V1formPaymentMerchantDataCustomer.  # noqa: E501

        Store customer identifier  # noqa: E501

        :return: The id of this V1formPaymentMerchantDataCustomer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1formPaymentMerchantDataCustomer.

        Store customer identifier  # noqa: E501

        :param id: The id of this V1formPaymentMerchantDataCustomer.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this V1formPaymentMerchantDataCustomer.  # noqa: E501

        Name of customer  # noqa: E501

        :return: The name of this V1formPaymentMerchantDataCustomer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1formPaymentMerchantDataCustomer.

        Name of customer  # noqa: E501

        :param name: The name of this V1formPaymentMerchantDataCustomer.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def surname(self):
        """Gets the surname of this V1formPaymentMerchantDataCustomer.  # noqa: E501

        Surname of customer  # noqa: E501

        :return: The surname of this V1formPaymentMerchantDataCustomer.  # noqa: E501
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this V1formPaymentMerchantDataCustomer.

        Surname of customer  # noqa: E501

        :param surname: The surname of this V1formPaymentMerchantDataCustomer.  # noqa: E501
        :type: str
        """

        self._surname = surname

    @property
    def email(self):
        """Gets the email of this V1formPaymentMerchantDataCustomer.  # noqa: E501

        Email of customer  # noqa: E501

        :return: The email of this V1formPaymentMerchantDataCustomer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this V1formPaymentMerchantDataCustomer.

        Email of customer  # noqa: E501

        :param email: The email of this V1formPaymentMerchantDataCustomer.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def home_phone(self):
        """Gets the home_phone of this V1formPaymentMerchantDataCustomer.  # noqa: E501


        :return: The home_phone of this V1formPaymentMerchantDataCustomer.  # noqa: E501
        :rtype: V1formPaymentMerchantDataCustomerHomePhone
        """
        return self._home_phone

    @home_phone.setter
    def home_phone(self, home_phone):
        """Sets the home_phone of this V1formPaymentMerchantDataCustomer.


        :param home_phone: The home_phone of this V1formPaymentMerchantDataCustomer.  # noqa: E501
        :type: V1formPaymentMerchantDataCustomerHomePhone
        """

        self._home_phone = home_phone

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this V1formPaymentMerchantDataCustomer.  # noqa: E501


        :return: The mobile_phone of this V1formPaymentMerchantDataCustomer.  # noqa: E501
        :rtype: V1formPaymentMerchantDataCustomerMobilePhone
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this V1formPaymentMerchantDataCustomer.


        :param mobile_phone: The mobile_phone of this V1formPaymentMerchantDataCustomer.  # noqa: E501
        :type: V1formPaymentMerchantDataCustomerMobilePhone
        """

        self._mobile_phone = mobile_phone

    @property
    def work_phone(self):
        """Gets the work_phone of this V1formPaymentMerchantDataCustomer.  # noqa: E501


        :return: The work_phone of this V1formPaymentMerchantDataCustomer.  # noqa: E501
        :rtype: V1formPaymentMerchantDataCustomerWorkPhone
        """
        return self._work_phone

    @work_phone.setter
    def work_phone(self, work_phone):
        """Sets the work_phone of this V1formPaymentMerchantDataCustomer.


        :param work_phone: The work_phone of this V1formPaymentMerchantDataCustomer.  # noqa: E501
        :type: V1formPaymentMerchantDataCustomerWorkPhone
        """

        self._work_phone = work_phone

    @property
    def first_buy(self):
        """Gets the first_buy of this V1formPaymentMerchantDataCustomer.  # noqa: E501

        Indicates whether the user has already bought in this business ('si' if has made a operation, 'no' in opposite scenario)  # noqa: E501

        :return: The first_buy of this V1formPaymentMerchantDataCustomer.  # noqa: E501
        :rtype: str
        """
        return self._first_buy

    @first_buy.setter
    def first_buy(self, first_buy):
        """Sets the first_buy of this V1formPaymentMerchantDataCustomer.

        Indicates whether the user has already bought in this business ('si' if has made a operation, 'no' in opposite scenario)  # noqa: E501

        :param first_buy: The first_buy of this V1formPaymentMerchantDataCustomer.  # noqa: E501
        :type: str
        """

        self._first_buy = first_buy

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
        if issubclass(V1formPaymentMerchantDataCustomer, dict):
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
        if not isinstance(other, V1formPaymentMerchantDataCustomer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
