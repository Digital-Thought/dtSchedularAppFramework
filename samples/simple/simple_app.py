import sys
import os
import time

sys.path.append(os.path.abspath('../../src'))

from dtSchedularAppFramework.app import AbstractSchedularApp
from dtAppFramework.settings import Settings


class SimpleApp(AbstractSchedularApp):

    def define_args(self, arg_parser):
        pass


if __name__ == "__main__":
    os.environ['DEV_MODE'] = "True"
    SimpleApp(description="Simple App showing paths in Dev Mode", version="1.0", short_name="simple_dev_app",
                 full_name="Simple Development Application", console_app=True).run()
