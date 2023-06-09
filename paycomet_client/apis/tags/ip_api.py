# coding: utf-8

"""
    PAYCOMET REST API

    PAYCOMET API REST for customers.  # noqa: E501

    The version of the OpenAPI document: 2.78.0
    Contact: tecnico@paycomet.com
    Generated by: https://openapi-generator.tech
"""

from paycomet_client.paths.v1_ip.post import GetCountrybyIp
from paycomet_client.paths.v1_ip_remote.post import GetRemoteAddress


class IpApi(
    GetCountrybyIp,
    GetRemoteAddress,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
