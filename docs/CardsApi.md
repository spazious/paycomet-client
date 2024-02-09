# paycomet_client.CardsApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](CardsApi.md#add_user) | **POST** /v1/cards | Tokenizes a card. Either card number and CVC2 or jetToken are required. For you to send directly the card data you should be PCI certified or the accepting the requirement to submit quarterly SAQ-AEP and get ASV scans. For most users is strongly recommended getting the jetToken with JETIFRAME or using GET integration to register the cards instead of REST.
[**edit_user**](CardsApi.md#edit_user) | **POST** /v1/cards/edit | Changes the expiry date, cvc2 or both
[**info_user**](CardsApi.md#info_user) | **POST** /v1/cards/info | Get card info
[**physical_add_card**](CardsApi.md#physical_add_card) | **POST** /v1/cards/physical | Tokenize a card by physical encrypted data
[**physical_edit_card**](CardsApi.md#physical_edit_card) | **POST** /v1/cards/physical/edit | Edit a card entered by physical encrypted data
[**remove_user**](CardsApi.md#remove_user) | **POST** /v1/cards/delete | Removes a card

# **add_user**
> InlineResponse2001 add_user(body=body, paycomet_api_token=paycomet_api_token)

Tokenizes a card. Either card number and CVC2 or jetToken are required. For you to send directly the card data you should be PCI certified or the accepting the requirement to submit quarterly SAQ-AEP and get ASV scans. For most users is strongly recommended getting the jetToken with JETIFRAME or using GET integration to register the cards instead of REST.

This method supposes the registration of the card in PAYCOMET, it is not valid for subsequent charges with the exception of MIT. To register the card against the processor for subsequent recurring charges, it is necessary to charge for a secure environment, regardless of the amount.

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.CardsApi()
body = paycomet_client.V1CardsBody() # V1CardsBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Token actions privilege required) (optional)

try:
    # Tokenizes a card. Either card number and CVC2 or jetToken are required. For you to send directly the card data you should be PCI certified or the accepting the requirement to submit quarterly SAQ-AEP and get ASV scans. For most users is strongly recommended getting the jetToken with JETIFRAME or using GET integration to register the cards instead of REST.
    api_response = api_instance.add_user(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardsApi->add_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CardsBody**](V1CardsBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Token actions privilege required) | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_user**
> InlineResponse2001 edit_user(body=body, paycomet_api_token=paycomet_api_token)

Changes the expiry date, cvc2 or both

edit_user

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.CardsApi()
body = paycomet_client.CardsEditBody() # CardsEditBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Token actions privilege required) (optional)

try:
    # Changes the expiry date, cvc2 or both
    api_response = api_instance.edit_user(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardsApi->edit_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CardsEditBody**](CardsEditBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Token actions privilege required) | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_user**
> InlineResponse2002 info_user(body=body, paycomet_api_token=paycomet_api_token)

Get card info

Info about an user card.

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.CardsApi()
body = paycomet_client.CardsInfoBody() # CardsInfoBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Query privilege required) (optional)

try:
    # Get card info
    api_response = api_instance.info_user(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardsApi->info_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CardsInfoBody**](CardsInfoBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Query privilege required) | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **physical_add_card**
> InlineResponse2004 physical_add_card(body=body, paycomet_api_token=paycomet_api_token)

Tokenize a card by physical encrypted data

cards_physical

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.CardsApi()
body = paycomet_client.CardsPhysicalBody() # CardsPhysicalBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Token actions privilege required) (optional)

try:
    # Tokenize a card by physical encrypted data
    api_response = api_instance.physical_add_card(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardsApi->physical_add_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CardsPhysicalBody**](CardsPhysicalBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Token actions privilege required) | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **physical_edit_card**
> InlineResponse2005 physical_edit_card(body=body, paycomet_api_token=paycomet_api_token)

Edit a card entered by physical encrypted data

cards_physical_edit

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.CardsApi()
body = paycomet_client.PhysicalEditBody() # PhysicalEditBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Token actions privilege required) (optional)

try:
    # Edit a card entered by physical encrypted data
    api_response = api_instance.physical_edit_card(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardsApi->physical_edit_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhysicalEditBody**](PhysicalEditBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Token actions privilege required) | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user**
> InlineResponse2003 remove_user(body=body, paycomet_api_token=paycomet_api_token)

Removes a card

Deletes the user.

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.CardsApi()
body = paycomet_client.CardsDeleteBody() # CardsDeleteBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Token actions privilege required) (optional)

try:
    # Removes a card
    api_response = api_instance.remove_user(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardsApi->remove_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CardsDeleteBody**](CardsDeleteBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Token actions privilege required) | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

