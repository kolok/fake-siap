from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('operation/create/', views.OperationCreate.as_view(), name='create'),
    path('operation/<int:pk>/update/', views.OperationUpdate.as_view(), name='update'),
    path('operation/<int:pk>/delete/', views.OperationDelete.as_view(), name='delete'),
]
