# paycomet-client.ErrorApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**info_error**](ErrorApi.md#info_error) | **POST** /v1/errors | Gets an error description

# **info_error**
> InlineResponse200 info_error(body=body, paycomet_api_token=paycomet_api_token)

Gets an error description

info_error

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.ErrorApi()
body = paycomet-client.V1ErrorsBody() # V1ErrorsBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Query privilege required) (optional)

try:
    # Gets an error description
    api_response = api_instance.info_error(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ErrorApi->info_error: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ErrorsBody**](V1ErrorsBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Query privilege required) | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

