import pytest

@pytest.mark.fail_ci
def test_always_fail():
    assert False, "Этот тест падает намеренно (для проверки Telegram)"