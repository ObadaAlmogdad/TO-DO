from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

router = DefaultRouter()
router.register(r'', TodoViewSet, basename='todo')

urlpatterns = [
    # API URLs
    path('api/', include(router.urls)),
    
    # Template URLs
    path('', views.task_list, name='task_list'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/update/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('<int:pk>/toggle/', views.task_toggle, name='task_toggle'),
]