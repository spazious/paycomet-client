# paycomet-client.PreauthorizationsApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_preauthorization**](PreauthorizationsApi.md#cancel_preauthorization) | **POST** /v1/payments/{order}/preauth/cancel | Cancel previous preauthorization
[**confirm_preauthorization**](PreauthorizationsApi.md#confirm_preauthorization) | **POST** /v1/payments/{order}/preauth/confirm | Confirm previous preauthorization
[**create_preauthorization**](PreauthorizationsApi.md#create_preauthorization) | **POST** /v1/payments/preauth | Create preauthorization
[**create_preauthorization_rtoken**](PreauthorizationsApi.md#create_preauthorization_rtoken) | **POST** /v1/payments/preauthrtoken | Creates a preauthorization by reference

# **cancel_preauthorization**
> InlineResponse20019 cancel_preauthorization(paycomet_api_token, order, body=body)

Cancel previous preauthorization

cancel_preauthorization

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.PreauthorizationsApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Preauthorization privilege required)
order = 'order_example' # str | 
body = paycomet-client.PreauthCancelBody() # PreauthCancelBody |  (optional)

try:
    # Cancel previous preauthorization
    api_response = api_instance.cancel_preauthorization(paycomet_api_token, order, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreauthorizationsApi->cancel_preauthorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Preauthorization privilege required) | 
 **order** | **str**|  | 
 **body** | [**PreauthCancelBody**](PreauthCancelBody.md)|  | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_preauthorization**
> InlineResponse20020 confirm_preauthorization(paycomet_api_token, order, body=body)

Confirm previous preauthorization

confirm_preauthorization

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.PreauthorizationsApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Preauthorization privilege required)
order = 'order_example' # str | 
body = paycomet-client.PreauthConfirmBody() # PreauthConfirmBody |  (optional)

try:
    # Confirm previous preauthorization
    api_response = api_instance.confirm_preauthorization(paycomet_api_token, order, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreauthorizationsApi->confirm_preauthorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Preauthorization privilege required) | 
 **order** | **str**|  | 
 **body** | [**PreauthConfirmBody**](PreauthConfirmBody.md)|  | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_preauthorization**
> InlineResponse20018 create_preauthorization(paycomet_api_token, body=body)

Create preauthorization

create_preauthorization

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.PreauthorizationsApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Preauthorization privilege required)
body = paycomet-client.PaymentsPreauthBody() # PaymentsPreauthBody |  (optional)

try:
    # Create preauthorization
    api_response = api_instance.create_preauthorization(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreauthorizationsApi->create_preauthorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Preauthorization privilege required) | 
 **body** | [**PaymentsPreauthBody**](PaymentsPreauthBody.md)|  | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_preauthorization_rtoken**
> InlineResponse20021 create_preauthorization_rtoken(body=body, paycomet_api_token=paycomet_api_token)

Creates a preauthorization by reference

Creates a preauthorization with reference.

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.PreauthorizationsApi()
body = paycomet-client.PaymentsPreauthrtokenBody() # PaymentsPreauthrtokenBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required) (optional)

try:
    # Creates a preauthorization by reference
    api_response = api_instance.create_preauthorization_rtoken(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreauthorizationsApi->create_preauthorization_rtoken: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentsPreauthrtokenBody**](PaymentsPreauthrtokenBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

