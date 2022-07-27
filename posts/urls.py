from django.urls import path
# from .views import UserList, UserDetail, PostList, PostDetail

from .views import UserViewSet, PostViewSet
from rest_framework.routers import SimpleRouter

# urlpatterns = [
#     path('users/', UserList.as_view()), # new
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
# ]

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls