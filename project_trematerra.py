
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from joblib import dump

df = pd.read_excel("./dataset.xlsx")

df["price_per_m2"] = df["Y house price of unit area"] / 3.3 * 10000

# primo modello
X = df[["X5 latitude", "X6 longitude"]]
y = df["price_per_m2"]

model = LinearRegression()
model.fit(X, y)
print(model.intercept_)

X_with_const = sm.add_constant(X)

model_ols = sm.OLS(y, X_with_const).fit()

print(model_ols.summary())

dump(model, 'model.joblib')

#secondo modello
X2 = df[["X2 house age", "X3 distance to the nearest MRT station", "X4 number of convenience stores"]]

model2 = LinearRegression()
model2.fit(X2, y)
print(model.intercept_)

X_with_const2 = sm.add_constant(X2)

model_ols2 = sm.OLS(y, X_with_const2).fit()

print(model_ols2.summary())

dump(model2, 'model2.joblib')

# web app
import streamlit as st
import numpy as np
from joblib import load

model = load('model.joblib')
model2 = load("model2.joblib")

st.set_page_config(page_title="Stima Prezzo Casa")

st.title("Stima il Prezzo della Casa (Regione di Sindian, Nuova Taipei, Taiwan)")

group = st.radio("Quali informazioni hai a disposizione?", ("Latitudine e Longitudine", "Età casa, Distanza da stazione MRT più vicina, Numero di minimarket vicini"))

if group == "Latitudine e Longitudine":
    lat = st.number_input("Latitudine")
    lon = st.number_input("Longitudine")
    X = np.array([[lat, lon]])
    if lat < 24.93207 or lat > 25.01459 or lon < 121.47353 or lon > 121.56627:
        st.error(f"Inserisci coordinate valide")
    else:
        prediction = model.predict(X)[0]
        st.success(f"Prezzo stimato (geo): {prediction:.2f} TWD/mq")

elif group == "Età casa, Distanza da stazione MRT più vicina, Numero di minimarket vicini":
    age = st.number_input("Età della casa")
    dist = st.number_input("Distanza da stazione MRT più vicina (in metri)")
    conv = st.number_input("Numero di minimarket vicini")
    X2 = np.array([[age, dist, conv]])
    if age < 0 or dist < 0 or conv < 0:
        st.error(f"Inserisci valori validi (non negativi)")
    else:
        prediction = model2.predict(X2)[0]
        st.success(f"Prezzo stimato (caratteristiche casa): {prediction:.2f} TWD/mq")