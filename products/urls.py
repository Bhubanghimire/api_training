from django.urls import path
from products.views import ProductListAPI, LoginAPIView

urlpatterns = [
    path('', ProductListAPI.as_view()),
    path('login/', LoginAPIView.as_view()),

]