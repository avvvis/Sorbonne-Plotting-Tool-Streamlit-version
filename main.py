import streamlit as st
import matplotlib.pyplot as plt

st.title("Plot figure change")
figures = ["rectangle", "circle", "scatter plot", "custom figure"]
fig = st.selectbox(label="choose figure", options=figures)
st.write("You selected:", fig)

def line(p1, p2, f):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    X = [p1[0]]
    Y = [p1[1]]
    for i in range(f):
        X.append(X[i] + (1 / f) * dx)
        Y.append(Y[i] + (1 / f) * dy)
    return X, Y



if fig == "rectangle":
    x1 = 1
    y1 = 10
    x2 = 10
    y2 = -10
else:
    x1 = 1
    y1 = -10
    x2 = 10
    y2 = 10
fig, ax = plt.subplots()
ax.scatter(line([x1, y1], [x2, y2], 10)[0], line([x1, y1], [x2, y2], 10)[1])

st.pyplot(fig)


