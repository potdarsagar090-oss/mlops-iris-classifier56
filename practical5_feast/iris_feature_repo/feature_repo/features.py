from feast import Entity, FeatureView, Field, FileSource, FeatureService
from feast.types import Float32
from datetime import timedelta

sample = Entity(
    name="sample_id",
    join_keys=["sample_id"],
    description="Unique Iris sample identifier",
)

iris_source = FileSource(
    path="data/iris_features.parquet",
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp",
)

iris_measurements = FeatureView(
    name="iris_measurements",
    entities=[sample],
    ttl=timedelta(days=365),
    schema=[
        Field(name="sepal_length_cm", dtype=Float32),
        Field(name="sepal_width_cm", dtype=Float32),
        Field(name="petal_length_cm", dtype=Float32),
        Field(name="petal_width_cm", dtype=Float32),
    ],
    online=True,
    source=iris_source,
)

iris_engineered_features = FeatureView(
    name="iris_engineered_features",
    entities=[sample],
    ttl=timedelta(days=365),
    schema=[
        Field(name="sepal_area", dtype=Float32),
        Field(name="petal_area", dtype=Float32),
        Field(name="sepal_to_petal_length_ratio", dtype=Float32),
    ],
    online=True,
    source=iris_source,
)

iris_feature_service = FeatureService(
    name="iris_feature_service",
    features=[
        iris_measurements,
        iris_engineered_features,
    ],
)