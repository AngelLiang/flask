# -*- coding: utf-8 -*-
"""
    flask.globals
    ~~~~~~~~~~~~~

    Defines all the global objects that are proxies to the current
    active context.

    :copyright: © 2010 by the Pallets team.
    :license: BSD, see LICENSE for more details.

笔记：
    线程本地变量模块
"""

from functools import partial
from werkzeug.local import LocalStack, LocalProxy


_request_ctx_err_msg = '''\
Working outside of request context.

This typically means that you attempted to use functionality that needed
an active HTTP request.  Consult the documentation on testing for
information about how to avoid this problem.\
'''
_app_ctx_err_msg = '''\
Working outside of application context.

This typically means that you attempted to use functionality that needed
to interface with the current application object in some way. To solve
this, set up an application context with app.app_context().  See the
documentation for more information.\
'''


def _lookup_req_object(name):
    top = _request_ctx_stack.top
    if top is None:
        raise RuntimeError(_request_ctx_err_msg)
    return getattr(top, name)


def _lookup_app_object(name):
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError(_app_ctx_err_msg)
    return getattr(top, name)


def _find_app():
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError(_app_ctx_err_msg)
    return top.app


# context locals

# LocalStack：多线程或协程隔离的栈结构
_request_ctx_stack = LocalStack()
_app_ctx_stack = LocalStack()

current_app = LocalProxy(_find_app)
# 返回一个 _lookup_req_object 对象，_lookup_req_object 的形参默认值为 'request'
# _lookup_req_object('request') # 获取当前请求上下文的 request
# 把当前请求上下文的 request 作为全局变量
request = LocalProxy(partial(_lookup_req_object, 'request'))
session = LocalProxy(partial(_lookup_req_object, 'session'))
# 把当前应用上下文的 g 作为全局变量
g = LocalProxy(partial(_lookup_app_object, 'g'))
