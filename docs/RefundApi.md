# paycomet-client.RefundApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_refund**](RefundApi.md#execute_refund) | **POST** /v1/payments/{order}/refund | Perform a refund

# **execute_refund**
> InlineResponse20015 execute_refund(paycomet_api_token, order, body=body)

Perform a refund

execute_refund

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.RefundApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Refund privilege required)
order = 'order_example' # str | 
body = paycomet-client.OrderRefundBody() # OrderRefundBody |  (optional)

try:
    # Perform a refund
    api_response = api_instance.execute_refund(paycomet_api_token, order, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundApi->execute_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Refund privilege required) | 
 **order** | **str**|  | 
 **body** | [**OrderRefundBody**](OrderRefundBody.md)|  | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

