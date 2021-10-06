from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views

from app.API.resources import NoteList

router = routers.SimpleRouter()
router.register(r'notes', NoteList)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token)
]

urlpatterns += router.urls
