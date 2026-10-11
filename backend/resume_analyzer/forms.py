
from pathlib import Path

from django import forms

from .models import Resume


class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ["title", "file"]

    def clean_file(self):
        uploaded_file = self.cleaned_data["file"]
        extension = Path(uploaded_file.name).suffix.lower()

        if extension not in [".pdf", ".docx"]:
            raise forms.ValidationError(
                "Please upload a PDF or DOCX resume."
            )

        if uploaded_file.size > 5 * 1024 * 1024:
            raise forms.ValidationError(
                "The resume must be 5 MB or smaller."
            )

        return uploaded_file