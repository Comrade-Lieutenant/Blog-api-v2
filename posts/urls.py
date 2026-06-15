from rest_framework.routers import SimpleRouter

from .views import UserViewSet, PostViewSet


# Routers work directly with viewsets to automatically generate url patterns.
# DRF has 2 default routers: Simplerouter / DefaultRouter

"""
urlpatterns = [
    path("users/", UserList.as_view()),
    path("users/<int:pk>/", UserDetail.as_view()),
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="post_list"),
]
"""

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")  # /api/v1/users/
router.register("", PostViewSet, basename="posts")  # /api/v1/

urlpatterns = router.urls
