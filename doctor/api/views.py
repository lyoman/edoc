from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from doctor.models import DoctorRole
 

from django.db.models import Q

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)

from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,)


from .permissions import IsOwnerOrReadOnly

from .serializers import (
    DoctorCreateUpdateSerializer,
    DoctorListSerializer,
    DoctorDetailSerializer, 
    )


#Creating an Doctor
class DoctorCreateAPIView(CreateAPIView):
    queryset = DoctorRole.objects.all()
    serializer_class = DoctorCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an report
class DoctorUpdateAPIView(RetrieveUpdateAPIView):
    queryset = DoctorRole.objects.all()
    serializer_class = DoctorCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an Doctor
class DoctorDeleteAPIView(DestroyAPIView):
    queryset = DoctorRole.objects.all()
    serializer_class = DoctorDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

# Doctor Details
class DoctorDetailAPIView(RetrieveAPIView):
    queryset = DoctorRole.objects.all()
    serializer_class = DoctorDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

# All Doctors List
class DoctorListAPIView(ListAPIView):
    serializer_class = DoctorListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['role', 'years', 'rating', "qualification1", "qualification2", "qualification3", "description"]
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = DoctorRole.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(user_id=id)
        return queryset