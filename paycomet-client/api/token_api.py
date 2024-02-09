# coding: utf-8

"""
    PAYCOMET REST API

    PAYCOMET API REST for customers.  # noqa: E501

    OpenAPI spec version: 2.99.0
    Contact: tecnico@paycomet.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from paycomet-client.api_client import ApiClient


class TokenApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_token(self, **kwargs):  # noqa: E501
        """Tokenizes an APM.  # noqa: E501

        This method supposes the registration of the APM in PAYCOMET for subsequent charges.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_token(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1TokenBody body:
        :param str paycomet_api_token: PAYCOMET API key (Token actions privilege required)
        :return: InlineResponse20038
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_token_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.add_token_with_http_info(**kwargs)  # noqa: E501
            return data

    def add_token_with_http_info(self, **kwargs):  # noqa: E501
        """Tokenizes an APM.  # noqa: E501

        This method supposes the registration of the APM in PAYCOMET for subsequent charges.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_token_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1TokenBody body:
        :param str paycomet_api_token: PAYCOMET API key (Token actions privilege required)
        :return: InlineResponse20038
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'paycomet_api_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_token" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'paycomet_api_token' in params:
            header_params['PAYCOMET-API-TOKEN'] = params['paycomet_api_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20038',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
