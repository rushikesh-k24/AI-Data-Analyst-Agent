import streamlit as st
from src.etl.file_loader import load_data
from src.utils.profiler import (
    profile_dataset,
    get_missing_values,
)


st.set_page_config(
    page_title="AI Data Analyst Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Data Analyst Agent")
st.caption("Version 1.0.0")

uploaded_file = st.file_uploader(
    "📂 Upload your dataset", 
    type=["csv", "xlsx"]
)

if uploaded_file is not None:
    df = load_data(uploaded_file)
    profile = profile_dataset(df)
    missing_df = get_missing_values(df)
    missing_df = missing_df[
        missing_df["Missing Values"] > 0 
    ]
   
    st.success("Dataset loaded successfully!")
    
    st.subheader("Dataset Summary")
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "Rows", 
            f"{profile['rows']:,}"
        )
                  

    with col2:
        st.metric(
            "Columns", 
            profile["columns"]
        )

    with col3:
        st.metric(
            "Memory", 
            f"{profile['memory_usage_mb']} MB"
        )


    with col4:
        st.metric(
            "Missing Values", 
            profile["missing_values"]
        )

    with col5:
        st.metric(
            "Duplicate Rows", 
            profile["duplicate_rows"]
        )
        
    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(),
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Data Quality Report")

    st.dataframe(
        missing_df,
        use_container_width=True,
        hide_index=True,
    )




   