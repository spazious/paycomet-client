# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from paycomet_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    IVR = "IVR"
    BALANCE = "balance"
    CARDS = "cards"
    DCC = "dcc"
    ERROR = "error"
    EXCHANGE = "exchange"
    FORM = "form"
    HEARTBEAT = "heartbeat"
    IP = "ip"
    LAUNCHPAD = "launchpad"
    MARKETPLACE = "marketplace"
    METHODS = "methods"
    MIRAKL = "mirakl"
    PAYMENTS = "payments"
    PREAUTHORIZATIONS = "preauthorizations"
    REFUND = "refund"
    SEPA = "sepa"
    SUSBCRIPTIONS = "susbcriptions"
    TOKEN = "token"
