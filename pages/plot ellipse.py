import form_functions as ff
import animation as ani
from matplotlib.pyplot import*
from matplotlib.axes import*
from math import*
import numpy as np
import streamlit as st
import streamlit.components.v1 as components


# creating points of ellipse before change
def make_ellipse(xc, yc, a, b):
    a = float(a)
    b = float(b)
    x_coords = []
    y_coords = []
    angle = 0
    while angle <= 2 * pi:
        x_coords.append(cos(angle) * a + xc)
        y_coords.append(sin(angle) * b + yc)
        angle += (2 * pi) / 360
    x_coords = np.array(x_coords)
    y_coords = np.array(y_coords)
    return x_coords, y_coords


# plotting ellipse after change with animation
def make_ellipse_changed(var, eq):
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

    circle_ani = ani.animation(ff.ellipse(xc, yc, a, b, 100), e, v, grid_cb, 120, 120, 0, 10)
    # following line shows animation on the website
    components.html(circle_ani.to_jshtml(), height=1000)


# -front end-
st.subheader("input change equations")
equations = st.text_area(label="equations:", value="x = x + sin(t)\ny = y + cos(t)")
variables = st.text_area(label="variables:", value="alpha = 0")
grid_cb = st.checkbox(label="add gird ?", value=0)

st.subheader("Select center of the figure")
xc = st.slider(label="x coordinate", min_value=-100, max_value=100, value=0, step=1)
yc = st.slider(label="y coordinate", min_value=-100, max_value=100, value=0, step=1)

st.subheader("select parameters a and b of the ellipse")
st.image(image="https://www.mathsisfun.com/geometry/images/ellipse-axes.svg")

a = st.slider(label="a", min_value=0, max_value=100, value=10, step=1)
b = st.slider(label="b", min_value=0, max_value=100, value=10, step=1)

st.subheader("Change animation:")

# -figure plotting-
fig, ax = subplots()
points = make_ellipse(xc, yc, a, b)

# plotting figure before change
plot = ax.plot(points[0], points[1])

# setting the plot
gca().set_aspect('equal', adjustable='box')
xlim([-120, 120])
ylim([-120, 120])
xticks(range(-120, 121, 10))
yticks(range(-120, 121, 10))
setp(ax.get_xticklabels()[1::2], visible=False)
setp(ax.get_yticklabels()[1::2], visible=False)

# plotting figure after change with animation
make_ellipse_changed(variables, equations)
