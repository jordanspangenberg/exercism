from datetime import *
class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round(earthYears(self.seconds), 2)

    def on_mercury(self):
        return round(earthYears(self.seconds) / 0.2408467, 2)

    def on_venus(self):
        return round(earthYears(self.seconds) / 0.61519726, 2)

    def on_mars(self):
        return round(earthYears(self.seconds) / 1.8808158, 2)

    def on_jupiter(self):
        return round(earthYears(self.seconds) / 11.862615, 2)

    def on_saturn(self):
        return round(earthYears(self.seconds) / 29.447498, 2)

    def on_uranus(self):
        return round(earthYears(self.seconds) / 84.016846, 2)

    def on_neptune(self):
        return round(earthYears(self.seconds) / 164.79132, 2)


def earthYears(seconds):
    return seconds / 60 / 60 / 24 / 365.25
