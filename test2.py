import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.offline as pyo
import plotly.express as px
import random
from plotly.subplots import make_subplots

from pathlib import Path
from PIL import Image

import numpy as np
import math



x_recovery = np.array([0, 30, 60, 90])
y_recovery = np.array([3.64, 8.47, 9.52, 9.59])

x_nutrition = np.array([0, 30, 60, 90])
y_nutrition = np.array([2.12, 7.02, 9.00, 9.875])

x_training = np.array([0, 30, 60, 90])
y_training = np.array([2.96, 5.05, 8.26, 9.67])

x_overall = np.array([0, 30, 60, 90])
y_overall = np.array([3.2, 7.5, 9.16, 9.66])



r1 =[3,3,5.5]

fig = make_subplots(
    rows=2, cols=3,
    specs=[[{"type": "scatter"}, {"type": "scatter"}, {"type": "scatter"}],
           [{"colspan": 3}, None, None]
              ],
    horizontal_spacing= 0.08, vertical_spacing= 0.18,
    row_heights=[0.23, 0.25],
    subplot_titles=("RECOVERY", "NUTRITION", "EXERCISE")
    )

#fig = make_subplots(
#    rows=2, cols=3,
#    specs=[[{"type": "scatter"}, {"type": "scatter"}, {"type": "scatter"}],
#           [None, {"type": "scatter"}, None]
#              ],
#    horizontal_spacing= 0.15, vertical_spacing= 0.17,
#    row_heights=[0.25, 0.25]
#    )





fig.add_trace(
    go.Scatter(
        x=x_recovery, y=y_recovery,
        mode='lines+markers',
        name='Time (Days)',
        line=dict(color='orange', width=2),
        showlegend=False
    ),
    row=1,
    col=1,

    )

fig.add_trace(
    go.Scatter(
        x=x_nutrition, y=y_nutrition,
        mode='lines+markers',
        name='Time (Days)',
        line=dict(color='orange', width=2),
        showlegend=False
    ),
    row=1,
    col=2,
    )

fig.add_trace(
    go.Scatter(
        x=x_training, y=y_training,
        mode='lines+markers',
        name='Time (Days)',
        line=dict(color='orange', width=2),
        showlegend=False
    ),
    row=1,
    col=3,
    )

fig.add_trace(
    go.Scatter(
        x=x_overall, y=y_overall,
        mode='lines',
        name='Time (Days)',
        line=dict(color='royalblue', width=2),
        showlegend=False
    ),
    row=2,
    col=1,
    )
#fig.add_annotation(xref="x domain",yref="y domain",x=0.5, y=1.2, showarrow=False,
#                   text="<b>Hey</b>", row=1, col=1)


fig.update_layout(
    autosize=True,
#    minreducedwidth=350,
#    minreducedheight=350,
    width=920,
    height=520,
#    title_text = 'PEAK PERFORMANCE',

    font=dict(
        family="Arial",
        size=7,  # Set the font size here
        color="White"
    ),

    title_xref="paper",

    margin=dict(l=0, r=200, t=30, b=0),


    #title={
    #    'text': "Peak Performance",
    #    'y':0.9,
    #    'x':0.2,
    #    'xanchor': 'center',
    #    'yanchor': 'top'},

    title_font_family="Times New Roman",
    title_font_color="black",

    #polar=dict(            # first chart y-axis labels
    #radialaxis=dict(
    #  visible=True,
    #  range=[0, 10],
    #    tickfont_size = 10,
    #    color="Yellow"
    #)),

    #polar2=dict(        # second chart y-axis labels
    #radialaxis=dict(
    #  visible=True,
    #  range=[0, 10],
    #    tickfont_size = 10,
    #    color="Yellow"
    #)),


    #template="plotly_dark",

    #legend1=dict(
    #    title= "RECOVERY",
    #    x=-0.05,
    #    y=1.1,
    #    title_font_family="Arial",
    #    font=dict(
    #        family="Arial",
    #        size=9,
    #        color="White"
    #    ),
    #    bgcolor="Black",
    #    bordercolor="Black",
    #    borderwidth=1
    #),

    #legend2=dict(
    #    title="NUTRITION",
    #    x=0.55,
    #    y=1.1,
    #    title_font_family="Arial",
    #    font=dict(
    #        family="Arial",
    #        size=9,
    #        color="White"
    #    ),
    #    bgcolor="Black",
    #    bordercolor="Black",
    #    borderwidth=1
    #),

    #legend3=dict(
    #    title="TRAINING",
    #    x=-0.05,
    #    y=0.5,
    #    title_font_family="Arial",
    #    font=dict(
    #        family="Arial",
    #        size=9,
    #        color="White"
    #    ),
    #    bgcolor="Black",
    #    bordercolor="Black",
    #    borderwidth=1
    #),

  showlegend=True
)

#fig.update_polars(
#    radialaxis=dict(
#        angle=45,
#        range=[1, 10]
#    )
#)

#fig.update_polars(radialaxis=dict(range=[0, 1]))

fig.update_xaxes(title_text="DAYS", ticks="inside", tickcolor="white", showgrid=True, showline=True, linewidth=1, linecolor='white', mirror=True, tick0=0.0, dtick=30, row=1, col=1)
fig.update_yaxes(title_text="LEVEL", range=[1, 10], showgrid=True, showline=True, linewidth=1, linecolor='white', mirror=True, title_standoff = 10, row=1, col=1)
#fig.update_yaxes(range=[1, 10], showgrid=True, showline=True, linewidth=1, linecolor='white', mirror=True, title_standoff = 10, row=1, col=1)

fig.update_xaxes(title_text="DAYS", ticks="inside", tickcolor="white", tick0=0.0, showline=True, linewidth=1, linecolor='white', mirror=True, showgrid=True, dtick=30, row=1, col=2)
fig.update_yaxes(range=[1, 10], showgrid=True, showline=True, linewidth=1, linecolor='white', mirror=True, title_standoff = 10, row=1, col=2)
fig.update_xaxes(title_text="DAYS", ticks="inside", tickcolor="white", showgrid=True, showline=True, linewidth=1, linecolor='white', mirror=True, tick0=0.0, dtick=30, row=1, col=3)
fig.update_yaxes(range=[1, 10], showgrid=True, showline=True, linewidth=1, linecolor='white', mirror=True, title_standoff = 10, row=1, col=3)
fig.update_xaxes(title_text="DAYS", ticks="inside", tickcolor="white", showgrid=True, showline=True, linewidth=1, linecolor='white', mirror=True, tick0=0.0, dtick=30, row=2, col=1)
fig.update_yaxes(title_text="TOTAL<br>PERFORMANCE", range=[1, 10], showgrid=True, showline=True, linewidth=1, linecolor='white', mirror=True, title_standoff = 10, row=2, col=1)

fig.layout.annotations[0].update(y=1.02, font= dict(size=14))
fig.layout.annotations[1].update(y=1.02, font= dict(size=14))
fig.layout.annotations[2].update(y=1.02, font= dict(size=14))


# use below only if necessary
#fig.update_traces(mode = "lines+markers",
#      r = [1,2,3,4,5],
#      theta = [0,90,180,360,0],
#      line_color = "magenta",
#      marker = dict(
#        color = "royalblue",
#        symbol = "square",
#        size = 8
#      ))

st.plotly_chart(fig)
