from model.predict import predict


def test_basic():
    excepted = 1
    actual = predict(3)
    assert actual == excepted
