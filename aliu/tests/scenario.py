"""Set-up the default scenario for demo and testing purposes."""

import os

from aliu.service import FtpReader


def default_scenario_aliu():
    """Default scenario for the academy."""
    folder = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'data',
        'ftp_static_dir',
    )
    FtpReader(folder).update()
