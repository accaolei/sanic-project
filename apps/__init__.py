from sanic.views import HTTPMethodView
from common import exceptions
from sanic.response import HTTPResponse, json
import logging
import traceback
from functools import wraps


logger = logging.getLogger(__name__)


def response():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            try:
                result = await f(request, *args, **kwargs)
            except exceptions.Errors as ee:
                # logger.exception(traceback.format_exc())
                return json({
                    'error_code': ee.error_code or ee.ERROR_CODE,
                    'msg': ee.msg
                }, status=ee.status_code or ee.ERROR_CODE)
            except Exception as e:
                logger.exception('错误: {}'.format(traceback.format_exc()))
                return json({
                    'error_code': 1, 'msg': '系统内部错误', 'detail': e.args
                })
            if isinstance(result, HTTPResponse):
                return result
            resp = {'error_code': 0, 'msg': 'ok'}
            resp.update(result)
            return json(resp)
        return decorated_function

    return decorator


class BaseView(HTTPMethodView):
    '''
    基础视图
    '''
    decorators = [response()]


class BaseService(object):

    def __init__(self, request, *args, **kwargs):
        self.request = request
