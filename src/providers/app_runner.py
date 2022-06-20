import logging


class AppRunner:
    def __init__(self, start_date: str):
        # TODO use dependency injection here
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )
        self.start_date = start_date

    def run(self) -> str:
        return self.start_date
