from rest_framework import generics, parsers, filters, status
from .models import User, Calendar, Journal
from .serializers import UserSerializer, CalendarSerializer, JournalSerializer, CalendarUsernameSerializer, TaggitSerializer, TagListSerializerField
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q, Count, Aggregate, Avg
from .permissions import IsOwner
from datetime import date, timedelta
from itertools import chain

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
        q = Journal.objects.all()
        q = Journal.objects.filter(
            calendar__owner__id=self.request.user.id)
        q = q.filter(calendar__owner=self.request.user).distinct()
        return q

    # def get_queryset(self):
    #     return Journal.objects.filter(Q(calendar__users__id=self.request.user.id) | Q(calendar__owner=self.request.user)).distinct()

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


class YearInReviewView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        q = Journal.objects.all()
        q = Journal.objects.filter(
            calendar__owner__id=self.request.user.id)
        q = q.filter(calendar__owner=self.request.user).distinct()
        q = q.filter(date__iso_year='2022')
        return q


class JanFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        q = Journal.objects.all()
        q = Journal.objects.filter(
            calendar__owner__id=self.request.user.id)
        q = q.filter(calendar__owner=self.request.user).distinct()
        q = q.filter(date__year='2022', date__month='1')
        return q


class FebFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date']

    def get_queryset(self):
        q = Journal.objects.all()
        q = Journal.objects.filter(
            calendar__owner__id=self.request.user.id)
        q = q.filter(calendar__owner=self.request.user).distinct()
        q = q.filter(date__year='2022', date__month='2')
        return q


class MarFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        q = Journal.objects.all()
        q = Journal.objects.filter(
            calendar__owner__id=self.request.user.id)
        q = q.filter(calendar__owner=self.request.user).distinct()
        q = q.filter(date__year='2022', date__month='3')
        return q


class AprFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        q = Journal.objects.all()
        q = Journal.objects.filter(
            calendar__owner__id=self.request.user.id)
        q = q.filter(calendar__owner=self.request.user).distinct()
        q = q.filter(date__year='2022', date__month='4')
        return q


class MayFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        q = Journal.objects.all()
        q = Journal.objects.filter(
            calendar__owner__id=self.request.user.id)
        q = q.filter(calendar__owner=self.request.user).distinct()
        q = q.filter(date__year='2022', date__month='5')
        return q


class JunFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        q = Journal.objects.all()
        q = Journal.objects.filter(
            calendar__owner__id=self.request.user.id)
        q = q.filter(calendar__owner=self.request.user).distinct()
        q = q.filter(date__year='2022', date__month='6')
        return q


class JulFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        q = Journal.objects.all()
        q = Journal.objects.filter(
            calendar__owner__id=self.request.user.id)
        q = q.filter(calendar__owner=self.request.user).distinct()
        q = q.filter(date__year='2022', date__month='7')
        return q


class AugFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        q = Journal.objects.all()
        q = Journal.objects.filter(
            calendar__owner__id=self.request.user.id)
        q = q.filter(calendar__owner=self.request.user).distinct()
        q = q.filter(date__year='2022', date__month='8')
        return q


class SepFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        q = Journal.objects.all()
        q = Journal.objects.filter(
            calendar__owner__id=self.request.user.id)
        q = q.filter(calendar__owner=self.request.user).distinct()
        q = q.filter(date__year='2022', date__month='9')
        return q


class OctFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        q = Journal.objects.all()
        q = Journal.objects.filter(
            calendar__owner__id=self.request.user.id)
        q = q.filter(calendar__owner=self.request.user).distinct()
        q = q.filter(date__year='2022', date__month='10')
        return q


class NovFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']

    def get_queryset(self):
        q = Journal.objects.all()
        q = Journal.objects.filter(
            calendar__owner__id=self.request.user.id)
        q = q.filter(calendar__owner=self.request.user).distinct()
        q = q.filter(date__year='2022', date__month='11')
        return q


class DecFilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['date']
    queryset = Journal.objects.all()

    def get_queryset(self):
        q = Journal.objects.all()
        q = Journal.objects.filter(
            calendar__owner__id=self.request.user.id)
        q = q.filter(calendar__owner=self.request.user).distinct()
        q = q.filter(date__year='2022', date__month='12')
        return q


class ThisDayAYearAgoView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer

    def get_queryset(self):
        todaysdate = date.today()
        datepast = todaysdate - timedelta(days=365)
        calendar_query = Calendar.objects.filter(
            journals__in=self.request.user.journals.all())
        queryset = Journal.objects.filter(
            date=datepast).filter(calendar__in=calendar_query)
        return queryset


# class JanRev(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = JournalSerializer
#     # filter_backends = [filters.OrderingFilter]
#     # ordering = ['date']
#     # queryset = Journal.objects.all()

#     def get_queryset(self):
#         q = Journal.objects.all()

#         return q

    # def get_queryset(self):
    #     q = Journal.tags.all()
    #     q = q.annotate(num_times=Count('name'))
    #     mydict = {}
    #     for tag in q:
    #         mydict[tag.name] = tag.num_times
        # q = Journal.taggit_taggeditem_items.filter(
        #     calendar__owner__id=self.request.user.id)
        # q = q.filter(calendar__owner=self.request.user).distinct()
        # q = q.filter(date__year='2022', date__month='12')
        # q = q.filter(tags).count()

    # def get_queryset(self):
    #     q = Journal.objects.all()
    #     q = Journal.objects.filter(
    #         calendar__owner__id=self.request.user.id)
    #     q = q.filter(calendar__owner=self.request.user).distinct()
    #     q = q.filter(date__year='2022', date__month='12')
    #     q = q.filter(tags).count()
    #     return q

    # 'taggit_taggeditem_items' into field. Choices are: calendar, calendar_id, date, entry, event, id, journal_files, journal_images, tagged_items, tags, user, user_id
