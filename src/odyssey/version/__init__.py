from enum import Enum, unique, auto


@unique
class VersionType(Enum):
    PEP440 = auto()
    SemVer2_0 = auto()


class Version:
    def __init__(self, text: str = "1.0.0") -> None:
        self.text = text

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.text == other.text

        return False


def example() -> str:
    return "Hello, World!"
