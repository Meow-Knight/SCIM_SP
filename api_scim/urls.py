from rest_framework import routers

from api_scim.views.scim import ScimViewSet

app_name = 'api_scim'
router = routers.SimpleRouter(trailing_slash=True)

# router.register(r'role', RoleViewSet, basename='role')
# router.register(r'account', AccountViewSet, basename='account')
router.register(r'', ScimViewSet, basename='')

urlpatterns = router.urls
