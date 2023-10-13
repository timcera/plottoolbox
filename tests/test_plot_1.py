import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pytest

from plottoolbox import plottoolbox
from plottoolbox.toolbox_utils.src.toolbox_utils import tsutils

# Pull this in once.
idf = tsutils.common_kwds(input_tsd="tests/02234500_65_65.csv", clean=True)

df = idf.resample("D").agg("mean")

dfa = idf.resample("A").agg("mean")


@pytest.mark.mpl_image_compare(tolerance=6)
def test_time_plot():
    plt.close("all")
    return plottoolbox.time(
        columns=1,
        clean=True,
        input_ts="tests/02234500_65_65.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_time_multiple_traces_plot():
    plt.close("all")
    return plottoolbox.time(
        columns=[2, 3],
        style="b-,r*",
        input_ts="tests/data_daily_sample.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_time_multiple_traces_style_plot():
    plt.close("all")
    return plottoolbox.time(
        columns=[2, 3],
        style="b-,r  ",
        input_ts="tests/data_daily_sample.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_time_multiple_traces_new_style_plot():
    plt.close("all")
    return plottoolbox.time(
        columns=[2, 3],
        markerstyles=" ,*",
        linestyles="-, ",
        input_ts="tests/data_daily_sample.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_time_markers():
    plt.close("all")
    return plottoolbox.time(
        columns=[2, 3],
        linestyles=" ",
        markerstyles="auto",
        input_ts="tests/data_daily_sample.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_xy():
    plt.close("all")
    return plottoolbox.xy(
        clean=True,
        input_ts="tests/02234500_65_65.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_hexbin():
    plt.close("all")
    return plottoolbox.hexbin(
        clean=True,
        input_ts="tests/02234500_65_65.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_xy_multiple_traces():
    plt.close("all")
    return plottoolbox.xy(
        columns=[2, 3, 3, 2],
        input_ts="tests/data_daily_sample.csv",
        ofilename=None,
        plot_styles="classic",
    )


# @pytest.mark.mpl_image_compare(tolerance=6)
# def test_xy_multiple_traces_logy():
#    plt.close("all")
#    return plottoolbox.xy(
#        columns=[2, 3, 3, 2],
#        yaxis="log",
#        input_ts="tests/data_daily_sample.csv",
#        ofilename=None,
#        plot_styles="classic",
#    )


# @pytest.mark.mpl_image_compare(tolerance=6)
# def test_xy_multiple_traces_logx():
#    plt.close("all")
#    return plottoolbox.xy(
#        columns=[2, 3, 3, 2],
#        xaxis="log",
#        input_ts="tests/data_daily_sample.csv",
#        ofilename=None,
#        plot_styles="classic",
#    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_xy_multiple_traces_markers():
    plt.close("all")
    return plottoolbox.xy(
        columns=[2, 3, 3, 2],
        linestyles=" ",
        markerstyles="auto",
        input_ts="tests/data_daily_sample.csv",
        ofilename=None,
        plot_styles="classic",
    )
