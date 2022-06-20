"""Containers module."""

import logging.config

from dependency_injector import containers, providers

from src.providers.app_runner import AppRunner


class Core(containers.DeclarativeContainer):

    config = providers.Configuration()

    logging = providers.Resource(
        logging.config.dictConfig,
        config=config.logging,
    )


class Services(containers.DeclarativeContainer):

    config = providers.Configuration()

    app_runner = providers.Factory(AppRunner, config.app_runner.start_date_iso)


class Application(containers.DeclarativeContainer):

    config = providers.Configuration(
        yaml_files=["/Users/lajp/workspace/python/project-skeleton/src/config.yml"]
    )

    core = providers.Container(
        Core,
        config=config.core,
    )

    services = providers.Container(Services, config=config.services)
