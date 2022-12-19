from rest_framework import generics, parsers, filters
from .models import User, Calendar, Journal
from .serializers import UserSerializer, CalendarSerializer, JournalSerializer, TaggitSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []


class CalendarView(generics.ListCreateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    permission_classes = []

    def get_queryset(self):
        return Calendar.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CalendarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    permission_classes = []


class JournalView(generics.ListCreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = []
    filter_backends = [filters.SearchFilter]
    search_fields = ['tags__name']


class JournalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = []


class UserAvatarView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [parsers.FileUploadParser]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
