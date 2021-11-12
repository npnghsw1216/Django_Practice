def check_available(received_text: str) -> bool:
    return received_text.startswith("거꾸로:")


def make_response(received_text: str) -> str:
    return received_text[4:][::-1].strip()