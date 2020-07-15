from fastapi import Request
import database
import datetime
import time
import ast

async def db_logging(request: Request,  call_next):
    start_time = time.time()

    response = await call_next(request)
    
    query = database.fastapi_logs.insert().values(
        response_status_code=response.status_code,
        request_method=request.method,
        request_url=str(request.url),
        request_query_params=dict(request.query_params),
        request_path_parameters=dict(request.path_params),
        created=datetime.datetime.now(),
        timespan=time.time() - start_time
    )
    await database.db.execute(query)

    return response