from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Parcel
from .serializers import ParcelSerializer
from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class ParcelCreateView(generics.CreateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ParcelRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    permission_classes = [IsOwner]

    def update(self, request, *args, **kwargs):
        return super(ParcelRetrieveUpdateView, self).update(request, *args, **kwargs)

class ParcelDeleteView(generics.DestroyAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    permission_classes = [IsOwner]
    
class UserParcelsListView(generics.ListAPIView):
    serializer_class = ParcelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Parcel.objects.filter(user=user)
        return Parcel.objects.none()