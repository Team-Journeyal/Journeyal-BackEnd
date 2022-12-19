from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [

    path('user/', views.UserView.as_view(), name='user'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('calendar/<int:pk>/', views.CalendarDetail.as_view(),
         name='calendar-detail'),
    path('journal/', views.JournalView.as_view(), name='journal'),
    path('journal/<int:pk>/', views.JournalDetail.as_view(), name='journal-detail'),
    path("auth/users/me/avatar/", views.UserAvatarView.as_view(), name='user_avatar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
