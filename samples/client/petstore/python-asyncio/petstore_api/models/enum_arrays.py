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


class EnumArrays(object):
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
        'just_symbol': 'str',
        'array_enum': 'List[str]'
    }

    attribute_map = {
        'just_symbol': 'just_symbol',
        'array_enum': 'array_enum'
    }

    def __init__(self, just_symbol=None, array_enum=None, local_vars_configuration=None):  # noqa: E501
        """EnumArrays - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._just_symbol = None
        self._array_enum = None
        self.discriminator = None

        if just_symbol is not None:
            self.just_symbol = just_symbol
        if array_enum is not None:
            self.array_enum = array_enum

    @property
    def just_symbol(self):
        """Gets the just_symbol of this EnumArrays.  # noqa: E501


        :return: The just_symbol of this EnumArrays.  # noqa: E501
        :rtype: str
        """
        return self._just_symbol

    @just_symbol.setter
    def just_symbol(self, just_symbol):
        """Sets the just_symbol of this EnumArrays.


        :param just_symbol: The just_symbol of this EnumArrays.  # noqa: E501
        :type just_symbol: str
        """
        allowed_values = [">=", "$"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and just_symbol not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `just_symbol` ({0}), must be one of {1}"  # noqa: E501
                .format(just_symbol, allowed_values)
            )

        self._just_symbol = just_symbol

    @property
    def array_enum(self):
        """Gets the array_enum of this EnumArrays.  # noqa: E501


        :return: The array_enum of this EnumArrays.  # noqa: E501
        :rtype: List[str]
        """
        return self._array_enum

    @array_enum.setter
    def array_enum(self, array_enum):
        """Sets the array_enum of this EnumArrays.


        :param array_enum: The array_enum of this EnumArrays.  # noqa: E501
        :type array_enum: List[str]
        """
        allowed_values = ["fish", "crab"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(array_enum).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `array_enum` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(array_enum) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._array_enum = array_enum

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
        if not isinstance(other, EnumArrays):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnumArrays):
            return True

        return self.to_dict() != other.to_dict()
