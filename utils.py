import matplotlib.pyplot as plt
from typing import Tuple
import geopandas as gpd
from tqdm import tqdm

CB_SAFE_PALLETE = [
    "#377eb8",
    "#ff7f00",
    "#4daf4a",
    "#f781bf",
    "#a65628",
    "#984ea3",
    "#999999",
    "#e41a1c",
    "#dede00",
]


def dd2dms(deg):
    d = int(deg)
    md = abs(deg - d) * 60
    m = int(md)
    sd = (md - m) * 60
    return [d, m, sd]


def plot_rectangle_with_text(
    ax: plt.Axes,
    coords: Tuple[float, float],
    title: str,
    subtitle: str = "",
):
    width = 1.0
    height = 0.1
    fontsize_title = 45
    fontsize_subtitle = 15

    rectangle = plt.Rectangle(
        coords,
        width,
        height,
        facecolor="#ecedea",
        alpha=0.8,
        transform=ax.transAxes,
        zorder=2,
    )

    ax.add_patch(rectangle)
    rx, ry = rectangle.get_xy()
    cx = rx + rectangle.get_width() / 2.0
    cy = ry + rectangle.get_height() / 2.0

    ax.text(
        cx,
        cy,
        title,
        fontsize=fontsize_title,
        transform=ax.transAxes,
        horizontalalignment="center",
        verticalalignment="center",
        color="#2b2b2b",
    )

    ax.text(
        cx,
        cy - 0.038,
        subtitle,
        fontsize=fontsize_subtitle,
        transform=ax.transAxes,
        horizontalalignment="center",
        verticalalignment="center",
        color="#2b2b2b",
    )


def plot_poster(gdf: gpd.GeoDataFrame, city: str, country: str) -> plt.axes:
    centroid = gdf.dissolve().centroid.item()
    lat = dd2dms(centroid.y)
    lng = dd2dms(centroid.x)

    fig = plt.figure(figsize=(8.27, 11.69))
    ax = fig.add_subplot()
    ax.set_position([0, 0, 1, 1])

    gdf.dropna(subset=["water", "waterway"], how="all").plot(ax=ax, color="#a8e1e6")

    gdf.dropna(subset=["highway"], how="all").plot(
        ax=ax, color="#181818", markersize=0.1
    )

    plot_rectangle_with_text(
        ax,
        (0, 0.90),
        f"{abs(lat[0])}°{lat[1]}' {'N' if centroid.y >= 0 else 'S'}, {abs(lng[0])}°{lng[1]}' {'E' if centroid.x >= 0 else 'W'}",
    )
    plot_rectangle_with_text(ax, (0, 0.15), city, country)

    xmin, ymin, xmax, ymax = gdf.total_bounds
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    ax.set_axis_off()
    ax.add_patch(
        plt.Rectangle(
            (0, 0), 1, 1, facecolor="#ecedea", transform=ax.transAxes, zorder=-1
        )
    )

    ax.margins(0, 0)

    return ax


def map_flats(flats_value: str) -> int:
    try:
        flats = int(flats_value)
    except Exception:
        flats = 1

    return flats


def interpolate_spatial_data(regions, features, weight_column, result_column):
    for bsu in tqdm(regions.to_dict(orient="records")):
        matching_features = features[features.intersects(bsu["geometry"])]
        total_value = matching_features[weight_column].sum()
        for feature_index, feature_row in matching_features.iterrows():
            features.loc[feature_index, result_column] = bsu[result_column] * (
                feature_row[weight_column] / total_value
            )


def plot_population(buildings):
    import matplotlib.pyplot as plt

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8), dpi=300)
    buildings.plot("population", markersize=2, cmap="Spectral", alpha=0.1, ax=ax1)
    buildings.cx[14.42:14.47, 50.06:50.085].plot(
        "population", cmap="Spectral", markersize=4, ax=ax2
    )
    _ = ax1.axis("off"), ax2.axis("off"), fig.show()


def plot_market_share(regions, pois):
    from srai.plotting.folium_wrapper import _generate_linear_colormap

    brand_color_mapping = {
        "KFC": ("#fa9ea0", "#a3080c"),
        "McDonald's": ("#ffeec0", "#ffc72c"),
        "Starbucks": ("#88ffd6", "#00704A"),
        "Costa": ("#fe638a", "#74011e"),
        "Albert": ("#66c2a5", "#1b9e77"),
        "Billa": ("#fc8d62", "#d95f02"),
        "Kaufland": ("#8da0cb", "#7570b3"),
        "Lidl": ("#e78ac3", "#e7298a"),
        "PENNY": ("#a6d854", "#66a61e"),
        "Tesco": ("#ffd92f", "#e6ab02"),
    }

    prague_map = None

    for brand, colors in brand_color_mapping.items():
        regions_subset = regions[regions["brand"] == brand]
        if not len(regions_subset):
            continue
        colormap = _generate_linear_colormap(
            colors, min_value=0, max_value=regions_subset["population"].max()
        )
        colormap.caption = brand
        prague_map = regions_subset.explore(
            m=prague_map,
            column="population",
            cmap=colormap,
            tiles="CartoDB positron",
            style_kwds=dict(opacity=0.25, color=colors[1]),
        )

    prague_map = pois.explore(
        m=prague_map,
        marker_kwds=dict(radius=3),
        style_kwds=dict(color="#444", opacity=1, fillColor="#f2f2f2", fillOpacity=1),
    )

    return prague_map
