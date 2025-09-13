import streamlit as st
import time

# --- Configuración ---
st.set_page_config(page_title="🐧 Kernel Linux & Red Hat", page_icon="🐧", layout="centered")

# --- Estilos ---
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
button {
    background-color: #1971c2 !important;
    color: white !important;
    font-weight: 700 !important;
    padding: 10px 25px;
    border-radius: 8px;
    cursor: pointer;
}
.stTextInput>div>div>input {
    border-radius: 8px !important;
    padding: 8px !important;
    border: 2px solid #1971c2 !important;
    font-weight: 600 !important;
}
img {
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    margin: 10px 0;
    max-width: 300px;
}
</style>
""", unsafe_allow_html=True)

# --- Funciones ---
def show_welcome():
    st.markdown("<h1 style='text-align:center; color:#1c7ed6;'>🐧 Bienvenido a Kernel Linux & Red Hat</h1>", unsafe_allow_html=True)

    st.markdown("<p style='text-align:center; font-size:18px;'>Una app interactiva para aprender sobre Linux y Red Hat, y probar tus conocimientos con un quiz.</p>", unsafe_allow_html=True)
    if st.button("🚀 Iniciar"):
        st.session_state.page = "Información"

def show_information():
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown("## ¿Qué es el Kernel Linux?")
    st.write(
        "El Kernel Linux es el corazón del sistema operativo Linux. Fue creado en 1991 por Linus Torvalds con el propósito de desarrollar un núcleo robusto, libre y abierto que maneje las operaciones esenciales del sistema. "
        "El kernel actúa como un intermediario entre el hardware y el software, gestionando recursos como la memoria, el procesador, los dispositivos conectados y los procesos que se ejecutan. "
        "Gracias a su diseño modular y flexible, el kernel Linux se adapta a una gran variedad de sistemas, desde computadoras personales hasta supercomputadoras y dispositivos embebidos. "
        "Su naturaleza de código abierto ha permitido que miles de desarrolladores alrededor del mundo colaboren y mejoren continuamente este proyecto, convirtiéndolo en una pieza fundamental en el mundo tecnológico actual."
    )
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg", width=140, caption="Tux, la mascota oficial de Linux")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown("## ¿Qué es Red Hat?")
    st.write(
        "Red Hat, Inc. es una empresa pionera en el desarrollo y soporte de soluciones de código abierto. Es ampliamente conocida por Red Hat Enterprise Linux (RHEL), una distribución de Linux enfocada en el sector empresarial que destaca por su estabilidad, seguridad y soporte profesional. "
        "RHEL se utiliza en una gran cantidad de servidores y entornos corporativos donde la confiabilidad es crítica. En 2019, Red Hat fue adquirida por IBM, una jugada estratégica que consolidó su influencia en el mercado tecnológico, especialmente en soluciones de nube híbrida y software empresarial. "
        "Más allá de RHEL, Red Hat impulsa múltiples proyectos de código abierto y ofrece herramientas que facilitan la gestión, automatización y escalabilidad de infraestructuras TI en todo el mundo."
    )
    # Imagen con URL que permite acceso directo para evitar problema de hotlink
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Red_Hat_logo.svg/2560px-Red_Hat_logo.svg.png", width=220, caption="Logo de Red Hat")
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("➡️ Ir al Quiz"):
        st.session_state.page = "Quiz"

def show_quiz():
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False

    if not st.session_state.quiz_started:
        st.markdown("<h2>📝 Por favor, ingresa tu nombre para comenzar el quiz:</h2>", unsafe_allow_html=True)
        name = st.text_input("Nombre")
        if st.button("Comenzar Quiz"):
            if name.strip():
                st.session_state.quiz_started = True
                st.session_state.user_name = name.strip()
                st.experimental_rerun()
            else:
                st.warning("Por favor, ingresa tu nombre antes de continuar.")
    else:
        st.markdown(f"<h2>Hola, <span style='color:#1971c2;'>{st.session_state.user_name}</span>, responde las siguientes preguntas:</h2>", unsafe_allow_html=True)

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

        if "answers" not in st.session_state:
            st.session_state.answers = ["Selecciona una opción"] * len(questions)

        for idx, q in enumerate(questions):
            st.markdown(f"**{idx+1}. {q['q']}**")
            options = ["Selecciona una opción"] + q["options"]
            st.session_state.answers[idx] = st.selectbox(
                "", options,
                index=options.index(st.session_state.answers[idx]) if st.session_state.answers[idx] in options else 0,
                key=f"q{idx}"
            )

        if st.button("Finalizar y Ver Resultado"):
            if "Selecciona una opción" in st.session_state.answers:
                st.warning("Por favor responde todas las preguntas antes de finalizar.")
            else:
                score = 0
                results = []
                for idx, q in enumerate(questions):
                    correct = (st.session_state.answers[idx] == q["answer"])
                    if correct:
                        score += 1
                    results.append((q["q"], st.session_state.answers[idx], q["answer"], correct))

                st.markdown("---")
                st.markdown(f"### {st.session_state.user_name}, obtuviste {score} de {len(questions)} preguntas correctas.")

                if score == len(questions):
                    st.balloons()
                    motivacion = "🎉 ¡Excelente! Eres un experto en Kernel Linux y Red Hat."
                elif score >= len(questions)//2:
                    motivacion = "👍 ¡Buen trabajo! Sigue aprendiendo para ser un experto."
                else:
                    motivacion = "💪 ¡No te rindas! Sigue investigando y practicando."

                st.markdown(f"### {motivacion}")

                for q_text, user_ans, correct_ans, is_correct in results:
                    color = "#28a745" if is_correct else "#dc3545"
                    st.markdown(f"**Pregunta:** {q_text}")
                    st.markdown(f"Tu respuesta: <span style='color:{color}; font-weight:600'>{user_ans}</span>", unsafe_allow_html=True)
                    if not is_correct:
                        st.markdown(f"Respuesta correcta: <span style='color:#198754; font-weight:600'>{correct_ans}</span>", unsafe_allow_html=True)
                    st.markdown("---")

                if st.button("Reiniciar Quiz"):
                    st.session_state.quiz_started = False
                    st.session_state.answers = ["Selecciona una opción"] * len(questions)
                    st.experimental_rerun()

# --- Navegación ---
if "page" not in st.session_state:
    st.session_state.page = "Inicio"

page = st.session_state.page

st.sidebar.title("Navegación")
options = ["Inicio", "Información", "Quiz"]
choice = st.sidebar.radio("Ir a:", options, index=options.index(page))
if choice != page:
    st.session_state.page = choice
    st.experimental_rerun()

# --- Mostrar páginas ---
if page == "Inicio":
    show_welcome()
elif page == "Información":
    show_information()
elif page == "Quiz":
    show_quiz()
