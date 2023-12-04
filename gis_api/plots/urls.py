from django.urls import path
from .views import PlotCreateView, PlotRetrieveUpdateView, UserPlotsListView, PlotDeleteView

urlpatterns = [
    path('create/', PlotCreateView.as_view(), name='create_parcel'),
    path('<int:pk>/', PlotRetrieveUpdateView.as_view(), name='parcel-update'),
    path('<int:pk>/delete/', PlotDeleteView.as_view(), name='parcel-delete'),
    path('user/', UserPlotsListView.as_view(), name='user-parcels-list'),
    path('test/', UserPlotsListView.as_view(), name='user-parcels-list'),
]