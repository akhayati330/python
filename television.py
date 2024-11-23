class Television:
    # My class constants for volume and channel limits
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Set up the TV with default settings."""
        # TV is off
        self.__status = False
        # TV is not muted
        self.__muted = False
        # Start at minimum volume
        self.__volume = Television.MIN_VOLUME
        # Start at minimum channel
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """Turn the TV on or off."""
        self.__status = not self.__status

    def mute(self):
        """Mute or unmute the TV (only works when the TV is on)."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """Increase the channel (loops to MIN_CHANNEL if MAX_CHANNEL is reached)."""
        # Try to only change channels if the TV is on
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """Decrease the channel (loops to MAX_CHANNEL if MIN_CHANNEL is reached)."""
        # Try to only change channels if the TV is on
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """Increase the volume (unmutes if muted)."""
        if self.__status:
            # Unmute first
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """Decrease the volume (unmutes if muted)."""
        if self.__status:
            # Unmute first
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """Show the current state of the TV."""
        power_status = "On" if self.__status else "Off"
        volume_display = "Muted" if self.__muted else self.__volume
        return f"Power = {power_status}, Channel = {self.__channel}, Volume = {volume_display}"