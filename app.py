import streamlit as st
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
st.title("Linear Regression Model")
st.write("---")

num1 = st.number_input("Advertisement amount:")

x = [23,26,30,34,43,48,52,57,58]
y = [651,762,856,1063,1190,1298,1421,1440,1518]

# Show x and y in browser as a table
data = pd.DataFrame({
    "Advertisement (x)": x,
    "Sales (y)": y
})
st.subheader("Input Data (x and y)")
st.dataframe(data)  # or use st.table(data) for a static table

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(val):
    return slope * val + intercept

def plot_scatter():
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_title("Scatter Plot")
    st.pyplot(fig)

def plot_regression():
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    mymodel = list(map(myfunc, x))
    ax.plot(x, mymodel, color='red')
    ax.set_title("Scatter Plot with Regression Line")
    st.pyplot(fig)

if st.button("Predict"):
    Predicted_Sale = myfunc(num1)
    st.success(f"Predicted Sale for Advertisement amount {num1}: {Predicted_Sale:.2f}")
    plot_scatter()
    plot_regression()

