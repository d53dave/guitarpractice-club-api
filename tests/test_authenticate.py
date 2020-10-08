import pendulum

from . import authentication

authentication.settings.TOKEN_TIMEOUT_HOURS = 1


def test_is_expired():
    now = pendulum.now('utc')
    two_hours_ago = now.subtract(hours=2)
    assert not authentication._is_expired(now.int_timestamp)
    assert authentication._is_expired(two_hours_ago.int_timestamp)
