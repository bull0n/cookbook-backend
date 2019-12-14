from django.urls import path, include

from . import views
from graphene_django.views import GraphQLView

urlpatterns = [
    path('', GraphQLView.as_view(graphiql=True)),
]