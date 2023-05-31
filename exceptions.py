class NegativeTitlesError(Exception):
    def __init__(self) -> None:
        message = "titles cannot be negative"
        super().__init__(message)


class InvalidYearCupError(Exception):
    def __init__(self) -> None:
        message = "there was no world cup this year"
        super().__init__(message)


class ImpossibleTitlesError(Exception):
    def __init__(self) -> None:
        message = "impossible to have more titles than disputed cups"
        super().__init__(message)
