# V1CardsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal** | **int** | Product or terminal Id. | 
**cvc2** | **str** | cvc2. Mandatory if no JetToken provided | [optional] 
**jet_token** | **str** | Temporary token provided from PAYCOMET. Mandatory if no card provided. | [optional] 
**expiry_year** | **str** | Expiry year.  Mandatory if no JetToken provided | [optional] 
**expiry_month** | **str** | Expiry month.  Mandatory if no JetToken provided. | [optional] 
**pan** | **str** | Card number. Mandatory if no JetToken provided | [optional] 
**order** | **str** | Reference, will be included in callback. | [optional] 
**product_description** | **str** | Concept, will be included in callback. | [optional] 
**language** | **str** | Language for callback translation. | [optional] [default to 'es']
**notify** | **int** | Configure POST notification of the card tokenization result (possible values: 1 - force notify, 2 - not notify). Default product value will be used if notify is not informed | [optional] 
**card_holder_name** | **str** | Card holder name | [optional] 
**secure_authentication** | [**V1cardsSecureAuthentication**](V1cardsSecureAuthentication.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

