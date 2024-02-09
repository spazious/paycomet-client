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


class IVRApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def check_session(self, paycomet_api_token, **kwargs):  # noqa: E501
        """Checks an IVR session  # noqa: E501

        check_session  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_session(paycomet_api_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str paycomet_api_token: PAYCOMET API key (Authorization privilege required) (required)
        :param IvrSessionstateBody body:
        :return: InlineResponse20036
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.check_session_with_http_info(paycomet_api_token, **kwargs)  # noqa: E501
        else:
            (data) = self.check_session_with_http_info(paycomet_api_token, **kwargs)  # noqa: E501
            return data

    def check_session_with_http_info(self, paycomet_api_token, **kwargs):  # noqa: E501
        """Checks an IVR session  # noqa: E501

        check_session  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_session_with_http_info(paycomet_api_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str paycomet_api_token: PAYCOMET API key (Authorization privilege required) (required)
        :param IvrSessionstateBody body:
        :return: InlineResponse20036
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
                    " to method check_session" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'paycomet_api_token' is set
        if ('paycomet_api_token' not in params or
                params['paycomet_api_token'] is None):
            raise ValueError("Missing the required parameter `paycomet_api_token` when calling `check_session`")  # noqa: E501

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
            '/v1/ivr/session-state', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20036',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_session(self, paycomet_api_token, **kwargs):  # noqa: E501
        """Creates an IVR session  # noqa: E501

        get_session  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_session(paycomet_api_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str paycomet_api_token: PAYCOMET API key (Authorization privilege required) (required)
        :param IvrGetsessionBody body:
        :return: InlineResponse20035
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_session_with_http_info(paycomet_api_token, **kwargs)  # noqa: E501
        else:
            (data) = self.get_session_with_http_info(paycomet_api_token, **kwargs)  # noqa: E501
            return data

    def get_session_with_http_info(self, paycomet_api_token, **kwargs):  # noqa: E501
        """Creates an IVR session  # noqa: E501

        get_session  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_session_with_http_info(paycomet_api_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str paycomet_api_token: PAYCOMET API key (Authorization privilege required) (required)
        :param IvrGetsessionBody body:
        :return: InlineResponse20035
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
                    " to method get_session" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'paycomet_api_token' is set
        if ('paycomet_api_token' not in params or
                params['paycomet_api_token'] is None):
            raise ValueError("Missing the required parameter `paycomet_api_token` when calling `get_session`")  # noqa: E501

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
            '/v1/ivr/get-session', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20035',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def session_cancel(self, paycomet_api_token, **kwargs):  # noqa: E501
        """Cancel an IVR session  # noqa: E501

        session_cancell  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.session_cancel(paycomet_api_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str paycomet_api_token: PAYCOMET API key (Authorization privilege required) (required)
        :param IvrSessioncancelBody body:
        :return: InlineResponse20037
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.session_cancel_with_http_info(paycomet_api_token, **kwargs)  # noqa: E501
        else:
            (data) = self.session_cancel_with_http_info(paycomet_api_token, **kwargs)  # noqa: E501
            return data

    def session_cancel_with_http_info(self, paycomet_api_token, **kwargs):  # noqa: E501
        """Cancel an IVR session  # noqa: E501

        session_cancell  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.session_cancel_with_http_info(paycomet_api_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str paycomet_api_token: PAYCOMET API key (Authorization privilege required) (required)
        :param IvrSessioncancelBody body:
        :return: InlineResponse20037
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
                    " to method session_cancel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'paycomet_api_token' is set
        if ('paycomet_api_token' not in params or
                params['paycomet_api_token'] is None):
            raise ValueError("Missing the required parameter `paycomet_api_token` when calling `session_cancel`")  # noqa: E501

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
            '/v1/ivr/session-cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20037',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)