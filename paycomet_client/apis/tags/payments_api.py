# coding: utf-8

"""
    PAYCOMET REST API

    PAYCOMET API REST for customers.  # noqa: E501

    The version of the OpenAPI document: 2.78.0
    Contact: tecnico@paycomet.com
    Generated by: https://openapi-generator.tech
"""

from paycomet_client.paths.v1_payments.post import ExecutePurchase
from paycomet_client.paths.v1_payments_rtoken.post import ExecutePurchaseRtoken
from paycomet_client.paths.v1_payments_order_info.post import OperationInfo
from paycomet_client.paths.v1_payments_search.post import OperationSearch


class PaymentsApi(
    ExecutePurchase,
    ExecutePurchaseRtoken,
    OperationInfo,
    OperationSearch,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
