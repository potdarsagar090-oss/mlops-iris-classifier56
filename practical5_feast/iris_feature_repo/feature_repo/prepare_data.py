import pandas as pd
from datetime import datetime, timezone

INPUT = "C:/Users/Admin/mlops-iris-classifier56/data/processed/iris_features.csv"
OUTPUT = "data/iris_features.parquet"

df = pd.read_csv(INPUT)
df = df.rename(columns={
    "sepal length (cm)": "sepal_length_cm",
    "sepal width (cm)": "sepal_width_cm",
    "petal length (cm)": "petal_length_cm",
    "petal width (cm)": "petal_width_cm",
})

df.insert(0, "sample_id", range(1, len(df) + 1))

now = datetime.now(timezone.utc)
now = datetime.now(timezone.utc) + pd.Timedelta(minutes=5)
df["event_timestamp"] = pd.date_range(
    end=now,
    periods=len(df),
    freq="min",
    tz="UTC"
)

df["created_timestamp"] = df["event_timestamp"]
df.to_parquet(OUTPUT, index=False)

print(f"Created {OUTPUT}")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(df.head())