import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots

# CSV of year wise accident data
df1 = pd.read_csv('requireddf/yearWiseAccident.csv')
df1 = df1.iloc[:29, :]

# csv of reason wise accident data 
df2=pd.read_csv('requireddf/reasonOfAccident.csv')

#csv of age wise accident data
df3=pd.read_csv('requireddf/ageWiseData.csv')

#csv file of Male and Female accident data
df4=pd.read_csv('requireddf/MaleFemaleData.csv')

#csv file of vehicle wise accident data
df5=pd.read_csv('requireddf/vehicleWiseAccident.csv')

#rural and urban data of accident
df6=pd.read_csv('requireddf/ruralUrbanData.csv')

#year wise rural and urban data of accident
df7=pd.read_csv('requireddf/yearWiseRuralUrbanData.csv')

#weather wise accident data
df8=pd.read_csv('requireddf/wetherWiseAccidentData.csv')

def returnYearVSAccidentGraph():
    fig = px.line(df1, x='Years', y='Total Number of Road Accidents (in numbers) ', title='Number of Accidents per year', template='plotly_dark')
    return fig

def returnDeathAndDiedGraphPerYear():
    fig = px.line(df1, x='Years', y=['Total Number of Persons Killed (in numbers) ', 'Total Number of Persons Injured (in numbers)'], title='Number of Persons Killed and Injured Per year', template='plotly_dark')
    return fig

def returnRoadLengthGraph():
    fig = px.line(df1, x='Years', y='Road Length (in kms)', title='Length of Roads per Year', template='plotly_dark')
    return fig


def returnReasonWiseAccidentGraph():
    fig = px.pie(df2, values='Number of Accidents', names='Reasons', title='Reasons of Accidents in India 2019', template='plotly_dark')
    return fig


def returnAgeWiseAccidentGraph():
    fig = px.bar(df3, x='Age Group', y='Count', color='Gender', barmode='group',
             title='Age Group Distribution by Gender 2019',template='plotly_dark')
    return fig

def returnGenderWiseAccidentGraph():
    fig = px.pie(df4, names='gender', values='count', color='gender', template='plotly_dark')
    return fig

def returnVehicleWiseAccidentGrapth():
    fig=px.pie(df5, values='Accident', names='Vehicle', title='Total Accidents by Vehicle Type 2019',template='plotly_dark')
    fig.update_traces(textinfo='percent+label')
    return fig

def returnRuralUrbanAccidentGraph():
    fig = px.bar(df6, x='State/UTs', y=['Urban ', 'Rural'], title='Accidental Deaths by State/UTs', barmode='group',template='plotly_dark')
    return fig

def returnYearWiseRuralUrbanGraph(year):
    if year == 'Combined':
        df7['Year'] = df7['Year'].astype(str)

        # Filter the dataframe for each year
        df_2018 = df7[df7['Year'] == '2018']
        df_2019 = df7[df7['Year'] == '2019']
        df_2020 = df7[df7['Year'] == '2020']
        df_2021 = df7[df7['Year'] == '2021']

        # Create subplots
        fig = make_subplots(rows=2, cols=2, subplot_titles=('2018', '2019', '2020', '2021'), specs=[[{'type':'pie'}, {'type':'pie'}], [{'type':'pie'}, {'type':'pie'}]])

        # Add each pie chart to the subplot
        fig.add_trace(px.pie(df_2018, names='area', values='count').data[0], row=1, col=1)
        fig.add_trace(px.pie(df_2019, names='area', values='count').data[0], row=1, col=2)
        fig.add_trace(px.pie(df_2020, names='area', values='count').data[0], row=2, col=1)
        fig.add_trace(px.pie(df_2021, names='area', values='count').data[0], row=2, col=2)

        # Update the layout with a title and theme
        fig.update_layout(title_text="Total Accidental Deaths in India (2018-2021)", template='plotly_dark')

        return fig
    
    elif year == '2018':
        df_2018 = df7[df7['Year'] == '2018']
        fig = px.pie(df_2018, names='area', values='count', title='Total Accidental Deaths in India (2018)', template='plotly_dark')
        return fig
    
    elif year == '2019':
        df_2019 = df7[df7['Year'] == '2019']
        fig = px.pie(df_2019, names='area', values='count', title='Total Accidental Deaths in India (2019)', template='plotly_dark')
        return fig
    elif year == '2020':
        df_2020 = df7[df7['Year'] == '2020']
        fig = px.pie(df_2020, names='area', values='count', title='Total Accidental Deaths in India (2020)', template='plotly_dark')
        return fig
    elif year == '2021':
        df_2021 = df7[df7['Year'] == '2021']
        fig = px.pie(df_2021, names='area', values='count', title='Total Accidental Deaths in India (2021)', template='plotly_dark')
        return fig
    

def returnWeatherWiseAccidentGraph():
    fig = px.pie(df8, values='Accidents', names='Weather', title='Accidents According to Weather', template='plotly_dark')
    return fig
