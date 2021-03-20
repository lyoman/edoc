from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from patient.models import PatientProfile
 

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
    PatientCreateUpdateSerializer,
    PatientListSerializer,
    PatientDetailSerializer, 
    )


#Creating an Patient
class PatientCreateAPIView(CreateAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an report
class PatientUpdateAPIView(RetrieveUpdateAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an Patient
class PatientDeleteAPIView(DestroyAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

# Patient Details
class PatientDetailAPIView(RetrieveAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

# All Patients List
class PatientListAPIView(ListAPIView):
    serializer_class = PatientListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["location"]
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = PatientProfile.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(user_id=id)
        return queryset