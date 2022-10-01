import streamlit as st
import matplotlib.pyplot as plt

st.title("Plot figure change")

st.subheader("How does it work ?")
st.text("""
On the left there is a sidebar, on which you can choose what type of\n
figure change you want to see. All you need to do is click on the sidebar\n
and input all the data needed to plot. The website will automatically refresh\n
and an animation will appear. Enjoy !
""")
st.subheader("Two colors on the animation")
st.text("""
You can notice that on the animation there are two figures visible.\n
One is blue and the second one is black. The blue figure is figure before change,\n
and the black figure is figure after change. The same is true for scatter points,\n
but there blue points are the points without the change equations applied, and \n
black points are the ones with the equations applied.
""")
