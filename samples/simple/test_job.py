import sys
import os
import time

sys.path.append(os.path.abspath('../../src'))

from dtSchedularAppFramework.app import AbstractJob
from dtAppFramework.settings import Settings


class Job(AbstractJob):

    def __init__(self, job_name, message) -> None:
        super().__init__(job_name)
        self.message = message

    def run(self):
        print(self.message)