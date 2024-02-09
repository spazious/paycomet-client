# V1subscriptionPayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal** | **int** | Product or terminal Id. | 
**method_id** | **str** | PAYCOMET payment method ID. 1 is for card. | 
**order** | **str** | Unique reference for merchant&#x27;s purchase | 
**amount** | **str** | Amount of the operation in number format. 1.00 EURO &#x3D; 100, 4.50 EUROS &#x3D; 450... | 
**currency** | **str** | Currency of the transaction.  | 
**original_ip** | **str** | IP Address of the customer that initiated the payment transaction | 
**id_user** | **int** | Identification of user card given by PAYCOMET. Mandatory if is a card payment. | 
**token_user** | **str** | Identification of user card given by PAYCOMET. Mandatory if is a card payment. | 
**secure** | **int** | 0 or 1. Indicates if the transaction is secure. | 
**scoring** | **str** | Risk scoring value from 0 to 100. | [optional] 
**product_description** | **str** | Description of the product sold. | [optional] 
**merchant_descriptor** | **str** | Allows the business to send a text up to 25 characters that will be printed on the customer invoice. Limited to simple characters, no accents or special characters. | [optional] 
**user_interaction** | **int** | Indicates wether the business can interact with the customer | [optional] 
**trx_type** | **str** | Obligatory only if an MIT exception has been selected in scaException | [optional] 
**sca_exception** | **str** | TYPE OF EXCEPTION TO THE SECURE PAYMENT. If not specified, PAYCOMET will try to assign it the most appropriate possible | [optional] 
**url_ok** | **str** | Url where the customer will be redirected after finishing a correct transaction. (Max 255 characters) | [optional] 
**url_ko** | **str** | Url where the customer will be redirected after finishing a failed transaction. (Max 255 characters) | [optional] 
**notify_direct_payment** | **int** | Configurate POST notification of the operation result in frictionless payment (possible values: 1 - force notify, 2 - not notify). It will notify if is not informed | [optional] 
**merchant_data** | [**V1paymentspreauthPaymentMerchantData**](V1paymentspreauthPaymentMerchantData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

