from django.shortcuts import render


# Create your views here.
# @app.route('/tests')
# @jwt_required(optional=False)
def tests(request):  # put application's code here
    # current_user = get_jwt_identity()
    # print(current_user)
    return render(request, 'tests.html')
