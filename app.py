import streamlit as st
from src.etl.file_loader import load_data
from src.utils.profiler import profile_dataset

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
    total_cells = profile["rows"] * profile["columns"]

    missing_percentage = round(
        (profile["missing_values"] / total_cells) * 100, 2
    )

    duplicate_percentage = round(
        (profile["duplicate_rows"] / profile["rows"]) * 100, 2
    )
    st.success("Dataset loaded successfully!")
    st.subheader("Dataset Summary")
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "Rows", 
            f"{profile["rows"]:,}"
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
            profile["missing_values"],
            f"{missing_percentage}%"
        )

    with col5:
        st.metric(
            "Duplicate Rows", 
            profile["duplicate_rows"],
            f"{duplicate_percentage}%"
        )
        
    st.subheader("Dataset Preview")
    
    st.dataframe(
        df.head(),
        use_container_width=True,
        hide_index=True
    )