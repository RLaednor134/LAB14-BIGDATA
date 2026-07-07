import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# Configuración
# -------------------------
st.set_page_config(
    page_title="Dashboard - Churn",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Analítico")
st.subheader("Predicción de Abandono de Clientes (Customer Churn)")

st.markdown("---")

# -------------------------
# Leer Dataset
# -------------------------
df = pd.read_csv("dataset_personal.csv")

# -------------------------
# Sidebar
# -------------------------
st.sidebar.header("Filtros")

planes = st.sidebar.multiselect(
    "Tipo de Plan",
    options=df["Plan"].unique(),
    default=df["Plan"].unique()
)

df = df[df["Plan"].isin(planes)]

# -------------------------
# KPI
# -------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Clientes", len(df))

with col2:
    abandono = df["Churn"].sum()
    st.metric("Clientes que abandonan", abandono)

with col3:
    porcentaje = (df["Churn"].mean()) * 100
    st.metric("Porcentaje de abandono", f"{porcentaje:.2f}%")

st.markdown("---")

# -------------------------
# Gráfico Barras
# -------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("Abandono por Tipo de Plan")

    fig, ax = plt.subplots(figsize=(6,4))

    sns.countplot(
        data=df,
        x="Plan",
        hue="Churn",
        palette="Blues",
        ax=ax
    )

    ax.set_xlabel("Plan")

    ax.set_ylabel("Cantidad")

    st.pyplot(fig)

# -------------------------
# Histograma
# -------------------------

with col2:

    st.subheader("Distribución del Gasto Mensual")

    fig, ax = plt.subplots(figsize=(6,4))

    ax.hist(
        df["Gasto_Mensual"],
        bins=20
    )

    ax.set_xlabel("Gasto Mensual")

    ax.set_ylabel("Frecuencia")

    st.pyplot(fig)

st.markdown("---")

# -------------------------
# Scatter Plot
# -------------------------

col3, col4 = st.columns(2)

with col3:

    st.subheader("Antigüedad vs Gasto Mensual")

    fig, ax = plt.subplots(figsize=(6,4))

    sns.scatterplot(
        data=df,
        x="Antiguedad",
        y="Gasto_Mensual",
        hue="Churn",
        palette="Set1",
        ax=ax
    )

    st.pyplot(fig)

# -------------------------
# Heatmap
# -------------------------

with col4:

    st.subheader("Mapa de Correlaciones")

    fig, ax = plt.subplots(figsize=(6,4))

    sns.heatmap(
        df.corr(numeric_only=True),
        annot=True,
        cmap="Blues",
        ax=ax
    )

    st.pyplot(fig)

st.markdown("---")

# -------------------------
# Estadísticas
# -------------------------

st.subheader("Estadísticas Descriptivas")

st.dataframe(df.describe())

st.markdown("---")

# -------------------------
# Hallazgos
# -------------------------

st.header("📌 Hallazgos Principales")

st.write("""
**Hallazgo 1:** Existe un porcentaje importante de clientes con riesgo de abandono.

**Hallazgo 2:** Los clientes con mayor cantidad de reclamos presentan mayor probabilidad de abandonar el servicio.

**Hallazgo 3:** La antigüedad del cliente influye en la permanencia dentro de la empresa.
""")

st.markdown("---")

# -------------------------
# Recomendaciones
# -------------------------

st.header("✅ Recomendaciones")

st.write("""
- Implementar programas de fidelización para clientes con alto riesgo de abandono.

- Reducir el tiempo de atención de reclamos.

- Ofrecer promociones a clientes nuevos y con mayor gasto mensual.

- Monitorear continuamente los indicadores del dashboard para apoyar la toma de decisiones.
""")

st.markdown("---")

st.success("Dashboard desarrollado para el Laboratorio 14 - Business Intelligence & Big Data")
