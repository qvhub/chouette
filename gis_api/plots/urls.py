from django.urls import path
from .views import ParcelCreateView, ParcelRetrieveUpdateView, UserParcelsListView, ParcelDeleteView

urlpatterns = [
    path('create/', ParcelCreateView.as_view(), name='create_parcel'),
    path('parcel/<int:pk>/', ParcelRetrieveUpdateView.as_view(), name='parcel-update'),
    path('parcel/<int:pk>/delete/', ParcelDeleteView.as_view(), name='parcel-delete'),
    path('user-parcels/', UserParcelsListView.as_view(), name='user-parcels-list'),
]