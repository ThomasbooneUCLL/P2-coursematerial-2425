class Time:
    def __init__(self):
        self._hours = 0
        self._minutes = 0
        self._seconds = 0
    @hours.setter
    def hours(self,hours):
        if not(0 <= hours <= 23):
            raise ValueError ("It must be between 0 and 23")
        else:
            self._hours = hours
    @minutes.setter
    def minutes(self,minutes):
        if not(0 <= hours <= 59):
            raise ValueError ("It must be between 0 and 59")
        else:
            self._minutes = minutes
    @seconds.setter
    def seconds(self,seconds):
        if not(0 <= seconds <= 59):
            raise ValueError ("It must be between 0 and 59")
        else:
            self._seconds = seconds
    @property
    def hours(self):
        return self._hours
    @property
    def minutes(self):
        return self._minutes
    @property
    def seconds(self):
        return self._seconds
    
