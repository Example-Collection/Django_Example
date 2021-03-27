from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetailAPIView, GenericAPIView

urlpatterns = [
    path('article/<int:id>/', GenericAPIView.as_view()),
    # path('article/', article_list),
    # path('article/', ArticleAPIView.as_view()),
    # path('detail/<int:pk>', article_detail)
    # path('detail/<int:id>/', ArticleDetailAPIView.as_view())
]