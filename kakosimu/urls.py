from django.urls import path, include
# ↓"."は同じフォルダの中のという意味
#"urlpatterns"の"Index"と"Detail"は、viewから持ってきている
from . import views

urlpatterns = [
    # パスの後ろに何も文字がなければ、viewsのIndexページに飛ばす
    path('', views.index, name="index"),  
]