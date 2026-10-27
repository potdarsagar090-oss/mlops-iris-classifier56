import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score


MIN_ACCEPTABLE_ACCURACY = 0.90


def load_model_data():
    df = pd.read_csv("data/processed/iris_features.csv")

    feature_columns = [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
        "sepal_area",
        "petal_area",
        "sepal_to_petal_length_ratio",
    ]

    X = df[feature_columns]

    encoder = LabelEncoder()
    y = encoder.fit_transform(df["species"])

    return X, y, encoder


def train_quality_model():
    X, y, encoder = load_model_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model, X_test, y_test, encoder


def test_model_predictions_are_valid():
    model, X_test, y_test, encoder = train_quality_model()

    predictions = model.predict(X_test)

    known_labels = set(range(len(encoder.classes_)))

    assert set(predictions).issubset(known_labels)
    assert len(predictions) == len(y_test)


def test_model_meets_minimum_accuracy():
    model, X_test, y_test, encoder = train_quality_model()

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    assert accuracy >= MIN_ACCEPTABLE_ACCURACY, (
        f"Accuracy {accuracy:.4f} is below the required "
        f"threshold of {MIN_ACCEPTABLE_ACCURACY:.2f}"
    )
