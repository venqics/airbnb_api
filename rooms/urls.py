from rest_framework.routers import DefaultRouter
from . import views

app_name = "rooms"
router = DefaultRouter()
router.register("", views.RoomViewSet)


urlpatterns = router.urls


###Creating API from scratch

#from django.urls import path
#from . import views

#app_name = "rooms"

#urlpatterns = [
    #path("", views.RoomsView.as_view()),
    #path("search/", views.room_search),
    #path("<int:pk>/", views.RoomView.as_view()),
#]