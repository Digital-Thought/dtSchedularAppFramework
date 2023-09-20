import logging
from dtAppFramework.settings import Settings
from dtAppFramework.secrets_store import SecretsManager


class AbstractJob:

    def __init__(self, job_name) -> None:
        self.job_name = job_name
        self.settings = Settings()
        self.secrets_manager = SecretsManager()
        logging.info(f'Initialising {self.job_name}')

    def run(self):
        raise NotImplementedError
