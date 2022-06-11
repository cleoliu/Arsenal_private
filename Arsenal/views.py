
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
# from django.core.exceptions import PermissionDenied
# from django.http import JsonResponse
# from django.shortcuts import redirect, render
# from rest_framework import permissions
# from rest_framework.authentication import (BasicAuthentication,
#                                            SessionAuthentication)
# from rest_framework.decorators import api_view
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView

# from ..Users.forms import LoginForm, RegisterForm



        
# def login_page(request):
#     form = LoginForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'index.html', context)

# # @api_view(['POST'])
# # def login(request):
# #     username = request.json.get('username', None)
# #     password = request.json.get('password', None)
# #     print(username, password)

# #     # if username != 'test' or password != 'test':
# #     #     return jsonify({"msg": "Bad username or password"}), 401

# #     response = JsonResponse({"msg": "login successful"})
# #     access_token = create_access_token(identity=username)
# #     set_access_cookies(response, access_token, max_age=100)
# #     return response, 200

# # Login
# def do_login(request):
#     form = LoginForm()
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         # login pass
#         if user is not None:
#             login(request, user)
#             return redirect('/team/')

#     context = {
#         'form': form
#     }
#     return render(request, 'index.html', context)


# # Register
# def register(request):
#     form = RegisterForm()
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         # register pass
#         if form.is_valid():
#             form.save()
#             print("==is_valid")
#             return render(request, 'index.html')
    
#     context = {
#         'form': form
#     }
#     return render(request, 'register.html', context)
