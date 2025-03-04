from starlette.responses import JSONResponse


async def request_validation_exception_handler(request, exc):
    """
    自定义全局请求参数校验异常处理
    :param request:
    :param exc:
    :return:
    """
    return JSONResponse(status_code=400, content={"code": 400, "msg": "请求参数错误", "data": exc.errors()})


async def starlette_http_exception_handler(request, exc):
    """
    自定义全局HTTP异常处理
    :param request:
    :param exc:
    :return:
    """
    return JSONResponse(status_code=exc.status_code, content={"code": exc.status_code, "msg": exc.detail, "data": None})