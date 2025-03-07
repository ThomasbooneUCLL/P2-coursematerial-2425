class Duration:
    def __init__(self,from_seconds,from_minutes,from_hours):
        self.__from_seconds = from_seconds
        self.__from_minutes = from_minutes
        self.__from_hours = from_hours
    @property
    def seconds(self):
        return self.__from_seconds