from rest_framework.routers import DefaultRouter

from accounts.views import AccountsViewset

router = DefaultRouter()
router.register(r'users', AccountsViewset, basename='user')

urlpatterns = router.urls
