# paycomet-client.MiraklApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mirakl_invoices_search**](MiraklApi.md#mirakl_invoices_search) | **POST** /v1/invoices | Search Mirakl invoices

# **mirakl_invoices_search**
> InlineResponse2009 mirakl_invoices_search(paycomet_api_token, body=body)

Search Mirakl invoices

nirakl_invoice_search

### Example
```python
from __future__ import print_function
import time
import paycomet-client
from paycomet-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet-client.MiraklApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Query privilege required)
body = paycomet-client.V1InvoicesBody() # V1InvoicesBody |  (optional)

try:
    # Search Mirakl invoices
    api_response = api_instance.mirakl_invoices_search(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiraklApi->mirakl_invoices_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Query privilege required) | 
 **body** | [**V1InvoicesBody**](V1InvoicesBody.md)|  | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

