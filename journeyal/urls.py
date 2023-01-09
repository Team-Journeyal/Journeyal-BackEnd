from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [

    path('user/', views.UserView.as_view(), name='user'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('calendar/', views.CalendarListCreateView.as_view(), name='calendar'),
    path('calendar/<int:pk>/', views.CalendarDetail.as_view(),
         name='calendar-detail'),
    path('calendar/cover/<int:pk>/',
         views.CalCoverImageView.as_view(), name='calendar-cover'),
    path("calendar/users/", views.UserSearch.as_view(), name='user_search'),
    path('journal/', views.JournalView.as_view(), name='journal'),
    path('journal/<int:pk>/', views.JournalDetail.as_view(), name='journal-detail'),
    # path('image/', views.JournalImageView.as_view(), name='journal-image'),
    path("auth/users/me/avatar/", views.UserAvatarView.as_view(), name='user_avatar'),
    path('365/', views.ThisDayAYearAgoView.as_view(), name='365'),
    path('journal/YIR/', views.YearInReviewView.as_view(), name='YearInReview'),
    path('journal/Jan/', views.JanFilter.as_view(), name='MonthInReview'),
    path('journal/Feb/', views.FebFilter.as_view(), name='MonthInReview'),
    path('journal/Mar/', views.MarFilter.as_view(), name='MonthInReview'),
    path('journal/Apr/', views.AprFilter.as_view(), name='MonthInReview'),
    path('journal/May/', views.MayFilter.as_view(), name='MonthInReview'),
    path('journal/Jun/', views.JunFilter.as_view(), name='MonthInReview'),
    path('journal/Jul/', views.JulFilter.as_view(), name='MonthInReview'),
    path('journal/Aug/', views.AugFilter.as_view(), name='MonthInReview'),
    path('journal/Sep/', views.SepFilter.as_view(), name='MonthInReview'),
    path('journal/Oct/', views.OctFilter.as_view(), name='MonthInReview'),
    path('journal/Nov/', views.NovFilter.as_view(), name='MonthInReview'),
    path('journal/Dec/', views.DecFilter.as_view(), name='MonthInReview'),
    path('JanRev/', views.JanRev.as_view(), name='JanReview'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
