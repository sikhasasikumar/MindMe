from django.contrib import admin
from django.urls import path

from reminder.views import ReminderList, ReminderCreate, ReminderDetail, ReminderUpdate, ReminderDelete

urlpatterns = [
    path('', ReminderList.as_view(), name='index'),
    path('new', ReminderCreate.as_view(), name='new-reminder'),
    path('<pk>', ReminderDetail.as_view(), name='view-reminder'),
    path('<pk>/edit', ReminderUpdate.as_view(), name='edit-reminder'),
    path('<pk>/delete', ReminderDelete.as_view(), name='del-reminder')
]
