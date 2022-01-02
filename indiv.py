import csv
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("student.csv")

def studentScores(student_id):
    studentdf = df.loc[df["student_id"] == student_id]

    print(studentdf.groupby("level")["attempt"].mean())

    fig = go.Figure(go.Bar(
        x = studentdf.groupby("level")["attempt"].mean(),
        y = ["level 1", "level 2", "level 3", "level 4"],
        orientation = "h"
    ))

    fig.show()

studentScores("TRL_xsl")