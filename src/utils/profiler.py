import pandas as pd


def profile_dataset(df: pd.DataFrame) -> dict:
    """
    Generate basic statistics about a dataset.

    Parameters:
        df: Pandas DataFrame.
    Returns:
        dict: Dataset profile information.
    """

    profile = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "memory_usage_mb": round(
            df.memory_usage(deep=True).sum() / (1024 * 1024), 2
        ),
    }

    return profile


def get_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return missing value statistics for each column
    """

    missing_df = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": df.isnull().sum().values
    })

    missing_df["Missing %"] = (
        missing_df["Missing Values"] / len(df) * 100
    ).round(2)

    missing_df = missing_df.sort_values(
        by="Missing %",
        ascending=False
    )

    return missing_df