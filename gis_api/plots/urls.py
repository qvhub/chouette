from django.urls import path
from .views import ParcelCreateView, ParcelRetrieveUpdateView, UserParcelsListView, ParcelDeleteView

urlpatterns = [
    path('create/', ParcelCreateView.as_view(), name='create_parcel'),
    path('<int:pk>/', ParcelRetrieveUpdateView.as_view(), name='parcel-update'),
    path('<int:pk>/delete/', ParcelDeleteView.as_view(), name='parcel-delete'),
    path('user/', UserParcelsListView.as_view(), name='user-parcels-list'),
]