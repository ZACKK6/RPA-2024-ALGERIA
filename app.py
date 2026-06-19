import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

# إعدادات الصفحة والواجهة
st.set_page_config(page_title="RPA 2024 Pro Max", page_icon="🏗️", layout="centered")

# --- قاموس اللغات المتكامل ---
lang_dict = {
    "العربية": {
        "title": "🏗️ نظام التحليل الزلزالي المتكامل - RPA 2024",
        "subtitle": "أداة احترافية لحساب القوة القصية القاعدية ورسم طيف الاستجابة وتصدير التقارير.",
        "sec1_title": "📊 معطيات المنشأ والموقع",
        "zone_label": "اختر المنطقة الزلزالية:",
        "groupe_label": "اختر مجموعة الاستخدام (Groupe):",
        "sys_label": "اختر نظام مقاومة القوى الأفقية (R):",
        "sec2_title": "🌱 خصائص التربة والأبعاد",
        "site_label": "اختر صنف التربة (Site):",
        "hn_label": "ارتفاع المبنى الإجمالي Hn (بالمتر m):",
        "d_label": "بُعد المبنى في اتجاه القوة D (بالمتر m):",
        "w_label": "الوزن الإجمالي للمبنى W (بالكيلو نيوتن kN):",
        "q_label": "معامل الجودة (Q):",
        "btn_calc": "🧮 إجراء التحليل الزلزالي ورسم المنحنى",
        "success_msg": "🎉 تم التحليل بنجاح وفق اشتراطات صياغة RPA 2024!",
        "m_t": "الفترة الزمنية للمبنى (T)",
        "m_d": "المعامل الديناميكي (D)",
        "m_v": "القوة القاعدية (V)",
        "chart_title": "📈 منحنى طيف الاستجابة وموقع منشأك عليه",
        "report_title": "📝 تقرير تفصيلي لخطوات التحليل:",
        "rep_a": "معامل التسارع المعتمد (A):",
        "rep_t": "فترات الطيف للصنف المحدد ($T_1$ / $T_2$):",
        "rep_r": "معامل السلوك الهيكلي (R):",
        "download_btn": "📥 تحميل بيانات التقرير كملف نصي الجاهز"
    },
    "Français": {
        "title": "🏗️ Système d'Analyse Sismique Expert - RPA 2024",
        "subtitle": "Calcul de l'effort tranchant, tracé du spectre de réponse et exportation des rapports.",
        "sec1_title": "📊 Données de la Structure et du Site",
        "zone_label": "Sélectionnez la zone sismique :",
        "groupe_label": "Sélectionnez le groupe d'usage :",
        "sys_label": "Système de contreventement (R) :",
        "sec2_title": "🌱 Caractéristiques du Sol et Dimensions",
        "site_label": "Catégorie du sol (Site) :",
        "hn_label": "Hauteur totale du bâtiment Hn (m) :",
        "d_label": "Dimension du bâtiment D (m) :",
        "w_label": "Poids total de la structure W (en kN) :",
        "q_label": "Facteur de qualité (Q) :",
        "btn_calc": "🧮 Calculer et Tracer le Spectre",
        "success_msg": "🎉 Analyse réussie selon les critères du RPA 2024 !",
        "m_t": "Période fondamentale (T)",
        "m_d": "Facteur d'amplification (D)",
        "m_v": "Effort tranchant (V)",
        "chart_title": "📈 Spectre de réponse et position de votre structure",
        "report_title": "📝 Rapport détaillé des étapes de calcul :",
        "rep_a": "Coefficient d'accélération (A) :",
        "rep_t": "Périodes caractéristiques ($T_1$ / $T_2$) :",
        "rep_r": "Coefficient de comportement (R) :",
        "download_btn": "📥 Télécharger le rapport textuel prêt"
    },
    "English": {
        "title": "🏗️ Advanced Seismic Analysis System - RPA 2024",
        "subtitle": "Calculate base shear, plot response spectrum, and export reports easily.",
        "sec1_title": "📊 Structure & Site Data",
        "zone_label": "Select Seismic Zone:",
        "groupe_label": "Select Usage Group:",
        "sys_label": "Structural System (R):",
        "sec2_title": "🌱 Soil Characteristics & Dimensions",
        "site_label": "Select Soil Category (Site):",
        "hn_label": "Total Building Height Hn (m):",
        "d_label": "Building Dimension D (m):",
        "w_label": "Total Building Weight W (kN):",
        "q_label": "Quality Factor (Q):",
        "btn_calc": "🧮 Run Analysis & Plot Spectrum",
        "success_msg": "🎉 Analysis successfully completed according to RPA 2024!",
        "m_t": "Building Period (T)",
        "m_d": "Dynamic Factor (D)",
        "m_v": "Base Shear Force (V)",
        "chart_title": "📈 Response Spectrum Curve & Your Structure Position",
        "report_title": "📝 Detailed Analysis Report:",
        "rep_a": "Acceleration Coefficient (A):",
        "rep_t": "Spectral Periods ($T_1$ / $T_2$):",
        "rep_r": "Behavior Coefficient (R):",
        "download_btn": "📥 Download Ready Report File"
    }
}

selected_lang = st.sidebar.selectbox("🌐 Language / اللغة / Langue", ["العربية", "Français", "English"])
text = lang_dict[selected_lang]

# اتجاه واجهة المستخدم بناءً على اللغة
if selected_lang == "العربية":
    st.markdown('<style>div.block-container{text-align: right;}</style>', unsafe_allow_html=True)
else:
    st.markdown('<style>div.block-container{text-align: left;}</style>', unsafe_allow_html=True)

st.title(text["title"])
st.write(text["subtitle"])
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader(text["sec1_title"])
    a_options_2024 = {
        "Zone 0" if selected_lang != "العربية" else "Zone 0 (نشاط مهمل)": 0.0,
        "Zone I" if selected_lang != "العربية" else "Zone I (نشاط ضئيل)": 0.10,
        "Zone IIa" if selected_lang != "العربية" else "Zone IIa (نشاط متوسط)": 0.15,
        "Zone IIb" if selected_lang != "العربية" else "Zone IIb (نشاط متوسط مرتفع)": 0.25,
        "Zone III" if selected_lang != "العربية" else "Zone III (نشاط قوي)": 0.35
    }
    selected_zone = st.selectbox(text["zone_label"], list(a_options_2024.keys()))
    A_base = a_options_2024[selected_zone]
    
    groupe_options = {
        "Groupe 1A": 1.30, "Groupe 1B": 1.15, "Groupe 2": 1.00, "Groupe 3": 0.85
    }
    selected_groupe = st.selectbox(text["groupe_label"], list(groupe_options.keys()))
    A = A_base * groupe_options[selected_groupe]
    
    r_options_2024 = {
        "Portiques auto-stables (R=5)": 5.0,
        "Voiles porteurs (R=4)": 4.0,
        "Système mixte (R=5.5)": 5.5,
        "Charpente métallique (R=6)": 6.0
    }
    selected_r = st.selectbox(text["sys_label"], list(r_options_2024.keys()))
    R = r_options_2024[selected_r]

with col2:
    st.subheader(text["sec2_title"])
    site_options = {
        "S1: Rocheux / تربة صخرية صلبة": (0.15, 0.40),
        "S2: Ferme / تربة ثابتة ومتماسكة": (0.15, 0.50),
        "S3: Meuble / تربة مفككة أو متوسطة": (0.20, 0.60),
        "S4: Très meuble / تربة ضعيفة جداً": (0.25, 0.80)
    }
    selected_site = st.selectbox(text["site_label"], list(site_options.keys()))
    T1, T2 = site_options[selected_site]
    
    H_n = st.number_input(text["hn_label"], min_value=0.0, value=12.0, step=1.0)
    D_dimension = st.number_input(text["d_label"], min_value=1.0, value=15.0, step=1.0)
    W = st.number_input(text["w_label"], min_value=0.0, value=1500.0, step=50.0)
    Q = st.slider(text["q_label"], min_value=1.0, max_value=1.6, value=1.2, step=0.05)

st.markdown("---")

# الحسابات الهندسية الخلفية
C_t = 0.05 if "Voiles" in selected_r else 0.075 
T = C_t * (H_n ** 0.75)
T_final = min(T, 0.09 * H_n / math.sqrt(D_dimension))

# تحديد دالة حساب D لرسم المنحنى بالكامل بكافة نقاطه الزمنية
def calculate_d(t_val, t1, t2):
    if 0 <= t_val <= t1:
        return 1.0 + (1.5 * (t_val / t1))
    elif t1 <= t_val <= t2:
        return 2.5
    elif t2 <= t_val <= 3.0:
        return 2.5 * (t2 / t_val)
    else:
        return 2.5 * (t2 / 3.0) * (3.0 / t_val)**2

D = calculate_d(T_final, T1, T2)
V = (A * D * Q / R) * W

if st.button(text["btn_calc"], type="primary"):
    st.success(text["success_msg"])
    
    col_r1, col_r2, col_r3 = st.columns(3)
    col_r1.metric(label=text["m_t"], value=f"{T_final:.3f} s")
    col_r2.metric(label=text["m_d"], value=f"{D:.3f}")
    col_r3.metric(label=text["m_v"], value=f"{V:.2f} kN")
    
    st.markdown("---")
    st.subheader(text["chart_title"])
    
    # توليد ورسم منحنى طيف الاستجابة الفعلي لـ RPA 2024
    t_periods = np.linspace(0.0, 4.0, 500)
    d_values = [calculate_d(t, T1, T2) for t in t_periods]
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(t_periods, d_values, label="Spectre RPA 2024", color="#FF4B4B", linewidth=2.5)
    ax.scatter(T_final, D, color="blue", s=120, zorder=5, label=f"Votre Structure (T={T_final:.3f}s, D={D:.1f})")
    
    ax.set_xlabel("Période T (seconds)" if selected_lang != "العربية" else "الفترة الزمنية T (بالثواني)")
    ax.set_ylabel("Facteur d'amplification D" if selected_lang != "العربية" else "معامل التضخيم الديناميكي D")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend()
    st.pyplot(fig)
    
    st.markdown("---")
    
    # توليد نص التقرير الاحترافي الجاهز للتنزيل الباشر
    report_text = f"""==================================================
RAPPORT D'ANALYSE SISMIQUE - RPA 2024
==================================================
- Zone Sismique Sélectionnée: {selected_zone}
- Coefficient d'accélération de base (A): {A:.3f}
- Catégorie de Sol (Site): {selected_site} (T1={T1}s, T2={T2}s)
- Coefficient de comportement (R): {R}
- Facteur de qualité (Q): {Q}
--------------------------------------------------
RÉSULTATS DE CALCUL:
--------------------------------------------------
- Période fondamentale du bâtiment (T): {T_final:.3f} s
- Facteur d'amplification dynamique (D): {D:.3f}
- Poids total de la structure (W): {W:.2f} kN
- EFFORT TRANCHANT A LA BASE (V): {V:.2f} kN

Formule finale: V = (A * D * Q / R) * W
Généré automatiquement par l'outil Intelligent RPA 2024.
=================================================="""
    
    st.subheader(text["report_title"])
    st.code(report_text, language="text")
    
    # زر التنزيل السحري للملف المكتوب
    st.download_button(
        label=text["download_btn"],
        data=report_text,
        file_name=f"Rapport_RPA_2024_{T_final:.2f}s.txt",
        mime="text/plain"
    )