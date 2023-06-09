# paycomet-client
PAYCOMET API REST for customers.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.78.0
- Package version: 2.78.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.paycomet.com](https://www.paycomet.com)

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://bitbucket.org/it_spazious/paycomet_client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://bitbucket.org/it_spazious/paycomet_client.git`)

Then import the package:
```python
import paycomet_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import paycomet_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import paycomet_client
from pprint import pprint
from paycomet_client.apis.tags import ivr_api
# Defining the host is optional and defaults to https://rest.paycomet.com
# See configuration.py for a list of all supported configuration parameters.
configuration = paycomet_client.Configuration(
    host = "https://rest.paycomet.com"
)


# Enter a context with an instance of the API client
with paycomet_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ivr_api.IVRApi(api_client)
    paycomet_api_token = "27ce3b8ab7b31a03ec7ce2r73623ee2be0634979" # str | PAYCOMET API key (Authorization privilege required)
any_type = dict(
        terminal=1234,
        ivr_provider_id=18,
        ivr_merchant_order="ABCD1234",
    ) # anyType |  (optional)

    try:
        # Checks an IVR session
        api_response = api_instance.check_session(paycomet_api_tokenany_type=any_type)
        pprint(api_response)
    except paycomet_client.ApiException as e:
        print("Exception when calling IVRApi->check_session: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://rest.paycomet.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*IVRApi* | [**check_session**](docs/apis/tags/IVRApi.md#check_session) | **post** /v1/ivr/session-state | Checks an IVR session
*IVRApi* | [**get_session**](docs/apis/tags/IVRApi.md#get_session) | **post** /v1/ivr/get-session | Creates an IVR session
*IVRApi* | [**session_cancel**](docs/apis/tags/IVRApi.md#session_cancel) | **post** /v1/ivr/session-cancel | Cancel an IVR session
*BalanceApi* | [**product_balance**](docs/apis/tags/BalanceApi.md#product_balance) | **post** /v1/balance | Get balance info
*CardsApi* | [**add_user**](docs/apis/tags/CardsApi.md#add_user) | **post** /v1/cards | Tokenizes a card. Either card number and CVC2 or jetToken are required. For you to send directly the card data you should be PCI certified or the accepting the requirement to submit quarterly SAQ-AEP and get ASV scans. For most users is strongly recommended getting the jetToken with JETIFRAME or using GET integration to register the cards instead of REST.
*CardsApi* | [**edit_user**](docs/apis/tags/CardsApi.md#edit_user) | **post** /v1/cards/edit | Changes the expiry date, cvc2 or both
*CardsApi* | [**info_user**](docs/apis/tags/CardsApi.md#info_user) | **post** /v1/cards/info | Get card info
*CardsApi* | [**physical_add_card**](docs/apis/tags/CardsApi.md#physical_add_card) | **post** /v1/cards/physical | Tokenize a card by physical encrypted data
*CardsApi* | [**physical_edit_card**](docs/apis/tags/CardsApi.md#physical_edit_card) | **post** /v1/cards/physical/edit | Edit a card entered by physical encrypted data
*CardsApi* | [**remove_user**](docs/apis/tags/CardsApi.md#remove_user) | **post** /v1/cards/delete | Removes a card
*DccApi* | [**dcc_purchase_confirm**](docs/apis/tags/DccApi.md#dcc_purchase_confirm) | **post** /v1/payments/{order}/dcc/confirm | Confirm previous DCC payment
*DccApi* | [**dcc_purchase_create**](docs/apis/tags/DccApi.md#dcc_purchase_create) | **post** /v1/payments/dcc | Create an DCC payment
*ErrorApi* | [**info_error**](docs/apis/tags/ErrorApi.md#info_error) | **post** /v1/errors | Gets an error description
*ExchangeApi* | [**exchange**](docs/apis/tags/ExchangeApi.md#exchange) | **post** /v1/exchange | Converts a certain amount from a currency to another.
*FormApi* | [**form**](docs/apis/tags/FormApi.md#form) | **post** /v1/form | Create form view for user capture
*HeartbeatApi* | [**heartbeat**](docs/apis/tags/HeartbeatApi.md#heartbeat) | **post** /v1/heartbeat | Check the system
*IpApi* | [**get_countryby_ip**](docs/apis/tags/IpApi.md#get_countryby_ip) | **post** /v1/ip | Retrieves country info by IP
*IpApi* | [**get_remote_address**](docs/apis/tags/IpApi.md#get_remote_address) | **post** /v1/ip/remote | Retrieves request remote address IP
*LaunchpadApi* | [**launch_authorization**](docs/apis/tags/LaunchpadApi.md#launch_authorization) | **post** /v1/launchpad/authorization | Creates a payment link and sends it to customer
*LaunchpadApi* | [**launch_preauthorization**](docs/apis/tags/LaunchpadApi.md#launch_preauthorization) | **post** /v1/launchpad/preauthorization | Executes a preauthorization link and sends it to customer
*LaunchpadApi* | [**launch_subscription**](docs/apis/tags/LaunchpadApi.md#launch_subscription) | **post** /v1/launchpad/subscription | Creates a subscription link and sends it to customer
*MarketplaceApi* | [**split_transfer**](docs/apis/tags/MarketplaceApi.md#split_transfer) | **post** /v1/marketplace/split-transfer | Make a transfer to other accounts on PAYCOMET
*MarketplaceApi* | [**split_transfer_reversal**](docs/apis/tags/MarketplaceApi.md#split_transfer_reversal) | **post** /v1/marketplace/split-transfer-reversal | Run a split transfer reversal based on a previous split transfer
*MarketplaceApi* | [**transfer**](docs/apis/tags/MarketplaceApi.md#transfer) | **post** /v1/marketplace/transfer | Run a transfer
*MarketplaceApi* | [**transfer_reversal**](docs/apis/tags/MarketplaceApi.md#transfer_reversal) | **post** /v1/marketplace/transfer-reversal | Make a transfer reversal based on a previous transfer
*MethodsApi* | [**get_user_payment_methods**](docs/apis/tags/MethodsApi.md#get_user_payment_methods) | **post** /v1/methods | Retrieves product methods
*MiraklApi* | [**mirakl_invoices_search**](docs/apis/tags/MiraklApi.md#mirakl_invoices_search) | **post** /v1/invoices | Search Mirakl invoices
*PaymentsApi* | [**execute_purchase**](docs/apis/tags/PaymentsApi.md#execute_purchase) | **post** /v1/payments | Executes a payment
*PaymentsApi* | [**execute_purchase_rtoken**](docs/apis/tags/PaymentsApi.md#execute_purchase_rtoken) | **post** /v1/payments/rtoken | Executes a payment by refence
*PaymentsApi* | [**operation_info**](docs/apis/tags/PaymentsApi.md#operation_info) | **post** /v1/payments/{order}/info | Get info of a order
*PaymentsApi* | [**operation_search**](docs/apis/tags/PaymentsApi.md#operation_search) | **post** /v1/payments/search | Search orders
*PreauthorizationsApi* | [**cancel_preauthorization**](docs/apis/tags/PreauthorizationsApi.md#cancel_preauthorization) | **post** /v1/payments/{order}/preauth/cancel | Cancel previous preauthorization
*PreauthorizationsApi* | [**confirm_preauthorization**](docs/apis/tags/PreauthorizationsApi.md#confirm_preauthorization) | **post** /v1/payments/{order}/preauth/confirm | Confirm previous preauthorization
*PreauthorizationsApi* | [**create_preauthorization**](docs/apis/tags/PreauthorizationsApi.md#create_preauthorization) | **post** /v1/payments/preauth | Create preauthorization
*PreauthorizationsApi* | [**create_preauthorization_rtoken**](docs/apis/tags/PreauthorizationsApi.md#create_preauthorization_rtoken) | **post** /v1/payments/preauthrtoken | Creates a preauthorization by reference
*RefundApi* | [**execute_refund**](docs/apis/tags/RefundApi.md#execute_refund) | **post** /v1/payments/{order}/refund | Perform a refund
*SepaApi* | [**add_document**](docs/apis/tags/SepaApi.md#add_document) | **post** /v1/sepa/add-document | Adds a SEPA document
*SepaApi* | [**cancel**](docs/apis/tags/SepaApi.md#cancel) | **post** /v1/sepa/cancel | Cancel a SEPA order
*SepaApi* | [**check_customer**](docs/apis/tags/SepaApi.md#check_customer) | **post** /v1/sepa/check-customer | Check a customers SEPA documentation
*SepaApi* | [**check_document**](docs/apis/tags/SepaApi.md#check_document) | **post** /v1/sepa/check-document | Check a SEPA document
*SepaApi* | [**enrole_customer**](docs/apis/tags/SepaApi.md#enrole_customer) | **post** /v1/sepa/enrole-customer | Generate a link to make a account check to a customer
*SepaApi* | [**sepa_operations**](docs/apis/tags/SepaApi.md#sepa_operations) | **post** /v1/sepa/operations | Send SEPA operations
*SusbcriptionsApi* | [**create_subscription**](docs/apis/tags/SusbcriptionsApi.md#create_subscription) | **post** /v1/subscription | Create susbcription payment
*SusbcriptionsApi* | [**edit_subscription**](docs/apis/tags/SusbcriptionsApi.md#edit_subscription) | **post** /v1/subscription/{order}/edit | Edit susbcription payment.
*SusbcriptionsApi* | [**info_subscription**](docs/apis/tags/SusbcriptionsApi.md#info_subscription) | **post** /v1/subscription/{order}/info | Gets susbcription info. If the susbscription is not a card subscription only the idUser is need. TokenUser is just for card subscriptions.
*SusbcriptionsApi* | [**remove_subscription**](docs/apis/tags/SusbcriptionsApi.md#remove_subscription) | **post** /v1/subscription/{order}/remove | Remove susbcription payment. If the susbscription is not a card subscription only the idUser is need. TokenUser is just for card subscriptions.
*TokenApi* | [**add_token**](docs/apis/tags/TokenApi.md#add_token) | **post** /v1/token | Tokenizes an APM.

## Documentation For Models


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

tecnico@paycomet.com
tecnico@paycomet.com
tecnico@paycomet.com
tecnico@paycomet.com
tecnico@paycomet.com
tecnico@paycomet.com
tecnico@paycomet.com
tecnico@paycomet.com
tecnico@paycomet.com
tecnico@paycomet.com
tecnico@paycomet.com
tecnico@paycomet.com
tecnico@paycomet.com
tecnico@paycomet.com
tecnico@paycomet.com
tecnico@paycomet.com
tecnico@paycomet.com
tecnico@paycomet.com
tecnico@paycomet.com

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in paycomet_client.apis and paycomet_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from paycomet_client.apis.default_api import DefaultApi`
- `from paycomet_client.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import paycomet_client
from paycomet_client.apis import *
from paycomet_client.models import *
```
