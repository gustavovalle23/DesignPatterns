class Budget(object):

    def __init__(self, value: float) -> None:
        self.__value: float = value

    @property
    def value(self) -> float:
        return self.__value
