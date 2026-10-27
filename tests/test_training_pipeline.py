import numpy as np

from src.train import load_data, train_model, evaluate_model


def test_training_pipeline_fits_successfully():
    X_train, X_test, y_train, y_test = load_data()

    model = train_model(
        X_train,
        y_train,
        n_estimators=10,
        max_depth=5
    )

    assert hasattr(model, "predict")
    assert hasattr(model, "predict_proba")


def test_model_prediction_output_shape():
    X_train, X_test, y_train, y_test = load_data()

    model = train_model(
        X_train,
        y_train,
        n_estimators=10,
        max_depth=5
    )

    predictions = model.predict(X_test)

    assert predictions.shape == (len(X_test),)


def test_model_predict_proba_sums_to_one():
    X_train, X_test, y_train, y_test = load_data()

    model = train_model(
        X_train,
        y_train,
        n_estimators=10,
        max_depth=5
    )

    probabilities = model.predict_proba(X_test)

    assert probabilities.shape[0] == len(X_test)
    assert np.allclose(probabilities.sum(axis=1), 1.0)


def test_evaluate_model_returns_accuracy_and_report():
    X_train, X_test, y_train, y_test = load_data()

    model = train_model(
        X_train,
        y_train,
        n_estimators=10,
        max_depth=5
    )

    accuracy, report = evaluate_model(model, X_test, y_test)

    assert 0.0 <= accuracy <= 1.0
    assert isinstance(report, str)
