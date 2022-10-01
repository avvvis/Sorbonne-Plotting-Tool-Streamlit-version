import form_functions as ff
import animation as ani
from matplotlib.pyplot import*
from matplotlib.axes import*
from math import*
import numpy as np
import streamlit as st
import streamlit.components.v1 as components

def make_rectangle_changed(var, eq):

    # -getting variables and equations out of stings-
    var = variables.split("\n")
    v = {}
    for i in var:
        i = i.split("=")
        i[0] = i[0].replace(" ", "")
        i[1] = i[1].replace(" ", "")
        v[i[0]] = i[1]

    eq = equations.split("\n")
    e = {}
    for i in eq:
        i = i.split("=")
        i[0] = i[0].replace(" ", "")
        i[1] = i[1].replace(" ", "")
        e[i[0]] = i[1]

    rectangle_ani = ani.animation(ff.rectangle(xc, yc, length, height, 10), e, v, grid_cb, 120, 120, 0, 10)
    components.html(rectangle_ani.to_jshtml(), height=1000)


# -front end-
st.subheader("input change equations")
equations = st.text_area(label="equations:", value="x = x + sin(t)*10\ny = y + cos(t)*10")
variables = st.text_area(label="variables:", value="alpha = 0")
grid_cb = st.checkbox(label="add gird ?", value=0)

st.subheader("Select center of the figure")
xc = st.slider(label="x coordinate", min_value=-100, max_value=100, value=0, step=1)
yc = st.slider(label="y coordinate", min_value=-100, max_value=100, value=0, step=1)

st.subheader("Select parameters of the rectangle")
length = st.slider(label="length", min_value=0, max_value=100, value=10, step=1)
height = st.slider(label="height", min_value=0, max_value=100, value=10, step=1)

# -figure plotting-
fig, ax = subplots()
points = ff.rectangle(xc, yc, length, height, 10)

plot = ax.plot(points[0], points[1])

make_rectangle_changed(variables, equations)
