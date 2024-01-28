#importing libraries
import streamlit as st
import plotly_express as px
import pandas as pd
from PIL import Image
import seaborn as sns
import plotly.figure_factory as ff
from warnings import filterwarnings
filterwarnings(action='ignore', category=DeprecationWarning, message='In the future `np.bool` will be defined as the corresponding NumPy scalar')



#title of the app
st.title("Data Visualization App")

#add a sidebar
st.sidebar.subheader("Visualization Settings")

# Setup file upload
uploaded_file= st.sidebar.file_uploader(label="Upload your CSV or Excel file.", type=['csv','xlsx'])

#uploading files to the streamlit app
global df
if uploaded_file is not None:
    print(uploaded_file)
    print('file uploaded')
    try:
        df= pd.read_csv(uploaded_file)
    
    except Exception as e:
        print(e)
        df= pd.read_excel(uploaded_file)
global numeric_columns
try:
    st.write(df)
    numeric_columns=list(df.select_dtypes(['float', 'int']).columns)

except Exception as e:
    print(e)
    st.write("Please upload file to the application.")

global categoric_columns
try:
    st.write(df)
    categoric_columns=list(df.select_dtypes(["bool","object"]).columns)
    
except Exception as e:
    print(e)
    st.write("Please upload file to the application.")

#add a select widget to the side bar
chart_select = st.sidebar.selectbox(
    label= "Select the chart type",
    options=['Scatterplots', 'Lineplots', 'Barplots', 'LinePlot', 'Boxplot', 'Histogram']
)

#main code where it lets you select x and y values
if chart_select == 'Scatterplots':
    st.sidebar.subheader("Scatterplot Settings")
    try:
        x_values=st.sidebar.selectbox('X axis', options=numeric_columns)
        y_values=st.sidebar.selectbox('Y axis', options=numeric_columns)
        plot=px.scatter(data_frame=df, x=x_values, y=y_values)
        #display the chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)


if chart_select == 'Barplots':
    st.sidebar.subheader("Barplot Settings")
    try:
        # x_values=x_axis
        # y_values=y_axis
        x_values=st.sidebar.selectbox("X_axis", options=numeric_columns)
        y_values=st.sidebar.selectbox("Y_axis", options=categoric_columns)
        plot=px.bar(data_frame=df, x=x_values, y=y_values)
        #display the chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
if chart_select == 'LinePlot':
    st.sidebar.subheader("Lineplot Settings")
    try:
        x_values=st.sidebar.selectbox("X_axis", options=numeric_columns)
        y_values=st.sidebar.selectbox("Y_axis", options=categoric_columns)
        plot=px.line(data_frame=df, x=x_values, y=y_values)
        # df=pd.DataFrame(y_values,index=x_values)
        #display the chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if chart_select == 'Boxplot':
    st.sidebar.subheader("Boxplot Settings")
    try:
        x_values=st.sidebar.selectbox('X axis', options=numeric_columns)
        y_values=st.sidebar.selectbox('Y axis', options=numeric_columns)
        plot=px.box(data_frame=df, x=x_values, y=y_values)
        #display the chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)