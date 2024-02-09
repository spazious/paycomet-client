# paycomet-client.LaunchpadApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**launch_authorization**](LaunchpadApi.md#launch_authorization) | **POST** /v1/launchpad/authorization | Creates a payment link and sends it to customer
[**launch_preauthorization**](LaunchpadApi.md#launch_preauthorization) | **POST** /v1/launchpad/preauthorization | Executes a preauthorization link and sends it to customer
[**launch_subscription**](LaunchpadApi.md#launch_subscription) | **POST** /v1/launchpad/subscription | Creates a subscription link and sends it to customer

# **launch_authorization**
> InlineResponse20024 launch_authorization(body=body, paycomet_api_token=paycomet_api_token)

Creates a payment link and sends it to customer

Generate a authorization link. It will send a challenge URL to the client.

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.LaunchpadApi()
body = paycomet-client.LaunchpadAuthorizationBody() # LaunchpadAuthorizationBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required) (optional)

try:
    # Creates a payment link and sends it to customer
    api_response = api_instance.launch_authorization(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LaunchpadApi->launch_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LaunchpadAuthorizationBody**](LaunchpadAuthorizationBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launch_preauthorization**
> InlineResponse20024 launch_preauthorization(body=body, paycomet_api_token=paycomet_api_token)

Executes a preauthorization link and sends it to customer

Generate a preauthorization link. It will send a challenge URL to the client.

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.LaunchpadApi()
body = paycomet-client.LaunchpadPreauthorizationBody() # LaunchpadPreauthorizationBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required) (optional)

try:
    # Executes a preauthorization link and sends it to customer
    api_response = api_instance.launch_preauthorization(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LaunchpadApi->launch_preauthorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LaunchpadPreauthorizationBody**](LaunchpadPreauthorizationBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launch_subscription**
> InlineResponse20024 launch_subscription(body=body, paycomet_api_token=paycomet_api_token)

Creates a subscription link and sends it to customer

Generate a subscription link. It will send a challenge URL to the client.

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.LaunchpadApi()
body = paycomet-client.LaunchpadSubscriptionBody() # LaunchpadSubscriptionBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required) (optional)

try:
    # Creates a subscription link and sends it to customer
    api_response = api_instance.launch_subscription(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LaunchpadApi->launch_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LaunchpadSubscriptionBody**](LaunchpadSubscriptionBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

