# hacking flask v1.0.2

version: v1.0.2

## 主要模块

path: `flask/`

| 模块/包 | 说明 |
| --- | --- |
| `json/` | 提供JSON支持 |
| `__init__.py` | 构造文件，导入了所有其他模块中开放的类和函数 |
| `__main__.py` | 用来启动flask命令 |
| `_compat.py` | 定义Python2与Python3版本兼容代码 |
| `app.py` | 主脚本，实现了WSGI程序对象，包含Flask类 |
| `blueprints.py` | 蓝本支持，包含Blueprint类定义 |
| `cli.py` | 提供命令行支持，包含内置的几个命令 |
| `config.py` | 实现配置相关的对象 |
| `ctx.py` | 实现上下文对象，比如请求上下文`RequestContext` |
| `debughelpers.py` | 一些辅助开发的函数/类 |
| `globals.py` | 定义全局对象，比如`request`、`session`等 |
| `helpers.py` | 包含常用的辅助函数，比如`flask()`、`url_for()` |
| `logging.py` | 提供日志支持 |
| `sessions.py` | 实现session功能 |
| `signals.py` | 实现信号支持，定义了内置的信号 |
| `templating.py` | 模板渲染功能 |
| `testing.py` | 提供用于测试的辅助函数 |
| `views.py` | 提供了类似Django中的类视图，用于编写Web API的`MethodView`就在这里定义 |
| `wrappers.py` | 实现WSGI封装对象，比如`Request`类和`Response`类 |

