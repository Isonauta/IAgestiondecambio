"""
╔══════════════════════════════════════════════════════════╗
║       NEXUS ADAPTIVE CHANGE — MVP v1.0                  ║
║       Plataforma de Gestión del Cambio con IA            ║
║       Desarrollado por Procesus / Isonauta               ║
╚══════════════════════════════════════════════════════════╝

Instalación:
    pip install streamlit numpy pandas

Ejecución:
    streamlit run nexus_adaptive_change.py
"""

import streamlit as st
import numpy as np
import pandas as pd
import time

# ─────────────────────────────────────────────
# CONFIGURACIÓN GLOBAL
# ─────────────────────────────────────────────

st.set_page_config(
    page_title="Nexus Adaptive Change",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# CSS PERSONALIZADO — DARK CORPORATE THEME
# ─────────────────────────────────────────────

st.markdown("""
<style>
/* ── IMPORTS ─────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Syne:wght@400;600;700;800&display=swap');

/* ── BASE ────────────────────────────────── */
html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
}

.stApp {
    background-color: #0a0c10;
    color: #e2e8f0;
}

/* ── SIDEBAR ─────────────────────────────── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1117 0%, #0a0f1e 100%);
    border-right: 1px solid #1e2d40;
}

[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span {
    color: #94a3b8 !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.05em;
}

/* ── MÉTRICAS ────────────────────────────── */
[data-testid="stMetric"] {
    background: linear-gradient(135deg, #0f172a 0%, #111827 100%);
    border: 1px solid #1e2d40;
    border-radius: 12px;
    padding: 1.2rem 1.5rem !important;
    position: relative;
    overflow: hidden;
    transition: border-color 0.3s ease;
}

[data-testid="stMetric"]:hover {
    border-color: #d97706;
}

[data-testid="stMetric"]::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 3px; height: 100%;
    background: linear-gradient(180deg, #d97706, #f59e0b);
    border-radius: 12px 0 0 12px;
}

[data-testid="stMetricLabel"] {
    color: #64748b !important;
    font-size: 0.72rem !important;
    font-family: 'JetBrains Mono', monospace !important;
    text-transform: uppercase;
    letter-spacing: 0.12em;
}

[data-testid="stMetricValue"] {
    color: #f1f5f9 !important;
    font-size: 2rem !important;
    font-weight: 800 !important;
    font-family: 'Syne', sans-serif !important;
}

[data-testid="stMetricDelta"] {
    font-size: 0.75rem !important;
    font-family: 'JetBrains Mono', monospace !important;
}

/* ── GRÁFICOS ────────────────────────────── */
[data-testid="stArrowVegaLiteChart"],
.stPlotlyChart,
[data-testid="stLineChart"],
[data-testid="stBarChart"] {
    background: #0f172a !important;
    border: 1px solid #1e2d40 !important;
    border-radius: 12px !important;
    padding: 1rem !important;
}

/* ── BOTÓN ───────────────────────────────── */
.stButton > button {
    background: linear-gradient(135deg, #d97706 0%, #b45309 100%) !important;
    color: #0a0c10 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 600 !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.6rem 1.8rem !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 20px rgba(217, 119, 6, 0.3) !important;
}

.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 28px rgba(217, 119, 6, 0.5) !important;
}

/* ── INFO / ALERT BOX ────────────────────── */
[data-testid="stAlert"] {
    background: linear-gradient(135deg, #0f172a 0%, #0c1a2e 100%) !important;
    border: 1px solid #1d4ed8 !important;
    border-left: 4px solid #3b82f6 !important;
    border-radius: 10px !important;
    color: #bfdbfe !important;
}

[data-testid="stAlert"] p {
    color: #bfdbfe !important;
    font-size: 0.9rem !important;
    line-height: 1.7;
}

/* ── HEADERS ─────────────────────────────── */
h1 { 
    color: #f1f5f9 !important; 
    font-weight: 800 !important;
    letter-spacing: -0.02em;
}
h2 { 
    color: #e2e8f0 !important; 
    font-weight: 700 !important;
    font-size: 1.1rem !important;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: #64748b !important;
}
h3 { 
    color: #cbd5e1 !important; 
    font-size: 0.9rem !important;
}

/* ── DIVIDER ─────────────────────────────── */
hr {
    border-color: #1e2d40 !important;
    margin: 1.5rem 0 !important;
}

/* ── SELECTBOX ───────────────────────────── */
[data-testid="stSelectbox"] > div > div {
    background: #0f172a !important;
    border: 1px solid #1e2d40 !important;
    color: #e2e8f0 !important;
    border-radius: 8px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.82rem !important;
}

/* ── SPINNER ─────────────────────────────── */
.stSpinner > div {
    border-top-color: #d97706 !important;
}

/* ── SCROLLBAR ───────────────────────────── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0a0c10; }
::-webkit-scrollbar-thumb { background: #1e2d40; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #d97706; }

/* ── BADGE CUSTOM ────────────────────────── */
.badge-alto {
    display: inline-block;
    background: linear-gradient(135deg, #7f1d1d, #991b1b);
    color: #fca5a5;
    border: 1px solid #b91c1c;
    border-radius: 6px;
    padding: 0.15rem 0.6rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

.badge-medio {
    display: inline-block;
    background: linear-gradient(135deg, #78350f, #92400e);
    color: #fcd34d;
    border: 1px solid #d97706;
    border-radius: 6px;
    padding: 0.15rem 0.6rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

.badge-bajo {
    display: inline-block;
    background: linear-gradient(135deg, #064e3b, #065f46);
    color: #6ee7b7;
    border: 1px solid #059669;
    border-radius: 6px;
    padding: 0.15rem 0.6rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

/* ── SECTION CARD ────────────────────────── */
.section-card {
    background: linear-gradient(135deg, #0f172a 0%, #111827 100%);
    border: 1px solid #1e2d40;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}

.section-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: #d97706;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    margin-bottom: 0.5rem;
}

.status-dot {
    display: inline-block;
    width: 8px; height: 8px;
    background: #22c55e;
    border-radius: 50%;
    margin-right: 6px;
    box-shadow: 0 0 8px #22c55e;
    animation: pulse-green 2s infinite;
}

@keyframes pulse-green {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# DATOS SIMULADOS — DUMMY DATA
# ─────────────────────────────────────────────

np.random.seed(42)

PROYECTOS = {
    "Implementación ERP (SAP S/4HANA)": {
        "resistencia": 34,
        "resistencia_delta": -5,
        "adopcion": 62,
        "adopcion_delta": +8,
        "saturacion": "Alta",
        "saturacion_nivel": "alto",
        "area_riesgo": "Finanzas",
        "semanas": 4,
        "insight_extra": "El 68% de los usuarios del módulo FI/CO no ha completado el onboarding básico.",
    },
    "Migración Cloud (Azure)": {
        "resistencia": 21,
        "resistencia_delta": -12,
        "adopcion": 78,
        "adopcion_delta": +14,
        "saturacion": "Media",
        "saturacion_nivel": "medio",
        "area_riesgo": "Operaciones TI",
        "semanas": 4,
        "insight_extra": "Detectado solapamiento de roles entre equipo legacy y nuevo equipo cloud.",
    },
    "Transformación Digital RRHH": {
        "resistencia": 48,
        "resistencia_delta": +3,
        "adopcion": 41,
        "adopcion_delta": -2,
        "saturacion": "Alta",
        "saturacion_nivel": "alto",
        "area_riesgo": "Jefaturas intermedias",
        "semanas": 4,
        "insight_extra": "Patrón de uso irregular en la plataforma HCM: 82% de accesos concentrados en 15% del equipo.",
    },
    "Implementación ISO 27001": {
        "resistencia": 18,
        "resistencia_delta": -8,
        "adopcion": 85,
        "adopcion_delta": +11,
        "saturacion": "Baja",
        "saturacion_nivel": "bajo",
        "area_riesgo": "Ninguna crítica",
        "semanas": 4,
        "insight_extra": "Proyecto en trayectoria óptima. Se recomienda acelerar la fase de auditoría interna.",
    },
}

def generar_serie_riesgo(resistencia: int, semanas: int = 4) -> pd.DataFrame:
    """Genera evolución de riesgo para las últimas N semanas."""
    base = resistencia
    valores = [max(5, min(95, base + np.random.randint(-10, 15) - i * 2)) for i in range(semanas * 7)]
    fechas = pd.date_range(end=pd.Timestamp.today(), periods=len(valores), freq="D")
    df = pd.DataFrame({"Índice de Riesgo": valores}, index=fechas)
    return df


def generar_sentimiento() -> pd.DataFrame:
    """Genera distribución de sentimiento de comentarios."""
    categorias = ["Positivo 👍", "Neutral 😐", "Negativo 👎"]
    valores = [np.random.randint(28, 52), np.random.randint(18, 35), np.random.randint(12, 28)]
    return pd.DataFrame({"Comentarios": valores}, index=categorias)


def generar_heatmap_areas() -> pd.DataFrame:
    """Genera matriz de riesgo por área y dimensión."""
    areas = ["Finanzas", "TI", "Operaciones", "RRHH", "Comercial"]
    dimensiones = ["Resistencia", "Capacitación", "Liderazgo", "Comunicación"]
    data = np.random.randint(15, 85, size=(len(areas), len(dimensiones)))
    return pd.DataFrame(data, index=areas, columns=dimensiones)


# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────

with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 1.5rem 0 1rem 0;">
        <div style="font-size:2.5rem; margin-bottom:0.3rem;">🚀</div>
        <div style="font-family:'Syne',sans-serif; font-size:1.2rem; font-weight:800; 
                    color:#f1f5f9; letter-spacing:-0.01em;">NEXUS</div>
        <div style="font-family:'JetBrains Mono',monospace; font-size:0.65rem; 
                    color:#d97706; letter-spacing:0.2em; text-transform:uppercase;">
            Adaptive Change
        </div>
    </div>
    <hr style="border-color:#1e2d40; margin:0.5rem 0 1.5rem 0;">
    """, unsafe_allow_html=True)

    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace; font-size:0.68rem; color:#64748b; text-transform:uppercase; letter-spacing:0.12em;">Proyecto activo</p>', unsafe_allow_html=True)
    
    proyecto_seleccionado = st.selectbox(
        label="proyecto",
        options=list(PROYECTOS.keys()),
        label_visibility="collapsed",
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace; font-size:0.68rem; color:#64748b; text-transform:uppercase; letter-spacing:0.12em;">Estado del sistema</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background:#0f172a; border:1px solid #1e2d40; border-radius:8px; padding:0.8rem 1rem;">
        <div style="font-family:'JetBrains Mono',monospace; font-size:0.72rem; color:#94a3b8; margin-bottom:0.4rem;">
            <span class="status-dot"></span>Motor IA — Activo
        </div>
        <div style="font-family:'JetBrains Mono',monospace; font-size:0.72rem; color:#94a3b8; margin-bottom:0.4rem;">
            <span style="display:inline-block; width:8px; height:8px; background:#3b82f6; border-radius:50%; margin-right:6px;"></span>
            n8n Engine — En espera
        </div>
        <div style="font-family:'JetBrains Mono',monospace; font-size:0.72rem; color:#94a3b8;">
            <span style="display:inline-block; width:8px; height:8px; background:#22c55e; border-radius:50%; margin-right:6px;"></span>
            Data Pipeline — OK
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p style="font-family:\'JetBrains Mono\',monospace; font-size:0.68rem; color:#64748b; text-transform:uppercase; letter-spacing:0.12em;">Módulos</p>', unsafe_allow_html=True)
    
    modulos = ["📊  Dashboard OCM", "🧠  IA Insights", "📋  Plan de Acción", "👥  Stakeholders", "📁  Documentos"]
    for i, modulo in enumerate(modulos):
        activo = i == 0
        color = "#d97706" if activo else "#475569"
        bg = "#1e2d40" if activo else "transparent"
        st.markdown(f"""
        <div style="background:{bg}; border-radius:6px; padding:0.45rem 0.8rem; margin-bottom:0.2rem; 
                    font-family:'Syne',sans-serif; font-size:0.82rem; color:{color}; cursor:pointer;">
            {modulo}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="position:fixed; bottom:1.5rem; left:0; width:260px; text-align:center;">
        <div style="font-family:'JetBrains Mono',monospace; font-size:0.62rem; color:#334155; letter-spacing:0.08em;">
            v1.0.0 · Procesus / Isonauta<br>
            © 2025 — Nexus Adaptive Change
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# DATOS DEL PROYECTO ACTIVO
# ─────────────────────────────────────────────

p = PROYECTOS[proyecto_seleccionado]
nombre_corto = proyecto_seleccionado.split("(")[0].strip()

# ─────────────────────────────────────────────
# HEADER PRINCIPAL
# ─────────────────────────────────────────────

col_title, col_sync = st.columns([5, 1])

with col_title:
    st.markdown(f"""
    <div style="padding-top:0.5rem;">
        <div style="font-family:'JetBrains Mono',monospace; font-size:0.68rem; color:#d97706; 
                    text-transform:uppercase; letter-spacing:0.18em; margin-bottom:0.3rem;">
            Nexus Adaptive Change · Dashboard OCM
        </div>
        <h1 style="margin:0; font-size:1.7rem; font-weight:800; color:#f1f5f9;">{nombre_corto}</h1>
        <div style="font-family:'JetBrains Mono',monospace; font-size:0.72rem; color:#475569; margin-top:0.2rem;">
            Última actualización: {pd.Timestamp.now().strftime('%d %b %Y, %H:%M')} · Semana {pd.Timestamp.now().isocalendar()[1]}/52
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_sync:
    st.markdown("<br>", unsafe_allow_html=True)
    sync_btn = st.button("⚡ Sincronizar con n8n Engine", use_container_width=True)

if sync_btn:
    with st.status("🔄 Conectando con la API...", expanded=True) as status:
        st.write("Estableciendo handshake con n8n Engine...")
        time.sleep(0.9)
        st.write("Autenticando token de acceso...")
        time.sleep(0.7)
        st.write("Sincronizando flujos de trabajo activos...")
        time.sleep(0.8)
        st.write("✅ Pipeline actualizado correctamente.")
        status.update(label="✅ Sincronización completada", state="complete", expanded=False)

st.markdown("<hr style='border-color:#1e2d40; margin:1rem 0;'>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FILA 1 — KPIs
# ─────────────────────────────────────────────

st.markdown('<div class="section-label">◈ Indicadores Clave del Cambio</div>', unsafe_allow_html=True)

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

badge_html = f'<span class="badge-{p["saturacion_nivel"]}">{p["saturacion"]}</span>'

with kpi1:
    st.metric(
        label="Índice de Resistencia",
        value=f"{p['resistencia']}%",
        delta=f"{p['resistencia_delta']}% vs. semana anterior",
        delta_color="inverse",
    )

with kpi2:
    st.metric(
        label="Adopción Tecnológica",
        value=f"{p['adopcion']}%",
        delta=f"{p['adopcion_delta']:+d}% vs. semana anterior",
    )

with kpi3:
    st.metric(
        label="Stakeholders Activos",
        value="47",
        delta="+3 incorporados",
    )

with kpi4:
    st.metric(
        label="Acciones Pendientes",
        value="12",
        delta="-4 cerradas hoy",
        delta_color="inverse",
    )

# Badge de saturación separado para que sea visible
st.markdown(f"""
<div style="margin-top:0.5rem; font-family:'JetBrains Mono',monospace; font-size:0.72rem; color:#64748b;">
    Saturación del equipo: {badge_html} &nbsp;&nbsp;·&nbsp;&nbsp; 
    Área de mayor riesgo: <span style="color:#f59e0b; font-weight:600;">{p['area_riesgo']}</span>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FILA 2 — TENDENCIA + SENTIMIENTO
# ─────────────────────────────────────────────

col_trend, col_sent = st.columns([3, 2])

with col_trend:
    st.markdown('<div class="section-label">◈ Evolución del Índice de Riesgo — Últimas 4 semanas</div>', unsafe_allow_html=True)
    
    df_riesgo = generar_serie_riesgo(p["resistencia"])
    
    # Enriquecer con una segunda serie (benchmark)
    df_riesgo["Benchmark Industria"] = [max(10, min(90, 45 + np.random.randint(-5, 5))) for _ in range(len(df_riesgo))]
    
    st.line_chart(
        df_riesgo,
        height=280,
        use_container_width=True,
        color=["#d97706", "#334155"],
    )
    
    st.markdown(f"""
    <div style="display:flex; gap:1.5rem; margin-top:0.3rem; font-family:'JetBrains Mono',monospace; font-size:0.68rem; color:#64748b;">
        <span><span style="color:#d97706;">●</span> Proyecto actual</span>
        <span><span style="color:#334155;">●</span> Benchmark industria</span>
        <span style="margin-left:auto;">Variación 28d: <span style="color:{('#ef4444' if p['resistencia_delta'] > 0 else '#22c55e')}">
            {p['resistencia_delta']:+d}%</span></span>
    </div>
    """, unsafe_allow_html=True)

with col_sent:
    st.markdown('<div class="section-label">◈ Análisis de Sentimiento — Comentarios del equipo</div>', unsafe_allow_html=True)
    
    df_sent = generar_sentimiento()
    
    st.bar_chart(
        df_sent,
        height=280,
        use_container_width=True,
        color="#d97706",
    )
    
    total = df_sent["Comentarios"].sum()
    pos_pct = int(df_sent.loc["Positivo 👍", "Comentarios"] / total * 100)
    neg_pct = int(df_sent.loc["Negativo 👎", "Comentarios"] / total * 100)
    
    st.markdown(f"""
    <div style="font-family:'JetBrains Mono',monospace; font-size:0.68rem; color:#64748b; margin-top:0.3rem;">
        Total: {total} comentarios procesados por IA · 
        Sentimiento positivo: <span style="color:#22c55e;">{pos_pct}%</span> · 
        Negativo: <span style="color:#ef4444;">{neg_pct}%</span>
    </div>
    """, unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FILA 3 — HEATMAP DE ÁREAS + AI INSIGHTS
# ─────────────────────────────────────────────

col_heat, col_ai = st.columns([2, 3])

with col_heat:
    st.markdown('<div class="section-label">◈ Matriz de Riesgo por Área</div>', unsafe_allow_html=True)
    
    df_heat = generar_heatmap_areas()
    
    # Mostrar como tabla estilizada
    st.dataframe(
        df_heat.style
            .background_gradient(cmap="YlOrRd", vmin=0, vmax=100)
            .format("{:.0f}%"),
        use_container_width=True,
        height=240,
    )
    
    st.markdown("""
    <div style="font-family:'JetBrains Mono',monospace; font-size:0.65rem; color:#475569; margin-top:0.3rem;">
        Escala: 0% (bajo riesgo) → 100% (riesgo crítico)
    </div>
    """, unsafe_allow_html=True)

with col_ai:
    st.markdown('<div class="section-label">◈ IA Insights — Motor de Análisis Nexus</div>', unsafe_allow_html=True)
    
    # Insight principal
    st.info(f"""
**🧠 Diagnóstico Adaptativo — Proyecto: {nombre_corto}**

Se detecta **riesgo de cuello de botella en el área de {p['area_riesgo']}** por déficit de capacitación y baja densidad de patrocinadores activos en niveles de jefatura. {p['insight_extra']}

**Recomendación prioritaria:** Activar protocolo de intervención focalizada en las próximas 72 horas. Se sugiere una sesión de alineamiento con líderes clave y la revisión del plan de comunicación del cambio para el segmento afectado.

El modelo predictivo estima una probabilidad del **{35 + p['resistencia']}%** de que la resistencia escale si no se interviene antes del cierre del sprint actual.
    """)
    
    # Acciones sugeridas
    st.markdown('<div style="margin-top:1rem;" class="section-label">◈ Acciones sugeridas por IA</div>', unsafe_allow_html=True)
    
    acciones = [
        ("Alta", "Capacitación urgente módulo clave", p["area_riesgo"]),
        ("Media", "Refuerzo de comunicación del cambio", "Todas las áreas"),
        ("Alta", "Reunión de alineamiento con sponsors", "Dirección"),
        ("Baja", "Encuesta de pulso (15 min)", "Equipo operativo"),
    ]
    
    col_a1, col_a2 = st.columns(2)
    for i, (prioridad, accion, area) in enumerate(acciones):
        col = col_a1 if i % 2 == 0 else col_a2
        nivel = prioridad.lower()
        color_badge = {"alta": "#ef4444", "media": "#f59e0b", "baja": "#22c55e"}[nivel]
        with col:
            st.markdown(f"""
            <div style="background:#0f172a; border:1px solid #1e2d40; border-radius:8px; 
                        padding:0.7rem 0.9rem; margin-bottom:0.5rem;">
                <div style="display:flex; align-items:center; gap:0.4rem; margin-bottom:0.2rem;">
                    <span style="width:6px; height:6px; background:{color_badge}; 
                                border-radius:50%; display:inline-block; flex-shrink:0;"></span>
                    <span style="font-family:'JetBrains Mono',monospace; font-size:0.62rem; 
                                color:{color_badge}; text-transform:uppercase; letter-spacing:0.1em;">
                        {prioridad}
                    </span>
                </div>
                <div style="font-family:'Syne',sans-serif; font-size:0.78rem; color:#e2e8f0; font-weight:600;">
                    {accion}
                </div>
                <div style="font-family:'JetBrains Mono',monospace; font-size:0.65rem; color:#475569; margin-top:0.15rem;">
                    {area}
                </div>
            </div>
            """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────

st.markdown("""
<hr style="border-color:#1e2d40; margin:2rem 0 1rem 0;">
<div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:1rem;">
    <div style="font-family:'JetBrains Mono',monospace; font-size:0.65rem; color:#334155;">
        🚀 NEXUS ADAPTIVE CHANGE · Powered by Procesus / Isonauta · Motor IA activo
    </div>
    <div style="font-family:'JetBrains Mono',monospace; font-size:0.65rem; color:#334155;">
        Todos los datos son simulados para demostración · MVP v1.0.0
    </div>
</div>
""", unsafe_allow_html=True)
