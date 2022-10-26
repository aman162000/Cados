from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import AdvocateListAPIView,CompanyListAPIView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Cados 💻')

router = DefaultRouter()

router.register(r'advocate',AdvocateListAPIView,'advocate')
router.register(r'companies',CompanyListAPIView,'company')

urlpatterns = [
    path('docs/',schema_view),
    path('',include(router.urls))
]
