from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from nurse.models import NurseProfile
 

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
    NurseCreateUpdateSerializer,
    NurseListSerializer,
    NurseDetailSerializer, 
    )


#Creating an Nurse
class NurseCreateAPIView(CreateAPIView):
    queryset = NurseProfile.objects.all()
    serializer_class = NurseCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# Updating an report
class NurseUpdateAPIView(RetrieveUpdateAPIView):
    queryset = NurseProfile.objects.all()
    serializer_class = NurseCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

# Delete an Nurse
class NurseDeleteAPIView(DestroyAPIView):
    queryset = NurseProfile.objects.all()
    serializer_class = NurseDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

# Nurse Details
class NurseDetailAPIView(RetrieveAPIView):
    queryset = NurseProfile.objects.all()
    serializer_class = NurseDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

# All Nurses List
class NurseListAPIView(ListAPIView):
    serializer_class = NurseListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['role', 'years', 'rating', "qualification1", "qualification2", "qualification3", "description"]
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = NurseProfile.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(user_id=id)
        return queryset