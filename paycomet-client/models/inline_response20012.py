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

class InlineResponse20012(object):
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
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'active': 'str',
        'allow_api_refunds': 'int',
        'logo_square': 'str',
        'logo_landscape': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'active': 'active',
        'allow_api_refunds': 'allowAPIRefunds',
        'logo_square': 'logo_square',
        'logo_landscape': 'logo_landscape'
    }

    def __init__(self, id=None, name=None, description=None, active=None, allow_api_refunds=None, logo_square=None, logo_landscape=None):  # noqa: E501
        """InlineResponse20012 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._active = None
        self._allow_api_refunds = None
        self._logo_square = None
        self._logo_landscape = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if active is not None:
            self.active = active
        if allow_api_refunds is not None:
            self.allow_api_refunds = allow_api_refunds
        if logo_square is not None:
            self.logo_square = logo_square
        if logo_landscape is not None:
            self.logo_landscape = logo_landscape

    @property
    def id(self):
        """Gets the id of this InlineResponse20012.  # noqa: E501


        :return: The id of this InlineResponse20012.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20012.


        :param id: The id of this InlineResponse20012.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20012.  # noqa: E501


        :return: The name of this InlineResponse20012.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20012.


        :param name: The name of this InlineResponse20012.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this InlineResponse20012.  # noqa: E501


        :return: The description of this InlineResponse20012.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponse20012.


        :param description: The description of this InlineResponse20012.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def active(self):
        """Gets the active of this InlineResponse20012.  # noqa: E501


        :return: The active of this InlineResponse20012.  # noqa: E501
        :rtype: str
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this InlineResponse20012.


        :param active: The active of this InlineResponse20012.  # noqa: E501
        :type: str
        """

        self._active = active

    @property
    def allow_api_refunds(self):
        """Gets the allow_api_refunds of this InlineResponse20012.  # noqa: E501


        :return: The allow_api_refunds of this InlineResponse20012.  # noqa: E501
        :rtype: int
        """
        return self._allow_api_refunds

    @allow_api_refunds.setter
    def allow_api_refunds(self, allow_api_refunds):
        """Sets the allow_api_refunds of this InlineResponse20012.


        :param allow_api_refunds: The allow_api_refunds of this InlineResponse20012.  # noqa: E501
        :type: int
        """

        self._allow_api_refunds = allow_api_refunds

    @property
    def logo_square(self):
        """Gets the logo_square of this InlineResponse20012.  # noqa: E501

        encoded image of squared logo in base64 format  # noqa: E501

        :return: The logo_square of this InlineResponse20012.  # noqa: E501
        :rtype: str
        """
        return self._logo_square

    @logo_square.setter
    def logo_square(self, logo_square):
        """Sets the logo_square of this InlineResponse20012.

        encoded image of squared logo in base64 format  # noqa: E501

        :param logo_square: The logo_square of this InlineResponse20012.  # noqa: E501
        :type: str
        """

        self._logo_square = logo_square

    @property
    def logo_landscape(self):
        """Gets the logo_landscape of this InlineResponse20012.  # noqa: E501

        encoded image of landscape logo in base64 format  # noqa: E501

        :return: The logo_landscape of this InlineResponse20012.  # noqa: E501
        :rtype: str
        """
        return self._logo_landscape

    @logo_landscape.setter
    def logo_landscape(self, logo_landscape):
        """Sets the logo_landscape of this InlineResponse20012.

        encoded image of landscape logo in base64 format  # noqa: E501

        :param logo_landscape: The logo_landscape of this InlineResponse20012.  # noqa: E501
        :type: str
        """

        self._logo_landscape = logo_landscape

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
        if issubclass(InlineResponse20012, dict):
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
        if not isinstance(other, InlineResponse20012):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other