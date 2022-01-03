from django.urls import path
from . import views

urlpatterns = [
    path("operations", views.operation_list, name="operation_list"),
    path("conventions", views.convention_list, name="convention_list"),
    path('operation/create/', views.OperationCreate.as_view(), name='create'),
    path('operation/<int:pk>/update/', views.OperationUpdate.as_view(), name='update'),
    path('operation/<int:pk>/delete/', views.OperationDelete.as_view(), name='delete'),
]
