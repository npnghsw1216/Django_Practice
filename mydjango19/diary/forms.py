from django import forms
from django.core.validators import RegexValidator

# class PostForm(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField()
#     phone = forms.CharField(
#         validators=[
#             RegexValidator(r"^\d{3}-?\d{4}-?\d{4}$", message="휴대폰 번호를 입력해주세요."),
#         ]
#     )
from diary.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "author_name",
            "title",
            "content",
            "photo",
            "tag_set",
        ]



