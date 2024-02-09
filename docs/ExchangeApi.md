# paycomet-client.ExchangeApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchange**](ExchangeApi.md#exchange) | **POST** /v1/exchange | Converts a certain amount from a currency to another.

# **exchange**
> InlineResponse2007 exchange(body=body, paycomet_api_token=paycomet_api_token)

Converts a certain amount from a currency to another.

Gets the exchange of an amount.

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.ExchangeApi()
body = paycomet-client.V1ExchangeBody() # V1ExchangeBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Query privilege required) (optional)

try:
    # Converts a certain amount from a currency to another.
    api_response = api_instance.exchange(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangeApi->exchange: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ExchangeBody**](V1ExchangeBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Query privilege required) | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

