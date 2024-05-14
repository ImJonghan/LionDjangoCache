from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# 라우터 인스턴스 생성
router = DefaultRouter()

# 라우터에 ViewSet 등록
router.register(r'products', ProductViewSet)

# URL 패턴을 urlpatterns 리스트에 포함시키기
urlpatterns = [
    path('', include(router.urls)),
]