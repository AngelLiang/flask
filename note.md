# hacking flask v1.0.2

version: v1.0.2

## Flask 程序包各模块分析

path: `flask/`

| 模块/包           | 说明                                                                      |
| ----------------- | ------------------------------------------------------------------------- |
| `json/`           | 提供 JSON 支持                                                            |
| `__init__.py`     | 构造文件，导入了所有其他模块中开放的类和函数                              |
| `__main__.py`     | 用来启动 flask 命令                                                       |
| `_compat.py`      | 定义 Python2 与 Python3 版本兼容代码                                      |
| `app.py`          | 主脚本，实现了 WSGI 程序对象，包含 Flask 类                               |
| `blueprints.py`   | 蓝本支持，包含 Blueprint 类定义                                           |
| `cli.py`          | 提供命令行支持，包含内置的几个命令                                        |
| `config.py`       | 实现配置相关的对象                                                        |
| `ctx.py`          | 实现上下文对象，比如请求上下文`RequestContext`                            |
| `debughelpers.py` | 一些辅助开发的函数/类                                                     |
| `globals.py`      | 定义全局对象，比如`request`、`session`等                                  |
| `helpers.py`      | 包含常用的辅助函数，比如`flask()`、`url_for()`                            |
| `logging.py`      | 提供日志支持                                                              |
| `sessions.py`     | 实现 session 功能                                                         |
| `signals.py`      | 实现信号支持，定义了内置的信号                                            |
| `templating.py`   | 模板渲染功能                                                              |
| `testing.py`      | 提供用于测试的辅助函数                                                    |
| `views.py`        | 提供了类似 Django 中的类视图，用于编写 Web API 的`MethodView`就在这里定义 |
| `wrappers.py`     | 实现 WSGI 封装对象，比如`Request`类和`Response`类                         |
