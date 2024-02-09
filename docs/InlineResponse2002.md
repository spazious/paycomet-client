# InlineResponse2002

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pan** | **str** | Card number, without any spaces or dashes. Only the last four digits will be returned. The rest will be masked with X | [optional] 
**card_brand** | **str** | Card brand. If it can be identified, information on the card brand will be sent (Visa, MasterCard, American Express, etc). Otherwise, the field will be returned blank. | [optional] 
**card_type** | **str** | Type of card. If it can be identified, information on the type of card will be sent (DEBIT, CREDIT, etc). Otherwise, the field will be returned blank. | [optional] 
**card_i_country_iso3** | **str** | ISO3 Code the country of the issuer of the card. If it can be identified, the ISO3 Code of the country of the issuer of the card will be sent. Otherwise, the field will be returned blank. | [optional] 
**expiry_date** | **str** | Expiry date of the card expressed in the format YYYY/MM | [optional] 
**card_hash** | **str** | Hash unique credit card id. | [optional] 
**card_category** | **str** | Card category. | [optional] 
**sepa_card** | **int** | Card in SEPA country. | [optional] 
**psd2_card** | **str** | Express if card has PSD2 information (Y is a PSD2 Card, N is not and NA is not available). | [optional] 
**token_cof** | **int** | Express if card has COF registered. | [optional] 
**eea_card** | **str** | Express if card country belongs to EEA zone or not. (Y/N or NA if not available). | [optional] 
**error_code** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

