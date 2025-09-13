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
    line-height: 1.6;
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
.stSelectbox > div[role="listbox"] {
    font-weight: 600;
}
button {
    background-color: #1971c2 !important;
    color: white !important;
    font-weight: 700 !important;
}
img {
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)


# --- Animación simple para el header ---
def animated_header(text, delay=0.07):
    placeholder = st.empty()
    displayed = ""
    for c in text:
        displayed += c
        placeholder.markdown(f"<h1 style='color:#1c7ed6;text-align:center'>{displayed}</h1>", unsafe_allow_html=True)
        time.sleep(delay)


animated_header("🐧 Kernel Linux & Red Hat: Aprende y Descubre")


st.markdown("---")

# --- Sección de Información ---
with st.container():
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown("## ¿Qué es el Kernel Linux?")
    st.write(
        "El Kernel Linux es el corazón del sistema operativo Linux. "
        "Fue creado en 1991 por Linus Torvalds con el propósito de desarrollar un núcleo robusto, libre y abierto que maneje las operaciones esenciales del sistema. "
        "El kernel actúa como un intermediario entre el hardware y el software, gestionando recursos como la memoria, el procesador, los dispositivos conectados y los procesos que se ejecutan. "
        "Gracias a su diseño modular y flexible, el kernel Linux se adapta a una gran variedad de sistemas, desde computadoras personales hasta supercomputadoras y dispositivos embebidos. "
        "Su naturaleza de código abierto ha permitido que miles de desarrolladores alrededor del mundo colaboren y mejoren continuamente este proyecto, convirtiéndolo en una pieza fundamental en el mundo tecnológico actual."
    )
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg", width=140, caption="Tux, la mascota oficial de Linux")
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown("## ¿Qué es Red Hat?")
    st.write(
        "Red Hat, Inc. es una empresa pionera en el desarrollo y soporte de soluciones de código abierto. "
        "Es ampliamente conocida por Red Hat Enterprise Linux (RHEL), una distribución de Linux enfocada en el sector empresarial que destaca por su estabilidad, seguridad y soporte profesional. "
        "RHEL se utiliza en una gran cantidad de servidores y entornos corporativos donde la confiabilidad es crítica. "
        "En 2019, Red Hat fue adquirida por IBM, una jugada estratégica que consolidó su influencia en el mercado tecnológico, especialmente en soluciones de nube híbrida y software empresarial. "
        "Más allá de RHEL, Red Hat impulsa múltiples proyectos de código abierto y ofrece herramientas que facilitan la gestión, automatización y escalabilidad de infraestructuras TI en todo el mundo."
    )
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Red_Hat_logo.svg/1200px-Red_Hat_logo.svg.png", width=220, caption="Logo de Red Hat")
    st.markdown("</div>", unsafe_allow_html=True)


st.markdown("---")

# --- Quiz interactivo ---
st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
st.markdown("## 🧠 Quiz: Pon a prueba tus conocimientos")

questions = [
    {
        "q": "¿Quién es el creador del Kernel Linux?",
        "options": ["Bill Gates", "Linus Torvalds", "Steve Jobs", "Richard Stallman"],
        "answer": "Linus Torvalds"
    },
    {
        "q": "¿En qué año fue creado el Kernel Linux?",
        "options": ["1985", "1991", "1998", "2000"],
        "answer": "1991"
    },
    {
        "q": "¿Cuál es la función principal del Kernel Linux?",
        "options": [
            "Gestionar hardware y recursos del sistema",
            "Navegar por Internet",
            "Editar documentos",
            "Ejecutar videojuegos"
        ],
        "answer": "Gestionar hardware y recursos del sistema"
    },
    {
        "q": "¿Qué es Red Hat Enterprise Linux (RHEL)?",
        "options": [
            "Un antivirus",
            "Una distribución empresarial de Linux",
            "Un editor de vídeo",
            "Un navegador web"
        ],
        "answer": "Una distribución empresarial de Linux"
    },
    {
        "q": "¿Cuál empresa adquirió Red Hat en 2019?",
        "options": ["Google", "IBM", "Microsoft", "Amazon"],
        "answer": "IBM"
    },
    {
        "q": "¿Linux es software libre y de código abierto?",
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
all_answered = True

for idx, q in enumerate(questions):
    st.markdown(f"### {idx+1}. {q['q']}")
    options = ["Selecciona una opción"] + q["options"]
    choice = st.selectbox("", options, key=f"q{idx}")
    if choice == "Selecciona una opción":
        all_answered = False
    elif choice == q["answer"]:
        score += 1

if st.button("📊 Ver Resultado"):
    if not all_answered:
        st.warning("⚠️ Por favor responde todas las preguntas antes de ver el resultado.")
    else:
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
