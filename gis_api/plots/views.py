from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
from .models import Plot
from .serializers import PlotListSerializer, PlotSerializer
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class PlotCreateView(generics.CreateAPIView):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class PlotRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    # permission_classes = [IsOwner]

    def update(self, request, *args, **kwargs):
        return super(PlotRetrieveUpdateView, self).update(request, *args, **kwargs)


class PlotDeleteView(generics.DestroyAPIView):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    # permission_classes = [IsOwner]


class UserPlotsListView(generics.ListAPIView):
    serializer_class = PlotListSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # user = self.request.user
        # if user.is_authenticated:
            # return Plot.objects.filter(user=user)
        return Plot.objects.all()
