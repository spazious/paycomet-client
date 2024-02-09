# paycomet_client.SepaApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document**](SepaApi.md#add_document) | **POST** /v1/sepa/add-document | Adds a SEPA document
[**cancel**](SepaApi.md#cancel) | **POST** /v1/sepa/cancel | Cancel a SEPA order
[**check_customer**](SepaApi.md#check_customer) | **POST** /v1/sepa/check-customer | Check a customers SEPA documentation
[**check_document**](SepaApi.md#check_document) | **POST** /v1/sepa/check-document | Check a SEPA document
[**del_customer_iban**](SepaApi.md#del_customer_iban) | **POST** /v1/sepa/del-customer-iban | Delete customer Iban
[**enrole_customer**](SepaApi.md#enrole_customer) | **POST** /v1/sepa/enrole-customer | Generate a link to make a account check to a customer
[**sepa_operations**](SepaApi.md#sepa_operations) | **POST** /v1/sepa/operations | Send SEPA operations

# **add_document**
> InlineResponse20029 add_document(paycomet_api_token, body=body)

Adds a SEPA document

add_document

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.SepaApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = paycomet_client.SepaAdddocumentBody() # SepaAdddocumentBody |  (optional)

try:
    # Adds a SEPA document
    api_response = api_instance.add_document(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SepaApi->add_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**SepaAdddocumentBody**](SepaAdddocumentBody.md)|  | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel**
> InlineResponse20033 cancel(paycomet_api_token, body=body)

Cancel a SEPA order

cancel

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.SepaApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = paycomet_client.SepaCancelBody() # SepaCancelBody |  (optional)

try:
    # Cancel a SEPA order
    api_response = api_instance.cancel(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SepaApi->cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**SepaCancelBody**](SepaCancelBody.md)|  | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_customer**
> InlineResponse20031 check_customer(paycomet_api_token, body=body)

Check a customers SEPA documentation

check_customer

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.SepaApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = paycomet_client.SepaCheckcustomerBody() # SepaCheckcustomerBody |  (optional)

try:
    # Check a customers SEPA documentation
    api_response = api_instance.check_customer(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SepaApi->check_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**SepaCheckcustomerBody**](SepaCheckcustomerBody.md)|  | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_document**
> InlineResponse20029 check_document(paycomet_api_token, body=body)

Check a SEPA document

check_document

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.SepaApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = paycomet_client.SepaCheckdocumentBody() # SepaCheckdocumentBody |  (optional)

try:
    # Check a SEPA document
    api_response = api_instance.check_document(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SepaApi->check_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**SepaCheckdocumentBody**](SepaCheckdocumentBody.md)|  | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_customer_iban**
> InlineResponse20034 del_customer_iban(paycomet_api_token, body=body)

Delete customer Iban

delCustomerIban

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.SepaApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = paycomet_client.SepaDelcustomeribanBody() # SepaDelcustomeribanBody |  (optional)

try:
    # Delete customer Iban
    api_response = api_instance.del_customer_iban(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SepaApi->del_customer_iban: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**SepaDelcustomeribanBody**](SepaDelcustomeribanBody.md)|  | [optional] 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrole_customer**
> InlineResponse20030 enrole_customer(paycomet_api_token, body=body)

Generate a link to make a account check to a customer

enrole_customer

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.SepaApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = paycomet_client.SepaEnrolecustomerBody() # SepaEnrolecustomerBody |  (optional)

try:
    # Generate a link to make a account check to a customer
    api_response = api_instance.enrole_customer(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SepaApi->enrole_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**SepaEnrolecustomerBody**](SepaEnrolecustomerBody.md)|  | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sepa_operations**
> InlineResponse20032 sepa_operations(paycomet_api_token, body=body)

Send SEPA operations

sepa_operations

### Example
```python
from __future__ import print_function
import time
import paycomet_client
from paycomet_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = paycomet_client.SepaApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = paycomet_client.SepaOperationsBody() # SepaOperationsBody |  (optional)

try:
    # Send SEPA operations
    api_response = api_instance.sepa_operations(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SepaApi->sepa_operations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**SepaOperationsBody**](SepaOperationsBody.md)|  | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

