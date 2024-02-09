# paycomet_client.IpApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_countryby_ip**](IpApi.md#get_countryby_ip) | **POST** /v1/ip | Retrieves country info by IP
[**get_remote_address**](IpApi.md#get_remote_address) | **POST** /v1/ip/remote | Retrieves request remote address IP

# **get_countryby_ip**
> InlineResponse20010 get_countryby_ip(body=body, paycomet_api_token=paycomet_api_token)

Retrieves country info by IP

Country by IP

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.IpApi()
body = paycomet_client.V1IpBody() # V1IpBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Query privilege required) (optional)

try:
    # Retrieves country info by IP
    api_response = api_instance.get_countryby_ip(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpApi->get_countryby_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1IpBody**](V1IpBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Query privilege required) | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_address**
> InlineResponse20011 get_remote_address(body=body, paycomet_api_token=paycomet_api_token)

Retrieves request remote address IP

Remote address by request

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.IpApi()
body = paycomet_client.IpRemoteBody() # IpRemoteBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Query privilege required) (optional)

try:
    # Retrieves request remote address IP
    api_response = api_instance.get_remote_address(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpApi->get_remote_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpRemoteBody**](IpRemoteBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Query privilege required) | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

