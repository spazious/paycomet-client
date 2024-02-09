# paycomet-client.TokenApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_token**](TokenApi.md#add_token) | **POST** /v1/token | Tokenizes an APM.

# **add_token**
> InlineResponse20038 add_token(body=body, paycomet_api_token=paycomet_api_token)

Tokenizes an APM.

This method supposes the registration of the APM in PAYCOMET for subsequent charges.

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.TokenApi()
body = paycomet-client.V1TokenBody() # V1TokenBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Token actions privilege required) (optional)

try:
    # Tokenizes an APM.
    api_response = api_instance.add_token(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->add_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1TokenBody**](V1TokenBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Token actions privilege required) | [optional] 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

