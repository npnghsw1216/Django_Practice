from . import predict_lotto_numbers


def test_predict_lotto_numbers():
    assert predict_lotto_numbers.check_available("로또")
    assert predict_lotto_numbers.check_available("로또번호 점지해줘")

    candidate_numbers = [1, 2, 3, 4, 5, 6, 7]
    response_text = predict_lotto_numbers.make_response("", candidate_numbers)
    assert response_text == f"로또번호는 1, 2, 3, 4, 5, 6 이며, 보너스 번호는 7입니다."