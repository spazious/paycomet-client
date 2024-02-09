# LaunchpadSubscriptionBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal** | **int** | Product or terminal Id. | 
**order** | **str** | Unique reference for merchant&#x27;s purchase | 
**amount** | **str** | Amount of the operation in number format. 1.00 EURO &#x3D; 100, 4.50 EUROS &#x3D; 450... | 
**currency** | **str** | Currency of the transaction.  | 
**method_id** | **str** | PAYCOMET payment method ID. 1 is for card. | 
**original_ip** | **str** | IP Address of the customer that initiated the payment transaction | 
**secure** | **int** | 0 or 1. Indicates if the transaction is secure. | 
**language** | **str** | ISO2 code of language. | [default to 'es']
**sms_email** | **str** | Sending channel of the payment url. Should be \&quot;sms\&quot; or \&quot;email\&quot;. | 
**template_id** | **int** | Email or SMS template id to be sent. You can get it in the Control panel. | 
**email_address** | **str** | Conditional. Mandatory in sending method is EMAIL. Email address where link must be sent | [optional] 
**email_name** | **str** | Conditional. Mandatory in sending method is EMAIL. Email recipient of the email address where link must be sent | [optional] 
**sms_prefix** | **str** | Conditional. Mandatory in sending method is SMS. International mobile prefix where link must be sent | [optional] 
**sms_number** | **str** | Conditional. Mandatory in sending method is SMS. Mobile number where link must be sent | [optional] 
**expiry_date** | **str** | Optional. Link expiration date. Format YYYYMMDD | [optional] 
**expiry_hour** | **str** | Optional. Link expiration hour. Format HH | [optional] 
**expiry_minute** | **str** | Optional. Link expiration minute. Format MM | [optional] 
**scoring** | **str** | Risk scoring value from 0 to 100. | [optional] 
**start_date** | **str** | Subscription start date yyyymmdd. IMPORTANT Subscriptions are charged on the first run if this field has value it will be taken into account for future charges. | [optional] 
**end_date** | **str** | Subscription end date yyyymmdd | [optional] 
**periodicity** | **str** | Subscription periodicity in days. Maximum 365. | [optional] 
**merchant_data** | [**V1launchpadsubscriptionMerchantData**](V1launchpadsubscriptionMerchantData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

