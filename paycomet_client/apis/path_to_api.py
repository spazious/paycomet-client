import typing_extensions

from paycomet_client.paths import PathValues
from paycomet_client.apis.paths.v1_errors import V1Errors
from paycomet_client.apis.paths.v1_cards import V1Cards
from paycomet_client.apis.paths.v1_cards_info import V1CardsInfo
from paycomet_client.apis.paths.v1_cards_delete import V1CardsDelete
from paycomet_client.apis.paths.v1_cards_edit import V1CardsEdit
from paycomet_client.apis.paths.v1_cards_physical import V1CardsPhysical
from paycomet_client.apis.paths.v1_cards_physical_edit import V1CardsPhysicalEdit
from paycomet_client.apis.paths.v1_balance import V1Balance
from paycomet_client.apis.paths.v1_exchange import V1Exchange
from paycomet_client.apis.paths.v1_heartbeat import V1Heartbeat
from paycomet_client.apis.paths.v1_invoices import V1Invoices
from paycomet_client.apis.paths.v1_ip import V1Ip
from paycomet_client.apis.paths.v1_ip_remote import V1IpRemote
from paycomet_client.apis.paths.v1_methods import V1Methods
from paycomet_client.apis.paths.v1_form import V1Form
from paycomet_client.apis.paths.v1_payments import V1Payments
from paycomet_client.apis.paths.v1_payments_order_refund import V1PaymentsOrderRefund
from paycomet_client.apis.paths.v1_payments_order_info import V1PaymentsOrderInfo
from paycomet_client.apis.paths.v1_payments_search import V1PaymentsSearch
from paycomet_client.apis.paths.v1_payments_preauth import V1PaymentsPreauth
from paycomet_client.apis.paths.v1_payments_order_preauth_cancel import V1PaymentsOrderPreauthCancel
from paycomet_client.apis.paths.v1_payments_order_preauth_confirm import V1PaymentsOrderPreauthConfirm
from paycomet_client.apis.paths.v1_payments_rtoken import V1PaymentsRtoken
from paycomet_client.apis.paths.v1_payments_preauthrtoken import V1PaymentsPreauthrtoken
from paycomet_client.apis.paths.v1_subscription import V1Subscription
from paycomet_client.apis.paths.v1_subscription_order_edit import V1SubscriptionOrderEdit
from paycomet_client.apis.paths.v1_subscription_order_remove import V1SubscriptionOrderRemove
from paycomet_client.apis.paths.v1_subscription_order_info import V1SubscriptionOrderInfo
from paycomet_client.apis.paths.v1_payments_dcc import V1PaymentsDcc
from paycomet_client.apis.paths.v1_payments_order_dcc_confirm import V1PaymentsOrderDccConfirm
from paycomet_client.apis.paths.v1_marketplace_split_transfer import V1MarketplaceSplitTransfer
from paycomet_client.apis.paths.v1_marketplace_split_transfer_reversal import V1MarketplaceSplitTransferReversal
from paycomet_client.apis.paths.v1_marketplace_transfer import V1MarketplaceTransfer
from paycomet_client.apis.paths.v1_marketplace_transfer_reversal import V1MarketplaceTransferReversal
from paycomet_client.apis.paths.v1_sepa_add_document import V1SepaAddDocument
from paycomet_client.apis.paths.v1_sepa_enrole_customer import V1SepaEnroleCustomer
from paycomet_client.apis.paths.v1_sepa_check_document import V1SepaCheckDocument
from paycomet_client.apis.paths.v1_sepa_check_customer import V1SepaCheckCustomer
from paycomet_client.apis.paths.v1_sepa_operations import V1SepaOperations
from paycomet_client.apis.paths.v1_sepa_cancel import V1SepaCancel
from paycomet_client.apis.paths.v1_ivr_get_session import V1IvrGetSession
from paycomet_client.apis.paths.v1_ivr_session_state import V1IvrSessionState
from paycomet_client.apis.paths.v1_ivr_session_cancel import V1IvrSessionCancel
from paycomet_client.apis.paths.v1_launchpad_authorization import V1LaunchpadAuthorization
from paycomet_client.apis.paths.v1_launchpad_preauthorization import V1LaunchpadPreauthorization
from paycomet_client.apis.paths.v1_launchpad_subscription import V1LaunchpadSubscription
from paycomet_client.apis.paths.v1_token import V1Token

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_ERRORS: V1Errors,
        PathValues.V1_CARDS: V1Cards,
        PathValues.V1_CARDS_INFO: V1CardsInfo,
        PathValues.V1_CARDS_DELETE: V1CardsDelete,
        PathValues.V1_CARDS_EDIT: V1CardsEdit,
        PathValues.V1_CARDS_PHYSICAL: V1CardsPhysical,
        PathValues.V1_CARDS_PHYSICAL_EDIT: V1CardsPhysicalEdit,
        PathValues.V1_BALANCE: V1Balance,
        PathValues.V1_EXCHANGE: V1Exchange,
        PathValues.V1_HEARTBEAT: V1Heartbeat,
        PathValues.V1_INVOICES: V1Invoices,
        PathValues.V1_IP: V1Ip,
        PathValues.V1_IP_REMOTE: V1IpRemote,
        PathValues.V1_METHODS: V1Methods,
        PathValues.V1_FORM: V1Form,
        PathValues.V1_PAYMENTS: V1Payments,
        PathValues.V1_PAYMENTS_ORDER_REFUND: V1PaymentsOrderRefund,
        PathValues.V1_PAYMENTS_ORDER_INFO: V1PaymentsOrderInfo,
        PathValues.V1_PAYMENTS_SEARCH: V1PaymentsSearch,
        PathValues.V1_PAYMENTS_PREAUTH: V1PaymentsPreauth,
        PathValues.V1_PAYMENTS_ORDER_PREAUTH_CANCEL: V1PaymentsOrderPreauthCancel,
        PathValues.V1_PAYMENTS_ORDER_PREAUTH_CONFIRM: V1PaymentsOrderPreauthConfirm,
        PathValues.V1_PAYMENTS_RTOKEN: V1PaymentsRtoken,
        PathValues.V1_PAYMENTS_PREAUTHRTOKEN: V1PaymentsPreauthrtoken,
        PathValues.V1_SUBSCRIPTION: V1Subscription,
        PathValues.V1_SUBSCRIPTION_ORDER_EDIT: V1SubscriptionOrderEdit,
        PathValues.V1_SUBSCRIPTION_ORDER_REMOVE: V1SubscriptionOrderRemove,
        PathValues.V1_SUBSCRIPTION_ORDER_INFO: V1SubscriptionOrderInfo,
        PathValues.V1_PAYMENTS_DCC: V1PaymentsDcc,
        PathValues.V1_PAYMENTS_ORDER_DCC_CONFIRM: V1PaymentsOrderDccConfirm,
        PathValues.V1_MARKETPLACE_SPLITTRANSFER: V1MarketplaceSplitTransfer,
        PathValues.V1_MARKETPLACE_SPLITTRANSFERREVERSAL: V1MarketplaceSplitTransferReversal,
        PathValues.V1_MARKETPLACE_TRANSFER: V1MarketplaceTransfer,
        PathValues.V1_MARKETPLACE_TRANSFERREVERSAL: V1MarketplaceTransferReversal,
        PathValues.V1_SEPA_ADDDOCUMENT: V1SepaAddDocument,
        PathValues.V1_SEPA_ENROLECUSTOMER: V1SepaEnroleCustomer,
        PathValues.V1_SEPA_CHECKDOCUMENT: V1SepaCheckDocument,
        PathValues.V1_SEPA_CHECKCUSTOMER: V1SepaCheckCustomer,
        PathValues.V1_SEPA_OPERATIONS: V1SepaOperations,
        PathValues.V1_SEPA_CANCEL: V1SepaCancel,
        PathValues.V1_IVR_GETSESSION: V1IvrGetSession,
        PathValues.V1_IVR_SESSIONSTATE: V1IvrSessionState,
        PathValues.V1_IVR_SESSIONCANCEL: V1IvrSessionCancel,
        PathValues.V1_LAUNCHPAD_AUTHORIZATION: V1LaunchpadAuthorization,
        PathValues.V1_LAUNCHPAD_PREAUTHORIZATION: V1LaunchpadPreauthorization,
        PathValues.V1_LAUNCHPAD_SUBSCRIPTION: V1LaunchpadSubscription,
        PathValues.V1_TOKEN: V1Token,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_ERRORS: V1Errors,
        PathValues.V1_CARDS: V1Cards,
        PathValues.V1_CARDS_INFO: V1CardsInfo,
        PathValues.V1_CARDS_DELETE: V1CardsDelete,
        PathValues.V1_CARDS_EDIT: V1CardsEdit,
        PathValues.V1_CARDS_PHYSICAL: V1CardsPhysical,
        PathValues.V1_CARDS_PHYSICAL_EDIT: V1CardsPhysicalEdit,
        PathValues.V1_BALANCE: V1Balance,
        PathValues.V1_EXCHANGE: V1Exchange,
        PathValues.V1_HEARTBEAT: V1Heartbeat,
        PathValues.V1_INVOICES: V1Invoices,
        PathValues.V1_IP: V1Ip,
        PathValues.V1_IP_REMOTE: V1IpRemote,
        PathValues.V1_METHODS: V1Methods,
        PathValues.V1_FORM: V1Form,
        PathValues.V1_PAYMENTS: V1Payments,
        PathValues.V1_PAYMENTS_ORDER_REFUND: V1PaymentsOrderRefund,
        PathValues.V1_PAYMENTS_ORDER_INFO: V1PaymentsOrderInfo,
        PathValues.V1_PAYMENTS_SEARCH: V1PaymentsSearch,
        PathValues.V1_PAYMENTS_PREAUTH: V1PaymentsPreauth,
        PathValues.V1_PAYMENTS_ORDER_PREAUTH_CANCEL: V1PaymentsOrderPreauthCancel,
        PathValues.V1_PAYMENTS_ORDER_PREAUTH_CONFIRM: V1PaymentsOrderPreauthConfirm,
        PathValues.V1_PAYMENTS_RTOKEN: V1PaymentsRtoken,
        PathValues.V1_PAYMENTS_PREAUTHRTOKEN: V1PaymentsPreauthrtoken,
        PathValues.V1_SUBSCRIPTION: V1Subscription,
        PathValues.V1_SUBSCRIPTION_ORDER_EDIT: V1SubscriptionOrderEdit,
        PathValues.V1_SUBSCRIPTION_ORDER_REMOVE: V1SubscriptionOrderRemove,
        PathValues.V1_SUBSCRIPTION_ORDER_INFO: V1SubscriptionOrderInfo,
        PathValues.V1_PAYMENTS_DCC: V1PaymentsDcc,
        PathValues.V1_PAYMENTS_ORDER_DCC_CONFIRM: V1PaymentsOrderDccConfirm,
        PathValues.V1_MARKETPLACE_SPLITTRANSFER: V1MarketplaceSplitTransfer,
        PathValues.V1_MARKETPLACE_SPLITTRANSFERREVERSAL: V1MarketplaceSplitTransferReversal,
        PathValues.V1_MARKETPLACE_TRANSFER: V1MarketplaceTransfer,
        PathValues.V1_MARKETPLACE_TRANSFERREVERSAL: V1MarketplaceTransferReversal,
        PathValues.V1_SEPA_ADDDOCUMENT: V1SepaAddDocument,
        PathValues.V1_SEPA_ENROLECUSTOMER: V1SepaEnroleCustomer,
        PathValues.V1_SEPA_CHECKDOCUMENT: V1SepaCheckDocument,
        PathValues.V1_SEPA_CHECKCUSTOMER: V1SepaCheckCustomer,
        PathValues.V1_SEPA_OPERATIONS: V1SepaOperations,
        PathValues.V1_SEPA_CANCEL: V1SepaCancel,
        PathValues.V1_IVR_GETSESSION: V1IvrGetSession,
        PathValues.V1_IVR_SESSIONSTATE: V1IvrSessionState,
        PathValues.V1_IVR_SESSIONCANCEL: V1IvrSessionCancel,
        PathValues.V1_LAUNCHPAD_AUTHORIZATION: V1LaunchpadAuthorization,
        PathValues.V1_LAUNCHPAD_PREAUTHORIZATION: V1LaunchpadPreauthorization,
        PathValues.V1_LAUNCHPAD_SUBSCRIPTION: V1LaunchpadSubscription,
        PathValues.V1_TOKEN: V1Token,
    }
)
