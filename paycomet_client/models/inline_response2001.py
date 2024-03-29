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

class InlineResponse2001(object):
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
        'id_user': 'int',
        'token_user': 'str',
        'error_code': 'int'
    }

    attribute_map = {
        'id_user': 'idUser',
        'token_user': 'tokenUser',
        'error_code': 'errorCode'
    }

    def __init__(self, id_user=None, token_user=None, error_code=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger"""  # noqa: E501
        self._id_user = None
        self._token_user = None
        self._error_code = None
        self.discriminator = None
        if id_user is not None:
            self.id_user = id_user
        if token_user is not None:
            self.token_user = token_user
        if error_code is not None:
            self.error_code = error_code

    @property
    def id_user(self):
        """Gets the id_user of this InlineResponse2001.  # noqa: E501


        :return: The id_user of this InlineResponse2001.  # noqa: E501
        :rtype: int
        """
        return self._id_user

    @id_user.setter
    def id_user(self, id_user):
        """Sets the id_user of this InlineResponse2001.


        :param id_user: The id_user of this InlineResponse2001.  # noqa: E501
        :type: int
        """

        self._id_user = id_user

    @property
    def token_user(self):
        """Gets the token_user of this InlineResponse2001.  # noqa: E501


        :return: The token_user of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._token_user

    @token_user.setter
    def token_user(self, token_user):
        """Sets the token_user of this InlineResponse2001.


        :param token_user: The token_user of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._token_user = token_user

    @property
    def error_code(self):
        """Gets the error_code of this InlineResponse2001.  # noqa: E501


        :return: The error_code of this InlineResponse2001.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this InlineResponse2001.


        :param error_code: The error_code of this InlineResponse2001.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

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
        if issubclass(InlineResponse2001, dict):
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
        if not isinstance(other, InlineResponse2001):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
