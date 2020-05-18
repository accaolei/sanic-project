from sanic import Sanic
from apps.hello.urls import hello_bp
app = Sanic('app')


# 使用peewee时在response关闭连接
# @app.middleware('response')
# async def close_db(request, response):
#     if not database.is_closed():
#         database.close()


app.blueprint(hello_bp)
