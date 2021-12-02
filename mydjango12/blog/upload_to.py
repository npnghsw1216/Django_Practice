import os
from uuid import uuid4
from django.utils import timezone


def uuid_name_upload_to(instance, filename):
    app_label = instance.__class__._meta.app_label      # 앱 이름을 디렉토리 경로명으로 사용
    cls_name = instance.__class__.__name__.lower()      # 모델 이름을 디렉토리 경로명으로 사용
    ymd_path = timezone.now().strftime("%Y/%m/%d")      # 업로드하는 년/월/일을 디렉토리 경로명으로 사용
    uuid_name = uuid4().hex                             # 16진수 포맷의 랜덤한 32글자 문자열
    extension = os.path.splitext(filename)[-1].lower()  # 확장자 추출하고, 소문자로 변환. ex) ".jpg"
    return "/".join(
        [
            app_label,
            cls_name,
            ymd_path,
            uuid_name[:2],  # uuid의 처음 2문자를 별도 디렉토리 명으로 사용
            uuid_name + extension,
        ]
    )