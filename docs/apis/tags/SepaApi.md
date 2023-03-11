<a name="__pageTop"></a>
# paycomet_client.apis.tags.sepa_api.SepaApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document**](#add_document) | **post** /v1/sepa/add-document | Adds a SEPA document
[**cancel**](#cancel) | **post** /v1/sepa/cancel | Cancel a SEPA order
[**check_customer**](#check_customer) | **post** /v1/sepa/check-customer | Check a customers SEPA documentation
[**check_document**](#check_document) | **post** /v1/sepa/check-document | Check a SEPA document
[**enrole_customer**](#enrole_customer) | **post** /v1/sepa/enrole-customer | Generate a link to make a account check to a customer
[**sepa_operations**](#sepa_operations) | **post** /v1/sepa/operations | Send SEPA operations

# **add_document**
<a name="add_document"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} add_document(paycomet_api_token)

Adds a SEPA document

add_document

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import sepa_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sepa_api.SepaApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    try:
        # Adds a SEPA document
        api_response = api_instance.add_document(
            header_params=header_params,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling SepaApi->add_document: %s\n" % e)

    # example passing only optional values
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    body = dict(
        terminal=1234,
        sepa_provider_id=18,
        merchant_code="abcdefgh",
        merchant_customer_id="ABCD1234",
        merchant_customer_iban="ES0123456789012345678901",
        document_type=12,
        file_content="JVBERi0xLjQNJeLjz9MNCjY...",
    )
    try:
        # Adds a SEPA document
        api_response = api_instance.add_document(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling SepaApi->add_document: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sepaProviderId** | decimal.Decimal, int,  | decimal.Decimal,  | Unique identifier assigned by PAYCOMET for the supplier sending SEPA operations. Available on the client control panel. | 
**merchantCode** | str,  | str,  | Unique identifier as PAYCOMET account. Available on the client control panel. | 
**documentType** | decimal.Decimal, int,  | decimal.Decimal,  | Identifier of the type of document on PAYCOMET. | 
**merchantCustomerIban** | str,  | str,  | Account number of the client in IBAN format. | 
**merchantCustomerId** | str,  | str,  | Unique identifier of the client of the supplier. | 
**terminal** | decimal.Decimal, int,  | decimal.Decimal,  | Product or terminal Id. | 
**fileContent** | str,  | str,  | Binary content of the file to send, codified in base 64. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
PAYCOMET-API-TOKEN | PAYCOMETAPITOKENSchema | | 

# PAYCOMETAPITOKENSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#add_document.ApiResponseFor200) | OK
422 | [ApiResponseFor422](#add_document.ApiResponseFor422) | Unprocessable Entity

#### add_document.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**merchantCustomerId** | str,  | str,  | Unique identifier of the client of the supplier. | [optional] 
**merchantCustomerIban** | str,  | str,  | Account number of the client in IBAN format. | [optional] 
**documentType** | decimal.Decimal, int,  | decimal.Decimal,  | Identifier of the type of document on PAYCOMET. | [optional] 
**documentStatus** | decimal.Decimal, int,  | decimal.Decimal,  | Identifier of the document status. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### add_document.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[error](#error)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# error

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**message** | str,  | str,  |  | [optional] 
**[detail](#detail)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# detail

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **cancel**
<a name="cancel"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} cancel(paycomet_api_token)

Cancel a SEPA order

cancel

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import sepa_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sepa_api.SepaApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    try:
        # Cancel a SEPA order
        api_response = api_instance.cancel(
            header_params=header_params,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling SepaApi->cancel: %s\n" % e)

    # example passing only optional values
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    body = dict(
        terminal=1234,
        sepa_provider_id=18,
        merchant_code="abcdefgh",
        operation_order="ABCD1234",
    )
    try:
        # Cancel a SEPA order
        api_response = api_instance.cancel(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling SepaApi->cancel: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sepaProviderId** | decimal.Decimal, int,  | decimal.Decimal,  | Unique identifier assigned by PAYCOMET for the supplier sending SEPA operations. Available on the client control panel. | 
**merchantCode** | str,  | str,  | Unique identifier as PAYCOMET account. Available on the client control panel. | 
**operationOrder** | str,  | str,  | Order reference | 
**terminal** | decimal.Decimal, int,  | decimal.Decimal,  | Product or terminal Id. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
PAYCOMET-API-TOKEN | PAYCOMETAPITOKENSchema | | 

# PAYCOMETAPITOKENSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cancel.ApiResponseFor200) | OK
422 | [ApiResponseFor422](#cancel.ApiResponseFor422) | Unprocessable Entity

#### cancel.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**operationResult** | str,  | str,  |  | [optional] 
**operationOrder** | str,  | str,  | Order reference | [optional] 
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### cancel.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[error](#error)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# error

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**message** | str,  | str,  |  | [optional] 
**[detail](#detail)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# detail

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **check_customer**
<a name="check_customer"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} check_customer(paycomet_api_token)

Check a customers SEPA documentation

check_customer

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import sepa_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sepa_api.SepaApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    try:
        # Check a customers SEPA documentation
        api_response = api_instance.check_customer(
            header_params=header_params,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling SepaApi->check_customer: %s\n" % e)

    # example passing only optional values
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    body = dict(
        terminal=1234,
        sepa_provider_id=18,
        merchant_code="abcdefgh",
        merchant_customer_id="ABCD1234",
        merchant_customer_iban="ES0123456789012345678901",
        merchant_customer_type=12,
    )
    try:
        # Check a customers SEPA documentation
        api_response = api_instance.check_customer(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling SepaApi->check_customer: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sepaProviderId** | decimal.Decimal, int,  | decimal.Decimal,  | Unique identifier assigned by PAYCOMET for the supplier sending SEPA operations. Available on the client control panel. | 
**merchantCode** | str,  | str,  | Unique identifier as PAYCOMET account. Available on the client control panel. | 
**merchantCustomerIban** | str,  | str,  | Account number of the client in IBAN format. | 
**merchantCustomerId** | str,  | str,  | Unique identifier of the client of the supplier. | 
**terminal** | decimal.Decimal, int,  | decimal.Decimal,  | Product or terminal Id. | 
**merchantCustomerType** | decimal.Decimal, int,  | decimal.Decimal,  | Identifier of the type of company on PAYCOMET. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
PAYCOMET-API-TOKEN | PAYCOMETAPITOKENSchema | | 

# PAYCOMETAPITOKENSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#check_customer.ApiResponseFor200) | OK
422 | [ApiResponseFor422](#check_customer.ApiResponseFor422) | Unprocessable Entity

#### check_customer.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**merchantCustomerId** | str,  | str,  | Unique identifier of the client of the supplier. | [optional] 
**merchantCustomerIban** | str,  | str,  | Account number of the client in IBAN format. | [optional] 
**[documents](#documents)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object with a pair key value to identify if a document type is verified or not. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# documents

Object with a pair key value to identify if a document type is verified or not.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object with a pair key value to identify if a document type is verified or not. | 

#### check_customer.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[error](#error)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# error

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**message** | str,  | str,  |  | [optional] 
**[detail](#detail)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# detail

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **check_document**
<a name="check_document"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} check_document(paycomet_api_token)

Check a SEPA document

check_document

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import sepa_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sepa_api.SepaApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    try:
        # Check a SEPA document
        api_response = api_instance.check_document(
            header_params=header_params,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling SepaApi->check_document: %s\n" % e)

    # example passing only optional values
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    body = dict(
        terminal=1234,
        sepa_provider_id=18,
        merchant_code="abcdefgh",
        merchant_customer_id="ABCD1234",
        merchant_customer_iban="ES0123456789012345678901",
        document_type=12,
    )
    try:
        # Check a SEPA document
        api_response = api_instance.check_document(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling SepaApi->check_document: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sepaProviderId** | decimal.Decimal, int,  | decimal.Decimal,  | Unique identifier assigned by PAYCOMET for the supplier sending SEPA operations. Available on the client control panel. | 
**merchantCode** | str,  | str,  | Unique identifier as PAYCOMET account. Available on the client control panel. | 
**documentType** | decimal.Decimal, int,  | decimal.Decimal,  | Identifier of the type of document on PAYCOMET. | 
**merchantCustomerIban** | str,  | str,  | Account number of the client in IBAN format. | 
**merchantCustomerId** | str,  | str,  | Unique identifier of the client of the supplier. | 
**terminal** | decimal.Decimal, int,  | decimal.Decimal,  | Product or terminal Id. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
PAYCOMET-API-TOKEN | PAYCOMETAPITOKENSchema | | 

# PAYCOMETAPITOKENSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#check_document.ApiResponseFor200) | OK
422 | [ApiResponseFor422](#check_document.ApiResponseFor422) | Unprocessable Entity

#### check_document.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**merchantCustomerId** | str,  | str,  | Unique identifier of the client of the supplier. | [optional] 
**merchantCustomerIban** | str,  | str,  | Account number of the client in IBAN format. | [optional] 
**documentType** | decimal.Decimal, int,  | decimal.Decimal,  | Identifier of the type of document on PAYCOMET. | [optional] 
**documentStatus** | decimal.Decimal, int,  | decimal.Decimal,  | Identifier of the document status. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### check_document.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[error](#error)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# error

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**message** | str,  | str,  |  | [optional] 
**[detail](#detail)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# detail

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **enrole_customer**
<a name="enrole_customer"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} enrole_customer(paycomet_api_token)

Generate a link to make a account check to a customer

enrole_customer

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import sepa_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sepa_api.SepaApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    try:
        # Generate a link to make a account check to a customer
        api_response = api_instance.enrole_customer(
            header_params=header_params,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling SepaApi->enrole_customer: %s\n" % e)

    # example passing only optional values
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    body = dict(
        terminal=1234,
        sepa_provider_id=18,
        merchant_code="abcdefgh",
        merchant_customer_id="ABCD1234",
        customer_market="ES",
        customer_language=1,
    )
    try:
        # Generate a link to make a account check to a customer
        api_response = api_instance.enrole_customer(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling SepaApi->enrole_customer: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sepaProviderId** | decimal.Decimal, int,  | decimal.Decimal,  | Unique identifier assigned by PAYCOMET for the supplier sending SEPA operations. Available on the client control panel. | 
**merchantCode** | str,  | str,  | Unique identifier as PAYCOMET account. Available on the client control panel. | 
**merchantCustomerId** | str,  | str,  | Unique identifier of the client of the supplier. | 
**terminal** | decimal.Decimal, int,  | decimal.Decimal,  | Product or terminal Id. | 
**customerMarket** | str,  | str,  | Pre selected customer market (allowed values: AT,BE,DK,EE,FI,FR,DE,IE,IT,LV,LT,NL,NO,PL,PT,ES,SE,GB) | [optional] 
**customerLanguage** | decimal.Decimal, int,  | decimal.Decimal,  | Desired interface language (allowed values: da_DK,de_DE,en_US,en_GB,es_ES,fi_FI,fr_FR,it_IT,nl_NL,no_NO,pt_PT,pl_PL,sv_SE,et_EE,lt_LT,lv_LV) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
PAYCOMET-API-TOKEN | PAYCOMETAPITOKENSchema | | 

# PAYCOMETAPITOKENSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#enrole_customer.ApiResponseFor200) | OK
422 | [ApiResponseFor422](#enrole_customer.ApiResponseFor422) | Unprocessable Entity

#### enrole_customer.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**merchantCustomerId** | str,  | str,  | Unique identifier of the client of the supplier. | [optional] 
**link** | str,  | str,  | Link to redirect the customer to check the bank account | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### enrole_customer.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[error](#error)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# error

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**message** | str,  | str,  |  | [optional] 
**[detail](#detail)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# detail

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **sepa_operations**
<a name="sepa_operations"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} sepa_operations(paycomet_api_token)

Send SEPA operations

sepa_operations

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import sepa_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sepa_api.SepaApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    try:
        # Send SEPA operations
        api_response = api_instance.sepa_operations(
            header_params=header_params,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling SepaApi->sepa_operations: %s\n" % e)

    # example passing only optional values
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    body = dict(
        terminal=1234,
        sepa_provider_id=18,
        operations=[
            dict(
                operation_type=2,
                merchant_code="abcdefgh",
                terminal_id_debtor=1234,
                unique_id_creditor="abcd1234",
                company_name_creditor="abcd1234",
                iban_number_creditor="ES123456789012341234",
                swift_code_creditor="",
                company_type_creditor=3,
                operation_order="test-001",
                operation_amount=203,
                operation_currency="EUR",
                operation_datetime="1970-01-01",
                operation_concept="Operation concept.",
            )
        ],
    )
    try:
        # Send SEPA operations
        api_response = api_instance.sepa_operations(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling SepaApi->sepa_operations: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sepaProviderId** | decimal.Decimal, int,  | decimal.Decimal,  | Unique identifier assigned by PAYCOMET for the supplier sending SEPA operations. Available on the client control panel. | 
**[operations](#operations)** | list, tuple,  | tuple,  |  | 
**terminal** | decimal.Decimal, int,  | decimal.Decimal,  | Product or terminal Id. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# operations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Operations parameters | 

# items

Operations parameters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Operations parameters | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**operationDatetime** | str, date,  | str,  | Date desired for sending the SEPA operation / remittance. Always after the current date. Format: yyyymmdd. | value must conform to RFC-3339 full-date YYYY-MM-DD
**merchantCode** | str,  | str,  | Unique identifier as PAYCOMET account. Available on the client control panel. | 
**terminalIDDebtor** | decimal.Decimal, int,  | decimal.Decimal,  | This will be the terminal number assigned to the product. Obtained from the control panel. Identifies the terminal number of the debtor/payer of a SEPA operation. Therefore, it will depend on the type of operation (debit, transfer). | 
**ibanNumberCreditor** | str,  | str,  | IBAN code of the account of the recipient. | 
**swiftCodeCreditor** | str,  | str,  | SWIFT code of the bank account of the recipient. Must be provided when the account IBAN is not Spanish. If the ibanNumberCreditor number belongs to a Spanish account, it must be sent as an empty string. | 
**uniqueIdCreditor** | str,  | str,  | This will be the unique identifier of this individual, freelancer, company (recipient) in the client. | 
**companyNameCreditor** | str,  | str,  | Name of the company, individual or freelancer corresponding to the previous indicator. | 
**operationOrder** | str,  | str,  | Unique reference of the operation. | 
**operationAmount** | decimal.Decimal, int,  | decimal.Decimal,  | Amount in the transaction currency with 2 decimals in integer format: (€2.25 &#x3D; 225). | 
**operationType** | decimal.Decimal, int,  | decimal.Decimal,  | Type of operation. Identifies whether the operation is a direct debit or a transfer. 1 – Direct Debit (N19) 2 – Transfer (N34) | 
**operationCurrency** | str,  | str,  | Currency type of the transaction. The only permitted currency is the euro, whose code is EUR. | 
**operationConcept** | str,  | str,  | Concept assigned to the operation / remittance. This is the descriptor which will appear in banking entries. Maximum length 100. Although error 1273 specified 140 characters, PAYCOMET reserves 40, the maximum permitted in the input therefore being 100. Allowed charactaers: ([A-Za-z0-9]|[+|?|/|-|:|(|)|.|,|&#x27;| ]) | 
**companyTypeCreditor** | decimal.Decimal, int,  | decimal.Decimal,  | Identifier of the type of recipient: 1: Individual / 2: Freelancer / 3: Commercial Company. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
PAYCOMET-API-TOKEN | PAYCOMETAPITOKENSchema | | 

# PAYCOMETAPITOKENSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#sepa_operations.ApiResponseFor200) | OK
422 | [ApiResponseFor422](#sepa_operations.ApiResponseFor422) | Unprocessable Entity

#### sepa_operations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[operations](#operations)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# operations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Detail of the operations | 

# items

Detail of the operations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Detail of the operations | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**operationResult** | str,  | str,  | Operation result OK/KO | [optional] 
**operationErrorCode** | decimal.Decimal, int,  | decimal.Decimal,  | Error code given by PAYCOMET for that operation | [optional] 
**operationOrder** | str,  | str,  | Order reference | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### sepa_operations.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[error](#error)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# error

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**message** | str,  | str,  |  | [optional] 
**[detail](#detail)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# detail

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

