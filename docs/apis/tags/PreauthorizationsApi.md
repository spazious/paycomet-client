<a name="__pageTop"></a>
# paycomet_client.apis.tags.preauthorizations_api.PreauthorizationsApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_preauthorization**](#cancel_preauthorization) | **post** /v1/payments/{order}/preauth/cancel | Cancel previous preauthorization
[**confirm_preauthorization**](#confirm_preauthorization) | **post** /v1/payments/{order}/preauth/confirm | Confirm previous preauthorization
[**create_preauthorization**](#create_preauthorization) | **post** /v1/payments/preauth | Create preauthorization
[**create_preauthorization_rtoken**](#create_preauthorization_rtoken) | **post** /v1/payments/preauthrtoken | Creates a preauthorization by reference

# **cancel_preauthorization**
<a name="cancel_preauthorization"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} cancel_preauthorization(orderpaycomet_api_token)

Cancel previous preauthorization

cancel_preauthorization

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import preauthorizations_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = preauthorizations_api.PreauthorizationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'order': "order_example",
    }
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    try:
        # Cancel previous preauthorization
        api_response = api_instance.cancel_preauthorization(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling PreauthorizationsApi->cancel_preauthorization: %s\n" % e)

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
            original_ip="127.0.0.1",
            auth_code="auth_code_example",
            deferred=0,
            notify_direct_payment=1,
        ),
    )
    try:
        # Cancel previous preauthorization
        api_response = api_instance.cancel_preauthorization(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling PreauthorizationsApi->cancel_preauthorization: %s\n" % e)
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
**amount** | str,  | str,  |  | 
**authCode** | str,  | str,  | Authorization bank code of the transaction (required to execute a return). | 
**terminal** | decimal.Decimal, int,  | decimal.Decimal,  | Product or terminal Id. | 
**originalIp** | str,  | str,  |  | 
**deferred** | decimal.Decimal, int,  | decimal.Decimal,  | Identify the preauthorization as deferred | [optional] if omitted the server will use the default value of 0
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
200 | [ApiResponseFor200](#cancel_preauthorization.ApiResponseFor200) | OK
422 | [ApiResponseFor422](#cancel_preauthorization.ApiResponseFor422) | Unprocessable Entity

#### cancel_preauthorization.ApiResponseFor200
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
**currency** | str,  | str,  |  | [optional] 
**order** | str,  | str,  |  | [optional] 
**amount** | str,  | str,  |  | [optional] 
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**cardCountry** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### cancel_preauthorization.ApiResponseFor422
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

# **confirm_preauthorization**
<a name="confirm_preauthorization"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} confirm_preauthorization(orderpaycomet_api_token)

Confirm previous preauthorization

confirm_preauthorization

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import preauthorizations_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = preauthorizations_api.PreauthorizationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'order': "order_example",
    }
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    try:
        # Confirm previous preauthorization
        api_response = api_instance.confirm_preauthorization(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling PreauthorizationsApi->confirm_preauthorization: %s\n" % e)

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
            original_ip="original_ip_example",
            auth_code="AC410397",
            deferred=0,
            notify_direct_payment=1,
        ),
    )
    try:
        # Confirm previous preauthorization
        api_response = api_instance.confirm_preauthorization(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling PreauthorizationsApi->confirm_preauthorization: %s\n" % e)
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
**amount** | str,  | str,  |  | 
**authCode** | str,  | str,  | Authorization bank code of the transaction (required to execute a return). | 
**terminal** | decimal.Decimal, int,  | decimal.Decimal,  | Product or terminal Id. | 
**originalIp** | str,  | str,  |  | 
**deferred** | decimal.Decimal, int,  | decimal.Decimal,  | Identify the preauthorization as deferred | [optional] if omitted the server will use the default value of 0
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
200 | [ApiResponseFor200](#confirm_preauthorization.ApiResponseFor200) | OK
422 | [ApiResponseFor422](#confirm_preauthorization.ApiResponseFor422) | Unprocessable Entity

#### confirm_preauthorization.ApiResponseFor200
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
**currency** | str,  | str,  |  | [optional] 
**order** | str,  | str,  |  | [optional] 
**amount** | str,  | str,  |  | [optional] 
**authCode** | str,  | str,  | Authorization bank code of the transaction (required to execute a return). | [optional] 
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### confirm_preauthorization.ApiResponseFor422
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
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_preauthorization**
<a name="create_preauthorization"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_preauthorization(paycomet_api_token)

Create preauthorization

create_preauthorization

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import preauthorizations_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = preauthorizations_api.PreauthorizationsApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    try:
        # Create preauthorization
        api_response = api_instance.create_preauthorization(
            header_params=header_params,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling PreauthorizationsApi->create_preauthorization: %s\n" % e)

    # example passing only optional values
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    body = dict(
        payment=dict(
            terminal=1,
            order="PAY987654321",
            amount="202",
            currency="EUR",
            original_ip="127.0.0.1",
            method_id="1",
            secure=1,
            scoring="0",
            product_description="Description of random product",
            merchant_descriptor="My custom name",
            user_interaction=1,
            trx_type="trx_type_example",
            sca_exception="sca_exception_example",
            url_ok="https://www.mycustom.url/ok",
            url_ko="https://www.mycustom.url/ko",
            notify_direct_payment=1,
            merchant_data=dict(
                customer=dict(
                    id="customer123",
                    name="John",
                    surname="Doe",
                    email="jdoe@myemail.com",
                    home_phone=dict(
                        cc=34,
                        subscriber=91820332211,
                    ),
                    mobile_phone=dict(
                        cc=34,
                        subscriber=640456999,
                    ),
                    work_phone=dict(
                        cc=34,
                        subscriber=913984300,
                    ),
                    first_buy="first_buy_example",
                ),
                shipping=dict(
                    ship_addr_city="Springfield",
                    ship_addr_country="840",
                    ship_addr_line1="742 Evergreen Terrace",
                    ship_addr_line2="ship_addr_line2_example",
                    ship_addr_line3="ship_addr_line3_example",
                    ship_addr_post_code="89011",
                    ship_addr_state="Z",
                ),
                billing=dict(
                    bill_addr_city="Scranton",
                    bill_addr_country="840",
                    bill_addr_line1="1725 Slough Avenue",
                    bill_addr_line2="bill_addr_line2_example",
                    bill_addr_line3="bill_addr_line3_example",
                    bill_addr_post_code="18501",
                    bill_addr_state="Z",
                ),
                acct_id="acct_id_example",
                acct_info=dict(
                    ch_acc_age_ind="5",
                    ch_acc_change="20200704",
                    ch_acc_change_ind="3",
                    ch_acc_date="20191225",
                    ch_acc_pw_change="20191225",
                    ch_acc_pw_change_ind="1",
                    nb_purchase_account=2,
                    provision_attempts_day=0,
                    txn_activity_day="0",
                    txn_activity_year="3",
                    payment_acc_age="20191228",
                    payment_acc_ind="5",
                    ship_address_usage="20191228",
                    ship_address_usage_ind="3",
                    ship_name_indicator="1",
                    suspicious_acc_activity="1",
                ),
                merchant_risk_indicator=dict(
                    delivery_email_address="jdoe@myemail.com",
                    delivery_timeframe="4",
                    gift_card_amount="123",
                    gift_card_count=1,
                    gift_card_curr="840",
                    pre_order_date="20201001",
                    pre_order_purchase_ind="1",
                    reorder_items_ind="1",
                    ship_indicator="3",
                ),
                three_ds_requestor_authentication_info=dict(
                    three_ds_req_auth_data="three_ds_req_auth_data_example",
                    three_ds_req_auth_method="1",
                    three_ds_req_auth_timestamp="20200612113044",
                ),
                shopping_cart=[
                    dict(
                        sku="CODE-01",
                        quantity=1,
                        unit_price=295,
                        name="Product 01",
                        category="Internet gift card",
                        article_type=8,
                    )
                ],
                addr_match="Y",
                purchase_instal_data=1,
                recurring_expiry="20200612",
                recurring_frequency="4",
            ),
            id_user=12345678,
            token_user="WHlSWmVDdzVQeUZ",
            deferred=0,
        ),
    )
    try:
        # Create preauthorization
        api_response = api_instance.create_preauthorization(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling PreauthorizationsApi->create_preauthorization: %s\n" % e)
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
**idUser** | decimal.Decimal, int,  | decimal.Decimal,  | Identification of user card given by PAYCOMET. Mandatory if is a card payment. | 
**amount** | str,  | str,  | Amount of the operation in number format. 1.00 EURO &#x3D; 100, 4.50 EUROS &#x3D; 450... | 
**methodId** | str,  | str,  | PAYCOMET payment method ID. 1 is for card. | 
**currency** | str,  | str,  | Currency of the transaction.  | 
**terminal** | decimal.Decimal, int,  | decimal.Decimal,  | Product or terminal Id. | 
**tokenUser** | str,  | str,  | Identification of user card given by PAYCOMET. Mandatory if is a card payment. | 
**secure** | decimal.Decimal, int,  | decimal.Decimal,  | 0 or 1. Indicates if the transaction is secure. | 
**order** | str,  | str,  | Unique reference for merchant&#x27;s purchase | 
**originalIp** | str,  | str,  | IP Address of the customer that initiated the payment transaction | 
**scoring** | str,  | str,  | Risk scoring value from 0 to 100. | [optional] 
**productDescription** | str,  | str,  | Description of the product sold. | [optional] 
**merchantDescriptor** | str,  | str,  | Allows the business to send a text up to 25 characters that will be printed on the customer invoice. Limited to simple characters, no accents or special characters. | [optional] 
**userInteraction** | decimal.Decimal, int,  | decimal.Decimal,  | Indicates wether the business can interact with the customer | [optional] 
**TRXType** | str,  | str,  | Obligatory only if an MIT exception has been selected in scaException | [optional] 
**scaException** | str,  | str,  | TYPE OF EXCEPTION TO THE SECURE PAYMENT. If not specified, PAYCOMET will try to assign it the most appropriate possible | [optional] 
**urlOk** | str,  | str,  | Url where the customer will be redirected after finishing a correct transaction. (Max 255 characters) | [optional] 
**urlKo** | str,  | str,  | Url where the customer will be redirected after finishing a failed transaction. (Max 255 characters) | [optional] 
**notifyDirectPayment** | decimal.Decimal, int,  | decimal.Decimal,  | Configurate POST notification of the operation result in frictionless payment (possible values: 1 - force notify, 2 - not notify). It will notify if is not informed | [optional] 
**[merchantData](#merchantData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Client authentication information. The more information is provided in this field, the more likely the authorization of the operation will be without requiring additional authentication. For this reason, it is recommended to send as much information as possible. | [optional] 
**deferred** | decimal.Decimal, int,  | decimal.Decimal,  | Identify the preauthorization as deferred | [optional] if omitted the server will use the default value of 0
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# merchantData

Client authentication information. The more information is provided in this field, the more likely the authorization of the operation will be without requiring additional authentication. For this reason, it is recommended to send as much information as possible.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Client authentication information. The more information is provided in this field, the more likely the authorization of the operation will be without requiring additional authentication. For this reason, it is recommended to send as much information as possible. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[customer](#customer)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[shipping](#shipping)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with shipping address related information. | [optional] 
**[billing](#billing)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**acctID** | str,  | str,  | Additional information you want to send to identify the account | [optional] 
**[acctInfo](#acctInfo)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with additional information on the user account at the store | [optional] 
**[merchantRiskIndicator](#merchantRiskIndicator)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with additional information of the business representing the evaluation of the level of risk of fraud for authentication. The delivery of this information is highly recommended | [optional] 
**[threeDSRequestorAuthenticationInfo](#threeDSRequestorAuthenticationInfo)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with additional information on how the client was authenticated at the start of the session in the business account | [optional] 
**[shoppingCart](#shoppingCart)** | list, tuple,  | tuple,  |  | [optional] 
**addrMatch** | str,  | str,  | Indicates whether the delivery address is the same as the invoice address. Y &#x3D; The delivery address is the same as the invoicing address, N &#x3D; The delivery and invoice addresses are different | [optional] 
**purchaseInstalData** | decimal.Decimal, int,  | decimal.Decimal,  | Mandatory for Instalment operations (MERCHANT_TRX_TYPE &#x3D; I). Indicates the maximum number of deferred payment authorizations. Accepted values: The value must be greater than 1 | [optional] 
**recurringExpiry** | str,  | str,  | Mandatory for Recurring and Instalment operations (MERCHANT_TRX_TYPE &#x3D; I or R). The date from which there will be no more authorizations. Accepted format: YYYYMMDD | [optional] 
**recurringFrequency** | str,  | str,  | Mandatory for Recurring and Instalment operations (MERCHANT_TRX_TYPE &#x3D; I or R). Indicates the minimum number of days between authorizations | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# customer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Store customer identifier | [optional] 
**name** | str,  | str,  | Name of customer | [optional] 
**surname** | str,  | str,  | Surname of customer | [optional] 
**email** | str,  | str,  | Email of customer | [optional] 
**[homePhone](#homePhone)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with user home phone data | [optional] 
**[mobilePhone](#mobilePhone)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with user mobile phone data | [optional] 
**[workPhone](#workPhone)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with user work phone data | [optional] 
**firstBuy** | str,  | str,  | Indicates whether the user has already bought in this business (&#x27;si&#x27; if has made a operation, &#x27;no&#x27; in opposite scenario) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# homePhone

Node with user home phone data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with user home phone data | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cc** | decimal.Decimal, int,  | decimal.Decimal,  | International dialling code of the customer’s home telephone number | [optional] 
**subscriber** | decimal.Decimal, int,  | decimal.Decimal,  | Customer’s home telephone number | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mobilePhone

Node with user mobile phone data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with user mobile phone data | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cc** | decimal.Decimal, int,  | decimal.Decimal,  | International dialling code of the customer’s mobile telephone number | [optional] 
**subscriber** | decimal.Decimal, int,  | decimal.Decimal,  | Customer’s mobile telephone number | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# workPhone

Node with user work phone data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with user work phone data | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cc** | decimal.Decimal, int,  | decimal.Decimal,  | International dialling code of the customer’s work telephone number | [optional] 
**subscriber** | decimal.Decimal, int,  | decimal.Decimal,  | Customer’s work telephone number | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# shipping

Node with shipping address related information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with shipping address related information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**shipAddrCity** | str,  | str,  | City of delivery address. | [optional] 
**shipAddrCountry** | str,  | str,  | Numerical code (ISO 3166-1) of the country of the delivery address | [optional] 
**shipAddrLine1** | str,  | str,  | Delivery address, line 1 | [optional] 
**shipAddrLine2** | str,  | str,  | Delivery address, line 2 | [optional] 
**shipAddrLine3** | str,  | str,  | Delivery address, line 3 | [optional] 
**shipAddrPostCode** | str,  | str,  | Post code of the delivery address | [optional] 
**shipAddrState** | str,  | str,  | State or province of the delivery address. Must comply with ISO 3166-2. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# billing

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**billAddrCity** | str,  | str,  | City of delivery address. | [optional] 
**billAddrCountry** | str,  | str,  | Numerical code (ISO 3166-1) of the country of the delivery address | [optional] 
**billAddrLine1** | str,  | str,  | Delivery address, line 1 | [optional] 
**billAddrLine2** | str,  | str,  | Delivery address, line 2 | [optional] 
**billAddrLine3** | str,  | str,  | Delivery address, line 3 | [optional] 
**billAddrPostCode** | str,  | str,  | Post code of the delivery address | [optional] 
**billAddrState** | str,  | str,  | State or province of the delivery address. Must comply with ISO 3166-2. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# acctInfo

Node with additional information on the user account at the store

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with additional information on the user account at the store | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**chAccAgeInd** | str,  | str,  | Period of time that the customer has had the account at the business. Possible values: 01 &#x3D; No account (checkout as guest), 02 &#x3D; Created in this transaction, 03 &#x3D; Under 30 days, 04 &#x3D; Between 30 and 60 days, 05 &#x3D; Over 60 days | [optional] 
**chAccChange** | str,  | str,  | Date on which the user account with the business was last modified, including the invoice or delivery address, the new payment account or new added users. Date format: YYYYMMDD | [optional] 
**chAccChangeInd** | str,  | str,  | Period of time passed since the payment user’s account with the business was last modified, including the invoice or delivery address, the new payment account or new added users. Accepted values: 01 &#x3D; Modified in this transaction, 02 &#x3D; Under 30 days, 03 &#x3D; 30-60 days, 04 &#x3D; Over 60 days | [optional] 
**chAccDate** | str,  | str,  | Date on which the payment user opened the account with the business. Date format: YYYYMMDD | [optional] 
**chAccPwChange** | str,  | str,  | Date on which the payment user changed the password of their account with the business, or reset their account. Date format: YYYYMMDD | [optional] 
**chAccPwChangeInd** | str,  | str,  | Indicates the period of time since the payment user’s account with the business changed its password or was reset. Accepted values: 01 &#x3D; No changes, 02 &#x3D; Changed during this transaction, 03 &#x3D; Under 30 days, 04 &#x3D; Between 30 and 60 days, 05 &#x3D; Over 60 days | [optional] 
**nbPurchaseAccount** | decimal.Decimal, int,  | decimal.Decimal,  | Number of purchases with this account during the last six months | [optional] 
**provisionAttemptsDay** | decimal.Decimal, int,  | decimal.Decimal,  | Number of attempts to add a card in the last 24 hours | [optional] 
**txnActivityDay** | str,  | str,  | Number of transactions (successful and abandoned) for this account with the business in all payment accounts in the last 24 hours | [optional] 
**txnActivityYear** | str,  | str,  | Number of transactions (successful and abandoned) for this account of the payment user with the business in all payment accounts of the last year | [optional] 
**paymentAccAge** | str,  | str,  | Date on which the payment account was registered on the payment user’s account with the business. | [optional] 
**paymentAccInd** | str,  | str,  | Indicates the period of time which the payment account was registered on the payment user’s account with the business. Accepted values: 01 &#x3D; No account (checkout as guest), 02 &#x3D; During this transaction, 03 &#x3D; Under 30 days, 04 &#x3D; Between 30 and 60 days, 05 &#x3D; Over 60 days | [optional] 
**shipAddressUsage** | str,  | str,  | Date on which the delivery address used for this transaction was used for the first time with the business. Date format: YYYYMMDD | [optional] 
**shipAddressUsageInd** | str,  | str,  | Indicates when the delivery address used for this transaction was used for the first time with the business. Accepted values: 01 &#x3D; This transaction, 02 &#x3D; Under 30 days, 03 &#x3D; Between 30 and 60 days, 04 &#x3D; Over 60 days | [optional] 
**shipNameIndicator** | str,  | str,  | Indicates whether the name of the payment user on the account is identical to the delivery name used for this transaction. Accepted values: 01 &#x3D; Name on the account identical to the delivery name, 02 &#x3D; Name on the account different from the delivery name | [optional] 
**suspiciousAccActivity** | str,  | str,  | Indicates whether the business has experienced suspicious activity (including previous fraud) on the payment user’s account. Accepted values: 01 &#x3D; No record of suspicious activity, 02 &#x3D; Record of suspicious activity | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# merchantRiskIndicator

Node with additional information of the business representing the evaluation of the level of risk of fraud for authentication. The delivery of this information is highly recommended

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with additional information of the business representing the evaluation of the level of risk of fraud for authentication. The delivery of this information is highly recommended | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**deliveryEmailAddress** | str,  | str,  | For electronic delivery, the email address to which the goods were delivered | [optional] 
**deliveryTimeframe** | str,  | str,  | Indicates the delivery period of the goods. Accepted values: 01 &#x3D; Electronic delivery, 02 &#x3D; Delivery on the same day, 03 &#x3D; 24 hour delivery, 04 &#x3D; Delivery in 2 days or more | [optional] 
**giftCardAmount** | str,  | str,  | For purchases from prepaid cards or gift cards, the total amount of the purchase in major units (for example, USD 123.45 is 123) | [optional] 
**giftCardCount** | decimal.Decimal, int,  | decimal.Decimal,  | For purchases from prepaid cards or gift cards, total count of prepaid cards or gift cards/gift codes purchased | [optional] 
**giftCardCurr** | str,  | str,  | For the purchase of prepaid/gift cards, code ISO-4217 of currency of the card | [optional] 
**preOrderDate** | str,  | str,  | For a pre-ordered purchase, the forecast availability date of the goods. Date format: YYYYMMDD | [optional] 
**preOrderPurchaseInd** | str,  | str,  | Indicates whether the customer makes an order with availability or future launch date. Accepted values: 01 &#x3D; Goods available, 02 &#x3D; Future availability | [optional] 
**reorderItemsInd** | str,  | str,  | Indicates whether the card is reordering previously purchased goods. Accepted values: 01 &#x3D; First time purchased, 02 &#x3D; Previously purchased | [optional] 
**shipIndicator** | str,  | str,  | Indicates the delivery method selected for the transaction. Businesses must select the delivery indicator code which more precisely describes the specific transaction of the payment user, not their general commercial activity. If one or more items are included in the sale, use the delivery Indicator code for physical goods, or if all products are digital, use the delivery Indicator code which describes the most expensive item. Accepted values: 01 &#x3D; Delivery to the invoice address of the customer, 02 &#x3D; Delivery to another verified address of the client, 03 &#x3D; Delivery to an address other than that of the customer’s invoice address, 04 &#x3D; Delivery to the store or collection at premises (the address of the store will be stored in the delivery address fields), 05 &#x3D; Digital goods (includes online services, electronic gift cards and discount coupons), 06 &#x3D; Tickets for events and trips, without delivery, 07 &#x3D; Other (for example, games, digital services without delivery, subscriptions to online services, etc.) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# threeDSRequestorAuthenticationInfo

Node with additional information on how the client was authenticated at the start of the session in the business account

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with additional information on how the client was authenticated at the start of the session in the business account | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**threeDSReqAuthData** | str,  | str,  | Data which documents and supports a specific authentication process. | [optional] 
**threeDSReqAuthMethod** | str,  | str,  | Mechanism used by the customer to authenticate themselves in the business. Accepted values: 01 &#x3D; Without 3DS authentication (for example, customer identified as guest), 02 &#x3D; Logged onto the account on the ACS using the credentials of the ACS, 03 &#x3D; Logged onto the account on the ACS using an affiliate identifier, 04 &#x3D; Logged onto the account on the ACS using the credentials of the issuer, 05 &#x3D; Logged onto the account on the ACS using a third party authentication, 06 &#x3D; Logged onto the account on the ACS using a FIDO authenticator | [optional] 
**threeDSReqAuthTimestamp** | str,  | str,  | Date and time UTC of the authentication. Date format: YYYYMMDDHHMM | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# shoppingCart

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with the list of items purchased in the store | 

# items

Node with the list of items purchased in the store

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with the list of items purchased in the store | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sku** | str,  | str,  | Product identifier | [optional] 
**quantity** | decimal.Decimal, int,  | decimal.Decimal,  | Units of product purchased | [optional] 
**unitPrice** | decimal.Decimal, int,  | decimal.Decimal,  | unit amount of each product in integer format. 1.00 EURO &#x3D; 100, 4.50 EUROS &#x3D; 450, etc. | [optional] 
**name** | str,  | str,  | Product name | [optional] 
**category** | str,  | str,  | Product category | [optional] 
**articleType** | decimal.Decimal, int,  | decimal.Decimal,  | article type (4 &#x3D; Discount, 5 &#x3D; Physical, 6 &#x3D; Shipping_fee, 7 &#x3D; Sales_tax, 8 &#x3D; Digital, 9 &#x3D; Gift_card, 10 &#x3D; Store_credit, 11 &#x3D; Surcharge) | [optional] 
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
200 | [ApiResponseFor200](#create_preauthorization.ApiResponseFor200) | OK
422 | [ApiResponseFor422](#create_preauthorization.ApiResponseFor422) | Unprocessable Entity

#### create_preauthorization.ApiResponseFor200
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
**challengeUrl** | str,  | str,  |  | [optional] 
**idUser** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**tokenUser** | str,  | str,  |  | [optional] 
**cardCountry** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### create_preauthorization.ApiResponseFor422
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

# **create_preauthorization_rtoken**
<a name="create_preauthorization_rtoken"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_preauthorization_rtoken()

Creates a preauthorization by reference

Creates a preauthorization with reference.

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import preauthorizations_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = preauthorizations_api.PreauthorizationsApi(api_client)

    # example passing only optional values
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    body = dict(
        payment=dict(
            terminal=1,
            order="PAY987654321",
            amount="202",
            currency="EUR",
            method_id="1",
            original_ip="127.0.0.1",
            secure=1,
            merchant_identifier="520adffce7d9f5ea6bea5b03b837fd3f29817ef7",
            merchant_group="WHlSWmVDdzVQeUZ",
            scoring="scoring_example",
            product_description="Random product",
            merchant_descriptor="merchant_descriptor_example",
            user_interaction=1,
            trx_type="trx_type_example",
            sca_exception="sca_exception_example",
            url_ok="https://www.mycustom.url/ok",
            url_ko="https://www.mycustom.url/ko",
            notify_direct_payment=1,
            merchant_data=dict(
                customer=dict(
                    id="customer123",
                    name="John",
                    surname="Doe",
                    email="jdoe@myemail.com",
                    home_phone=dict(
                        cc=34,
                        subscriber=91820332211,
                    ),
                    mobile_phone=dict(
                        cc=34,
                        subscriber=640456999,
                    ),
                    work_phone=dict(
                        cc=34,
                        subscriber=913984300,
                    ),
                    first_buy="first_buy_example",
                ),
                shipping=dict(
                    ship_addr_city="Springfield",
                    ship_addr_country="840",
                    ship_addr_line1="742 Evergreen Terrace",
                    ship_addr_line2="ship_addr_line2_example",
                    ship_addr_line3="ship_addr_line3_example",
                    ship_addr_post_code="89011",
                    ship_addr_state="Z",
                ),
                billing=dict(
                    bill_addr_city="Scranton",
                    bill_addr_country="840",
                    bill_addr_line1="1725 Slough Avenue",
                    bill_addr_line2="bill_addr_line2_example",
                    bill_addr_line3="bill_addr_line3_example",
                    bill_addr_post_code="18501",
                    bill_addr_state="Z",
                ),
                acct_id="acct_id_example",
                acct_info=dict(
                    ch_acc_age_ind="5",
                    ch_acc_change="20200704",
                    ch_acc_change_ind="3",
                    ch_acc_date="20191225",
                    ch_acc_pw_change="20191225",
                    ch_acc_pw_change_ind="1",
                    nb_purchase_account=2,
                    provision_attempts_day=0,
                    txn_activity_day="0",
                    txn_activity_year="3",
                    payment_acc_age="20191228",
                    payment_acc_ind="5",
                    ship_address_usage="20191228",
                    ship_address_usage_ind="3",
                    ship_name_indicator="1",
                    suspicious_acc_activity="1",
                ),
                merchant_risk_indicator=dict(
                    delivery_email_address="jdoe@myemail.com",
                    delivery_timeframe="4",
                    gift_card_amount="123",
                    gift_card_count=1,
                    gift_card_curr="840",
                    pre_order_date="20201001",
                    pre_order_purchase_ind="1",
                    reorder_items_ind="1",
                    ship_indicator="3",
                ),
                three_ds_requestor_authentication_info=dict(
                    three_ds_req_auth_data="three_ds_req_auth_data_example",
                    three_ds_req_auth_method="1",
                    three_ds_req_auth_timestamp="20200612113044",
                ),
                shopping_cart=[
                    dict(
                        sku="CODE-01",
                        quantity=1,
                        unit_price=295,
                        name="Product 01",
                        category="Internet gift card",
                        article_type=8,
                    )
                ],
                addr_match="Y",
                purchase_instal_data=1,
                recurring_expiry="20200612",
                recurring_frequency="4",
            ),
        ),
    )
    try:
        # Creates a preauthorization by reference
        api_response = api_instance.create_preauthorization_rtoken(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling PreauthorizationsApi->create_preauthorization_rtoken: %s\n" % e)
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
**merchantIdentifier** | str,  | str,  | External reference of card | 
**amount** | str,  | str,  | Amount of the operation in number format. 1.00 EURO &#x3D; 100, 4.50 EUROS &#x3D; 450... | 
**methodId** | str,  | str,  | PAYCOMET payment method ID. 1 is for card. | 
**currency** | str,  | str,  | Currency of the transaction.  | 
**terminal** | decimal.Decimal, int,  | decimal.Decimal,  | Product or terminal Id. | 
**secure** | decimal.Decimal, int,  | decimal.Decimal,  | 0 or 1. Indicates if the transaction is secure. | 
**order** | str,  | str,  | Unique reference for merchant&#x27;s purchase | 
**originalIp** | str,  | str,  | IP Address of the customer that initiated the payment transaction | 
**merchantGroup** | str,  | str,  | Identification of external merchant group | [optional] 
**scoring** | str,  | str,  | Risk scoring value from 0 to 100. | [optional] 
**productDescription** | str,  | str,  | Description of the product sold. | [optional] 
**merchantDescriptor** | str,  | str,  | Allows the business to send a text up to 25 characters that will be printed on the customer invoice. Limited to simple characters, no accents or special characters. | [optional] 
**userInteraction** | decimal.Decimal, int,  | decimal.Decimal,  | Indicates wether the business can interact with the customer | [optional] 
**trxType** | str,  | str,  | Obligatory only if an MIT exception has been selected in scaException | [optional] 
**scaException** | str,  | str,  | TYPE OF EXCEPTION TO THE SECURE PAYMENT. If not specified, PAYCOMET will try to assign it the most appropriate possible | [optional] 
**urlOk** | str,  | str,  | Url where the customer will be redirected after finishing a correct transaction. (Max 255 characters) | [optional] 
**urlKo** | str,  | str,  | Url where the customer will be redirected after finishing a failed transaction. (Max 255 characters) | [optional] 
**notifyDirectPayment** | decimal.Decimal, int,  | decimal.Decimal,  | Configurate POST notification of the operation result in frictionless payment (possible values: 1 - force notify, 2 - not notify). It will notify if is not informed | [optional] 
**[merchantData](#merchantData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Client authentication information. The more information is provided in this field, the more likely the authorization of the operation will be without requiring additional authentication. For this reason, it is recommended to send as much information as possible. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# merchantData

Client authentication information. The more information is provided in this field, the more likely the authorization of the operation will be without requiring additional authentication. For this reason, it is recommended to send as much information as possible.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Client authentication information. The more information is provided in this field, the more likely the authorization of the operation will be without requiring additional authentication. For this reason, it is recommended to send as much information as possible. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[customer](#customer)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[shipping](#shipping)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with shipping address related information. | [optional] 
**[billing](#billing)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**acctID** | str,  | str,  | Additional information you want to send to identify the account | [optional] 
**[acctInfo](#acctInfo)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with additional information on the user account at the store | [optional] 
**[merchantRiskIndicator](#merchantRiskIndicator)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with additional information of the business representing the evaluation of the level of risk of fraud for authentication. The delivery of this information is highly recommended | [optional] 
**[threeDSRequestorAuthenticationInfo](#threeDSRequestorAuthenticationInfo)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with additional information on how the client was authenticated at the start of the session in the business account | [optional] 
**[shoppingCart](#shoppingCart)** | list, tuple,  | tuple,  |  | [optional] 
**addrMatch** | str,  | str,  | Indicates whether the delivery address is the same as the invoice address. Y &#x3D; The delivery address is the same as the invoicing address, N &#x3D; The delivery and invoice addresses are different | [optional] 
**purchaseInstalData** | decimal.Decimal, int,  | decimal.Decimal,  | Mandatory for Instalment operations (MERCHANT_TRX_TYPE &#x3D; I). Indicates the maximum number of deferred payment authorizations. Accepted values: The value must be greater than 1 | [optional] 
**recurringExpiry** | str,  | str,  | Mandatory for Recurring and Instalment operations (MERCHANT_TRX_TYPE &#x3D; I or R). The date from which there will be no more authorizations. Accepted format: YYYYMMDD | [optional] 
**recurringFrequency** | str,  | str,  | Mandatory for Recurring and Instalment operations (MERCHANT_TRX_TYPE &#x3D; I or R). Indicates the minimum number of days between authorizations | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# customer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Store customer identifier | [optional] 
**name** | str,  | str,  | Name of customer | [optional] 
**surname** | str,  | str,  | Surname of customer | [optional] 
**email** | str,  | str,  | Email of customer | [optional] 
**[homePhone](#homePhone)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with user home phone data | [optional] 
**[mobilePhone](#mobilePhone)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with user mobile phone data | [optional] 
**[workPhone](#workPhone)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with user work phone data | [optional] 
**firstBuy** | str,  | str,  | Indicates whether the user has already bought in this business (&#x27;si&#x27; if has made a operation, &#x27;no&#x27; in opposite scenario) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# homePhone

Node with user home phone data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with user home phone data | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cc** | decimal.Decimal, int,  | decimal.Decimal,  | International dialling code of the customer’s home telephone number | [optional] 
**subscriber** | decimal.Decimal, int,  | decimal.Decimal,  | Customer’s home telephone number | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mobilePhone

Node with user mobile phone data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with user mobile phone data | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cc** | decimal.Decimal, int,  | decimal.Decimal,  | International dialling code of the customer’s mobile telephone number | [optional] 
**subscriber** | decimal.Decimal, int,  | decimal.Decimal,  | Customer’s mobile telephone number | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# workPhone

Node with user work phone data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with user work phone data | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cc** | decimal.Decimal, int,  | decimal.Decimal,  | International dialling code of the customer’s work telephone number | [optional] 
**subscriber** | decimal.Decimal, int,  | decimal.Decimal,  | Customer’s work telephone number | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# shipping

Node with shipping address related information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with shipping address related information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**shipAddrCity** | str,  | str,  | City of delivery address. | [optional] 
**shipAddrCountry** | str,  | str,  | Numerical code (ISO 3166-1) of the country of the delivery address | [optional] 
**shipAddrLine1** | str,  | str,  | Delivery address, line 1 | [optional] 
**shipAddrLine2** | str,  | str,  | Delivery address, line 2 | [optional] 
**shipAddrLine3** | str,  | str,  | Delivery address, line 3 | [optional] 
**shipAddrPostCode** | str,  | str,  | Post code of the delivery address | [optional] 
**shipAddrState** | str,  | str,  | State or province of the delivery address. Must comply with ISO 3166-2. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# billing

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**billAddrCity** | str,  | str,  | City of delivery address. | [optional] 
**billAddrCountry** | str,  | str,  | Numerical code (ISO 3166-1) of the country of the delivery address | [optional] 
**billAddrLine1** | str,  | str,  | Delivery address, line 1 | [optional] 
**billAddrLine2** | str,  | str,  | Delivery address, line 2 | [optional] 
**billAddrLine3** | str,  | str,  | Delivery address, line 3 | [optional] 
**billAddrPostCode** | str,  | str,  | Post code of the delivery address | [optional] 
**billAddrState** | str,  | str,  | State or province of the delivery address. Must comply with ISO 3166-2. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# acctInfo

Node with additional information on the user account at the store

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with additional information on the user account at the store | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**chAccAgeInd** | str,  | str,  | Period of time that the customer has had the account at the business. Possible values: 01 &#x3D; No account (checkout as guest), 02 &#x3D; Created in this transaction, 03 &#x3D; Under 30 days, 04 &#x3D; Between 30 and 60 days, 05 &#x3D; Over 60 days | [optional] 
**chAccChange** | str,  | str,  | Date on which the user account with the business was last modified, including the invoice or delivery address, the new payment account or new added users. Date format: YYYYMMDD | [optional] 
**chAccChangeInd** | str,  | str,  | Period of time passed since the payment user’s account with the business was last modified, including the invoice or delivery address, the new payment account or new added users. Accepted values: 01 &#x3D; Modified in this transaction, 02 &#x3D; Under 30 days, 03 &#x3D; 30-60 days, 04 &#x3D; Over 60 days | [optional] 
**chAccDate** | str,  | str,  | Date on which the payment user opened the account with the business. Date format: YYYYMMDD | [optional] 
**chAccPwChange** | str,  | str,  | Date on which the payment user changed the password of their account with the business, or reset their account. Date format: YYYYMMDD | [optional] 
**chAccPwChangeInd** | str,  | str,  | Indicates the period of time since the payment user’s account with the business changed its password or was reset. Accepted values: 01 &#x3D; No changes, 02 &#x3D; Changed during this transaction, 03 &#x3D; Under 30 days, 04 &#x3D; Between 30 and 60 days, 05 &#x3D; Over 60 days | [optional] 
**nbPurchaseAccount** | decimal.Decimal, int,  | decimal.Decimal,  | Number of purchases with this account during the last six months | [optional] 
**provisionAttemptsDay** | decimal.Decimal, int,  | decimal.Decimal,  | Number of attempts to add a card in the last 24 hours | [optional] 
**txnActivityDay** | str,  | str,  | Number of transactions (successful and abandoned) for this account with the business in all payment accounts in the last 24 hours | [optional] 
**txnActivityYear** | str,  | str,  | Number of transactions (successful and abandoned) for this account of the payment user with the business in all payment accounts of the last year | [optional] 
**paymentAccAge** | str,  | str,  | Date on which the payment account was registered on the payment user’s account with the business. | [optional] 
**paymentAccInd** | str,  | str,  | Indicates the period of time which the payment account was registered on the payment user’s account with the business. Accepted values: 01 &#x3D; No account (checkout as guest), 02 &#x3D; During this transaction, 03 &#x3D; Under 30 days, 04 &#x3D; Between 30 and 60 days, 05 &#x3D; Over 60 days | [optional] 
**shipAddressUsage** | str,  | str,  | Date on which the delivery address used for this transaction was used for the first time with the business. Date format: YYYYMMDD | [optional] 
**shipAddressUsageInd** | str,  | str,  | Indicates when the delivery address used for this transaction was used for the first time with the business. Accepted values: 01 &#x3D; This transaction, 02 &#x3D; Under 30 days, 03 &#x3D; Between 30 and 60 days, 04 &#x3D; Over 60 days | [optional] 
**shipNameIndicator** | str,  | str,  | Indicates whether the name of the payment user on the account is identical to the delivery name used for this transaction. Accepted values: 01 &#x3D; Name on the account identical to the delivery name, 02 &#x3D; Name on the account different from the delivery name | [optional] 
**suspiciousAccActivity** | str,  | str,  | Indicates whether the business has experienced suspicious activity (including previous fraud) on the payment user’s account. Accepted values: 01 &#x3D; No record of suspicious activity, 02 &#x3D; Record of suspicious activity | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# merchantRiskIndicator

Node with additional information of the business representing the evaluation of the level of risk of fraud for authentication. The delivery of this information is highly recommended

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with additional information of the business representing the evaluation of the level of risk of fraud for authentication. The delivery of this information is highly recommended | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**deliveryEmailAddress** | str,  | str,  | For electronic delivery, the email address to which the goods were delivered | [optional] 
**deliveryTimeframe** | str,  | str,  | Indicates the delivery period of the goods. Accepted values: 01 &#x3D; Electronic delivery, 02 &#x3D; Delivery on the same day, 03 &#x3D; 24 hour delivery, 04 &#x3D; Delivery in 2 days or more | [optional] 
**giftCardAmount** | str,  | str,  | For purchases from prepaid cards or gift cards, the total amount of the purchase in major units (for example, USD 123.45 is 123) | [optional] 
**giftCardCount** | decimal.Decimal, int,  | decimal.Decimal,  | For purchases from prepaid cards or gift cards, total count of prepaid cards or gift cards/gift codes purchased | [optional] 
**giftCardCurr** | str,  | str,  | For the purchase of prepaid/gift cards, code ISO-4217 of currency of the card | [optional] 
**preOrderDate** | str,  | str,  | For a pre-ordered purchase, the forecast availability date of the goods. Date format: YYYYMMDD | [optional] 
**preOrderPurchaseInd** | str,  | str,  | Indicates whether the customer makes an order with availability or future launch date. Accepted values: 01 &#x3D; Goods available, 02 &#x3D; Future availability | [optional] 
**reorderItemsInd** | str,  | str,  | Indicates whether the card is reordering previously purchased goods. Accepted values: 01 &#x3D; First time purchased, 02 &#x3D; Previously purchased | [optional] 
**shipIndicator** | str,  | str,  | Indicates the delivery method selected for the transaction. Businesses must select the delivery indicator code which more precisely describes the specific transaction of the payment user, not their general commercial activity. If one or more items are included in the sale, use the delivery Indicator code for physical goods, or if all products are digital, use the delivery Indicator code which describes the most expensive item. Accepted values: 01 &#x3D; Delivery to the invoice address of the customer, 02 &#x3D; Delivery to another verified address of the client, 03 &#x3D; Delivery to an address other than that of the customer’s invoice address, 04 &#x3D; Delivery to the store or collection at premises (the address of the store will be stored in the delivery address fields), 05 &#x3D; Digital goods (includes online services, electronic gift cards and discount coupons), 06 &#x3D; Tickets for events and trips, without delivery, 07 &#x3D; Other (for example, games, digital services without delivery, subscriptions to online services, etc.) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# threeDSRequestorAuthenticationInfo

Node with additional information on how the client was authenticated at the start of the session in the business account

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with additional information on how the client was authenticated at the start of the session in the business account | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**threeDSReqAuthData** | str,  | str,  | Data which documents and supports a specific authentication process. | [optional] 
**threeDSReqAuthMethod** | str,  | str,  | Mechanism used by the customer to authenticate themselves in the business. Accepted values: 01 &#x3D; Without 3DS authentication (for example, customer identified as guest), 02 &#x3D; Logged onto the account on the ACS using the credentials of the ACS, 03 &#x3D; Logged onto the account on the ACS using an affiliate identifier, 04 &#x3D; Logged onto the account on the ACS using the credentials of the issuer, 05 &#x3D; Logged onto the account on the ACS using a third party authentication, 06 &#x3D; Logged onto the account on the ACS using a FIDO authenticator | [optional] 
**threeDSReqAuthTimestamp** | str,  | str,  | Date and time UTC of the authentication. Date format: YYYYMMDDHHMM | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# shoppingCart

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with the list of items purchased in the store | 

# items

Node with the list of items purchased in the store

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with the list of items purchased in the store | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sku** | str,  | str,  | Product identifier | [optional] 
**quantity** | decimal.Decimal, int,  | decimal.Decimal,  | Units of product purchased | [optional] 
**unitPrice** | decimal.Decimal, int,  | decimal.Decimal,  | unit amount of each product in integer format. 1.00 EURO &#x3D; 100, 4.50 EUROS &#x3D; 450, etc. | [optional] 
**name** | str,  | str,  | Product name | [optional] 
**category** | str,  | str,  | Product category | [optional] 
**articleType** | decimal.Decimal, int,  | decimal.Decimal,  | article type (4 &#x3D; Discount, 5 &#x3D; Physical, 6 &#x3D; Shipping_fee, 7 &#x3D; Sales_tax, 8 &#x3D; Digital, 9 &#x3D; Gift_card, 10 &#x3D; Store_credit, 11 &#x3D; Surcharge) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
PAYCOMET-API-TOKEN | PAYCOMETAPITOKENSchema | | optional

# PAYCOMETAPITOKENSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_preauthorization_rtoken.ApiResponseFor200) | OK
422 | [ApiResponseFor422](#create_preauthorization_rtoken.ApiResponseFor422) | Unprocessable Entity

#### create_preauthorization_rtoken.ApiResponseFor200
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
**challengeUrl** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### create_preauthorization_rtoken.ApiResponseFor422
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

