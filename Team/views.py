from unicodedata import name

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def teams(request):  # put application's code here
    # current_user = get_jwt_identity()
    # print(current_user)
    return render(request, 'team.html')
