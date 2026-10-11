
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ResumeUploadForm


@login_required
def upload_resume(request):
    if request.method == "POST":
        form = ResumeUploadForm(request.POST, request.FILES)

        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()

            return redirect("upload_resume")
    else:
        form = ResumeUploadForm()

    return render(
        request,
        "resume_analyzer/upload.html",
        {"form": form}
    )