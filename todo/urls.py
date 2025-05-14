from django.urls import path
from .views import TodoViewSet

urlpatterns = [
    path('', TodoViewSet.as_view({'get': 'list', 'post': 'create'}), name='todo-list'),
    path('<int:pk>/', TodoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='todo-detail'),
]