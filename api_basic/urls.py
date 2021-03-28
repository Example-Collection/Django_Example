from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetailAPIView, GenericAPIView
from .views import ArticleViewSet, ArticleGenericViewSet, ArticleModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleModelViewSet, basename='article')
router.register('article/<int:pk>', ArticleModelViewSet, basename="article detail")

urlpatterns = [
    path('v1/', include(router.urls))
]

# urlpatterns = [
#     path('article/<int:id>/', GenericAPIView.as_view()),
#     # path('article/', article_list),
#     # path('article/', ArticleAPIView.as_view()),
#     # path('detail/<int:pk>', article_detail)
#     # path('detail/<int:id>/', ArticleDetailAPIView.as_view())
# ]