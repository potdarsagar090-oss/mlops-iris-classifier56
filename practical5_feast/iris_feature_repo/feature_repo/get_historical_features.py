from feast import FeatureStore
import pandas as pd

store = FeatureStore(repo_path=".")

entity_df = pd.DataFrame(
    {
        "sample_id": [1, 2, 3, 4, 5],
        "event_timestamp": pd.to_datetime(
            [
                "2026-09-22 08:49:45.075760+00:00",
"2026-09-22 08:50:45.075760+00:00",
"2026-09-22 08:51:45.075760+00:00",
"2026-09-22 08:52:45.075760+00:00",
"2026-09-22 08:53:45.075760+00:00",
            ]
        ),
    }
)

historical_features = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "iris_measurements:sepal_length_cm",
        "iris_measurements:sepal_width_cm",
        "iris_measurements:petal_length_cm",
        "iris_measurements:petal_width_cm",
        "iris_engineered_features:sepal_area",
        "iris_engineered_features:petal_area",
        "iris_engineered_features:sepal_to_petal_length_ratio",
    ],
).to_df()

print("Historical Features:")
print(historical_features)