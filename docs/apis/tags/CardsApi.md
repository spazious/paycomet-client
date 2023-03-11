<a name="__pageTop"></a>
# paycomet_client.apis.tags.cards_api.CardsApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](#add_user) | **post** /v1/cards | Tokenizes a card. Either card number and CVC2 or jetToken are required. For you to send directly the card data you should be PCI certified or the accepting the requirement to submit quarterly SAQ-AEP and get ASV scans. For most users is strongly recommended getting the jetToken with JETIFRAME or using GET integration to register the cards instead of REST.
[**edit_user**](#edit_user) | **post** /v1/cards/edit | Changes the expiry date, cvc2 or both
[**info_user**](#info_user) | **post** /v1/cards/info | Get card info
[**physical_add_card**](#physical_add_card) | **post** /v1/cards/physical | Tokenize a card by physical encrypted data
[**physical_edit_card**](#physical_edit_card) | **post** /v1/cards/physical/edit | Edit a card entered by physical encrypted data
[**remove_user**](#remove_user) | **post** /v1/cards/delete | Removes a card

# **add_user**
<a name="add_user"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} add_user()

Tokenizes a card. Either card number and CVC2 or jetToken are required. For you to send directly the card data you should be PCI certified or the accepting the requirement to submit quarterly SAQ-AEP and get ASV scans. For most users is strongly recommended getting the jetToken with JETIFRAME or using GET integration to register the cards instead of REST.

This method supposes the registration of the card in PAYCOMET, it is not valid for subsequent charges with the exception of MIT. To register the card against the processor for subsequent recurring charges, it is necessary to charge for a secure environment, regardless of the amount.

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import cards_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cards_api.CardsApi(api_client)

    # example passing only optional values
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    body = dict(
        terminal=1,
        cvc2="012",
        jet_token="rApGWqLdH8ExOyNiLukyMMs78PZRzDm5",
        expiry_year="23",
        expiry_month="11",
        pan="491801916000002",
        order="PAY987654321",
        product_description="Random product",
        language="fr",
        notify=1,
        card_holder_name="Michael Scott",
        secure_authentication=dict(
            cavv="AAMCCDIFUQSAMPLEAl4A5da8DRYw=",
            txid="4a9ertc3-c05b-4fc9-43ff-40s4mp1ea213e",
            eci="05",
            three_ds_server_trans_id="A999000999",
            authenticacion_value="e9aef4ef-467c-9173-a73a-2d1s71ffak3e",
            ds_trans_id="591724c2-d995-c05b-b49f-e194es8mp13a",
            three_ds_version="2.2.0",
            authentication_flow="F",
        ),
    )
    try:
        # Tokenizes a card. Either card number and CVC2 or jetToken are required. For you to send directly the card data you should be PCI certified or the accepting the requirement to submit quarterly SAQ-AEP and get ASV scans. For most users is strongly recommended getting the jetToken with JETIFRAME or using GET integration to register the cards instead of REST.
        api_response = api_instance.add_user(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling CardsApi->add_user: %s\n" % e)
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
**terminal** | decimal.Decimal, int,  | decimal.Decimal,  | Product or terminal Id. | 
**cvc2** | str,  | str,  | cvc2. Mandatory if no JetToken provided | [optional] 
**jetToken** | str,  | str,  | Temporary token provided from PAYCOMET. Mandatory if no card provided. | [optional] 
**expiryYear** | str,  | str,  | Expiry year.  Mandatory if no JetToken provided | [optional] 
**expiryMonth** | str,  | str,  | Expiry month.  Mandatory if no JetToken provided. | [optional] 
**pan** | str,  | str,  | Card number. Mandatory if no JetToken provided | [optional] 
**order** | str,  | str,  | Reference, will be included in callback. | [optional] 
**productDescription** | str,  | str,  | Concept, will be included in callback. | [optional] 
**language** | str,  | str,  | Language for callback translation. | [optional] if omitted the server will use the default value of "es"
**notify** | decimal.Decimal, int,  | decimal.Decimal,  | Configure POST notification of the card tokenization result (possible values: 1 - force notify, 2 - not notify). Default product value will be used if notify is not informed | [optional] 
**cardHolderName** | str,  | str,  | Card holder name | [optional] 
**[secureAuthentication](#secureAuthentication)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with user secure authentication details of a previous transaction to avoid future ACS. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# secureAuthentication

Node with user secure authentication details of a previous transaction to avoid future ACS.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Node with user secure authentication details of a previous transaction to avoid future ACS. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**CAVV** | str,  | str,  | CAVV value included in a 1.0.2 version ACS card emisor | [optional] 
**TXID** | str,  | str,  | XID value included in a 1.0.2 version ACS card emisor | [optional] 
**ECI** | str,  | str,  | ECI value included in a transaction info of the ACS card emisor | [optional] 
**threeDSServerTransID** | str,  | str,  | Transation unique identifier included in a transaction info of the ACS card emisor | [optional] 
**authenticacionValue** | str,  | str,  | Authenticacion value included in a transaction info of the ACS card emisor | [optional] 
**dsTransID** | str,  | str,  | Unique transaction identifier assigned by the DS | [optional] 
**threeDSVersion** | str,  | str,  | Version of the transaction of the ACS card emisor | [optional] 
**authenticationFlow** | str,  | str,  | Authentication field to indicate the flow (C: challenge or F: frictionless) given in the transaction | [optional] 
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
200 | [ApiResponseFor200](#add_user.ApiResponseFor200) | Created
422 | [ApiResponseFor422](#add_user.ApiResponseFor422) | Unprocessable Entity

#### add_user.ApiResponseFor200
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
**idUser** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**tokenUser** | str,  | str,  |  | [optional] 
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### add_user.ApiResponseFor422
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

# **edit_user**
<a name="edit_user"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_user()

Changes the expiry date, cvc2 or both

edit_user

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import cards_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cards_api.CardsApi(api_client)

    # example passing only optional values
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    body = dict(
        terminal=1,
        id_user=12345678,
        token_user="WHlSWmVDdzVQeUZ",
        cvc2="012",
        expiry_year="25",
        expiry_month="11",
    )
    try:
        # Changes the expiry date, cvc2 or both
        api_response = api_instance.edit_user(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling CardsApi->edit_user: %s\n" % e)
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
**idUser** | decimal.Decimal, int,  | decimal.Decimal,  | Identification of user card given by PAYCOMET. Mandatory if is a card payment. | 
**expiryMonth** | str,  | str,  | Expiry month.  Mandatory if no JetToken provided. | 
**expiryYear** | str,  | str,  | Expiry year.   Mandatory if no JetToken provided. | 
**terminal** | decimal.Decimal, int,  | decimal.Decimal,  | Product or terminal Id. | 
**tokenUser** | str,  | str,  | Identification of user card given by PAYCOMET. Mandatory if is a card payment. | 
**cvc2** | str,  | str,  | cvc2. Mandatory if no JetToken provided | [optional] 
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
200 | [ApiResponseFor200](#edit_user.ApiResponseFor200) | Edited
422 | [ApiResponseFor422](#edit_user.ApiResponseFor422) | Unprocessable Entity

#### edit_user.ApiResponseFor200
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
**idUser** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**tokenUser** | str,  | str,  |  | [optional] 
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### edit_user.ApiResponseFor422
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

# **info_user**
<a name="info_user"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} info_user()

Get card info

Info about an user card.

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import cards_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cards_api.CardsApi(api_client)

    # example passing only optional values
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    body = dict(
        id_user=12345678,
        token_user="WHlSWmVDdzVQeUZ",
        terminal=1,
    )
    try:
        # Get card info
        api_response = api_instance.info_user(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling CardsApi->info_user: %s\n" % e)
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
**idUser** | decimal.Decimal, int,  | decimal.Decimal,  | Identification of user card given by PAYCOMET. Mandatory if is a card payment. | 
**terminal** | decimal.Decimal, int,  | decimal.Decimal,  | Product or terminal Id. | 
**tokenUser** | str,  | str,  | Identification of user card given by PAYCOMET. Mandatory if is a card payment. | 
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
200 | [ApiResponseFor200](#info_user.ApiResponseFor200) | OK
403 | [ApiResponseFor403](#info_user.ApiResponseFor403) | Not Allowed
422 | [ApiResponseFor422](#info_user.ApiResponseFor422) | Unprocessable Entity

#### info_user.ApiResponseFor200
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
**pan** | str,  | str,  | Card number, without any spaces or dashes. Only the last four digits will be returned. The rest will be masked with X | [optional] 
**cardBrand** | str,  | str,  | Card brand. If it can be identified, information on the card brand will be sent (Visa, MasterCard, American Express, etc). Otherwise, the field will be returned blank. | [optional] 
**cardType** | str,  | str,  | Type of card. If it can be identified, information on the type of card will be sent (DEBIT, CREDIT, etc). Otherwise, the field will be returned blank. | [optional] 
**cardICountryISO3** | str,  | str,  | ISO3 Code the country of the issuer of the card. If it can be identified, the ISO3 Code of the country of the issuer of the card will be sent. Otherwise, the field will be returned blank. | [optional] 
**expiryDate** | str,  | str,  | Expiry date of the card expressed in the format YYYY/MM | [optional] 
**cardHash** | str,  | str,  | Hash unique credit card id. | [optional] 
**cardCategory** | str,  | str,  | Card category. | [optional] 
**sepaCard** | decimal.Decimal, int,  | decimal.Decimal,  | Card in SEPA country. | [optional] 
**psd2Card** | str,  | str,  | Express if card has PSD2 information (Y is a PSD2 Card, N is not and NA is not available). | [optional] 
**tokenCOF** | decimal.Decimal, int,  | decimal.Decimal,  | Express if card has COF registered. | [optional] 
**eeaCard** | str,  | str,  | Express if card country belongs to EEA zone or not. (Y/N or NA if not available). | [optional] 
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### info_user.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### info_user.ApiResponseFor422
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

# **physical_add_card**
<a name="physical_add_card"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} physical_add_card()

Tokenize a card by physical encrypted data

cards_physical

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import cards_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cards_api.CardsApi(api_client)

    # example passing only optional values
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    body = dict(
        terminal=1,
        provider_id=12345,
        merchant_id="123456",
        terminal_id="999888777",
        device_ksn="D1809182775K9SN00007",
        device_dukpt="P6C10M6E0T277E2274D9281FBAFE1234A2C34388D7C000T7",
        cof_identifier="2012P4YC0M350",
        original_ip="127.0.0.1",
    )
    try:
        # Tokenize a card by physical encrypted data
        api_response = api_instance.physical_add_card(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling CardsApi->physical_add_card: %s\n" % e)
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
**deviceKsn** | str,  | str,  | Card KSN info | 
**deviceDukpt** | str,  | str,  | Card DUKPT info | 
**merchantId** | str,  | str,  | Merchant identifier code for physical operations given by PAYCOMET | 
**providerId** | decimal.Decimal, int,  | decimal.Decimal,  | Provider identifier for physical operations given by PAYCOMET | 
**terminal** | decimal.Decimal, int,  | decimal.Decimal,  | Product or terminal Id. | 
**terminalId** | str,  | str,  | Terminal identifier | 
**originalIp** | str,  | str,  | IP Address of the customer | 
**cofIdentifier** | str,  | str,  | Processor COF identifier | [optional] 
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
200 | [ApiResponseFor200](#physical_add_card.ApiResponseFor200) | Added
422 | [ApiResponseFor422](#physical_add_card.ApiResponseFor422) | Unprocessable Entity

#### physical_add_card.ApiResponseFor200
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
**idUser** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**tokenUser** | str,  | str,  |  | [optional] 
**expiryYear** | str,  | str,  |  | [optional] 
**expiryMonth** | str,  | str,  |  | [optional] 
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### physical_add_card.ApiResponseFor422
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

# **physical_edit_card**
<a name="physical_edit_card"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} physical_edit_card()

Edit a card entered by physical encrypted data

cards_physical_edit

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import cards_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cards_api.CardsApi(api_client)

    # example passing only optional values
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    body = dict(
        terminal=1,
        provider_id=12345,
        merchant_id="123456",
        terminal_id="999888777",
        id_user=12345678,
        token_user="WHlSWmVDdzVQeUZ",
        cof_identifier="2012P4YC0M350",
    )
    try:
        # Edit a card entered by physical encrypted data
        api_response = api_instance.physical_edit_card(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling CardsApi->physical_edit_card: %s\n" % e)
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
**idUser** | decimal.Decimal, int,  | decimal.Decimal,  | Identification of user card given by PAYCOMET. Mandatory if is a card payment. | 
**merchantId** | str,  | str,  | Merchant identifier code for physical operations given by PAYCOMET | 
**providerId** | decimal.Decimal, int,  | decimal.Decimal,  | Provider identifier for physical operations given by PAYCOMET | 
**terminal** | decimal.Decimal, int,  | decimal.Decimal,  | Product or terminal Id. | 
**terminalId** | str,  | str,  | Terminal identifier | 
**tokenUser** | str,  | str,  | Identification of user card given by PAYCOMET. Mandatory if is a card payment. | 
**cofIdentifier** | str,  | str,  | Processor COF identifier | [optional] 
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
200 | [ApiResponseFor200](#physical_edit_card.ApiResponseFor200) | Added
422 | [ApiResponseFor422](#physical_edit_card.ApiResponseFor422) | Unprocessable Entity

#### physical_edit_card.ApiResponseFor200
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
**idUser** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**tokenUser** | str,  | str,  |  | [optional] 
**cofIdentifier** | str,  | str,  |  | [optional] 
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### physical_edit_card.ApiResponseFor422
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

# **remove_user**
<a name="remove_user"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} remove_user()

Removes a card

Deletes the user.

### Example

```python
import paycomet_client
from paycomet_client.apis.tags import cards_api
from pprint import pprint
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)

# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cards_api.CardsApi(api_client)

    # example passing only optional values
    header_params = {
        'PAYCOMET-API-TOKEN': "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979",
    }
    body = dict(
        terminal=1,
        id_user=12345678,
        token_user="WHlSWmVDdzVQeUZ",
    )
    try:
        # Removes a card
        api_response = api_instance.remove_user(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling CardsApi->remove_user: %s\n" % e)
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
**idUser** | decimal.Decimal, int,  | decimal.Decimal,  | Identification of user card given by PAYCOMET. Mandatory if is a card payment. | 
**terminal** | decimal.Decimal, int,  | decimal.Decimal,  | Product or terminal Id. | 
**tokenUser** | str,  | str,  | Identification of user card given by PAYCOMET. Mandatory if is a card payment. | 
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
200 | [ApiResponseFor200](#remove_user.ApiResponseFor200) | OK
403 | [ApiResponseFor403](#remove_user.ApiResponseFor403) | Not Allowed
422 | [ApiResponseFor422](#remove_user.ApiResponseFor422) | Unprocessable Entity

#### remove_user.ApiResponseFor200
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
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  | Error Id. 0 means no error. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### remove_user.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**errorCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### remove_user.ApiResponseFor422
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

