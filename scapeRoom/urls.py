from django.urls import include, path
from rest_framework import routers
from scapeRoom.quickstart import views
from django.contrib import admin
from whatGame.views import TicketView
from whatGame.views import send_request
from whatGame.views import EscapeRoomView
from whatGame.views import getDisableDate
from django.conf import settings
from django.conf.urls.static import static
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# router.register("ticket/", TicketView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('ticket/', TicketView),
    path('EscapeRoomGet/', EscapeRoomView),
    path('getDisableDate/', getDisableDate),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
