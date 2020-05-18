from sanic.response import json


class Errors(Exception):
    MSG = '系统内部错误'
    STATUS_CODE = 200
    ERROR_CODE = 1

    def __init__(self, msg='', error_code=1, status_code=None):
        super(Errors, self).__init__(msg, error_code)
        self.msg = msg or self.MSG
        self.error_code = error_code or self.ERROR_CODE
        self.status_code = status_code or self.STATUS_CODE

    def json_resp(self):
        return json({
            'error_code': self.error_code,
            'msg': self.msg
        }, status=self.status_code)


class PermissonDeniedError(Errors):
    MSG = '没有权限'
    STATUS_CODE = 403
    ERROR_CODE = 403


class Unauthorized(Errors):
    MSG = 'unauthorized'
    STATUS_CODE = 401
    ERROR_CODE = 401
