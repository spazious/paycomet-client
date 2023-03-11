# coding: utf-8

"""
    PAYCOMET REST API

    PAYCOMET API REST for customers.  # noqa: E501

    The version of the OpenAPI document: 2.78.0
    Contact: tecnico@paycomet.com
    Generated by: https://openapi-generator.tech
"""

from paycomet_client.paths.v1_cards.post import AddUser
from paycomet_client.paths.v1_cards_edit.post import EditUser
from paycomet_client.paths.v1_cards_info.post import InfoUser
from paycomet_client.paths.v1_cards_physical.post import PhysicalAddCard
from paycomet_client.paths.v1_cards_physical_edit.post import PhysicalEditCard
from paycomet_client.paths.v1_cards_delete.post import RemoveUser


class CardsApi(
    AddUser,
    EditUser,
    InfoUser,
    PhysicalAddCard,
    PhysicalEditCard,
    RemoveUser,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass