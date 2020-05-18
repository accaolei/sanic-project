from apps import BaseService


class HelloService(BaseService):

    def hello_handler(self):
        return {
            'data': 'hello'
        }
