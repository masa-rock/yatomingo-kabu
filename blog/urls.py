from django.urls import path, include
# ↓"."は同じフォルダの中のという意味
#"urlpatterns"の"Index"と"Detail"は、viewから持ってきている
from . import views

urlpatterns = [
    # パスの後ろに何も文字がなければ、viewsのIndexページに飛ばす
    path('', views.index),  
    path('form/',views.Index.as_view(),name="memo"),
    # <pk>にPostのIDを渡すと表示される。
    # <pk>←primary keyの略。IDのこと。勝手に割り付けられたIDを拾ってきてくれる。
    path('detail/<pk>/', views.Detail.as_view(), name="detail"),
    path('create/', views.Create.as_view(), name="create"),
    path('update/<pk>', views.Update.as_view(), name="update"),
    path('delete/<pk>', views.Delete.as_view(), name="delete"),
    path('simu/', views.simu),
]