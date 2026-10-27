import pandas as pd
import pytest

from src.pipeline.validate import validate, DataValidationError


def create_test_csv(tmp_path, data):
    input_path = tmp_path / "input.csv"
    pd.DataFrame(data).to_csv(input_path, index=False)
    return str(input_path)


def valid_data():
    return {
        "sepal length (cm)": [5.1, 6.0],
        "sepal width (cm)": [3.5, 3.0],
        "petal length (cm)": [1.4, 4.5],
        "petal width (cm)": [0.2, 1.5],
        "species": ["setosa", "versicolor"],

        "sepal_area": [17.85, 18.0],
        "petal_area": [0.28, 6.75],
        "sepal_to_petal_length_ratio": [
            5.1 / 1.4,
            6.0 / 4.5
        ],
        "petal_length_bin": ["short", "long"],
    }


def test_validate_clean_data_passes(tmp_path):
    input_path = create_test_csv(tmp_path, valid_data())

    result = validate(input_path)

    assert len(result) == 2


def test_validate_missing_column_raises_error(tmp_path):
    data = valid_data()
    del data["species"]

    input_path = create_test_csv(tmp_path, data)

    with pytest.raises(DataValidationError):
        validate(input_path)


def test_validate_invalid_species_raises_error(tmp_path):
    data = valid_data()
    data["species"] = ["setosa", "invalid_species"]

    input_path = create_test_csv(tmp_path, data)

    with pytest.raises(DataValidationError):
        validate(input_path)


def test_validate_out_of_range_value_raises_error(tmp_path):
    data = valid_data()
    data["sepal length (cm)"] = [5.1, 20.0]

    input_path = create_test_csv(tmp_path, data)

    with pytest.raises(DataValidationError):
        validate(input_path)
