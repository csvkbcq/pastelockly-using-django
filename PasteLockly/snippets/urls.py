from django.urls import path
from .views import home, create_snippet, view_snippet

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_snippet, name='create_snippet'),
    path('snippet/<int:snippet_id>/', view_snippet, name='view_snippet'),
]
