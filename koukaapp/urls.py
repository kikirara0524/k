from django.urls import path

from . import views


app_name = 'koukaapp'
urlpatterns = [
    # '' にアクセスされたらviews.pyのIndexViewを実行
    # ページ名はindex
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/',views.InquiryView.as_view(),name="inquiry"),
    path('diary-list', views.DiaryListView.as_view(), name="diary_list"),
    # <int:pk>・・・URL引数 pkという名前でビューに渡される int型に制限
    path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name="diary_detail"),
    path('diary-create/', views.DiaryCreateView.as_view(), name="diary_create"),
    path('diary-update/<int:pk>', views.DiaryUpdateView.as_view(), name="diary_update"),
    path('diary-delete/<int:pk>', views.DiaryDeleteView.as_view(), name="diary_delete"),

]
