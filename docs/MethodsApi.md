# paycomet-client.MethodsApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_payment_methods**](MethodsApi.md#get_user_payment_methods) | **POST** /v1/methods | Retrieves product methods

# **get_user_payment_methods**
> list[InlineResponse20012] get_user_payment_methods(body=body, paycomet_api_token=paycomet_api_token)

Retrieves product methods

Payment methods of the client

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.MethodsApi()
body = paycomet-client.V1MethodsBody() # V1MethodsBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Query privilege required) (optional)

try:
    # Retrieves product methods
    api_response = api_instance.get_user_payment_methods(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MethodsApi->get_user_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1MethodsBody**](V1MethodsBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Query privilege required) | [optional] 

### Return type

[**list[InlineResponse20012]**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

