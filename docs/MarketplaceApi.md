# paycomet-client.MarketplaceApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**split_transfer**](MarketplaceApi.md#split_transfer) | **POST** /v1/marketplace/split-transfer | Make a transfer to other accounts on PAYCOMET
[**split_transfer_reversal**](MarketplaceApi.md#split_transfer_reversal) | **POST** /v1/marketplace/split-transfer-reversal | Run a split transfer reversal based on a previous split transfer
[**transfer**](MarketplaceApi.md#transfer) | **POST** /v1/marketplace/transfer | Run a transfer
[**transfer_reversal**](MarketplaceApi.md#transfer_reversal) | **POST** /v1/marketplace/transfer-reversal | Make a transfer reversal based on a previous transfer

# **split_transfer**
> InlineResponse20027 split_transfer(paycomet_api_token, body=body)

Make a transfer to other accounts on PAYCOMET

Make a deposit in a destination account

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.MarketplaceApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = paycomet-client.MarketplaceSplittransferBody() # MarketplaceSplittransferBody |  (optional)

try:
    # Make a transfer to other accounts on PAYCOMET
    api_response = api_instance.split_transfer(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->split_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**MarketplaceSplittransferBody**](MarketplaceSplittransferBody.md)|  | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **split_transfer_reversal**
> InlineResponse20027 split_transfer_reversal(paycomet_api_token, body=body)

Run a split transfer reversal based on a previous split transfer

Make a split transfer reversal request

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.MarketplaceApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = paycomet-client.MarketplaceSplittransferreversalBody() # MarketplaceSplittransferreversalBody |  (optional)

try:
    # Run a split transfer reversal based on a previous split transfer
    api_response = api_instance.split_transfer_reversal(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->split_transfer_reversal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**MarketplaceSplittransferreversalBody**](MarketplaceSplittransferreversalBody.md)|  | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer**
> InlineResponse20028 transfer(paycomet_api_token, body=body)

Run a transfer

Run a transfer in a destination account

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.MarketplaceApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = paycomet-client.MarketplaceTransferBody() # MarketplaceTransferBody |  (optional)

try:
    # Run a transfer
    api_response = api_instance.transfer(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**MarketplaceTransferBody**](MarketplaceTransferBody.md)|  | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_reversal**
> InlineResponse20028 transfer_reversal(paycomet_api_token, body=body)

Make a transfer reversal based on a previous transfer

Make a transfer reversal based on a previous transfer

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.MarketplaceApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = paycomet-client.MarketplaceTransferreversalBody() # MarketplaceTransferreversalBody |  (optional)

try:
    # Make a transfer reversal based on a previous transfer
    api_response = api_instance.transfer_reversal(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketplaceApi->transfer_reversal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**MarketplaceTransferreversalBody**](MarketplaceTransferreversalBody.md)|  | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

