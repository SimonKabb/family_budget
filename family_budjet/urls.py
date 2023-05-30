from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_v1/', include('budget.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('', include('front.urls')),
]
