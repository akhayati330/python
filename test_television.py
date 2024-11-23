import pytest
from television import Television


def test_init():
    """Test the TV's initial settings."""
    tv = Television()
    assert str(tv) == "Power = Off, Channel = 0, Volume = 0"


def test_power():
    """Test turning the TV on and off."""
    tv = Television()
    tv.power()
    assert str(tv) == "Power = On, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = Off, Channel = 0, Volume = 0"


def test_mute():
    """Test muting and unmuting the TV."""
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = On, Channel = 0, Volume = Muted"
    tv.mute()
    assert str(tv) == "Power = On, Channel = 0, Volume = 1"


def test_channel_up():
    """Test increasing the channel and looping to the minimum."""
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = On, Channel = 1, Volume = 0"
    tv.channel_up()
    tv.channel_up()
    # Loop back to MIN_CHANNEL...
    tv.channel_up()
    assert str(tv) == "Power = On, Channel = 0, Volume = 0"


def test_channel_down():
    """Test decreasing the channel and looping to the maximum."""
    tv = Television()
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = On, Channel = 3, Volume = 0"


def test_volume_up():
    """Test increasing the volume and handling maximum volume."""
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = On, Channel = 0, Volume = 1"
    tv.volume_up()
    tv.volume_up()  # Try to stay at MAX_VOLUME
    assert str(tv) == "Power = On, Channel = 0, Volume = 2"


def test_volume_down():
    """Test decreasing the volume and handling minimum volume."""
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = On, Channel = 0, Volume = 0"
    tv.volume_down()  # Try to stay at MIN_VOLUME
    assert str(tv) == "Power = On, Channel = 0, Volume = 0"
