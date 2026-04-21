# Copy this to the cell at the end of notebook and run

# Calculate total prediction from area
import numpy as np

areas_test = msoa_stats_gdf.loc[test_msoa_codes, "area"]

y_test_total = msoa_stats_gdf.loc[test_msoa_codes, "Total"]
y_pred_total = np.rint(y_pred * areas_test)

print(r2_score(y_test_total, y_pred_total))

# Plot scatterplot
f, ax = plt.subplots(figsize=(8, 8))

sns.regplot(
    x=y_test_total,
    y=y_pred_total,
    scatter_kws=dict(alpha=0.5, s=10),
    line_kws=dict(color=".2", linestyle="--"),
    ax=ax,
)
min_population = y_test_total.min()
max_population = y_test_total.max()
sns.lineplot(
    x=[min_population, max_population],
    y=[min_population, max_population],
    color="red",
    ax=ax,
)

ax.set_xlabel("True population")
ax.set_ylabel("Predicted population")

plt.show()

# Calculate for whole dataset
msoa_stats_gdf["predicted_population_total"] = (
    msoa_stats_gdf["predicted_population_density"] * msoa_stats_gdf["area"]
)

# Plot raw values
f, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 16), sharex=True, sharey=True)
msoa_stats_gdf.plot("Total", ax=ax1, legend=True, cmap="plasma")
msoa_stats_gdf.plot("predicted_population_total", ax=ax2, legend=True, cmap="plasma")

ax1.set_title("Population")
ax2.set_title("Predicted population")

plt.show()

# Plot errors
msoa_stats_gdf["error_total"] = (
    msoa_stats_gdf["Total"] - msoa_stats_gdf["predicted_population_total"]
)

msoa_stats_gdf["normalized_error_total"] = (
    msoa_stats_gdf["error_total"].apply(
        lambda x, city_data=msoa_stats_gdf: (
            -x / city_data["error_total"].min()
            if x < 0
            else x / city_data["error_total"].max()
        )
    )
    + 1
) / 2

msoa_stats_gdf["alpha_total"] = (
    msoa_stats_gdf["normalized_error_total"] - 0.5
).abs() * 2

f, ax = plt.subplots(figsize=(12, 8))

msoa_stats_gdf.boundary.plot(ax=ax, color="black", alpha=0.8, lw=0.1)
msoa_stats_gdf.plot(
    "normalized_error_total",
    ax=ax,
    alpha=msoa_stats_gdf["alpha_total"],
    cmap="bwr_r",
    legend=True,
    legend_kwds={
        "shrink": 0.8,
        "label": "Prediction error",
        "ticks": [0, 0.5, 1],
        "format": mticker.FixedFormatter(
            [
                round(msoa_stats_gdf["error_total"].min(), 4),
                "0",
                round(msoa_stats_gdf["error_total"].max(), 4),
            ]
        ),
    },
)

cx.add_basemap(
    ax, crs=msoa_stats_gdf.crs, source=cx.providers.CartoDB.PositronNoLabels, zoom=12
)
ax.set_axis_off()

plt.show()
