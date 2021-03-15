# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from petstore_api.configuration import Configuration


class ArrayTest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'array_of_string': 'List[str]',
        'array_array_of_integer': 'List[List[int]]',
        'array_array_of_model': 'List[List[ReadOnlyFirst]]'
    }

    attribute_map = {
        'array_of_string': 'array_of_string',
        'array_array_of_integer': 'array_array_of_integer',
        'array_array_of_model': 'array_array_of_model'
    }

    def __init__(self, array_of_string=None, array_array_of_integer=None, array_array_of_model=None, local_vars_configuration=None):  # noqa: E501
        """ArrayTest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._array_of_string = None
        self._array_array_of_integer = None
        self._array_array_of_model = None
        self.discriminator = None

        if array_of_string is not None:
            self.array_of_string = array_of_string
        if array_array_of_integer is not None:
            self.array_array_of_integer = array_array_of_integer
        if array_array_of_model is not None:
            self.array_array_of_model = array_array_of_model

    @property
    def array_of_string(self):
        """Gets the array_of_string of this ArrayTest.  # noqa: E501


        :return: The array_of_string of this ArrayTest.  # noqa: E501
        :rtype: List[str]
        """
        return self._array_of_string

    @array_of_string.setter
    def array_of_string(self, array_of_string):
        """Sets the array_of_string of this ArrayTest.


        :param array_of_string: The array_of_string of this ArrayTest.  # noqa: E501
        :type array_of_string: List[str]
        """

        self._array_of_string = array_of_string

    @property
    def array_array_of_integer(self):
        """Gets the array_array_of_integer of this ArrayTest.  # noqa: E501


        :return: The array_array_of_integer of this ArrayTest.  # noqa: E501
        :rtype: List[List[int]]
        """
        return self._array_array_of_integer

    @array_array_of_integer.setter
    def array_array_of_integer(self, array_array_of_integer):
        """Sets the array_array_of_integer of this ArrayTest.


        :param array_array_of_integer: The array_array_of_integer of this ArrayTest.  # noqa: E501
        :type array_array_of_integer: List[List[int]]
        """

        self._array_array_of_integer = array_array_of_integer

    @property
    def array_array_of_model(self):
        """Gets the array_array_of_model of this ArrayTest.  # noqa: E501


        :return: The array_array_of_model of this ArrayTest.  # noqa: E501
        :rtype: List[List[ReadOnlyFirst]]
        """
        return self._array_array_of_model

    @array_array_of_model.setter
    def array_array_of_model(self, array_array_of_model):
        """Sets the array_array_of_model of this ArrayTest.


        :param array_array_of_model: The array_array_of_model of this ArrayTest.  # noqa: E501
        :type array_array_of_model: List[List[ReadOnlyFirst]]
        """

        self._array_array_of_model = array_array_of_model

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ArrayTest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArrayTest):
            return True

        return self.to_dict() != other.to_dict()
