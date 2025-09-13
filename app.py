import streamlit as st
from PIL import Image
import time

# --- Configuración de página ---
st.set_page_config(page_title="🐧 Kernel Linux & Red Hat", page_icon="🐧", layout="wide")

# --- Estilos CSS para decorar ---
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #4c6ef5, #d0ebff);
    color: #0b3d91;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
h1, h2, h3 {
    font-weight: 700;
}
.container {
    background: #f0f8ffcc;
    border-radius: 20px;
    padding: 25px 40px;
    margin-bottom: 40px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.15);
}
.quiz-container {
    background: #e0f2ffcc;
    border-radius: 20px;
    padding: 25px 40px;
    margin-top: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.25);
}
.stRadio > label {
    font-weight: 600;
}
button {
    background-color: #1971c2 !important;
    color: white !important;
    font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)


# --- Animación simple para el header ---
def animated_header(text, delay=0.07):
    placeholder = st.empty()
    displayed = ""
    for c in text:
        displayed += c
        placeholder.markdown(f"<h1 style='color:#1c7ed6'>{displayed}</h1>", unsafe_allow_html=True)
        time.sleep(delay)


animated_header("🐧 Kernel Linux & Red Hat: Aprende y Descubre")


st.markdown("---")

# --- Sección de Información ---
with st.container():
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown("## ¿Qué es el Kernel Linux?")
    st.write("""
    El **Kernel Linux** es el núcleo del sistema operativo Linux.  
    Se encarga de gestionar el hardware, controlar los procesos, la memoria y la comunicación entre los programas y la máquina física.  
    Fue creado por **Linus Torvalds** en 1991 y es un proyecto de código abierto que ha evolucionado hasta ser la base de muchas distribuciones.
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg", width=140, caption="Tux, la mascota oficial de Linux")
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown("## ¿Qué es Red Hat?")
    st.write("""
    **Red Hat, Inc.** es una empresa líder en soluciones de software de código abierto.  
    Su producto más destacado es **Red Hat Enterprise Linux (RHEL)**, una distribución de Linux enfocada en empresas, que ofrece estabilidad, soporte y seguridad.  
    Red Hat fue adquirida por IBM en 2019, reforzando su papel en el ecosistema tecnológico empresarial.
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Red_Hat_logo.svg/1200px-Red_Hat_logo.svg.png", width=220, caption="Logo de Red Hat")
    st.markdown("</div>", unsafe_allow_html=True)


st.markdown("---")

# --- Quiz interactivo ---
st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
st.markdown("## 🧠 Quiz: Pon a prueba tus conocimientos")

questions = [
    {
        "q": "¿Quién creó el Kernel Linux?",
        "options": ["Bill Gates", "Linus Torvalds", "Steve Jobs", "Richard Stallman"],
        "answer": "Linus Torvalds"
    },
    {
        "q": "¿En qué año se creó el Kernel Linux?",
        "options": ["1985", "1991", "1998", "2000"],
        "answer": "1991"
    },
    {
        "q": "¿Cuál es la función principal del Kernel Linux?",
        "options": [
            "Gestionar hardware y recursos",
            "Navegar por internet",
            "Editar documentos",
            "Ejecutar juegos"
        ],
        "answer": "Gestionar hardware y recursos"
    },
    {
        "q": "¿Qué es Red Hat Enterprise Linux (RHEL)?",
        "options": [
            "Un antivirus",
            "Una distribución de Linux para empresas",
            "Un software de edición de video",
            "Un navegador web"
        ],
        "answer": "Una distribución de Linux para empresas"
    },
    {
        "q": "¿Qué empresa compró Red Hat en 2019?",
        "options": ["Google", "IBM", "Microsoft", "Amazon"],
        "answer": "IBM"
    },
    {
        "q": "¿Linux es software de código abierto?",
        "options": ["Sí", "No"],
        "answer": "Sí"
    },
    {
        "q": "¿Cuál es la mascota oficial de Linux?",
        "options": ["Pingüino", "Perro", "Gato", "Águila"],
        "answer": "Pingüino"
    }
]

score = 0
responses = []

for idx, q in enumerate(questions):
    st.markdown(f"### {idx+1}. {q['q']}")
    choice = st.radio(f"Selecciona una opción:", q["options"], key=f"q{idx}")
    responses.append(choice)
    if choice == q["answer"]:
        score += 1

if st.button("📊 Ver Resultado"):
    st.markdown(f"### Tu puntaje es: {score} de {len(questions)}")
    if score == len(questions):
        st.balloons()
        st.success("🎉 ¡Excelente! Eres un experto en Kernel Linux y Red Hat.")
    elif score >= len(questions)//2:
        st.success("¡Buen trabajo! Sigue aprendiendo para ser un experto.")
    else:
        st.warning("¡No te rindas! Sigue investigando y practicando.")

st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align:center;color:#555;font-size:14px;'>© 2025 Kernel Linux & Red Hat Info | Creado con ❤️ usando Streamlit</p>", unsafe_allow_html=True)
