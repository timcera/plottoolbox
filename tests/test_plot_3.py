import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import pytest

from plottoolbox import plottoolbox
from plottoolbox.toolbox_utils.src.toolbox_utils import tsutils

# Pull this in once.
idf = tsutils.common_kwds(input_tsd="tests/02234500_65_65.csv", clean=True)

df = idf.resample("D").agg("mean")

dfa = idf.resample("A").agg("mean")


@pytest.mark.mpl_image_compare(tolerance=6)
def test_histogram():
    plt.close("all")
    return plottoolbox.histogram(
        clean=True,
        input_ts="tests/02234500_65_65.csv",
        ofilename=None,
        sharex=False,
        plot_styles="classic",
    )


# @pytest.mark.mpl_image_compare(tolerance=6)
# def test_heatmap():
#     plt.close("all")
#     return plottoolbox.heatmap(
#         columns=2,
#         clean=True,
#         input_ts=df,
#         ofilename=None,
#         plot_styles="classic",
#     )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_norm_xaxis():
    plt.close("all")
    return plottoolbox.norm_xaxis(
        columns=2,
        clean=True,
        input_ts="tests/02234500_65_65.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_norm_yaxis():
    plt.close("all")
    return plottoolbox.norm_yaxis(
        columns=2,
        clean=True,
        input_ts="tests/02234500_65_65.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_lognorm_xaxis():
    plt.close("all")
    return plottoolbox.lognorm_xaxis(
        columns=2,
        clean=True,
        input_ts="tests/02234500_65_65.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_lognorm_yaxis():
    plt.close("all")
    return plottoolbox.lognorm_yaxis(
        columns=2,
        clean=True,
        input_ts="tests/02234500_65_65.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_weibull_xaxis():
    plt.close("all")
    return plottoolbox.weibull_xaxis(
        columns=2,
        clean=True,
        input_ts="tests/02234500_65_65.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_weibull_yaxis():
    plt.close("all")
    return plottoolbox.weibull_yaxis(
        columns=2,
        clean=True,
        input_ts="tests/02234500_65_65.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_kde_time():
    plt.close("all")
    return plottoolbox.kde_time(
        columns=2,
        clean=True,
        input_ts="tests/02234500_65_65.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_kde_time_multiple_traces():
    plt.close("all")
    ndf = pd.read_csv("tests/data_daily.csv", index_col=0, parse_dates=True)
    ndf = ndf.join(
        pd.read_csv("tests/data_02325000_flow.csv", index_col=0, parse_dates=True),
        how="outer",
    )
    return plottoolbox.kde_time(
        columns=[2, 3],
        clean=True,
        input_ts=ndf,
        ytitle="Flow",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_autocorrelation():
    plt.close("all")
    return plottoolbox.autocorrelation(
        columns=2,
        input_ts=df,
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_taylor():
    plt.close("all")
    return plottoolbox.taylor(
        clean=True,
        input_ts="tests/02234500_65_65.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_target():
    plt.close("all")
    return plottoolbox.target(
        clean=True,
        input_ts="tests/02234500_65_65.csv",
        ofilename=None,
        plot_styles="classic",
    )


@pytest.mark.mpl_image_compare(tolerance=6)
def test_waterfall():
    plt.close("all")
    df = (
        pd.read_csv(
            "tests/02234500_65_65.csv", index_col=0, parse_dates=True, usecols=[0, 1]
        )
        .resample("Y")
        .agg("mean")
    )
    return plottoolbox.waterfall(
        clean=True,
        input_ts=df,
        ofilename=None,
        plot_styles="classic",
    )
