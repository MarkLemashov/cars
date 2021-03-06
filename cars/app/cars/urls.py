from django.urls import include, path
from rest_framework import routers
from cars.app.cars import views

router = routers.DefaultRouter()
router.register(r'cars', views.CarsViewSet)
router.register(r'customers', views.CustomersViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework'))
]
