import streamlit as st
import pandas as pd
import altair as alt
from matplotlib import pyplot as plt
import seaborn as sns


def Visualization(df):
    st.subheader("Mostly trains travel less than 1000 km")

    sns.histplot(df["distance"], color="cyan")
    plt.xlabel("Distance (In Kms)")
    plt.ylabel("Count of trains")
    st.pyplot()

    # Create a line chart showing the total distance travelled by each train
    st.subheader("The total distance travelled by each train")

    chart_data = df.groupby("number")["distance"].sum().reset_index()
    chart = (
        alt.Chart(chart_data)
        .mark_line()
        .encode(x="number", y="distance")
        .properties(width=600, height=400)
    )
    # Display the chart in Streamlit
    st.altair_chart(chart)

    st.subheader("Plot showing average distance travelled by various types of trains")
    df2 = df[["type", "distance"]].groupby("type").mean()
    colors = sns.color_palette("RdGy")[0:5]
    plt.bar(df2.index, df2.distance, color=colors)
    plt.xticks(range(len(df2)), rotation="vertical")
    plt.xlabel("Types of trains")
    plt.ylabel("Average distance travelled")
    st.pyplot()

    # Create a scatter plot showing the relationship between distance and duration
    st.subheader("The relationship between distance and duration and type of train")
    sns.scatterplot(x=df["distance"], y=df["duration"], hue=df["type"])
    st.pyplot()

    # Create a line chart showing the change in the number of trains over time
    st.subheader("the change in the number of trains over time")
    line_data = df.groupby("arrival")["number"].count().reset_index()
    line_data["arrival"] = pd.to_datetime(line_data["arrival"])
    line_chart = (
        alt.Chart(line_data)
        .mark_line()
        .encode(x="arrival", y="number")
        .properties(width=800, height=400)
    )
    # Display the line chart in Streamlit
    st.altair_chart(line_chart)

    st.header("Plot showing the types of seats available in various types of trains")
    st.subheader(
        "100% of GR trains have third AC, 100% of Mail trains have sleeper and 95% of JShtb have chair_car"
    )
    df2 = (
        df[
            [
                "type",
                "first_class",
                "first_ac",
                "second_ac",
                "third_ac",
                "sleeper",
                "chair_car",
            ]
        ]
        .groupby("type")
        .mean()
    )
    sns.heatmap(df2, annot=True, fmt=".1%")
    plt.xlabel("Types of seats")
    plt.ylabel("Types of trains")
    st.pyplot()

    st.header("Plot showing the split of trains accross various zones")
    st.subheader("Plot shows that the NR, WR, and SR occupies the major portion")
    data = df["zone"].value_counts()
    colors = sns.color_palette("dark")[0:5]
    plt.pie(data, labels=data.index, colors=colors, autopct="%.0f%%")
    st.pyplot()

    st.header("Plot showing the distance trains travel in various zones")
    st.subheader(" Trains in NFR zone travel more distances")
    plt.figure(figsize=(10, 6))
    sns.boxplot(y=df["distance"], x=df["zone"])
    plt.ylabel("Distance (In Kms)")
    plt.xlabel("Zones")
    st.pyplot()
