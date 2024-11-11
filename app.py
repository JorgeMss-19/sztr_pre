import streamlit as st
import joblib
import numpy as np

# Cargar el modelo
model = joblib.load('model.joblib')

# Sidebar para navegación
st.sidebar.title("Sistema de Predicción de Préstamos")
selected = st.sidebar.radio("Navegación", ["Predicción de Aprobación de Préstamo"])

# Página de predicción
if selected == "Predicción de Aprobación de Préstamo":
    st.title("Aprobación de Préstamo usando ML")

    # Entradas del usuario para cada característica
    person_age = st.number_input("Edad de la persona", min_value=18, max_value=100, step=1)
    person_income = st.number_input("Ingreso anual de la persona", min_value=0)
    person_emp_length = st.number_input("Años de experiencia laboral", min_value=0)
    loan_amnt = st.number_input("Monto del préstamo solicitado", min_value=0)
    loan_int_rate = st.number_input("Tasa de interés del préstamo (%)", min_value=0.0, format="%.2f")
    loan_percent_income = st.number_input("Porcentaje del ingreso destinado al préstamo", min_value=0.0, max_value=1.0, format="%.2f")
    cb_person_cred_hist_length = st.number_input("Longitud del historial crediticio", min_value=0)

    # Botón de predicción
    if st.button("Predecir Aprobación de Préstamo"):
        # Convertir los datos ingresados en un array y hacer predicción
        user_input = np.array([[person_age, person_income, person_emp_length, loan_amnt,
                                loan_int_rate, loan_percent_income, cb_person_cred_hist_length]])
        
        prediction = model.predict(user_input)

        # Mostrar el resultado
        if prediction[0] == 1:
            st.success("El préstamo será aprobado.")
        else:
            st.error("El préstamo no será aprobado.")
