# Copyright 2023 Krishna Gupta
# All rights reserved.

import streamlit as st
import pandas as pd
import os

def main():
    st.title("DATA ai")
    st.write("by Krishna Gupta")
    
    uploaded_files = st.file_uploader("Upload CSV or XLSM files", type=["csv", "xlsm"], accept_multiple_files=True)
    
    if uploaded_files:
        file_data = {}
        
        for file in uploaded_files:
            try:
                file.seek(0)
                if file.name.endswith('.csv'):
                    df = pd.read_csv(file)
                elif file.name.endswith('.xlsm'):
                    df = pd.read_excel(file, engine='openpyxl')
                file_data[file.name] = df
            except Exception as e:
                st.error(f"Could not decode file {file.name}. Error: {e}")
                continue
        
        st.write("### Available Files and Tables")
        
        selected_data = {}
        
        for file_name, df in file_data.items():
            st.write(f"**{file_name}** : Columns - {', '.join(df.columns)}")
            selected_columns = st.multiselect(f"Select columns from {file_name}", df.columns.tolist())
            
            if selected_columns:
                selected_data[file_name] = df[selected_columns]
        
        if st.button("Combine and Download"):
            combined_df = pd.concat(selected_data.values(), axis=1, keys=selected_data.keys())
            csv_data = combined_df.to_csv(index=False)
            st.download_button("Download Combined CSV", csv_data, "combined_data.csv", "text/csv")
    
    st.write("---")
    st.write("© 2023 Krishna Gupta")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/llt-misty/) | [GitHub](https://github.com/iamkrishnagupta10)")

if __name__ == "__main__":
    main()
