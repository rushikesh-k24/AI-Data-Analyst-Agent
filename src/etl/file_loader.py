import pandas as pd

def load_data(file) -> pd.DataFrame:
    """
    Load a CSV or Excel file and return a Pandas DataFrame
    Parameters: 
        file: Uploaded file object from Streamlit.
    Returns:
        pd.DataFrame: Loaded dataset.
    Raises: 
        ValueError: If the uploaded file format is not supported.
    """

    try:
        file_name = file.name.lower()
        if file_name.endswith(".csv"):
            return pd.read_csv(file)
        elif file_name.endswith(".xlsx"):
            return pd.read_excel(file)
        
        else:
            raise ValueError(
                "Unsupported file format. Please upload a CSV or Excel (.xlsx) file."
            )
        
    except Exception as error:
        raise Exception(f"Error loading file: {error}")