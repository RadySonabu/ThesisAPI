from django.urls import path, include
from . import api
from . import views
urlpatterns = [
    path('api/auth/', include('rest_framework.urls')),
    path('api/v1/user/create/', api.UserCreateAPI.as_view(), name='user-create'),
    path('api/v1/user/list/', api.UserListAPI.as_view(), name='user-list'),
    path('api/v1/user/retrieve/<pk>/', api.UserRetrieveAPI.as_view(), name='user-retrieve'),
    path('api/v1/user/update/<pk>/', api.UserUpdateAPI.as_view(), name='user-update'),
    path('api/v1/user/delete/<pk>/', api.UserDestroyAPI.as_view(), name='user-delete'),
    path('api/v1/user/login/', api.UserLoginAPI.as_view(), name='user-login'),
    path('api/v1/user/logout/', api.UserLogoutAPI.as_view(), name='user-logout'),

    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

]