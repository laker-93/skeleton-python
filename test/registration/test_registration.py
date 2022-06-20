import unittest
from datetime import datetime

from dependency_injector.wiring import Provide, inject

from src.providers.app_runner import AppRunner
from src.registration.containers import Application


# must run the test from the class level, rather than individual test cases
class TestStrategy(unittest.TestCase):
    def setUp(self) -> None:
        application = Application()
        application.init_resources()
        application.wire(modules=[__name__])

    @inject
    def test_bot(self, app_runner: AppRunner = Provide[Application.services.app_runner]):
        start_date = app_runner.run()
        self.assertEqual(start_date, '2021-01-01')
