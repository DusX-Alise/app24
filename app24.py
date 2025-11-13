import pandas as pd
import streamlit as st
import os

# --- Configuration ---
FILE_NAME = "EA_24_data.xlsx"

st.set_page_config(page_title="EA_24_data Viewer", layout="wide")
st.title(f"Data Viewer for {FILE_NAME}")

def load_data(filepath):
    """Loads data from the specified Excel file."""
    if not os.path.exists(filepath):
        st.error(f"Error: The file '{filepath}' was not found.")
        st.stop()
    
    try:
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(filepath)
        return df
    except Exception as e:
        st.error(f"An error occurred while reading the Excel file: {e}")
        st.stop()

# --- Main app logic ---
# Load the data
df = load_data(FILE_NAME)

if df is not None:
    st.success(f"Successfully loaded {len(df)} rows and {len(df.columns)} columns.")
    
    # Display the data using Streamlit's data element
    st.dataframe(df)

    # Optional: Display some basic statistics
    st.subheader("Data Overview")
    st.write(df.describe())

    # Optional: Allow download of the data (e.g., back to CSV)
    @st.cache_data
    def convert_df_to_csv(df):
        # IMPORTANT: This turns the data back into a CSV string
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df_to_csv(df)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='EA_24_data_export.csv',
        mime='text/csv',
    )
