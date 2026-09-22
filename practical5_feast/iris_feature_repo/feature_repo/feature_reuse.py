from feast import FeatureStore
from sklearn.cluster import KMeans
import pandas as pd

store = FeatureStore(repo_path=".")

entity_df = pd.DataFrame(
    {
        "sample_id": range(1, 6),
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

features = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "iris_measurements:sepal_length_cm",
        "iris_measurements:sepal_width_cm",
        "iris_measurements:petal_length_cm",
        "iris_measurements:petal_width_cm",
    ],
).to_df()

X = features[
    [
        "sepal_length_cm",
        "sepal_width_cm",
        "petal_length_cm",
        "petal_width_cm",
    ]
]

model = KMeans(n_clusters=2, random_state=42, n_init=10)
clusters = model.fit_predict(X)

features["cluster"] = clusters

print("Reused Features for Clustering:")
print(features)