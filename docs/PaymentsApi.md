# paycomet-client.PaymentsApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_purchase**](PaymentsApi.md#execute_purchase) | **POST** /v1/payments | Executes a payment
[**execute_purchase_rtoken**](PaymentsApi.md#execute_purchase_rtoken) | **POST** /v1/payments/rtoken | Executes a payment by refence
[**operation_info**](PaymentsApi.md#operation_info) | **POST** /v1/payments/{order}/info | Get info of a order
[**operation_search**](PaymentsApi.md#operation_search) | **POST** /v1/payments/search | Search orders

# **execute_purchase**
> InlineResponse20014 execute_purchase(body=body, paycomet_api_token=paycomet_api_token)

Executes a payment

Generate a purchase. It will confirms a charge or send a challenge URL to the commerce.

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.PaymentsApi()
body = paycomet-client.V1PaymentsBody() # V1PaymentsBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required) (optional)

try:
    # Executes a payment
    api_response = api_instance.execute_purchase(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->execute_purchase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PaymentsBody**](V1PaymentsBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_purchase_rtoken**
> InlineResponse20021 execute_purchase_rtoken(body=body, paycomet_api_token=paycomet_api_token)

Executes a payment by refence

Generate a purchase with reference. It will confirms a charge or send a challenge URL to the commerce.

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.PaymentsApi()
body = paycomet-client.PaymentsRtokenBody() # PaymentsRtokenBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required) (optional)

try:
    # Executes a payment by refence
    api_response = api_instance.execute_purchase_rtoken(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->execute_purchase_rtoken: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentsRtokenBody**](PaymentsRtokenBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operation_info**
> InlineResponse20016 operation_info(paycomet_api_token, order, body=body)

Get info of a order

operation_info

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.PaymentsApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Query privilege required)
order = 'order_example' # str | 
body = paycomet-client.OrderInfoBody() # OrderInfoBody |  (optional)

try:
    # Get info of a order
    api_response = api_instance.operation_info(paycomet_api_token, order, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->operation_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Query privilege required) | 
 **order** | **str**|  | 
 **body** | [**OrderInfoBody**](OrderInfoBody.md)|  | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operation_search**
> InlineResponse20017 operation_search(paycomet_api_token, body=body)

Search orders

operation_search

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.PaymentsApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Query privilege required)
body = paycomet-client.PaymentsSearchBody() # PaymentsSearchBody |  (optional)

try:
    # Search orders
    api_response = api_instance.operation_search(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->operation_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Query privilege required) | 
 **body** | [**PaymentsSearchBody**](PaymentsSearchBody.md)|  | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

