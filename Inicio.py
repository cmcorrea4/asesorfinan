import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import streamlit as st

# Generar datos de clientes ficticios
data = {
    'edad': [25, 35, 45, 55, 65, 75],
    'ingresos': [3000000, 5000000, 7000000, 10000000, 15000000, 20000000],
    'patrimonio': [5000000, 10000000, 15000000, 20000000, 30000000, 50000000],
    'tipo_cliente': ['individual','individual', 'pequeña_empresa', 'mediana_empresa', 'grande_empresa', 'alta_renta']
}
df = pd.DataFrame(data)

# Dividir datos en características y etiqueta
X = df[['edad', 'ingresos', 'patrimonio']]
y = df['tipo_cliente']

# Dividir datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo de árbol de decisión
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)

# Entrenar modelo SVM
svm_model = SVC()
svm_model.fit(X_train, y_train)

# Función para clasificar clientes
def classify_client(edad, ingresos, patrimonio):
    client_data = [[edad, ingresos, patrimonio]]
    dt_prediction = dt_model.predict(client_data)[0]
    svm_prediction = svm_model.predict(client_data)[0]
    return dt_prediction, svm_prediction

# Aplicación Streamlit
st.title("Sistema de Asesoría Financiera")

st.subheader("Ingrese información del cliente")
edad = st.number_input("Edad", min_value=18, max_value=100, step=1, value=35)
ingresos = st.number_input("Ingresos anuales ($)", min_value=0, max_value=1000000000, step=1000, value=500000)
patrimonio = st.number_input("Patrimonio ($)", min_value=0, max_value=1000000000, step=1000, value=1000000)

if st.button("Clasificar cliente"):
    dt_pred, svm_pred = classify_client(edad, ingresos, patrimonio)
    st.write(f"Clasificación por árbol de decisión: {dt_pred}")
    st.write(f"Clasificación por SVM: {svm_pred}")

    if dt_pred == svm_pred:
        st.write(f"El cliente es clasificado como un cliente {dt_pred}")
    else:
        st.write("Las clasificaciones difieren. Se recomienda revisar el caso manualmente.")

with st.sidebar:
  st.subheader("Información del sistema")
  st.write("Este sistema utiliza un árbol de decisión y una máquina de soporte vectorial (SVM) para clasificar a los clientes en diferentes tipos.")
  st.write("Los tipos de clientes son: individual, pequeña empresa, mediana empresa, grande empresa y alta renta.")
  st.write("La clasificación se basa en la edad, los ingresos anuales y el patrimonio del cliente.")
