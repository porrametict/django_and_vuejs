from django.urls import path, include
from rest_framework.routers import DefaultRouter
from borrowing import views

router = DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'borrow', views.BorrowingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
