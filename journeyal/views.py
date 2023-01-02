from rest_framework import generics, parsers, filters, status
from .models import User, Calendar, Journal
from .serializers import UserSerializer, CalendarSerializer, JournalSerializer, TaggitSerializer
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
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Calendar.objects.filter(Q(users=self.request.user) | Q(owner=self.request.user))


class CalendarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    permission_classes = [IsAuthenticated, IsOwner]


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
    queryset = Journal.objects.filter(date__iso_year=2022)

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id) | Q(calendar__owner=self.request.user))


class JanFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Journal.objects.filter(date__year='2022', date__month='1',)
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id) | Q(calendar__owner=self.request.user))


class FebFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Journal.objects.filter(date__year='2022', date__month='2',)
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id) | Q(calendar__owner=self.request.user))


class MarFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Journal.objects.filter(date__year='2022', date__month='3',)
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id) | Q(calendar__owner=self.request.user))


class AprFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Journal.objects.filter(date__year='2022', date__month='4',)
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id) | Q(calendar__owner=self.request.user))


class MayFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Journal.objects.filter(date__year='2022', date__month='5',)
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id) | Q(calendar__owner=self.request.user))


class JunFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Journal.objects.filter(date__year='2022', date__month='6',)
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id) | Q(calendar__owner=self.request.user))


class JulFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Journal.objects.filter(date__year='2022', date__month='7',)
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id) | Q(calendar__owner=self.request.user))


class AugFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Journal.objects.filter(date__year='2022', date__month='8',)
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id) | Q(calendar__owner=self.request.user))


class SepFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Journal.objects.filter(date__year='2022', date__month='9',)
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id) | Q(calendar__owner=self.request.user))


class OctFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Journal.objects.filter(date__year='2022', date__month='10',)
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id) | Q(calendar__owner=self.request.user))


class NovFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Journal.objects.filter(date__year='2022', date__month='11',)
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id) | Q(calendar__owner=self.request.user))


class DecFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Journal.objects.filter(date__year='2022', date__month='12',)
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        return Journal.objects.filter(Q(calendar__users__id=self.request.user.id) | Q(calendar__owner=self.request.user))


def get_queryset(self):
    return Calendar.objects.filter(Q(users=self.request.user) | Q(owner=self.request.user))
