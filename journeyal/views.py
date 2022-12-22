from rest_framework import generics, parsers, filters, status
from .models import User, Calendar, Journal
from .serializers import UserSerializer, CalendarSerializer, JournalSerializer, TaggitSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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
    # parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    permission_classes = []
    filter_backends = [filters.SearchFilter]
    search_fields = ['tags__name']
    def save(self, commit=True):
        instance = Journal.objects.tags
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except KeyError:
            error_data = {
                "error": "Please upload an image."
            }
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)


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


class CalCoverImageView(generics.UpdateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    parser_classes = [parsers.FileUploadParser]
    permission_classes = [IsAuthenticated]

# class JournalImageView(generics.UpdateAPIView):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
#     parser_classes = [parsers.MultiPartParser, parsers.FormParser]
#     permission_classes = [IsAuthenticated]
