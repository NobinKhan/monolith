from django.urls import path

from apps.users.apis import UserListApi

urlpatterns = [
    path("list", UserListApi.as_view(), name="user_list"),
]
