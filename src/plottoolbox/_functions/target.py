"""Collection of functions for the manipulation of time series."""

import warnings

import gitmodules
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scienceplots
from toolbox_utils import tsutils

from .. import _plotutils
from .. import _skill_metrics as sm

matplotlib.use("Agg")


warnings.filterwarnings("ignore")


@tsutils.doc(_plotutils.ldocstrings)
def target(
    obs_col=1,
    sim_col=2,
    input_ts="-",
    columns=None,
    start_date=None,
    end_date=None,
    clean=False,
    skiprows=None,
    index_type="datetime",
    names=None,
    ofilename="plot.png",
    title="",
    figsize="10,6.0",
    legend=None,
    legend_names=None,
    colors="auto",
    linestyles="auto",
    markerstyles=" ",
    style="auto",
    por=False,
    round_index=None,
    source_units=None,
    target_units=None,
    plot_styles="bright",
    **kwds,
):
    r"""[obs column, sim N columns] Creates a "target" diagram to plot goodness of fit.

    "target" creates a target diagram that compares three goodness of fit
    statistics on one plot.  The three goodness of fit statistics calculated
    and displayed are bias, root mean square deviation, and centered root mean
    square deviation.  The data columns have to be organized as
    'observed,simulated1,simulated2,simulated3,...etc.'

    Parameters
    ----------
    obs_col
        If integer represents the column number of standard input. Can be
        If integer represents the column number of standard input. Can be
        a csv, wdm, hdf or xlsx file following format specified in
        'tstoolbox read ...'.
    sim_col
        If integer represents the column number of standard input. Can be
        a csv, wdm, hdf or xlsx file following format specified in
        'tstoolbox read ...'.
    ${input_ts}
    ${columns}
    ${start_date}
    ${end_date}
    ${clean}
    ${skiprows}
    ${index_type}
    ${names}
    ${ofilename}
    ${title}
    ${figsize}
    ${legend}
    ${legend_names}
    ${colors}
    ${linestyles}
    ${markerstyles}
    ${style}
    ${por}
    ${round_index}
    ${source_units}
    ${target_units}
    ${plot_styles}
    """

    # set up dataframe
    # Use dropna='no' to get the lengths of both time-series.
    tsd = tsutils.common_kwds(
        [tsutils.make_list(obs_col), tsutils.make_list(sim_col)],
        input_ts=input_ts,
        index_type=index_type,
        start_date=start_date,
        end_date=end_date,
        round_index=round_index,
        dropna="no",
        source_units=source_units,
        target_units=target_units,
        clean=clean,
    )
    if len(tsd.columns) != 2:
        raise ValueError(
            tsutils.error_wrapper(
                """
                The "target" requires only two time-series, the first one is
                the observed values and the second is the simulated.
                """
            )
        )

    # Need to work around some old option defaults with the implementation of
    # cltoolbox
    legend = legend == "" or legend == "True" or legend is None or legend is True

    # process styles: colors, linestyles, markerstyles
    (
        style,
        colors,
        linestyles,
        markerstyles,
        icolors,
        ilinestyles,
        imarkerstyles,
    ) = _plotutils.prepare_styles(
        len(tsd.columns), style, colors, linestyles, markerstyles
    )

    plot_styles = tsutils.make_list(plot_styles) + ["no-latex"]
    plt.style.use(plot_styles)

    figsize = tsutils.make_list(figsize, n=2)
    _, ax = plt.subplots(figsize=figsize)

    # Calculate statistics for target diagram
    target_stats1 = sm.target_statistics(data["pred1"], data["ref"], "data")
    target_stats2 = sm.target_statistics(data["pred2"], data["ref"], "data")
    target_stats3 = sm.target_statistics(data["pred3"], data["ref"], "data")

    # Store statistics in arrays
    bias = np.array(
        [target_stats1["bias"], target_stats2["bias"], target_stats3["bias"]]
    )
    crmsd = np.array(
        [target_stats1["crmsd"], target_stats2["crmsd"], target_stats3["crmsd"]]
    )
    rmsd = np.array(
        [target_stats1["rmsd"], target_stats2["rmsd"], target_stats3["rmsd"]]
    )

    """
    Produce the target diagram

    Reference circles are plotted at the maximum range of the axes and at 0.7
    times the maximum range by default.
    """
    sm.target_diagram(bias, crmsd, rmsd)
    #     biases = []
    #     rmsds = []
    #     crmsds = []
    #     ref = tsd.iloc[:, 0].values
    #     for col in range(1, len(tsd.columns)):
    #         biases.append(bias(tsd.iloc[:, col].values, ref))
    #         crmsds.append(centered_rms_dev(tsd.iloc[:, col].values, ref))
    #         rmsds.append(rmsd(tsd.iloc[:, col].values, ref))
    #     target_diagram(np.array(biases), np.array(crmsds), np.array(rmsds))

    plt.title(title)
    plt.tight_layout()
    if ofilename is not None:
        plt.savefig(ofilename)
    return plt
