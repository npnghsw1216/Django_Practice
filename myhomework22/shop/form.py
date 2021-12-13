from django import forms
from shop.models import Shop, Tag


class ShopForm(forms.ModelForm):
    tags = forms.CharField()

    # 부모 클래스의 생성자에서 어떤 인자를 지원하는 지는 잘 모르겠지만,
    # 생성자 호출 시에 받은 인자 그대로
    # 부모에게 전달하겠다.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # tags는 우리가 Form 클래스에 직접 추가한 필드니까
        # 초기값도 우리가 직접 지정해주어야 합니다.
        if self.instance.pk:
            tag_qs = self.instance.tag_set.all()
            tags = ",".join([tag.name for tag in tag_qs])
            self.fields["tags"].initial = tags
            pass
        # else:  # 새롭게 생성 시
        #     pass

    def save(self):
        # 부모의 save를 호출해주어야 한다.
        saved_post = super().save()

        #  부가적인 연산을 수행할 수 있다.
        tag_list = []
        tags = self.cleaned_data.get("tags", "")
        for word in tags.split(","):
            tag_name = word.strip()
            tag, __ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)

        saved_post.tag_set.clear()  # 간단구현을 위해 clear 호출
        saved_post.tag_set.add(*tag_list)

        return saved_post

    class Meta:
        model = Shop
        fields = [
            "category",
            "title",
            "content",
        ]
