from argparse import ArgumentParser
from apscheduler.schedulers.blocking import BlockingScheduler
from dtAppFramework.app import AbstractApp
from dtAppFramework.settings import Settings
from .abstract_job import AbstractJob

import logging
import importlib


class AbstractSchedularApp(AbstractApp):

    def __init__(self, description=None, version=None, short_name=None, full_name=None, console_app=True) -> None:
        super().__init__(description=description, version=version, short_name=short_name, full_name=full_name,
                         console_app=console_app)
        self.scheduler = BlockingScheduler()
        self.jobs = []
        self.job_modules = []

    def define_args(self, arg_parser: ArgumentParser):
        pass

    def load_jobs(self):
        for job in Settings().get('jobs', []):
            if 'disabled' not in job or job['disabled']:
                logging.info(f'Loading Job: {job["name"]}')
                module = importlib.import_module(job["module"])
                if 'module_settings' in job:
                    job_module: AbstractJob = module.Job(job_name=job["name"], **job["module_settings"])
                else:
                    job_module: AbstractJob = module.Job(job_name=job["name"])

                job = self.scheduler.add_job(job_module.run, trigger=job['trigger'], id=job['name'], **job['schedule'])
                self.jobs.append(job)
                self.job_modules.append(job_module)

    def main(self, args):
        self.load_jobs()
        self.scheduler.start()
