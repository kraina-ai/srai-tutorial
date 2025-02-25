# Fill changes in the appropriate cells
train_city = "Amsterdam"
validation_city = "Utrecht"
test_city = "Rotterdam"

###

bicycle_stations = OSMOnlineLoader().load(
    area=regions, tags={"amenity": "charging_station"}
)

###

H3_RESOLUTION = 10
H3_PREDICTION_RANGE = 5
H3_NEIGHBOURS = 5

###

# Predict for the whole city

from srai.h3 import ring_buffer_h3_regions_gdf

city = geocode_to_region_gdf("Basel")

city_h3_cells = H3Regionalizer(resolution=H3_RESOLUTION).transform(city)
buffered_city_h3_cells = ring_buffer_h3_regions_gdf(
    city_h3_cells, distance=H3_NEIGHBOURS
)

city_features = OvertureMapsLoader(
    theme_type_pairs=list(OVERTURE_MAPS_HIERARCHY_DEPTH_VALUES.keys()),
    hierarchy_depth=list(OVERTURE_MAPS_HIERARCHY_DEPTH_VALUES.values()),
    include_all_possible_columns=True,
).load(area=buffered_city_h3_cells)

city_joint = IntersectionJoiner().transform(
    regions=buffered_city_h3_cells, features=city_features
)

city_embeddings = embedder.transform(
    regions_gdf=buffered_city_h3_cells, features_gdf=city_features, joint_gdf=city_joint
)

city_scaled_features = StandardScaler().fit_transform(
    city_embeddings.loc[city_h3_cells.index]
)
city_distances = bst.predict(
    xgb.DMatrix(city_scaled_features, feature_names=list(city_embeddings.columns))
)

city_h3_cells["predicted_distance"] = city_distances

ax = city_h3_cells.plot(
    column="predicted_distance",
    figsize=(20, 20),
    cmap=temps_cmap,
    alpha=0.6,
    legend=True,
    legend_kwds={
        "shrink": 0.3,
        "location": "bottom",
        "label": "Predicted distance",
        "pad": -0.05,
    },
    vmin=max(0, city_h3_cells["predicted_distance"].min()),
    vmax=city_h3_cells["predicted_distance"].max(),
)

cx.add_basemap(
    ax, crs=h3_regions.crs, source=cx.providers.CartoDB.PositronNoLabels, zoom=13
)
ax.set_axis_off()

title = "Predicted distance"

ax.set_title(title, fontsize=20)

plt.show()
