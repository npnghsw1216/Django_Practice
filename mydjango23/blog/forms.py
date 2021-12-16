from django import forms
from blog.models import Post, Tag


class PostForm(forms.ModelForm):
    tags = forms.CharField()

    # 초기값 지정
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            tag_qs = self.instance.tag_set.all()
            initial = ","
            self.fields["tags"].initial = initial

    # DB로 저장
    # def save(self, commit=True)
    #     saved_post = super().save(commit)
    #
    #     return saved_post
    # 아래 함수가 호출되기 전에, instance.save()가 호출되었음을 보장 받는다.
    def _save_m2m(self):
        super()._save_m2m()

        tag_list = []
        tags = self.cleaned_data.get("tags", "")
        for word in tags.split(","):
            tag_name = word .strip()
            tag, __ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)

        self.instance.tag_set.clear()
        self.instance.tag_set.add(*tag_list)

    class Meta:
        model = Post
        fields = [
            "category",
            "title",
            "content",
            "photo",
            "status",
        ]
