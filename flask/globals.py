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
    """获取当前栈顶请求对象的某个name属性。

    请求上下文压入栈后，再次访问其都会从这个栈的顶端通过 _request_ctx_stack.top
    来获取，所以取到的永远是只属于本线程中的对象，这样
    不同请求之间的上下文就做到了完全隔离。
    """
    top = _request_ctx_stack.top
    if top is None:
        raise RuntimeError(_request_ctx_err_msg)
    return getattr(top, name)


def _lookup_app_object(name):
    """获取当前栈顶app对象的某个name属性"""
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError(_app_ctx_err_msg)
    return getattr(top, name)


def _find_app():
    """获取当前栈顶的app对象"""
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError(_app_ctx_err_msg)
    return top.app


# context locals

# LocalStack：多线程/协程隔离的栈结构
# 在应用开发时不会使用上面的变量，一般在Flask扩展开发中才会使用
_request_ctx_stack = LocalStack()
_app_ctx_stack = LocalStack()

current_app = LocalProxy(_find_app)

# partial: 偏函数
# 返回一个 _lookup_req_object 对象，_lookup_req_object 的形参默认值为 'request'
# _lookup_req_object('request')  # 获取当前请求上下文的 request
# 把当前请求上下文的 request 作为全局变量
request = LocalProxy(partial(_lookup_req_object, 'request'))    # werkzeug.Local.__storage__[get_ident()]['request']
session = LocalProxy(partial(_lookup_req_object, 'session'))    # werkzeug.Local.__storage__[get_ident()]['session']

# 把当前应用上下文的 g 作为全局变量
g = LocalProxy(partial(_lookup_app_object, 'g'))    # werkzeug.Local.__storage__[get_ident()]['g']
