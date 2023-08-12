"""
This is a boilerplate pipeline 'visualizations'
generated using Kedro 0.18.7
"""
from typing import Any, Dict, List, Tuple

import contextily as ctx
import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.figure import Figure
from scipy.cluster.hierarchy import cut_tree, dendrogram
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from tqdm.auto import tqdm


MAP_SOURCE = ctx.providers.CartoDB.Positron
MATPLOTLIB_COLORMAP = "tab20"
PLOTLY_COLORMAP = list(
    map(
        lambda color: f"rgb{tuple(map(lambda color_compound: color_compound * 255, color))}",
        matplotlib.colormaps[MATPLOTLIB_COLORMAP].colors,
    )
)


def scale_embeddings(embeddings: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        StandardScaler().fit_transform(embeddings),
        index=embeddings.index,
        columns=embeddings.columns,
    )


def generate_clustering_model(
    embeddings: pd.DataFrame, clustering_params: Dict[str, Any]
):
    model = AgglomerativeClustering(
        n_clusters=clustering_params["n_clusters"],
        distance_threshold=clustering_params["distance_threshold"],
        metric=clustering_params["metric"],
        linkage=clustering_params["linkage"],
    )
    model.fit(embeddings)

    return model


def generate_linkage_matrix(model: AgglomerativeClustering) -> np.ndarray:
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    return linkage_matrix


def plot_dendrogram(
    linkage_matrix: np.ndarray, dendrogram_params: Dict[str, Any]
) -> Figure:
    fig, _ = plt.subplots(figsize=(12, 7))
    plt.xlabel("Number of microregions")
    dendrogram(linkage_matrix, **dendrogram_params)
    plt.tight_layout()
    return fig


def cluster_regions(
    linkage_matrix: np.ndarray,
    embeddings: gpd.GeoDataFrame,
    regions: gpd.GeoDataFrame,
    clusters: List[int],
) -> gpd.GeoDataFrame:
    regions_clustered = regions.loc[embeddings.index, :]

    cut_tree_results = cut_tree(linkage_matrix, n_clusters=clusters)
    for index, c in tqdm(list(enumerate(clusters))):
        assigned_clusters = cut_tree_results[:, index]
        regions_clustered[f"cluster_{c}"] = pd.Series(
            assigned_clusters, index=regions_clustered.index
        ).astype("category")

    return regions_clustered


def plot_clustered_regions_with_roads(
    regions_clustered: gpd.GeoDataFrame,
    roads: gpd.GeoDataFrame,
    area: gpd.GeoDataFrame,
    clusters: List[int],
) -> Dict[str, Figure]:
    plots = {}
    for c in clusters:
        cluster_column = f"cluster_{c}"
        fig, ax = _pyplot_clustered_regions_with_roads(
            regions_clustered.sjoin(area),
            roads.sjoin(area),
            cluster_column,
            title=cluster_column,
        )
        ax.set_axis_off()
        plt.tight_layout()
        plots[cluster_column] = fig
        # plt.close()

    return plots


def _pyplot_clustered_regions_with_roads(
    regions: gpd.GeoDataFrame, roads: gpd.GeoDataFrame, column: str, title: str = ""
) -> Tuple[Figure, plt.Axes]:
    fig, ax = plt.subplots(figsize=(10, 9))
    ax.set_aspect("equal")
    ax.set_title(title)
    regions.to_crs(epsg=3857).plot(
        column=column,
        ax=ax,
        alpha=0.9,
        legend=True,
        cmap=MATPLOTLIB_COLORMAP,
        vmin=0,
        vmax=len(PLOTLY_COLORMAP),
        linewidth=0,
    )
    roads.to_crs(epsg=3857).plot(ax=ax, color="black", alpha=0.5, linewidth=0.2)
    ctx.add_basemap(ax, source=MAP_SOURCE)
    return fig, ax
