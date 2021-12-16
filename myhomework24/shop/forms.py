import re

from django import forms

from shop.models import Tag, Shop


class ShopForm(forms.ModelForm):
    tags = forms.CharField()

    # 초기값 지정
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            tag_qs = self.instance.tag_set.all()
            initial = ",".join([tag.name for tag in tag_qs])
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

        self.instance.Tag_set.clear()
        self.instance.Tag_set.add(*tag_list)

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if content:
            # script 태그를 제거
            content = re.sub(
                r'<script.*?>.*?</script>',
                '',
                content,
                flags=re.I | re.S)
        return content

    class Meta:
        model = Shop
        fields = "__all__"
