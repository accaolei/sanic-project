from apps import BaseView
from .services import HelloService


class HelloView(BaseView):

    async def get(self, request, *args, **kwargs):
        result = HelloService(request).hello_handler()
        return result
