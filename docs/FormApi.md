# paycomet_client.FormApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**form**](FormApi.md#form) | **POST** /v1/form | Create form view for user capture

# **form**
> InlineResponse20013 form(body=body, paycomet_api_token=paycomet_api_token)

Create form view for user capture

Create form for user capture. Set operationType and attach the default request, PAYCOMET will generate a URL for user data capture. If you will use this url in an iframe please set `sandbox=\"allow-top-navigation allow-scripts allow-same-origin allow-forms\"` iframe option to avoid blocking the redirections required by the payment process in some browsers with security restrictions.

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.FormApi()
body = paycomet_client.V1FormBody() # V1FormBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required, token actions privilege required in case of tokenization) (optional)

try:
    # Create form view for user capture
    api_response = api_instance.form(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FormApi->form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1FormBody**](V1FormBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required, token actions privilege required in case of tokenization) | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

