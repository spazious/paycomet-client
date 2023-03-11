<a name="__pageTop"></a>
# paycomet_client.apis.tags.ivr_api.IVRApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_session**](#check_session) | **post** /v1/ivr/session-state | Checks an IVR session
[**get_session**](#get_session) | **post** /v1/ivr/get-session | Creates an IVR session
[**session_cancel**](#session_cancel) | **post** /v1/ivr/session-cancel | Cancel an IVR session

# **check_session**
<a name="check_session"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} check_session(paycomet_api_token)

Checks an IVR session

check_session

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import ivr_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ivr_api.IVRApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    try:
        # Checks an IVR session
        api_response = api_instance.check_session(
            header_params=header_params,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling IVRApi->check_session: %s\n" % e)

    # example passing only optional values
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    body = dict(
        terminal=1234,
        ivr_provider_id=18,
        ivr_merchant_order="ABCD1234",
    )
    try:
        # Checks an IVR session
        api_response = api_instance.check_session(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling IVRApi->check_session: %s\n" % e)
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
**ivrProviderId** | decimal.Decimal, int,  | decimal.Decimal,  | Supplier / IVR integrator code. | 
**ivrMerchantOrder** | str,  | str,  | Operation reference. It must be unique in each valid transaction. IMPORTANT IN CASE OF SUBSCRIPTIONS Do not include the characters “[“ or “]”, they will be used to recognise the business idUser. | 
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
200 | [ApiResponseFor200](#check_session.ApiResponseFor200) | OK
422 | [ApiResponseFor422](#check_session.ApiResponseFor422) | Unprocessable Entity

#### check_session.ApiResponseFor200
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
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  | The error code if something went wrong. 0 means no error. | [optional] 
**ivrResponse** | bool,  | BoolClass,  | Result of the session consultation. 0 -&gt; It will indicate that it was not possible to localize the IVR session. 1 -&gt; The session information have been found and will be returned afterwards. | [optional] 
**ivrSessionState** | decimal.Decimal, int,  | decimal.Decimal,  | The possible values are the following. 0 Waiting. 1 Processing. 2 Finalised. OK. 3 Finalised. KO. 4 Communication time exceeded. 5 Reference not found. 6 Operation cancelled by the agent. 7 Call ended. Waiting for next call | [optional] 
**ivrSessionResult** | decimal.Decimal, int,  | decimal.Decimal,  | The possible values are the following. 0 No error. 1 Payment operation error. 2 Error entering card data. 3 Error entering expiration month. 4 Error entering expiration year. 5 Error entering CVV | [optional] 
**ivrTimeLeft** | decimal.Decimal, int,  | decimal.Decimal,  | Time remaining expressed in seconds for finishing the IVR session. In state 0, the established maximum time will be returned. In state 1 the remaining time will be returned. In states 2, 3, 4 and 5 0 will be returned. | [optional] 
**ivrDigitPan** | decimal.Decimal, int,  | decimal.Decimal,  | When the IVR session is underway, the number of digits of the credit card that the client has entered will be returned. 0 will be returned if this information is not available. | [optional] 
**ivrDigitExp** | decimal.Decimal, int,  | decimal.Decimal,  | When the IVR session is underway, the number of digits of the expiry date that the client has entered will be returned. 0 will be returned if this information is not available. | [optional] 
**ivrDigitCvc** | decimal.Decimal, int,  | decimal.Decimal,  | When the IVR session is underway, the number of digits of the CVC2 that the client has entered will be returned. 0 will be shown if this information is not available. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### check_session.ApiResponseFor422
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

# **get_session**
<a name="get_session"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_session(paycomet_api_token)

Creates an IVR session

get_session

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import ivr_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ivr_api.IVRApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    try:
        # Creates an IVR session
        api_response = api_instance.get_session(
            header_params=header_params,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling IVRApi->get_session: %s\n" % e)

    # example passing only optional values
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    body = dict(
        terminal=1234,
        ivr_provider_id=18,
        ivr_station_id="14",
        ivr_merchant_amount=203,
        ivr_merchant_currency="EUR",
        ivr_merchant_order="ABCD1234",
        ivr_merchant_language="es",
        ivr_transaction_type="107",
        ivr_merchant_concept="Concept",
        ivr_subscription_startdate="2020-06-14",
        ivr_subscription_enddate="2025-06-14",
        ivr_subscription_periodicity=1,
        ivr_max_retries=3,
        ivr_session_timeout=10,
        ivr_callback_station_timeout="15",
        ivr_callback_station_ok="16",
        ivr_callback_station_ko="17",
        ivr_caller_phone_number="666555444",
        ivr_provider_data01="abcd",
        vr_provider_data02="abcd",
        ivr_provider_data03="abcd",
        ivr_provider_data04="abcd",
        ivr_provider_data05="abcd",
    )
    try:
        # Creates an IVR session
        api_response = api_instance.get_session(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling IVRApi->get_session: %s\n" % e)
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
**ivrMerchantLanguage** | str,  | str,  | Language (iso2) in which the IVR phrases will be sent | 
**ivrMerchantCurrency** | str,  | str,  | Transaction currency. | 
**ivrProviderId** | decimal.Decimal, int,  | decimal.Decimal,  | Supplier / IVR integrator code. | 
**ivrTransactionType** | str,  | str,  | Possible types 107 Bankstore user registration 1 Authorization 3 Pre-authorization 9 Subscription | 
**ivrMerchantOrder** | str,  | str,  | Operation reference. It must be unique in each valid transaction. IMPORTANT IN CASE OF SUBSCRIPTIONS Do not include the characters “[“ or “]”, they will be used to recognise the business idUser. | 
**ivrStationId** | str,  | str,  | Location identifier. | 
**terminal** | decimal.Decimal, int,  | decimal.Decimal,  | Product or terminal Id. | 
**ivrMerchantAmount** | decimal.Decimal, int,  | decimal.Decimal,  | Amount of the operation in full format. 1,00 EURO &#x3D; 100, 4,50 EUROS &#x3D; 450... | 
**ivrMerchantConcept** | str,  | str,  | Operation concept. | [optional] 
**ivrSubscriptionStartdate** | str,  | str,  | Mandatory in subscriptions. Subscription start date. | [optional] 
**ivrSubscriptionEnddate** | str,  | str,  | Mandatory in subscriptions. Subscription end date. | [optional] 
**ivrSubscriptionPeriodicity** | decimal.Decimal, int,  | decimal.Decimal,  | Mandatory in subscriptions. Frequency of the payment from the start date. The number is expressed in Days. It cannot be more than 365 days. | [optional] 
**ivrMaxRetries** | decimal.Decimal, int,  | decimal.Decimal,  | Number of attempts permitted. | [optional] 
**ivrSessionTimeout** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum session time. In seconds. | [optional] 
**ivrCallbackStationTimeout** | str,  | str,  | Extension of return in case of timeout. | [optional] 
**ivrCallbackStationOk** | str,  | str,  | Extension of return in case of operation OK. | [optional] 
**ivrCallbackStationKo** | str,  | str,  | Extension of return in case of operation KO. | [optional] 
**ivrCallerPhoneNumber** | str,  | str,  | Number of incoming call. | [optional] 
**ivrProviderData01** | str,  | str,  | Optional field. | [optional] 
**vrProviderData02** | str,  | str,  | Optional field. | [optional] 
**ivrProviderData03** | str,  | str,  | Optional field. | [optional] 
**ivrProviderData04** | str,  | str,  | Optional field. | [optional] 
**ivrProviderData05** | str,  | str,  | Optional field. | [optional] 
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
200 | [ApiResponseFor200](#get_session.ApiResponseFor200) | OK
422 | [ApiResponseFor422](#get_session.ApiResponseFor422) | Unprocessable Entity

#### get_session.ApiResponseFor200
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
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  | The error code if something went wrong. 0 means no error. | [optional] 
**ivrResponse** | bool,  | BoolClass,  | Indicates the session has been created. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_session.ApiResponseFor422
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

# **session_cancel**
<a name="session_cancel"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} session_cancel(paycomet_api_token)

Cancel an IVR session

session_cancell

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import ivr_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ivr_api.IVRApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    try:
        # Cancel an IVR session
        api_response = api_instance.session_cancel(
            header_params=header_params,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling IVRApi->session_cancel: %s\n" % e)

    # example passing only optional values
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    body = dict(
        terminal=1234,
        ivr_provider_id=18,
        ivr_merchant_order="ABCD1234",
    )
    try:
        # Cancel an IVR session
        api_response = api_instance.session_cancel(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling IVRApi->session_cancel: %s\n" % e)
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
**ivrProviderId** | decimal.Decimal, int,  | decimal.Decimal,  | Supplier / IVR integrator code. | 
**ivrMerchantOrder** | str,  | str,  | Operation reference. It must be unique in each valid transaction. IMPORTANT IN CASE OF SUBSCRIPTIONS Do not include the characters “[“ or “]”, they will be used to recognise the business idUser. | 
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
200 | [ApiResponseFor200](#session_cancel.ApiResponseFor200) | OK
422 | [ApiResponseFor422](#session_cancel.ApiResponseFor422) | Unprocessable Entity

#### session_cancel.ApiResponseFor200
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
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  | The error code if something went wrong. 0 means no error. | [optional] 
**ivrResponse** | bool,  | BoolClass,  | Result of the session consultation. 0 -&gt; It will indicate that it was not possible to localize the IVR session. 1 -&gt; The session information have been found and will be returned afterwards. | [optional] 
**ivrSessionState** | decimal.Decimal, int,  | decimal.Decimal,  | The possible values are the following. 0 Waiting. 1 Processing. 2 Finalised. OK. 3 Finalised. KO. 4 Communication time exceeded. 5 Reference not found. 6 Operation cancelled by the agent. 7 Call ended. Waiting for next call | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### session_cancel.ApiResponseFor422
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

