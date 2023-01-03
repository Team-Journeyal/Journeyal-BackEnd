from rest_framework import generics, parsers, filters, status
from .models import User, Calendar, Journal
from .serializers import UserSerializer, CalendarSerializer, JournalSerializer, CalendarUsernameSerializer, TaggitSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from .permissions import IsOwner

# Create your views here.


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class CalendarListCreateView(generics.ListCreateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['name']
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Calendar.objects.filter(Q(users=self.request.user) | Q(owner=self.request.user)).distinct()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CalendarUsernameSerializer
        return self.serializer_class


class CalendarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CalendarUsernameSerializer
        return self.serializer_class


class JournalView(generics.ListCreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    # parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['tags__name']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id) | Q(calendar__owner=self.request.user))

    def save(self, commit=True):
        instance = Journal.objects.tags

    # def create(self, request, *args, **kwargs):
    #     try:
    #         return super().create(request, *args, **kwargs)
    #     except KeyError:
    #         error_data = {
    #             "error": "Please upload an image."
    #         }
    #         return Response(error_data, status=status.HTTP_400_BAD_REQUEST)


class JournalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [IsAuthenticated]


class UserAvatarView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [parsers.FileUploadParser]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserSearch(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']


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


class YearInReviewView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id, date__iso_year='2022') | Q(calendar__owner=self.request.user, date__iso_year='2022'))


class JanFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id, date__year='2022', date__month='01') | Q(calendar__owner=self.request.user, date__year='2022', date__month='01'))


class FebFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id, date__year='2022', date__month='02') | Q(calendar__owner=self.request.user, date__year='2022', date__month='02'))


class MarFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id, date__year='2022', date__month='03') | Q(calendar__owner=self.request.user, date__year='2022', date__month='03'))


class AprFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id, date__year='2022', date__month='04') | Q(calendar__owner=self.request.user, date__year='2022', date__month='04'))


class MayFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id, date__year='2022', date__month='05') | Q(calendar__owner=self.request.user, date__year='2022', date__month='05'))


class JunFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id, date__year='2022', date__month='06') | Q(calendar__owner=self.request.user, date__year='2022', date__month='06'))


class JulFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id, date__year='2022', date__month='07') | Q(calendar__owner=self.request.user, date__year='2022', date__month='07'))


class AugFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id, date__year='2022', date__month='08') | Q(calendar__owner=self.request.user, date__year='2022', date__month='08'))


class SepFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id, date__year='2022', date__month='09') | Q(calendar__owner=self.request.user, date__year='2022', date__month='09'))


class OctFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id, date__year='2022', date__month='10') | Q(calendar__owner=self.request.user, date__year='2022', date__month='10'))


class NovFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id, date__year='2022', date__month='11') | Q(calendar__owner=self.request.user, date__year='2022', date__month='11'))


class DecFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id, date__year='2022', date__month='12') | Q(calendar__owner=self.request.user, date__year='2022', date__month='12'))
