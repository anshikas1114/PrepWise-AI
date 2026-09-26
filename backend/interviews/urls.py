from django.urls import path

from .views import start_interview, interview_session, complete_interview


urlpatterns = [
    path(
        'start/',
        start_interview,
        name='start_interview'
    ),

    path(
        '<int:interview_id>/',
        interview_session,
        name='interview_session'
    ),

    path(
    '<int:interview_id>/complete/',
    complete_interview,
    name='complete_interview'
    ),
]