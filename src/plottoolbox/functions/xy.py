# -*- coding: utf-8 -*-
"""Collection of functions for the manipulation of time series."""

from __future__ import absolute_import, division, print_function

import itertools
import os
import warnings

import mando
import numpy as np
import pandas as pd
from mando.rst_text_formatter import RSTHelpFormatter
from tstoolbox import tsutils

from .. import plotutils

warnings.filterwarnings("ignore")


@mando.command("xy", formatter_class=RSTHelpFormatter, doctype="numpy")
@tsutils.doc(plotutils.ldocstrings)
def xy_cli(
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
    subplots=False,
    sharex=True,
    sharey=False,
    colors="auto",
    linestyles="auto",
    markerstyles=" ",
    bar_hatchstyles="auto",
    style="auto",
    logx=False,
    logy=False,
    xaxis="arithmetic",
    yaxis="arithmetic",
    xlim=None,
    ylim=None,
    secondary_y=False,
    mark_right=True,
    xy_match_line="",
    grid=False,
    label_rotation=None,
    label_skip=1,
    drawstyle="default",
    por=False,
    invert_xaxis=False,
    invert_yaxis=False,
    round_index=None,
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
):
    r"""Creates an 'x,y' plot, also known as a scatter plot.

    ${xydata}

    Parameters
    ----------
    ${input_ts}

    ofilename : str
        [optional, defaults to 'plot.png']

        Output filename for the plot.  Extension defines
        the type, for example 'filename.png' will create a PNG file.

        If used within Python, and `ofilename` is None will return the
        Matplotlib figure that can then be changed or added to as
        needed.

    xtitle : str
        [optional, default depends on ``type``]

        Title of x-axis.

    ytitle : str
        [optional, default depends on ``type``]

        Title of y-axis.

    title : str
        [optional, defaults to '']

        Title of chart.

    figsize : str
        [optional, defaults to '10,6.5']

        The 'width,height' of plot in inches.

    legend
        [optional, defaults to True]

        Whether to display the legend.

    legend_names : str
        [optional, defaults to None]

        Legend would normally use the time-series names associated with
        the input data.  The 'legend_names' option allows you to
        override the names in the data set.  You must supply a comma
        separated list of strings for each time-series in the data set.

    subplots
        [optional, defaults to False]

        Make separate subplots for each time series.

    sharex
        [optional, default to True]

        In case subplots=True, share x axis.

    sharey
        [optional, default to False]

        In case subplots=True, share y axis.

    colors
        [optional, default is 'auto']

        The default 'auto' will cycle through matplotlib colors in the chosen
        style.

        At the command line supply a comma separated matplotlib
        color codes, or within Python a list of color code strings.

        Can identify colors in four different ways.

        1. Use 'CN' where N is a number from 0 to 9 that gets the Nth color
        from the current style.

        2. Single character code from the table below.

        +------+---------+
        | Code | Color   |
        +======+=========+
        | b    | blue    |
        +------+---------+
        | g    | green   |
        +------+---------+
        | r    | red     |
        +------+---------+
        | c    | cyan    |
        +------+---------+
        | m    | magenta |
        +------+---------+
        | y    | yellow  |
        +------+---------+
        | k    | black   |
        +------+---------+

        3. Number between 0 and 1 that represents the level of gray, where 0 is
        white an 1 is black.

        4. Any of the HTML color names.

        +------------------+
        | HTML Color Names |
        +==================+
        | red              |
        +------------------+
        | burlywood        |
        +------------------+
        | chartreuse       |
        +------------------+
        | ...etc.          |
        +------------------+

        Color reference:
        http://matplotlib.org/api/colors_api.html

    linestyles
        [optional, default to 'auto']

        If 'auto' will iterate through the available matplotlib line types.
        Otherwise on the command line a comma separated list, or a list of
        strings if using the Python API.

        To not display lines use a space (' ') as the linestyle code.

        Separated 'colors', 'linestyles', and 'markerstyles' instead of using
        the 'style' keyword.

        +---------+--------------+
        | Code    | Lines        |
        +=========+==============+
        | ``-``   | solid        |
        +---------+--------------+
        | --      | dashed       |
        +---------+--------------+
        | -.      | dash_dot     |
        +---------+--------------+
        | :       | dotted       |
        +---------+--------------+
        | None    | draw nothing |
        +---------+--------------+
        | ' '     | draw nothing |
        +---------+--------------+
        | ''      | draw nothing |
        +---------+--------------+

        Line reference:
        http://matplotlib.org/api/artist_api.html

    markerstyles
        [optional, default to ' ']

        The default ' ' will not plot a marker.  If 'auto' will iterate through
        the available matplotlib marker types.  Otherwise on the command line
        a comma separated list, or a list of strings if using the Python API.

        Separated 'colors', 'linestyles', and 'markerstyles' instead of using
        the 'style' keyword.

        +-------+----------------+
        | Code  | Markers        |
        +=======+================+
        | .     | point          |
        +-------+----------------+
        | o     | circle         |
        +-------+----------------+
        | v     | triangle down  |
        +-------+----------------+
        | ^     | triangle up    |
        +-------+----------------+
        | <     | triangle left  |
        +-------+----------------+
        | >     | triangle right |
        +-------+----------------+
        | 1     | tri_down       |
        +-------+----------------+
        | 2     | tri_up         |
        +-------+----------------+
        | 3     | tri_left       |
        +-------+----------------+
        | 4     | tri_right      |
        +-------+----------------+
        | 8     | octagon        |
        +-------+----------------+
        | s     | square         |
        +-------+----------------+
        | p     | pentagon       |
        +-------+----------------+
        | ``*`` | star           |
        +-------+----------------+
        | h     | hexagon1       |
        +-------+----------------+
        | H     | hexagon2       |
        +-------+----------------+
        | ``+`` | plus           |
        +-------+----------------+
        | x     | x              |
        +-------+----------------+
        | D     | diamond        |
        +-------+----------------+
        | d     | thin diamond   |
        +-------+----------------+
        | _     | hlines_y       |
        +-------+----------------+
        | None  | nothing        |
        +-------+----------------+
        | ' '   | nothing        |
        +-------+----------------+
        | ''    | nothing        |
        +-------+----------------+

        Marker reference:
        http://matplotlib.org/api/markers_api.html

    style
        [optional, default is None]

        Still available, but if None is replaced by 'colors', 'linestyles', and
        'markerstyles' options.  Currently the 'style' option will override the
        others.

        Comma separated matplotlib style strings per time-series.  Just
        combine codes in 'ColorMarkerLine' order, for example 'r*--' is
        a red dashed line with star marker.

    bar_hatchstyles
        [optional, default to "auto", only used if type equal to "bar", "barh",
        "bar_stacked", and "barh_stacked"]

        If 'auto' will iterate through the available matplotlib hatch types.
        Otherwise on the command line a comma separated list, or a list of
        strings if using the Python API.

        +-----------------+-------------------+
        | bar_hatchstyles | Description       |
        +=================+===================+
        | /               | diagonal hatching |
        +-----------------+-------------------+
        | ``\``           | back diagonal     |
        +-----------------+-------------------+
        | ``|``           | vertical          |
        +-----------------+-------------------+
        | -               | horizontal        |
        +-----------------+-------------------+
        | +               | crossed           |
        +-----------------+-------------------+
        | x               | crossed diagonal  |
        +-----------------+-------------------+
        | o               | small circle      |
        +-----------------+-------------------+
        | O               | large circle      |
        +-----------------+-------------------+
        | .               | dots              |
        +-----------------+-------------------+
        | *               | stars             |
        +-----------------+-------------------+

    logx
        DEPRECATED: use '--xaxis="log"' instead.

    logy
        DEPRECATED: use '--yaxis="log"' instead.

    xlim
        [optional, default is based on range of x values]

        Comma separated lower and upper limits for the x-axis of the
        plot.  For example, '--xlim 1,1000' would limit the plot from
        1 to 1000, where '--xlim ,1000' would base the lower limit on
        the data and set the upper limit to 1000.

    ylim
        [optional, default is based on range of y values]

        Comma separated lower and upper limits for the y-axis of the
        plot.  See `xlim` for examples.

    xaxis : str
        [optional, default is 'arithmetic']

        Defines the type of the xaxis.  One of 'arithmetic', 'log'.

    yaxis : str
        [optional, default is 'arithmetic']

        Defines the type of the yaxis.  One of 'arithmetic', 'log'.

    secondary_y
        [optional, default is False]

        Whether to plot on the secondary y-axis. If a list/tuple, which
        time-series to plot on secondary y-axis.

    mark_right
        [optional, default is True]

        When using a secondary_y axis, should the legend label the axis of the
        various time-series automatically.

    xy_match_line : str
        [optional, defaults is '']

        Will add a match line where x == y. Set to a line style code.

    grid
        [optional, default is False]

        Whether to plot grid lines on the major ticks.

    label_rotation : int
        [optional]

        Rotation for major labels for bar plots.

    label_skip : int
        [optional]

        Skip for major labels for bar plots.

    drawstyle : str
        [optional, default is 'default']

        'default' connects the points with lines. The
        steps variants produce step-plots. 'steps' is equivalent to 'steps-pre'
        and is maintained for backward-compatibility.

        ACCEPTS::

         ['default' | 'steps' | 'steps-pre' | 'steps-mid' | 'steps-post']

    por
        [optional]

        Plot from first good value to last good value.  Strips NANs
        from beginning and end.

    invert_xaxis
        [optional, default is False]

        Invert the x-axis.

    invert_yaxis
        [optional, default is False]

        Invert the y-axis.

    ${columns}

    ${start_date}

    ${end_date}

    ${clean}

    ${skiprows}

    ${index_type}

    ${names}

    ${source_units}

    ${target_units}

    ${round_index}

    plot_styles: str
        [optional, default is "default"]

        Set the style of the plot.  One or more of Matplotlib styles "classic",
        "Solarize_Light2", "bmh", "dark_background", "fast", "fivethirtyeight",
        "ggplot", "grayscale", "seaborn", "seaborn-bright",
        "seaborn-colorblind", "seaborn-dark", "seaborn-dark-palette",
        "seaborn-darkgrid", "seaborn-deep", "seaborn-muted",
        "seaborn-notebook", "seaborn-paper", "seaborn-pastel",
        "seaborn-poster", "seaborn-talk", "seaborn-ticks", "seaborn-white",
        "seaborn-whitegrid", "tableau-colorblind10", and

        SciencePlots styles "science", "grid", "ieee", "scatter", "notebook",
        "high-vis", "bright", "vibrant", "muted", and "retro".

        If multiple styles then each over rides some or all of the
        characteristics of the previous.

        Color Blind Appropriate Styles

        The styles "seaborn-colorblind", "tableau-colorblind10", "bright",
        "vibrant", and "muted" are all styles that are setup to be able to be
        distinguished by someone with color blindness.

        Black, White, and Gray Styles

        The "ieee" style is appropriate for black, white, and gray, however the
        "ieee" also will change the chart size to fit in a column of the "IEEE"
        journal.

        The "grayscale" is another style useful for photo-copyable black,
        white, nd gray.

        Matplotlib styles:
            https://matplotlib.org/3.3.1/gallery/style_sheets/style_sheets_reference.html

        SciencePlots styles:
            https://github.com/garrettj403/SciencePlots

    hlines_y:
        [optional, defaults to None]

        Number or list of y values where to place a horizontal line.

    hlines_xmin:
        [optional, defaults to None]

        List of minimum x values to start the horizontal line.  If a list must
        be same length as `hlines_y`.  If a single number will be used as the
        minimum x values for all horizontal lines.  A missing value or None
        will start at the minimum x value for the entire plot.

    hlines_xmax:
        [optional, defaults to None]

        List of maximum x values to end each horizontal line.  If a list must
        be same length as `hlines_y`.  If a single number will be the maximum
        x value for all horizontal lines.  A missing value or None will end at
        the maximum x value for the entire plot.

    hlines_colors:
        [optional, defaults to None]

        List of colors for the horizontal lines.  If a single color then will
        be used as the color for all horizontal lines.  If a list must be same
        length as `hlines_y`.  If None will take from the color pallette in the
        current plot style.

    hlines_linestyles:
        [optional, defaults to None]

        List of linestyles for the horizontal lines.  If a single linestyle
        then will be used as the linestyle for all horizontal lines.  If a list
        must be same length as `hlines_y`.  If None will take for the standard
        linestyles list.

    vlines_x:
        [optional, defaults to None]

        List of x values where to place a vertical line.

    vlines_ymin:
        [optional, defaults to None]

        List of minimum y values to start the vertical line.  If a list must be
        same length as `vlines_x`.  If a single number will be used as the
        minimum x values for all vertical lines.  A missing value or None will
        start at the minimum x value for the entire plot.

    vlines_ymax:
        [optional, defaults to None]

        List of maximum x values to end each vertical line.  If a list must be
        same length as `vlines_x`.  If a single number will be the maximum
        x value for all vertical lines.  A missing value or None will end at
        the maximum x value for the entire plot.

    vlines_colors:
        [optional, defaults to None]

        List of colors for the vertical lines.  If a single color then will be
        used as the color for all vertical lines.  If a list must be same
        length as `vlines_x`.  If None will take from the color pallette in the
        current plot style.

    vlines_linestyles:
        [optional, defaults to None]

        List of linestyles for the vertical lines.  If a single linestyle then
        will be used as the linestyle for all vertical lines.  If a list must
        be same length as `vlines_x`.  If None will take for the standard
        linestyles list.
    """
    plt = xy(
        input_ts=input_ts,
        columns=columns,
        start_date=start_date,
        end_date=end_date,
        clean=clean,
        skiprows=skiprows,
        index_type=index_type,
        names=names,
        ofilename=ofilename,
        xtitle=xtitle,
        ytitle=ytitle,
        title=title,
        figsize=figsize,
        legend=legend,
        legend_names=legend_names,
        subplots=subplots,
        sharex=sharex,
        sharey=sharey,
        colors=colors,
        linestyles=linestyles,
        markerstyles=markerstyles,
        bar_hatchstyles=bar_hatchstyles,
        style=style,
        logx=logx,
        logy=logy,
        xaxis=xaxis,
        yaxis=yaxis,
        xlim=xlim,
        ylim=ylim,
        secondary_y=secondary_y,
        mark_right=mark_right,
        xy_match_line=xy_match_line,
        grid=grid,
        label_rotation=label_rotation,
        label_skip=label_skip,
        drawstyle=drawstyle,
        por=por,
        invert_xaxis=invert_xaxis,
        invert_yaxis=invert_yaxis,
        round_index=round_index,
        source_units=source_units,
        target_units=target_units,
        plot_styles=plot_styles,
        hlines_y=hlines_y,
        hlines_xmin=hlines_xmin,
        hlines_xmax=hlines_xmax,
        hlines_colors=hlines_colors,
        hlines_linestyles=hlines_linestyles,
        vlines_x=vlines_x,
        vlines_ymin=vlines_ymin,
        vlines_ymax=vlines_ymax,
        vlines_colors=vlines_colors,
        vlines_linestyles=vlines_linestyles,
    )


# @tsutils.validator(
#     ofilename=[str, ["pass", []], 1],
#     kind=[str, ["domain", ["xy",],], 1,],
#     xtitle=[str, ["pass", []], 1],
#     ytitle=[str, ["pass", []], 1],
#     title=[str, ["pass", []], 1],
#     figsize=[float, ["range", [0, None]], 2],
#     legend=[bool, ["domain", [True, False]], 1],
#     legend_names=[str, ["pass", []], 1],
#     subplots=[bool, ["domain", [True, False]], 1],
#     sharex=[bool, ["domain", [True, False]], 1],
#     sharey=[bool, ["domain", [True, False]], 1],
#     colors=[str, ["pass", []], None],
#     linestyles=[str, ["domain", ["auto", None, "", " ", "  "] + plotutils.LINE_LIST], None],
#     markerstyles=[str, ["domain", ["auto", None, "", " ", "  "] + plotutils.MARKER_LIST], None],
#     bar_hatchstyles=[str, ["domain", ["auto", None, "", " ", "  "] + plotutils.HATCH_LIST], None],
#     style=[str, ["pass", []], None],
#     xlim=[float, ["pass", []], 2],
#     ylim=[float, ["pass", []], 2],
#     xaxis=[str, ["domain", ["arithmetic", "log"]], 1],
#     yaxis=[str, ["domain", ["arithmetic", "log"]], 1],
#     secondary_y=[bool, ["domain", [True, False]], 1],
#     mark_right=[bool, ["domain", [True, False]], 1],
#     xy_match_line=[str, ["pass", []], 1],
#     grid=[bool, ["domain", [True, False]], 1],
#     label_rotation=[float, ["pass", []], 1],
#     label_skip=[int, ["range", [1, None]], 1],
#     drawstyle=[str, ["pass", []], 1],
#     por=[bool, ["domain", [True, False]], 1],
#     invert_xaxis=[bool, ["domain", [True, False]], 1],
#     invert_yaxis=[bool, ["domain", [True, False]], 1],
#     ],
#     plot_styles=[
#         str,
#         [
#             "domain",
#             [
#                 "classic",
#                 "Solarize_Light2",
#                 "bmh",
#                 "dark_background",
#                 "fast",
#                 "fivethirtyeight",
#                 "ggplot",
#                 "grayscale",
#                 "seaborn",
#                 "seaborn-bright",
#                 "seaborn-colorblind",
#                 "seaborn-dark",
#                 "seaborn-dark-palette",
#                 "seaborn-darkgrid",
#                 "seaborn-deep",
#                 "seaborn-muted",
#                 "seaborn-notebook",
#                 "seaborn-paper",
#                 "seaborn-pastel",
#                 "seaborn-poster",
#                 "seaborn-talk",
#                 "seaborn-ticks",
#                 "seaborn-white",
#                 "seaborn-whitegrid",
#                 "tableau-colorblind10",
#                 "science",
#                 "grid",
#                 "ieee",
#                 "scatter",
#                 "notebook",
#                 "high-vis",
#                 "bright",
#                 "vibrant",
#                 "muted",
#                 "retro",
#             ],
#         ],
#         None,
#     ],
#     hlines_y=[float, ["pass", []], None],
#     hlines_xmin=[float, ["pass", []], None],
#     hlines_xmax=[float, ["pass", []], None],
#     hlines_colors=[str, ["pass", []], None],
#     hlines_linestyles=[
#         str,
#         ["domain", ["auto", None, "", " ", "  "] + plotutils.LINE_LIST],
#         None,
#     ],
#     vlines_x=[float, ["pass", []], None],
#     vlines_ymin=[float, ["pass", []], None],
#     vlines_ymax=[float, ["pass", []], None],
#     vlines_colors=[str, ["pass", []], None],
#     vlines_linestyles=[
#         str,
#         ["domain", ["auto", None, "", " ", "  "] + plotutils.LINE_LIST],
#         None,
#     ],
# )
def xy(
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
    subplots=False,
    sharex=True,
    sharey=False,
    colors="auto",
    linestyles="auto",
    markerstyles=" ",
    bar_hatchstyles="auto",
    style="auto",
    logx=False,
    logy=False,
    xaxis="arithmetic",
    yaxis="arithmetic",
    xlim=None,
    ylim=None,
    secondary_y=False,
    mark_right=True,
    xy_match_line="",
    grid=False,
    label_rotation=None,
    label_skip=1,
    drawstyle="default",
    por=False,
    invert_xaxis=False,
    invert_yaxis=False,
    round_index=None,
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
    r"""Plot data."""
    # Need to work around some old option defaults with the implementation of
    # mando
    legend = bool(legend == "" or legend == "True" or legend is None)

    kind = "xy"

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FixedLocator

    tsd = tsutils.common_kwds(
        input_ts,
        skiprows=skiprows,
        names=names,
        index_type=index_type,
        start_date=start_date,
        end_date=end_date,
        pick=columns,
        round_index=round_index,
        dropna="all",
        source_units=source_units,
        target_units=target_units,
        clean=clean,
        por=por,
    )

    tsd, lnames = plotutils.check(kind, tsd, legend_names)

    if colors == "auto":
        colors = None
    else:
        colors = tsutils.make_list(colors)

    if linestyles == "auto":
        linestyles = plotutils.LINE_LIST
    else:
        linestyles = tsutils.make_list(linestyles)

    if bar_hatchstyles == "auto":
        bar_hatchstyles = plotutils.HATCH_LIST
    else:
        bar_hatchstyles = tsutils.make_list(bar_hatchstyles)

    if markerstyles == "auto":
        markerstyles = plotutils.MARKER_LIST
    else:
        markerstyles = tsutils.make_list(markerstyles)
        if markerstyles is None:
            markerstyles = " "

    if style != "auto":

        nstyle = tsutils.make_list(style)
        if len(nstyle) != len(tsd.columns):
            raise ValueError(
                tsutils.error_wrapper(
                    """
You have to have the same number of style strings as time-series to plot.
You supplied '{}' for style which has {} style strings,
but you have {} time-series.
""".format(
                        style, len(nstyle), len(tsd.columns)
                    )
                )
            )
        colors = []
        markerstyles = []
        linestyles = []
        for st in nstyle:
            colors.append(st[0])
            if len(st) == 1:
                markerstyles.append(" ")
                linestyles.append("-")
                continue
            if st[1] in plotutils.MARKER_LIST:
                markerstyles.append(st[1])
                try:
                    linestyles.append(st[2:])
                except IndexError:
                    linestyles.append(" ")
            else:
                markerstyles.append(" ")
                linestyles.append(st[1:])
    if linestyles is None:
        linestyles = [" "]
    else:
        linestyles = [" " if i in ["  ", None] else i for i in linestyles]
    markerstyles = [" " if i is None else i for i in markerstyles]

    if colors is not None:
        icolors = itertools.cycle(colors)
    else:
        icolors = None
    imarkerstyles = itertools.cycle(markerstyles)
    ilinestyles = itertools.cycle(linestyles)

    if xaxis == "log":
        logx = True
    if yaxis == "log":
        logy = True

    xlim = plotutils.know_your_limits(xlim, axis=xaxis)
    ylim = plotutils.know_your_limits(ylim, axis=yaxis)

    plot_styles = tsutils.make_list(plot_styles) + ["no-latex"]
    style_loc = os.path.join(
        os.path.dirname(__file__), os.pardir, "SciencePlots_styles"
    )
    plot_styles = [
        os.path.join(style_loc, i + ".mplstyle")
        if os.path.exists(os.path.join(style_loc, i + ".mplstyle"))
        else i
        for i in plot_styles
    ]
    plt.style.use(plot_styles)

    figsize = tsutils.make_list(figsize, n=2)
    _, ax = plt.subplots(figsize=figsize)

    if kind in ["xy", "double_mass"]:
        if tsd.shape[1] > 1:
            if tsd.shape[1] % 2 != 0:
                raise AttributeError(
                    tsutils.error_wrapper(
                        """
The 'xy' and 'double_mass' types must have an even number of columns arranged
as x,y pairs or an x-index and one y data column.  You supplied {} columns.
""".format(
                            tsd.shape[1]
                        )
                    )
                )
        colcnt = tsd.shape[1] // 2

    plotdict = {
        (False, True): ax.semilogy,
        (True, False): ax.semilogx,
        (True, True): ax.loglog,
        (False, False): ax.plot,
    }

    if kind in ["xy", "double_mass"]:
        # PANDAS was not doing the right thing with xy plots
        # if you wanted lines between markers.
        # Fell back to using raw matplotlib.
        # Boy I do not like matplotlib.

        for colindex in range(colcnt):
            if colcnt == 0:
                ndf = tsd.reset_index()
            else:
                ndf = tsd.iloc[:, colindex * 2 : colindex * 2 + 2]

            ndf.dropna(inplace=True)

            if kind == "double_mass":
                ndf.iloc[:, 0] = ndf.iloc[:, 0].cumsum()
                ndf.iloc[:, 1] = ndf.iloc[:, 1].cumsum()
            oxdata = np.array(ndf.iloc[:, 0])
            oydata = np.array(ndf.iloc[:, 1])

            if icolors is not None:
                c = next(icolors)
            else:
                c = None

            plotdict[(logx, logy)](
                oxdata,
                oydata,
                linestyle=next(ilinestyles),
                color=c,
                marker=next(imarkerstyles),
                label=lnames[colindex],
                drawstyle=drawstyle,
            )

        ax.set_xlim(xlim)
        ax.set_ylim(ylim)

        if legend is True:
            ax.legend(loc="best")

        if kind == "double_mass":
            xtitle = xtitle or "Cumulative {}".format(tsd.columns[0])
            ytitle = ytitle or "Cumulative {}".format(tsd.columns[1])

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
        plt.vlines(
            vlines_x,
            vlines_ymin,
            vlines_ymax,
            colors=vlines_colors,
            linestyles=vlines_linestyles,
        )

    if xy_match_line:
        if isinstance(xy_match_line, str):
            xymsty = xy_match_line
        else:
            xymsty = "g--"
        nxlim = ax.get_xlim()
        nylim = ax.get_ylim()
        maxt = max(nxlim[1], nylim[1])
        mint = min(nxlim[0], nylim[0])
        ax.plot([mint, maxt], [mint, maxt], xymsty, zorder=1)
        ax.set_ylim(nylim)
        ax.set_xlim(nxlim)

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


xy.__doc__ = xy_cli.__doc__
