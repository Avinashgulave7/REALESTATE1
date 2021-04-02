from django.urls import path,include
from rest_framework import routers
from testapp.api.views import BuyAPI,RentAPI,LandAPI,AgentAPI
router=routers.DefaultRouter()
router.register('Buy',BuyAPI)
router.register('Rent',RentAPI)
router.register('Land',LandAPI)
router.register('Agent',AgentAPI)



urlpatterns = [
path('', include(router.urls)),


]