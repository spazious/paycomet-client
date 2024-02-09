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

class SepaOperationsBody(object):
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
        'operations': 'list[V1sepaoperationsOperations]'
    }

    attribute_map = {
        'terminal': 'terminal',
        'sepa_provider_id': 'sepaProviderId',
        'operations': 'operations'
    }

    def __init__(self, terminal=None, sepa_provider_id=None, operations=None):  # noqa: E501
        """SepaOperationsBody - a model defined in Swagger"""  # noqa: E501
        self._terminal = None
        self._sepa_provider_id = None
        self._operations = None
        self.discriminator = None
        self.terminal = terminal
        self.sepa_provider_id = sepa_provider_id
        self.operations = operations

    @property
    def terminal(self):
        """Gets the terminal of this SepaOperationsBody.  # noqa: E501

        Product or terminal Id.  # noqa: E501

        :return: The terminal of this SepaOperationsBody.  # noqa: E501
        :rtype: int
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this SepaOperationsBody.

        Product or terminal Id.  # noqa: E501

        :param terminal: The terminal of this SepaOperationsBody.  # noqa: E501
        :type: int
        """
        if terminal is None:
            raise ValueError("Invalid value for `terminal`, must not be `None`")  # noqa: E501

        self._terminal = terminal

    @property
    def sepa_provider_id(self):
        """Gets the sepa_provider_id of this SepaOperationsBody.  # noqa: E501

        Unique identifier assigned by PAYCOMET for the supplier sending SEPA operations. Available on the client control panel.  # noqa: E501

        :return: The sepa_provider_id of this SepaOperationsBody.  # noqa: E501
        :rtype: int
        """
        return self._sepa_provider_id

    @sepa_provider_id.setter
    def sepa_provider_id(self, sepa_provider_id):
        """Sets the sepa_provider_id of this SepaOperationsBody.

        Unique identifier assigned by PAYCOMET for the supplier sending SEPA operations. Available on the client control panel.  # noqa: E501

        :param sepa_provider_id: The sepa_provider_id of this SepaOperationsBody.  # noqa: E501
        :type: int
        """
        if sepa_provider_id is None:
            raise ValueError("Invalid value for `sepa_provider_id`, must not be `None`")  # noqa: E501

        self._sepa_provider_id = sepa_provider_id

    @property
    def operations(self):
        """Gets the operations of this SepaOperationsBody.  # noqa: E501


        :return: The operations of this SepaOperationsBody.  # noqa: E501
        :rtype: list[V1sepaoperationsOperations]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this SepaOperationsBody.


        :param operations: The operations of this SepaOperationsBody.  # noqa: E501
        :type: list[V1sepaoperationsOperations]
        """
        if operations is None:
            raise ValueError("Invalid value for `operations`, must not be `None`")  # noqa: E501

        self._operations = operations

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
        if issubclass(SepaOperationsBody, dict):
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
        if not isinstance(other, SepaOperationsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
