"""Define plottoolbox package."""

from toolbox_utils.tsutils import about as _about

from .cli.autocorrelation import autocorrelation
from .cli.bar import bar
from .cli.bar_stacked import bar_stacked
from .cli.barh import barh
from .cli.barh_stacked import barh_stacked
from .cli.bootstrap import bootstrap
from .cli.boxplot import boxplot
from .cli.double_mass import double_mass
from .cli.heatmap import heatmap
from .cli.histogram import histogram
from .cli.kde import kde
from .cli.kde_time import kde_time
from .cli.lag_plot import lag_plot
from .cli.lognorm_xaxis import lognorm_xaxis
from .cli.lognorm_yaxis import lognorm_yaxis
from .cli.norm_xaxis import norm_xaxis
from .cli.norm_yaxis import norm_yaxis
from .cli.probability_density import probability_density
from .cli.scatter_matrix import scatter_matrix
from .cli.target import target
from .cli.taylor import taylor
from .cli.time import time
from .cli.weibull_xaxis import weibull_xaxis
from .cli.weibull_yaxis import weibull_yaxis
from .cli.xy import xy


def about():
    """Display version number and system information."""
    _about(__name__)


__all__ = [
    "about",
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
