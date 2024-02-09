# V1paymentsdccPayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal** | **int** | Product or terminal Id. | [optional] 
**order** | **str** | Reference of the operation. Must be unique on every valid transaction. | [optional] 
**token_user** | **str** | Token code associated with the IdUser. | [optional] 
**id_user** | **int** | Unique identifier of the user registered in the system. | [optional] 
**original_ip** | **str** | IP Address of the application of the business | [optional] 
**amount** | **str** | Amount of the operation in number format. 1.00 EURO &#x3D; 100, 4.50 EUROS &#x3D; 450... | [optional] 
**scoring** | **str** | Risk scoring value from 0 to 100. | [optional] 
**product_description** | **str** | Description of the product | [optional] 
**merchant_descriptor** | **str** | Allows the business to send a text up to 25 characters that will be printed on the customer invoice. Limited to simple characters, no accents or special characters. | [optional] 
**user_interaction** | **int** | Indicates wether the business can interact with the customer | [optional] 
**trx_type** | **str** | Obligatory only if an MIT exception has been selected in scaException | [optional] 
**sca_exception** | **str** | TYPE OF EXCEPTION TO THE SECURE PAYMENT. If not specified, PAYCOMET will try to assign it the most appropriate possible | [optional] 
**url_ok** | **str** | Url where the customer will be redirected after finishing a correct transaction. (Max 255 characters) | [optional] 
**url_ko** | **str** | Url where the customer will be redirected after finishing a failed transaction. (Max 255 characters) | [optional] 
**merchant_data** | [**V1paymentspreauthPaymentMerchantData**](V1paymentspreauthPaymentMerchantData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

