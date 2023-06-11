import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_correlation(dataframe, x, y):
    correlation = np.corrcoef(dataframe[x], dataframe[y])[0, 1]
    return correlation

def plot_scatterplot(dataframe, x, y):
    plt.scatter(dataframe[x], dataframe[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f"Scatter Plot: {x} vs {y}")
    st.pyplot()

# Menampilkan judul halaman
st.title("Perhitungan Korelasi")

# Membuat form input untuk data manual
st.subheader("Input Data Manual")
data_rows = st.number_input("Jumlah Baris Data", min_value=2, value=5)
data_cols = st.number_input("Jumlah Kolom Data", min_value=2, value=2)

data = []
for i in range(data_rows):
    row = []
    for j in range(data_cols):
        value = st.number_input(f"Data ({i+1}, {j+1})", value=0.0)
        row.append(value)
    data.append(row)

dataframe = pd.DataFrame(data)
st.write(dataframe)

# Memilih kolom-kolom untuk perhitungan korelasi
columns = dataframe.columns
x = st.selectbox("Pilih variabel X:", columns)
y = st.selectbox("Pilih variabel Y:", columns)

clicked = st.button('do the Correlation !!')

# Memeriksa apakah variabel X dan Y telah dipilih
if clicked:
    correlation = calculate_correlation(dataframe, x, y)

    # Menampilkan hasil korelasi
    st.subheader("Hasil Korelasi:")
    st.write(f"Korelasi antara {x} dan {y} adalah {correlation:.2f}")

click = st.button('do the Scatterplot !!')
if click:
    plot_scatterplot(dataframe, x, y)
