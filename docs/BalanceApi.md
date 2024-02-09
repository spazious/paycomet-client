# paycomet-client.BalanceApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_balance**](BalanceApi.md#product_balance) | **POST** /v1/balance | Get balance info

# **product_balance**
> InlineResponse2006 product_balance(body=body, paycomet_api_token=paycomet_api_token)

Get balance info

Gets the balance of a product. Restricted.

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.BalanceApi()
body = paycomet-client.V1BalanceBody() # V1BalanceBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Query privilege required) (optional)

try:
    # Get balance info
    api_response = api_instance.product_balance(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanceApi->product_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1BalanceBody**](V1BalanceBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Query privilege required) | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

