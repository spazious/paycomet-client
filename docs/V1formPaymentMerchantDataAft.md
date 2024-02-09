# V1formPaymentMerchantDataAft

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Receiver name | [optional] 
**last_name** | **str** | Receiver lastname | [optional] 
**country** | **str** | Receiver country (ISO 6133 Alpha-3) | [optional] 
**address** | **str** | Address line of receiver. Format (^[a-zA-Z0-9\\s]{1,35}$) | [optional] 
**city** | **str** | City of the receiver. Format (^[a-zA-Z0-9\\s]{1,25}$) | [optional] 
**account_number** | **str** | Receiver account number. Format (^[a-zA-Z0-9]{34}$) | [optional] 
**account_number_type** | **int** | 00 (Other) | 01 (Card) | 02 (Account) | 03 (Cash) | 05 - Phone Number | 06 - Bank account number (BAN) + Bank Identification Сode (BIC) | 07 - Wallet ID  | 08 - | [optional] 
**utr** | **str** | Should be formatted as 0000000 + Year (n-1) last digit of current year + Julian date (n-3) day of the year  + hour (n-6) hhmmss + sequence number (n-2) from 00 to 99. | [optional] 
**bai** | **str** | Business Application Identifier. AA|BI | [optional] 
**sender_name** | **str** | The name of the sender | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

