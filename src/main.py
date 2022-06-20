"""Main module."""

from dependency_injector.wiring import Provide, inject

from src.providers.app_runner import AppRunner
from src.registration.containers import Application


@inject
def main(app_runner: AppRunner = Provide[Application.services.app_runner]) -> None:
    app_runner.run()


if __name__ == "__main__":
    application = Application()
    application.init_resources()
    application.wire(modules=[__name__])
    main()
