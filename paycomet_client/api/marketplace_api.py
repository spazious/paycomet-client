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

from paycomet_client.api_client import ApiClient


class MarketplaceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def split_transfer(self, paycomet_api_token, **kwargs):  # noqa: E501
        """Make a transfer to other accounts on PAYCOMET  # noqa: E501

        Make a deposit in a destination account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.split_transfer(paycomet_api_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str paycomet_api_token: PAYCOMET API key (Authorization privilege required) (required)
        :param MarketplaceSplittransferBody body:
        :return: InlineResponse20027
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.split_transfer_with_http_info(paycomet_api_token, **kwargs)  # noqa: E501
        else:
            (data) = self.split_transfer_with_http_info(paycomet_api_token, **kwargs)  # noqa: E501
            return data

    def split_transfer_with_http_info(self, paycomet_api_token, **kwargs):  # noqa: E501
        """Make a transfer to other accounts on PAYCOMET  # noqa: E501

        Make a deposit in a destination account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.split_transfer_with_http_info(paycomet_api_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str paycomet_api_token: PAYCOMET API key (Authorization privilege required) (required)
        :param MarketplaceSplittransferBody body:
        :return: InlineResponse20027
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['paycomet_api_token', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method split_transfer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'paycomet_api_token' is set
        if ('paycomet_api_token' not in params or
                params['paycomet_api_token'] is None):
            raise ValueError("Missing the required parameter `paycomet_api_token` when calling `split_transfer`")  # noqa: E501

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
            '/v1/marketplace/split-transfer', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20027',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def split_transfer_reversal(self, paycomet_api_token, **kwargs):  # noqa: E501
        """Run a split transfer reversal based on a previous split transfer  # noqa: E501

        Make a split transfer reversal request  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.split_transfer_reversal(paycomet_api_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str paycomet_api_token: PAYCOMET API key (Authorization privilege required) (required)
        :param MarketplaceSplittransferreversalBody body:
        :return: InlineResponse20027
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.split_transfer_reversal_with_http_info(paycomet_api_token, **kwargs)  # noqa: E501
        else:
            (data) = self.split_transfer_reversal_with_http_info(paycomet_api_token, **kwargs)  # noqa: E501
            return data

    def split_transfer_reversal_with_http_info(self, paycomet_api_token, **kwargs):  # noqa: E501
        """Run a split transfer reversal based on a previous split transfer  # noqa: E501

        Make a split transfer reversal request  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.split_transfer_reversal_with_http_info(paycomet_api_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str paycomet_api_token: PAYCOMET API key (Authorization privilege required) (required)
        :param MarketplaceSplittransferreversalBody body:
        :return: InlineResponse20027
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['paycomet_api_token', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method split_transfer_reversal" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'paycomet_api_token' is set
        if ('paycomet_api_token' not in params or
                params['paycomet_api_token'] is None):
            raise ValueError("Missing the required parameter `paycomet_api_token` when calling `split_transfer_reversal`")  # noqa: E501

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
            '/v1/marketplace/split-transfer-reversal', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20027',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def transfer(self, paycomet_api_token, **kwargs):  # noqa: E501
        """Run a transfer  # noqa: E501

        Run a transfer in a destination account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transfer(paycomet_api_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str paycomet_api_token: PAYCOMET API key (Authorization privilege required) (required)
        :param MarketplaceTransferBody body:
        :return: InlineResponse20028
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transfer_with_http_info(paycomet_api_token, **kwargs)  # noqa: E501
        else:
            (data) = self.transfer_with_http_info(paycomet_api_token, **kwargs)  # noqa: E501
            return data

    def transfer_with_http_info(self, paycomet_api_token, **kwargs):  # noqa: E501
        """Run a transfer  # noqa: E501

        Run a transfer in a destination account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transfer_with_http_info(paycomet_api_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str paycomet_api_token: PAYCOMET API key (Authorization privilege required) (required)
        :param MarketplaceTransferBody body:
        :return: InlineResponse20028
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['paycomet_api_token', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transfer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'paycomet_api_token' is set
        if ('paycomet_api_token' not in params or
                params['paycomet_api_token'] is None):
            raise ValueError("Missing the required parameter `paycomet_api_token` when calling `transfer`")  # noqa: E501

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
            '/v1/marketplace/transfer', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20028',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def transfer_reversal(self, paycomet_api_token, **kwargs):  # noqa: E501
        """Make a transfer reversal based on a previous transfer  # noqa: E501

        Make a transfer reversal based on a previous transfer  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transfer_reversal(paycomet_api_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str paycomet_api_token: PAYCOMET API key (Authorization privilege required) (required)
        :param MarketplaceTransferreversalBody body:
        :return: InlineResponse20028
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transfer_reversal_with_http_info(paycomet_api_token, **kwargs)  # noqa: E501
        else:
            (data) = self.transfer_reversal_with_http_info(paycomet_api_token, **kwargs)  # noqa: E501
            return data

    def transfer_reversal_with_http_info(self, paycomet_api_token, **kwargs):  # noqa: E501
        """Make a transfer reversal based on a previous transfer  # noqa: E501

        Make a transfer reversal based on a previous transfer  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transfer_reversal_with_http_info(paycomet_api_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str paycomet_api_token: PAYCOMET API key (Authorization privilege required) (required)
        :param MarketplaceTransferreversalBody body:
        :return: InlineResponse20028
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['paycomet_api_token', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transfer_reversal" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'paycomet_api_token' is set
        if ('paycomet_api_token' not in params or
                params['paycomet_api_token'] is None):
            raise ValueError("Missing the required parameter `paycomet_api_token` when calling `transfer_reversal`")  # noqa: E501

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
            '/v1/marketplace/transfer-reversal', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20028',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
