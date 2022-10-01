import form_functions as ff
import animation as ani
from matplotlib.pyplot import*
from matplotlib.axes import*
from math import*
import numpy as np
import streamlit as st
import streamlit.components.v1 as components


def animate_points(var, eq):

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

    str_lop = points
    str_lop = str_lop.split("=")[1]

    # changing string into list
    # note that you have to use specific formula for list to work [x1, y1], [x2, y2], ... [xn, yn]
    str_lop = str_lop.replace(" ", '').replace("\n", '').replace("[", '').replace("]", '')
    str_lop = str_lop.split(",")
    lop = []

    # data after strip = x1,y1,x2,y2...xn,yn
    for i in range(0, len(str_lop), 2):
        lop.append([float(str_lop[i]), float(str_lop[i + 1])])

    # running animation
    points_animation = ani.animation(ff.scatterpoints(lop), e, v, False, 120, 120, 0, 10)
    components.html(points_animation.to_jshtml(), height=1000)



st.subheader("Input change equations")
equations = st.text_area(label="equations", value="x = x+sin(t)*10\ny = y+cos(t)*10")
variables = st.text_area(label="variables", value="alpha = 0")

st.subheader("Input Points")
points = st.text_area(label="Remember to keep the notation !", value="points=[[1, 1], [2, 2]]")
st.text("points=[[x1, y1], [x2, y2], ...]")

animate_points(variables, equations)
