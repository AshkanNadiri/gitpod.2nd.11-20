from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from bank import views as customer_view


router = routers.DefaultRouter()
router.register(r'users', customer_view.User_ViewSet)
router.register(r'groups', customer_view.Group_ViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path(r'read', customer_view.read, name = 'read')

]

