#!/usr/bin/env python3

from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    print(f'This web server is running at {request.remote_addr}')
    return Response('AWSGI generated this response!')
if __name__ == 'main':
    from werkzeug.serving import run_simple
    run_simple(
        hostname='localhost',
        port=5555,
        application=application
    )
