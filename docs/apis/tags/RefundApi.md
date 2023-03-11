<a name="__pageTop"></a>
# paycomet_client.apis.tags.refund_api.RefundApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_refund**](#execute_refund) | **post** /v1/payments/{order}/refund | Perform a refund

# **execute_refund**
<a name="execute_refund"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} execute_refund(orderpaycomet_api_token)

Perform a refund

execute_refund

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import refund_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = refund_api.RefundApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'order': "order_example",
    }
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    try:
        # Perform a refund
        api_response = api_instance.execute_refund(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling RefundApi->execute_refund: %s\n" % e)

    # example passing only optional values
    path_params = {
        'order': "order_example",
    }
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    body = dict(
        payment=dict(
            terminal=1,
            amount="202",
            currency="EUR",
            auth_code="auth_code_example",
            original_ip="127.0.0.1",
            token_user="WHlSWmVDdzVQeUZ",
            id_user=12345678,
            notify_direct_payment=1,
        ),
    )
    try:
        # Perform a refund
        api_response = api_instance.execute_refund(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling RefundApi->execute_refund: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
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
**[payment](#payment)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# payment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | str,  | str,  | Amount to refund in number format. If empty, total refund asumed. | 
**authCode** | str,  | str,  |  Original bank code of the authorization of the transaction. | 
**currency** | str,  | str,  | Currency of the transaction | 
**terminal** | decimal.Decimal, int,  | decimal.Decimal,  | Product or terminal Id. | 
**originalIp** | str,  | str,  | IP Address of the application of the business. | 
**tokenUser** | str,  | str,  | Token code associated with the IdUser. | [optional] 
**idUser** | decimal.Decimal, int,  | decimal.Decimal,  | Unique identifier of the user registered in the system. | [optional] 
**notifyDirectPayment** | decimal.Decimal, int,  | decimal.Decimal,  | Configurate POST notification of the operation result (possible values: 1 - force notify, 2 - not notify). It will notify if is not informed | [optional] 
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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
order | OrderSchema | | 

# OrderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#execute_refund.ApiResponseFor200) | OK
422 | [ApiResponseFor422](#execute_refund.ApiResponseFor422) | Unprocessable Entity

#### execute_refund.ApiResponseFor200
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
**amount** | str,  | str,  |  | [optional] 
**currency** | str,  | str,  |  | [optional] 
**methodId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**order** | str,  | str,  |  | [optional] 
**authCode** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### execute_refund.ApiResponseFor422
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

