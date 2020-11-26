from django.urls import path, include
from . import api
from . import views
urlpatterns = [
    path('create/', api.UserCreateAPI.as_view(), name='user-create'),
    path('list/', api.UserListAPI.as_view(), name='user-list'),
    path('retrieve/<pk>/', api.UserRetrieveAPI.as_view(), name='user-retrieve'),
    path('update/<pk>/', api.UserUpdateAPI.as_view(), name='user-update'),
    path('delete/<pk>/', api.UserDestroyAPI.as_view(), name='user-delete'),
    path('login/', api.UserLoginAPI.as_view(), name='user-login'),
    path('logout/', api.UserLogoutAPI.as_view(), name='user-logout'),
    
]