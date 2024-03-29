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

class InlineResponse20032Operations(object):
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
        'operation_result': 'str',
        'operation_error_code': 'int',
        'operation_order': 'str'
    }

    attribute_map = {
        'operation_result': 'operationResult',
        'operation_error_code': 'operationErrorCode',
        'operation_order': 'operationOrder'
    }

    def __init__(self, operation_result=None, operation_error_code=None, operation_order=None):  # noqa: E501
        """InlineResponse20032Operations - a model defined in Swagger"""  # noqa: E501
        self._operation_result = None
        self._operation_error_code = None
        self._operation_order = None
        self.discriminator = None
        if operation_result is not None:
            self.operation_result = operation_result
        if operation_error_code is not None:
            self.operation_error_code = operation_error_code
        if operation_order is not None:
            self.operation_order = operation_order

    @property
    def operation_result(self):
        """Gets the operation_result of this InlineResponse20032Operations.  # noqa: E501

        Operation result OK/KO  # noqa: E501

        :return: The operation_result of this InlineResponse20032Operations.  # noqa: E501
        :rtype: str
        """
        return self._operation_result

    @operation_result.setter
    def operation_result(self, operation_result):
        """Sets the operation_result of this InlineResponse20032Operations.

        Operation result OK/KO  # noqa: E501

        :param operation_result: The operation_result of this InlineResponse20032Operations.  # noqa: E501
        :type: str
        """

        self._operation_result = operation_result

    @property
    def operation_error_code(self):
        """Gets the operation_error_code of this InlineResponse20032Operations.  # noqa: E501

        Error code given by PAYCOMET for that operation  # noqa: E501

        :return: The operation_error_code of this InlineResponse20032Operations.  # noqa: E501
        :rtype: int
        """
        return self._operation_error_code

    @operation_error_code.setter
    def operation_error_code(self, operation_error_code):
        """Sets the operation_error_code of this InlineResponse20032Operations.

        Error code given by PAYCOMET for that operation  # noqa: E501

        :param operation_error_code: The operation_error_code of this InlineResponse20032Operations.  # noqa: E501
        :type: int
        """

        self._operation_error_code = operation_error_code

    @property
    def operation_order(self):
        """Gets the operation_order of this InlineResponse20032Operations.  # noqa: E501

        Order reference  # noqa: E501

        :return: The operation_order of this InlineResponse20032Operations.  # noqa: E501
        :rtype: str
        """
        return self._operation_order

    @operation_order.setter
    def operation_order(self, operation_order):
        """Sets the operation_order of this InlineResponse20032Operations.

        Order reference  # noqa: E501

        :param operation_order: The operation_order of this InlineResponse20032Operations.  # noqa: E501
        :type: str
        """

        self._operation_order = operation_order

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
        if issubclass(InlineResponse20032Operations, dict):
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
        if not isinstance(other, InlineResponse20032Operations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
