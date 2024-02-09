# V1formPaymentMerchantData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | [**V1formPaymentMerchantDataCustomer**](V1formPaymentMerchantDataCustomer.md) |  | [optional] 
**shipping** | [**V1formPaymentMerchantDataShipping**](V1formPaymentMerchantDataShipping.md) |  | [optional] 
**billing** | [**V1formPaymentMerchantDataBilling**](V1formPaymentMerchantDataBilling.md) |  | [optional] 
**acct_id** | **str** | Additional information you want to send to identify the account | [optional] 
**acct_info** | [**V1formPaymentMerchantDataAcctInfo**](V1formPaymentMerchantDataAcctInfo.md) |  | [optional] 
**merchant_risk_indicator** | [**V1formPaymentMerchantDataMerchantRiskIndicator**](V1formPaymentMerchantDataMerchantRiskIndicator.md) |  | [optional] 
**three_ds_requestor_authentication_info** | [**V1formPaymentMerchantDataThreeDSRequestorAuthenticationInfo**](V1formPaymentMerchantDataThreeDSRequestorAuthenticationInfo.md) |  | [optional] 
**shopping_cart** | [**list[V1formPaymentMerchantDataShoppingCart]**](V1formPaymentMerchantDataShoppingCart.md) |  | [optional] 
**addr_match** | **str** | Indicates whether the delivery address is the same as the invoice address. Y &#x3D; The delivery address is the same as the invoicing address, N &#x3D; The delivery and invoice addresses are different | [optional] 
**purchase_instal_data** | **int** | Mandatory for Instalment operations (MERCHANT_TRX_TYPE &#x3D; I). Indicates the maximum number of deferred payment authorizations. Accepted values: The value must be greater than 1 | [optional] 
**recurring_expiry** | **str** | Mandatory for Recurring and Instalment operations (MERCHANT_TRX_TYPE &#x3D; I or R). The date from which there will be no more authorizations. Accepted format: YYYYMMDD | [optional] 
**recurring_frequency** | **str** | Mandatory for Recurring and Instalment operations (MERCHANT_TRX_TYPE &#x3D; I or R). Indicates the minimum number of days between authorizations | [optional] 
**aft** | [**V1formPaymentMerchantDataAft**](V1formPaymentMerchantDataAft.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

