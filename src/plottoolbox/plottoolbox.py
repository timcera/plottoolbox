"""Collection of functions for the manipulation of time series."""

import os.path as _osp
import sys as _sys

from cltoolbox import command as _command
from cltoolbox import main as _main
from toolbox_utils.tsutils import about as _about

from . import *

__all__ = [
    "autocorrelation",
    "bar",
    "bar_stacked",
    "barh",
    "barh_stacked",
    "bootstrap",
    "boxplot",
    "double_mass",
    "heatmap",
    "histogram",
    "kde",
    "kde_time",
    "lag_plot",
    "lognorm_xaxis",
    "lognorm_yaxis",
    "norm_xaxis",
    "norm_yaxis",
    "probability_density",
    "scatter_matrix",
    "target",
    "taylor",
    "time",
    "weibull_xaxis",
    "weibull_yaxis",
    "xy",
]


@_command()
def about():
    """Display version number and system information."""
    _about(__name__)


def _lmain():
    """Set debug and run cltoolbox.main function."""
    if not _osp.exists("debug_plottoolbox"):
        _sys.tracebacklimit = 0
    _main()


if __name__ == "__main__":
    _lmain()
