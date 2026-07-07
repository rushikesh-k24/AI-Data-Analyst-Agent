import pandas as pd

from typing import Any


def analyze_columns(df: pd.DataFrame) -> dict[str, dict[str, Any]]:
    """
    Analyze every column and return metadata that can be reused 
    across the application.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataset.
    
    Returns
    -------
    dict
        Dictionary containing metadata for each column.
    """

    column_metadata: dict[str, dict[str, Any]] = {}

    for column in df.columns:

        column_data = df[column]

        column_metadata[column] = {
            "technical_dtype": str(column_data.dtype),

            "total_values": len(column_data),

            "missing_values": int(column_data.isnull().sum()),

            "unique_values": int(column_data.nunique()),

            "unique_percentage": round(
                (column_data.nunique() / len(column_data)) * 100,
                2,
            ),

            "sample_values": (
                column_data
                .dropna()
                .head(5)
                .tolist()
            ),
        }

    return column_metadata
