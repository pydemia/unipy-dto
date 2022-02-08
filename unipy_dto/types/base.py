from enum import Enum, unique


__all__ = [
    "BaseEnum",
]


@unique
class BaseEnum(Enum):

    def __init__(self, type):
        # self._value_ = code
        self.type = type

    @classmethod
    @property
    def describe(self):
        # self is the member here
        return self.name, self.value

    def __new__(cls, type):
        obj = object.__new__(cls)
        # obj._value_ = code
        obj.type = type
        # cls = self.__class__
        # if any(type == e.value for e in cls):
        #     a = self.name
        #     e = cls(self.type).name
        #     raise ValueError(
        #         "aliases not allowed to prevent duplicatation:  %r --> %r"
        #         % (a, e))

        return obj

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def _missing_(cls, type):
        if isinstance(type, str):
            for item in cls:
                if item.value.lower() == type.lower():
                    return item
        else:
            for item in cls:
                if item.value == type:
                    return item

    def ignore_case(self) -> str:
        return str(self.value).lower()

    @classmethod
    def of(cls, type):
        return cls._missing_(type)


def trim_error_msg(s: str):
    return s[:10_000]
