import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File path for the CSV file
FILE_PATH = 'loan.csv'

# Function to load data with caching to avoid reloading unnecessarily
@st.cache_data
def load_data():
    data = pd.read_csv(FILE_PATH)
    return data

# Load the data
df = load_data()

# Exclude 'Loan_ID' from the columns for analysis
columns_for_analysis = df.columns.drop('Loan_ID')

# Set up the title of the dashboard
st.title('Loan Data Analysis Dashboard')

# Display the first few rows of the DataFrame
st.subheader('Preview of Loan Data')
st.write(df.head())

# Create tabs for each type of analysis
tab1, tab2, tab3 = st.tabs(["Univariate Analysis", "Bivariate Analysis", "Segment-based Analysis"])

with tab1:
    st.header('Univariate Analysis')
    univariate_column = st.selectbox('Select a column for univariate analysis:', columns_for_analysis)
    if st.button('Show Univariate Analysis', key='uni'):
        st.write(df[univariate_column].describe())
        plt.figure(figsize=(10, 4))
        sns.histplot(df[univariate_column].dropna(), bins=20, kde=True)
        plt.title(f'Distribution of {univariate_column}')
        st.pyplot(plt)

with tab2:
    st.header('Bivariate Analysis')
    column_x = st.selectbox('Select the first column:', columns_for_analysis, index=0, key='col_x')
    column_y = st.selectbox('Select the second column:', columns_for_analysis, index=1, key='col_y')
    if st.button('Show Bivariate Analysis', key='bi'):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=df[column_x], y=df[column_y])
        plt.title(f'Relationship between {column_x} and {column_y}')
        st.pyplot(plt)

with tab3:
    st.header('Segment-based Analysis')
    segment_column = st.selectbox('Select a segment column:', df.select_dtypes(include='object').columns.drop('Loan_ID'), key='segment')
    analysis_column = st.selectbox('Select a column to analyze within segments:', columns_for_analysis, key='analysis')
    if st.button('Show Segment Analysis', key='seg'):
        unique_segments = df[segment_column].unique()
        fig, ax = plt.subplots(len(unique_segments), 1, figsize=(10, 6*len(unique_segments)))
        for i, segment in enumerate(unique_segments):
            segment_data = df[df[segment_column] == segment]
            sns.histplot(segment_data[analysis_column].dropna(), ax=ax[i], kde=True)
            ax[i].set_title(f'Distribution of {analysis_column} for {segment}')
        st.pyplot(fig)
