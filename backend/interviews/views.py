from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Interview, Response
from questions.models import Question


@login_required
def start_interview(request):
    if request.method == 'POST':
        interview_type = request.POST.get('interview_type')
        target_role = request.POST.get('target_role')
        difficulty = request.POST.get('difficulty')

        interview = Interview.objects.create(
            user=request.user,
            interview_type=interview_type,
            target_role=target_role,
            difficulty=difficulty
        )

        return redirect(
            'interview_session',
            interview_id=interview.id
        )

    return render(request, 'interviews/start_interview.html')


@login_required
def interview_session(request, interview_id):

    interview = get_object_or_404(
        Interview,
        id=interview_id,
        user=request.user
    )

    questions = Question.objects.filter(
        category=interview.interview_type,
        difficulty=interview.difficulty
    )

    if not questions.exists():
        return render(
            request,
            'interviews/no_questions.html',
            {'interview': interview}
        )

    question_number = request.session.get(
        f'interview_{interview.id}_question_number',
        0
    )

    if question_number >= questions.count():
        return redirect(
            'complete_interview',
            interview_id=interview.id
        )

    question = questions[question_number]

    if request.method == 'POST':
        answer = request.POST.get('answer', '').strip()

        Response.objects.create(
            interview=interview,
            question=question,
            answer=answer
        )

        request.session[
            f'interview_{interview.id}_question_number'
        ] = question_number + 1

        return redirect(
            'interview_session',
            interview_id=interview.id
        )

    return render(
        request,
        'interviews/interview_session.html',
        {
            'interview': interview,
            'question': question,
            'question_number': question_number + 1,
            'total_questions': questions.count(),
        }
    )
@login_required
def complete_interview(request, interview_id):
    interview = get_object_or_404(
        Interview,
        id=interview_id,
        user=request.user
    )

    interview.completed_at = timezone.now()

    responses = interview.responses.all()

    if responses.exists():
        total_score = sum(response.score for response in responses)
        interview.score = total_score / responses.count()
    else:
        interview.score = 0

    interview.save()

    request.session.pop(
        f'interview_{interview.id}_question_number',
        None
    )

    return render(
        request,
        'interviews/interview_complete.html',
        {'interview': interview}
    )