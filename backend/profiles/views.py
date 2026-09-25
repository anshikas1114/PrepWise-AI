from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile


@login_required
def profile(request):
    user_profile, created = Profile.objects.get_or_create(
        user=request.user,
        defaults={
            'full_name': request.user.username
        }
    )

    if request.method == 'POST':
        user_profile.full_name = request.POST.get('full_name')
        user_profile.education = request.POST.get('education')
        user_profile.skills = request.POST.get('skills')
        user_profile.experience_level = request.POST.get('experience_level')
        user_profile.target_role = request.POST.get('target_role')
        user_profile.bio = request.POST.get('bio')

        user_profile.save()

        return redirect('profile')

    return render(
        request,
        'profiles/profile.html',
        {'profile': user_profile}
    )