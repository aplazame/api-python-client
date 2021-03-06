# coding: utf-8

"""
    Onfido API

    The Onfido API is used to submit check requests.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ReportTypeGroupsList(object):
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
        'report_type_groups': 'list[ReportTypeGroup]'
    }

    attribute_map = {
        'report_type_groups': 'report_type_groups'
    }

    def __init__(self, report_type_groups=None):  # noqa: E501
        """ReportTypeGroupsList - a model defined in OpenAPI"""  # noqa: E501

        self._report_type_groups = None
        self.discriminator = None

        if report_type_groups is not None:
            self.report_type_groups = report_type_groups

    @property
    def report_type_groups(self):
        """Gets the report_type_groups of this ReportTypeGroupsList.  # noqa: E501


        :return: The report_type_groups of this ReportTypeGroupsList.  # noqa: E501
        :rtype: list[ReportTypeGroup]
        """
        return self._report_type_groups

    @report_type_groups.setter
    def report_type_groups(self, report_type_groups):
        """Sets the report_type_groups of this ReportTypeGroupsList.


        :param report_type_groups: The report_type_groups of this ReportTypeGroupsList.  # noqa: E501
        :type: list[ReportTypeGroup]
        """

        self._report_type_groups = report_type_groups

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReportTypeGroupsList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
