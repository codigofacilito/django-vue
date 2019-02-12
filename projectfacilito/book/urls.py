from rest_framework import routers

from .viewsets import BookViewSet

router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls
