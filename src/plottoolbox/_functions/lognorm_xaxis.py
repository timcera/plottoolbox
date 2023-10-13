"""Collection of functions for the manipulation of time series."""

import sys
import warnings
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FixedLocator

from plottoolbox.toolbox_utils.src.toolbox_utils import tsutils

from .. import _plotutils

sys.path.append(str(Path(__file__).parent / ".." / "SciencePlots"))
import scienceplots

matplotlib.use("Agg")

warnings.filterwarnings("ignore")


@tsutils.doc(_plotutils.ldocstrings)
def lognorm_xaxis(
    input_ts="-",
    columns=None,
    start_date=None,
    end_date=None,
    clean=False,
    skiprows=None,
    index_type="datetime",
    names=None,
    ofilename="plot.png",
    xtitle="",
    ytitle="",
    title="",
    figsize="10,6.0",
    legend=None,
    legend_names=None,
    colors="auto",
    linestyles="auto",
    markerstyles=" ",
    style="auto",
    xaxis="arithmetic",
    yaxis="arithmetic",
    xlim=None,
    ylim=None,
    grid=False,
    drawstyle="default",
    por=False,
    invert_xaxis=False,
    invert_yaxis=False,
    round_index=None,
    dropna="all",
    plotting_position="weibull",
    prob_plot_sort_values="descending",
    source_units=None,
    target_units=None,
    plot_styles="bright",
    hlines_y=None,
    hlines_xmin=None,
    hlines_xmax=None,
    hlines_colors=None,
    hlines_linestyles="-",
    vlines_x=None,
    vlines_ymin=None,
    vlines_ymax=None,
    vlines_colors=None,
    vlines_linestyles="-",
    **kwds,
):
    r"""[N columns] Log-normal x-axis.

    "lognorm_yaxis" will sort, calculate probabilities, and plot data against
    a y axis lognormal distribution.

    Parameters
    ----------
    ${input_ts}
    ${columns}
    ${start_date}
    ${end_date}
    ${clean}
    ${skiprows}
    ${index_type}
    ${names}
    ${ofilename}
    ${xtitle}
    ${ytitle}
    ${title}
    ${figsize}
    ${legend}
    ${legend_names}
    ${colors}
    ${linestyles}
    ${markerstyles}
    ${style}
    ${xaxis}
    ${yaxis}
    ${xlim}
    ${ylim}
    ${grid}
    ${drawstyle}
    ${por}
    ${invert_xaxis}
    ${invert_yaxis}
    ${round_index}
    ${plotting_position}
    ${prob_plot_sort_values}
    ${source_units}
    ${target_units}
    ${plot_styles}
    ${hlines_y}
    ${hlines_xmin}
    ${hlines_xmax}
    ${hlines_colors}
    ${hlines_linestyles}
    ${vlines_x}
    ${vlines_ymin}
    ${vlines_ymax}
    ${vlines_colors}
    ${vlines_linestyles}
    """

    # set up dataframe
    tsd = tsutils.common_kwds(
        input_ts,
        skiprows=skiprows,
        names=names,
        index_type=index_type,
        start_date=start_date,
        end_date=end_date,
        pick=columns,
        round_index=round_index,
        dropna=dropna,
        source_units=source_units,
        target_units=target_units,
        clean=clean,
        por=por,
    )

    # Need to work around some old option defaults with the implementation of
    # cltoolbox
    legend = legend == "" or legend == "True" or legend is None or legend is True
    plottype = "lognorm_xaxis"
    lnames = tsutils.make_list(legend_names)
    tsd, lnames = _plotutils.check_column_legend(plottype, tsd, lnames)

    # check axis scales
    logx = xaxis == "log"
    logy = yaxis == "log"
    xaxis = "normal"
    if logx:
        logx = False
        warnings.warn(
            tsutils.error_wrapper(
                f"""
                The plot type {plottype} cannot also have the xaxis set to
                {yaxis}. The {yaxis} setting for xaxis is ignored.
                """
            )
        )
    xlim = _plotutils.know_your_limits(xlim, axis=xaxis)
    ylim = _plotutils.know_your_limits(ylim, axis=yaxis)

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

    colcnt = tsd.shape[1]

    plotdict = {
        (False, True): ax.semilogy,
        (True, False): ax.semilogx,
        (True, True): ax.loglog,
        (False, False): ax.plot,
    }

    ppf = tsutils.set_ppf(plottype.split("_", maxsplit=1)[0])
    ys = tsd.iloc[:, :]

    for colindex in range(colcnt):
        oydata = np.array(ys.iloc[:, colindex].dropna())
        if prob_plot_sort_values == "ascending":
            oydata = np.sort(oydata)
        elif prob_plot_sort_values == "descending":
            oydata = np.sort(oydata)[::-1]
        n = len(oydata)

        norm_axis = ax.xaxis
        oxdata = ppf(tsutils.set_plotting_position(n, plotting_position))

        c = next(icolors) if icolors is not None else None
        plotdict[(logx, logy)](
            oxdata,
            oydata,
            linestyle=next(ilinestyles),
            color=c,
            marker=next(imarkerstyles),
            label=lnames[colindex],
            drawstyle=drawstyle,
        )

    # Make it pretty
    xtmaj = np.array([0.01, 0.1, 0.5, 0.9, 0.99])
    xtmaj_str = ["1", "10", "50", "90", "99"]
    xtmin = np.concatenate(
        [
            np.linspace(0.001, 0.01, 10),
            np.linspace(0.01, 0.1, 10),
            np.linspace(0.1, 0.9, 9),
            np.linspace(0.9, 0.99, 10),
            np.linspace(0.99, 0.999, 10),
        ]
    )
    xtmaj = ppf(xtmaj)
    xtmin = ppf(xtmin)

    norm_axis.set_major_locator(FixedLocator(xtmaj))
    norm_axis.set_minor_locator(FixedLocator(xtmin))

    ax.set_xticklabels(xtmaj_str)
    ax.set_ylim(ylim)
    ax.set_xlim(ppf(xlim))

    xtitle = xtitle or "Log Normal Distribution"
    ytitle = ytitle or tsd.columns[0]

    if legend:
        ax.legend(loc="best")

    if hlines_y is not None:
        hlines_y = tsutils.make_list(hlines_y)
        hlines_xmin = tsutils.make_list(hlines_xmin)
        hlines_xmax = tsutils.make_list(hlines_xmax)
        hlines_colors = tsutils.make_list(hlines_colors)
        hlines_linestyles = tsutils.make_list(hlines_linestyles)
        nxlim = ax.get_xlim()
        if hlines_xmin is None:
            hlines_xmin = nxlim[0]
        if hlines_xmax is None:
            hlines_xmax = nxlim[1]
    if vlines_x is not None:
        vlines_x = tsutils.make_list(vlines_x)
        vlines_ymin = tsutils.make_list(vlines_ymin)
        vlines_ymax = tsutils.make_list(vlines_ymax)
        vlines_colors = tsutils.make_list(vlines_colors)
        vlines_linestyles = tsutils.make_list(vlines_linestyles)
        nylim = ax.get_ylim()
        if vlines_ymin is None:
            vlines_ymin = nylim[0]
        if vlines_ymax is None:
            vlines_ymax = nylim[1]
    if hlines_y is not None:
        plt.hlines(
            hlines_y,
            hlines_xmin,
            hlines_xmax,
            colors=hlines_colors,
            linestyles=hlines_linestyles,
        )
    if vlines_x is not None:
        vlines_x = ppf(tsutils.make_list(vlines_x))
        plt.vlines(
            vlines_x,
            vlines_ymin,
            vlines_ymax,
            colors=vlines_colors,
            linestyles=vlines_linestyles,
        )

    plt.xlabel(xtitle)
    plt.ylabel(ytitle)

    if invert_xaxis is True:
        plt.gca().invert_xaxis()
    if invert_yaxis is True:
        plt.gca().invert_yaxis()

    plt.grid(grid)

    plt.title(title)
    plt.tight_layout()
    if ofilename is not None:
        plt.savefig(ofilename)
    return plt
