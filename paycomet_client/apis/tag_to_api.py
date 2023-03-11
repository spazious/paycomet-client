import typing_extensions

from paycomet_client.apis.tags import TagValues
from paycomet_client.apis.tags.ivr_api import IVRApi
from paycomet_client.apis.tags.balance_api import BalanceApi
from paycomet_client.apis.tags.cards_api import CardsApi
from paycomet_client.apis.tags.dcc_api import DccApi
from paycomet_client.apis.tags.error_api import ErrorApi
from paycomet_client.apis.tags.exchange_api import ExchangeApi
from paycomet_client.apis.tags.form_api import FormApi
from paycomet_client.apis.tags.heartbeat_api import HeartbeatApi
from paycomet_client.apis.tags.ip_api import IpApi
from paycomet_client.apis.tags.launchpad_api import LaunchpadApi
from paycomet_client.apis.tags.marketplace_api import MarketplaceApi
from paycomet_client.apis.tags.methods_api import MethodsApi
from paycomet_client.apis.tags.mirakl_api import MiraklApi
from paycomet_client.apis.tags.payments_api import PaymentsApi
from paycomet_client.apis.tags.preauthorizations_api import PreauthorizationsApi
from paycomet_client.apis.tags.refund_api import RefundApi
from paycomet_client.apis.tags.sepa_api import SepaApi
from paycomet_client.apis.tags.susbcriptions_api import SusbcriptionsApi
from paycomet_client.apis.tags.token_api import TokenApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.IVR: IVRApi,
        TagValues.BALANCE: BalanceApi,
        TagValues.CARDS: CardsApi,
        TagValues.DCC: DccApi,
        TagValues.ERROR: ErrorApi,
        TagValues.EXCHANGE: ExchangeApi,
        TagValues.FORM: FormApi,
        TagValues.HEARTBEAT: HeartbeatApi,
        TagValues.IP: IpApi,
        TagValues.LAUNCHPAD: LaunchpadApi,
        TagValues.MARKETPLACE: MarketplaceApi,
        TagValues.METHODS: MethodsApi,
        TagValues.MIRAKL: MiraklApi,
        TagValues.PAYMENTS: PaymentsApi,
        TagValues.PREAUTHORIZATIONS: PreauthorizationsApi,
        TagValues.REFUND: RefundApi,
        TagValues.SEPA: SepaApi,
        TagValues.SUSBCRIPTIONS: SusbcriptionsApi,
        TagValues.TOKEN: TokenApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.IVR: IVRApi,
        TagValues.BALANCE: BalanceApi,
        TagValues.CARDS: CardsApi,
        TagValues.DCC: DccApi,
        TagValues.ERROR: ErrorApi,
        TagValues.EXCHANGE: ExchangeApi,
        TagValues.FORM: FormApi,
        TagValues.HEARTBEAT: HeartbeatApi,
        TagValues.IP: IpApi,
        TagValues.LAUNCHPAD: LaunchpadApi,
        TagValues.MARKETPLACE: MarketplaceApi,
        TagValues.METHODS: MethodsApi,
        TagValues.MIRAKL: MiraklApi,
        TagValues.PAYMENTS: PaymentsApi,
        TagValues.PREAUTHORIZATIONS: PreauthorizationsApi,
        TagValues.REFUND: RefundApi,
        TagValues.SEPA: SepaApi,
        TagValues.SUSBCRIPTIONS: SusbcriptionsApi,
        TagValues.TOKEN: TokenApi,
    }
)
