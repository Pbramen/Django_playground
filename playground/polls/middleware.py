def new_middleware(get_response):

    def middleware(request):
        print('middleware runs before the view')
        response = get_response(request)
        print('after the view executes')
        return response

    return middleware