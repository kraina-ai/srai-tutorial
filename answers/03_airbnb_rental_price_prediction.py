# Easier task

# Louvre pyramid
CITY_CENTRE = (48.861010, 2.335855)

# Haversine, or great circle distance
from osmnx.distance import great_circle

listings_gdf["city_centre_distance"] = great_circle(
    lat1=CITY_CENTRE[0],
    lon1=CITY_CENTRE[1],
    lat2=listings_gdf.geometry.y,
    lon2=listings_gdf.geometry.x,
)

features = listings_gdf.merge(
    context_embeddings.reset_index(),
    left_on=h3_embedding_column,
    right_on=context_embeddings.index.name,
).drop(
    columns=[
        target_column,
        geometry_column,
        h3_splitting_column,
        h3_embedding_column,
        context_embeddings.index.name,
    ]
)
target = listings_gdf[target_column]

optuna_result = find_best_lightgbm_model(features, target, timeout=120)
optuna_result["experiment"] = "cce with distance to center"

results.append(optuna_result)

# Harder task
from srai.loaders import OSMOnlineLoader

# Get metro stations as points
metro_stations = (
    OSMOnlineLoader()
    .load(
        area=buffered_regions_gdf.union_all(),  # this unification is important
        tags={"railway": "station", "station": "subway"},
    )
    .dropna()  # we want points that are both station and a subway
    .representative_point()
)


def get_closest_metro_distance(pt) -> float:
    return min(
        great_circle(
            lat1=pt.y,
            lon1=pt.x,
            lat2=metro_stations.y,
            lon2=metro_stations.x,
        )
    )


listings_gdf["metro_distance"] = listings_gdf["geometry"].apply(
    get_closest_metro_distance
)

features = listings_gdf.merge(
    context_embeddings.reset_index(),
    left_on=h3_embedding_column,
    right_on=context_embeddings.index.name,
).drop(
    columns=[
        target_column,
        geometry_column,
        h3_splitting_column,
        h3_embedding_column,
        context_embeddings.index.name,
    ]
)
target = listings_gdf[target_column]

optuna_result = find_best_lightgbm_model(features, target, timeout=120)
optuna_result["experiment"] = "cce with distance to metro"

results.append(optuna_result)

aggregated_results = pd.DataFrame(results)[
    ["experiment", "n_features", "RMSE", "R2", "MAE"]
]
aggregated_results

# not much better results, but the features are important and show up high in the list
