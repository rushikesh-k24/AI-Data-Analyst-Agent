import pandas as pd

from pandas.api.types import (
    is_numeric_dtype,
    is_datetime64_any_dtype,
    is_bool_dtype,
)

def detect_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Detect the logical datatype of each column.
    
    Parameters:
        df: Input DataFrame.
        
    Returns: 
        DataFrame containing column names and detected data types.
    """

    detected_types = []

    for column in df.columns:

        dtype = df[column].dtype

        if is_numeric_dtype(dtype):
            logical_type = "Numeric"

        elif is_datetime64_any_dtype(dtype):
            logical_type = "Datetime"

        elif is_bool_dtype(dtype):
            logical_type = "Boolean"

        else:
            logical_type = "Categorical / Text"

        detected_types.append(
            {
                "Column": column,
                "Detected Type": logical_type,
            }
        )

    return pd.DataFrame(detected_types)