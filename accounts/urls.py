from rest_framework.routers import DefaultRouter
from accounts.views import MemberInfoViewset


account_router = DefaultRouter()
account_router.register(r'memberinfo',MemberInfoViewset , basename='auth')
account_router.register(r'otp',MemberInfoViewset , basename='otp')