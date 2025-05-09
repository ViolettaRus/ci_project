import pytest

def test_always_fail():
    """Этот тест всегда падает, чтобы проверить CI-уведомления."""
    assert False, "Этот тест упал намеренно (для проверки CI)"