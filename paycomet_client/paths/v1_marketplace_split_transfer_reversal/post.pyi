# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from paycomet_client import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from paycomet_client import schemas  # noqa: F401

# Header params
PAYCOMETAPITOKENSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
        'PAYCOMET-API-TOKEN': typing.Union[PAYCOMETAPITOKENSchema, str, ],
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_paycomet_api_token = api_client.HeaderParameter(
    name="PAYCOMET-API-TOKEN",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PAYCOMETAPITOKENSchema,
    required=True,
)
# body param


class SchemaForRequestBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        required = {
            "authCode",
            "submerchant",
            "payment",
        }
        
        class properties:
            
            
            class submerchant(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "amount",
                        "currency",
                        "splitId",
                        "splitAuthCode",
                    }
                    
                    class properties:
                        splitId = schemas.StrSchema
                        amount = schemas.NumberSchema
                        currency = schemas.StrSchema
                        splitAuthCode = schemas.StrSchema
                        __annotations__ = {
                            "splitId": splitId,
                            "amount": amount,
                            "currency": currency,
                            "splitAuthCode": splitAuthCode,
                        }
                
                amount: MetaOapg.properties.amount
                currency: MetaOapg.properties.currency
                splitId: MetaOapg.properties.splitId
                splitAuthCode: MetaOapg.properties.splitAuthCode
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["splitId"]) -> MetaOapg.properties.splitId: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["splitAuthCode"]) -> MetaOapg.properties.splitAuthCode: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["splitId", "amount", "currency", "splitAuthCode", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["splitId"]) -> MetaOapg.properties.splitId: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["splitAuthCode"]) -> MetaOapg.properties.splitAuthCode: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["splitId", "amount", "currency", "splitAuthCode", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, ],
                    currency: typing.Union[MetaOapg.properties.currency, str, ],
                    splitId: typing.Union[MetaOapg.properties.splitId, str, ],
                    splitAuthCode: typing.Union[MetaOapg.properties.splitAuthCode, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'submerchant':
                    return super().__new__(
                        cls,
                        *_args,
                        amount=amount,
                        currency=currency,
                        splitId=splitId,
                        splitAuthCode=splitAuthCode,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class payment(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "authCode",
                        "terminal",
                        "order",
                    }
                    
                    class properties:
                        terminal = schemas.IntSchema
                        order = schemas.StrSchema
                        authCode = schemas.StrSchema
                        __annotations__ = {
                            "terminal": terminal,
                            "order": order,
                            "authCode": authCode,
                        }
                
                authCode: MetaOapg.properties.authCode
                terminal: MetaOapg.properties.terminal
                order: MetaOapg.properties.order
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["terminal"]) -> MetaOapg.properties.terminal: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["authCode"]) -> MetaOapg.properties.authCode: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["terminal", "order", "authCode", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["terminal"]) -> MetaOapg.properties.terminal: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["authCode"]) -> MetaOapg.properties.authCode: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["terminal", "order", "authCode", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    authCode: typing.Union[MetaOapg.properties.authCode, str, ],
                    terminal: typing.Union[MetaOapg.properties.terminal, decimal.Decimal, int, ],
                    order: typing.Union[MetaOapg.properties.order, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'payment':
                    return super().__new__(
                        cls,
                        *_args,
                        authCode=authCode,
                        terminal=terminal,
                        order=order,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "submerchant": submerchant,
                "payment": payment,
            }
    
    authCode: schemas.AnyTypeSchema
    submerchant: MetaOapg.properties.submerchant
    payment: MetaOapg.properties.payment
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["submerchant"]) -> MetaOapg.properties.submerchant: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment"]) -> MetaOapg.properties.payment: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["submerchant", "payment", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["submerchant"]) -> MetaOapg.properties.submerchant: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment"]) -> MetaOapg.properties.payment: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["submerchant", "payment", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        authCode: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        submerchant: typing.Union[MetaOapg.properties.submerchant, dict, frozendict.frozendict, ],
        payment: typing.Union[MetaOapg.properties.payment, dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaForRequestBodyApplicationJson':
        return super().__new__(
            cls,
            *_args,
            authCode=authCode,
            submerchant=submerchant,
            payment=payment,
            _configuration=_configuration,
            **kwargs,
        )


request_body_any_type = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)


class SchemaFor200ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            errorCode = schemas.IntSchema
            order = schemas.StrSchema
            
            
            class submerchant(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        amount = schemas.NumberSchema
                        currency = schemas.StrSchema
                        splitAuthCode = schemas.StrSchema
                        __annotations__ = {
                            "amount": amount,
                            "currency": currency,
                            "splitAuthCode": splitAuthCode,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["splitAuthCode"]) -> MetaOapg.properties.splitAuthCode: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount", "currency", "splitAuthCode", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["splitAuthCode"]) -> typing.Union[MetaOapg.properties.splitAuthCode, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount", "currency", "splitAuthCode", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                    currency: typing.Union[MetaOapg.properties.currency, str, schemas.Unset] = schemas.unset,
                    splitAuthCode: typing.Union[MetaOapg.properties.splitAuthCode, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'submerchant':
                    return super().__new__(
                        cls,
                        *_args,
                        amount=amount,
                        currency=currency,
                        splitAuthCode=splitAuthCode,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "errorCode": errorCode,
                "order": order,
                "submerchant": submerchant,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errorCode"]) -> MetaOapg.properties.errorCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["submerchant"]) -> MetaOapg.properties.submerchant: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["errorCode", "order", "submerchant", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errorCode"]) -> typing.Union[MetaOapg.properties.errorCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["submerchant"]) -> typing.Union[MetaOapg.properties.submerchant, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["errorCode", "order", "submerchant", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        errorCode: typing.Union[MetaOapg.properties.errorCode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        order: typing.Union[MetaOapg.properties.order, str, schemas.Unset] = schemas.unset,
        submerchant: typing.Union[MetaOapg.properties.submerchant, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *_args,
            errorCode=errorCode,
            order=order,
            submerchant=submerchant,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


class SchemaFor422ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            errorCode = schemas.IntSchema
            
            
            class error(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        message = schemas.StrSchema
                        
                        
                        class detail(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                items = schemas.AnyTypeSchema
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'detail':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        __annotations__ = {
                            "message": message,
                            "detail": detail,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["detail"]) -> MetaOapg.properties.detail: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["message", "detail", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["detail"]) -> typing.Union[MetaOapg.properties.detail, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message", "detail", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
                    detail: typing.Union[MetaOapg.properties.detail, list, tuple, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'error':
                    return super().__new__(
                        cls,
                        *_args,
                        message=message,
                        detail=detail,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "errorCode": errorCode,
                "error": error,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errorCode"]) -> MetaOapg.properties.errorCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["errorCode", "error", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errorCode"]) -> typing.Union[MetaOapg.properties.errorCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["errorCode", "error", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        errorCode: typing.Union[MetaOapg.properties.errorCode, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        error: typing.Union[MetaOapg.properties.error, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor422ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *_args,
            errorCode=errorCode,
            error=error,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor422ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _split_transfer_reversal_oapg(
        self,
        content_type: typing_extensions.Literal["application/json"] = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _split_transfer_reversal_oapg(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def _split_transfer_reversal_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _split_transfer_reversal_oapg(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _split_transfer_reversal_oapg(
        self,
        content_type: str = 'application/json',
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Run a split transfer reversal based on a previous split transfer
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value

        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_paycomet_api_token,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        _fields = None
        _body = None
        if body is not schemas.unset:
            serialized_data = request_body_any_type.serialize(body, content_type)
            _headers.add('Content-Type', content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class SplitTransferReversal(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def split_transfer_reversal(
        self,
        content_type: typing_extensions.Literal["application/json"] = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def split_transfer_reversal(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def split_transfer_reversal(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def split_transfer_reversal(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def split_transfer_reversal(
        self,
        content_type: str = 'application/json',
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._split_transfer_reversal_oapg(
            body=body,
            header_params=header_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        content_type: typing_extensions.Literal["application/json"] = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def post(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def post(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def post(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def post(
        self,
        content_type: str = 'application/json',
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        header_params: RequestHeaderParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._split_transfer_reversal_oapg(
            body=body,
            header_params=header_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


