from rest_framework import routers
from search.views import StudiosViewSet


router = routers.DefaultRouter()
router.register(r'studios', StudiosViewSet)
