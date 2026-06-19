import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

# Configuration de la page
st.set_page_config(page_title="RPA 2024 Pro Max", page_icon="🏗️", layout="centered")

# --- 1. Menu de Navigation Latéral ---
st.sidebar.title("🛠️ Menu / القائمة الهندسية")
page = st.sidebar.radio("Choisir l'outil / اختر الأداة:", [
    "1. Effort Tranchant à la Base (V)", 
    "2. Distribution des Forces (Fi)", 
    "3. Vérification des Déplacements (P-Delta)"
])

# --- 2. PAGE 1: CALCUL DE L'EFFORT TRANCHANT (V) ---
if page == "1. Effort Tranchant à la Base (V)":

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

    selected_lang = st.sidebar.selectbox("🌐 Language / اللغة / Langue", ["Français", "العربية", "English"])
    text = lang_dict[selected_lang]

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

    C_t = 0.05 if "Voiles" in selected_r else 0.075 
    T = C_t * (H_n ** 0.75)
    T_final = min(T, 0.09 * H_n / math.sqrt(D_dimension))

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

# --- 3. PAGE 2: DISTRIBUTION DES FORCES PAR ÉTAGE (Fi) ---
elif page == "2. Distribution des Forces (Fi)":
    st.title("📊 Distribution de l'Effort Sismique Relatif (Fi)")
    st.write("Calculez la répartition de la force sismique globale sur la hauteur du bâtiment selon les critères du RPA 2024.")
    
    st.markdown("---")
    
    col_v1, col_v2 = st.columns(2)
    with col_v1:
        V_input = st.number_input("Entrez l'effort tranchant global V (kN) :", min_value=0.0, value=122.73)
    with col_v2:
        nb_etages = st.number_input("Nombre total d'étages :", min_value=1, max_value=20, value=3, step=1)
    
    st.markdown("### 🏢 Caractéristiques des Niveaux (Du bas vers le haut) :")
    
    weights = []
    heights = []
    cumulative_height = 0.0
    
    for i in range(int(nb_etages)):
        st.markdown(f"*Niveau {i+1}*")
        c1, c2 = st.columns(2)
        with c1:
            w_i = st.number_input(f"Poids du niveau {i+1} - Wi (kN) :", min_value=1.0, value=500.0, key=f"w_{i}")
        with c2:
            h_i = st.number_input(f"Hauteur de cet étage hi (m) :", min_value=1.0, value=3.0, key=f"h_{i}")
        
        weights.append(w_i)
        cumulative_height += h_i
        heights.append(cumulative_height)
        
    st.markdown("---")
    
    if st.button("🧮 Calculer la Répartition Horizontale (Fi)", type="primary"):
        total_wh = sum(w * h for w, h in zip(weights, heights))
        f_forces = []
        
        for i in range(int(nb_etages)):
            fi = (V_input * weights[i] * heights[i]) / total_wh
            f_forces.append(fi)
            
        st.success("🎉 Les forces horizontales par niveau ont été calculées avec succès !")
        
        st.markdown("### 📋 Tableau des forces appliquées à chaque niveau :")
        for i in range(int(nb_etages)):
            st.metric(label=f"Force latérale au Niveau {i+1} (F{i+1})", value=f"{f_forces[i]:.2f} kN")
            
        st.markdown("---")
        st.markdown("### 📉 Diagramme de distribution des charges horizontales (F) :")
        
        fig_f, ax_f = plt.subplots(figsize=(6, 4))
        plot_heights = [0] + heights
        plot_forces = [0] + f_forces
        
        ax_f.plot(plot_forces, plot_heights, marker='o', color='#00a896', linewidth=2.5, label="Force Fi (kN)")
        ax_f.set_ylabel("Hauteur cumulée du bâtiment (m)")
        ax_f.set_xlabel("Effort horizontal appliqué (kN)")
        ax_f.grid(True, linestyle="--", alpha=0.5)
        ax_f.legend()
        st.pyplot(fig_f)

# --- 4. PAGE 3: VÉRIFICATION P-DELTA ---
elif page == "3. Vérification des Déplacements (P-Delta)":
    st.title("📉 Validation de l'Effet P-Delta (RPA 2024)")
    st.write("Vérifiez l'indice de stabilité (θ) de chaque niveau pour valider la sécurité du second ordre.")
    
    st.markdown("---")
    
    nb_niveaux = st.number_input("Nombre de niveaux à vérifier :", min_value=1, max_value=20, value=3, step=1)
    
    st.markdown("### 📥 Entrez les données mécaniques de chaque niveau :")
    
    list_theta = []
    
    for i in range(int(nb_niveaux)):
        st.markdown(f"*Niveau {i+1}*")
        col_p1, col_p2, col_p3, col_p4 = st.columns(4)
        
        with col_p1:
            pk = st.number_input(f"Poids cumulé Pk (kN) :", min_value=1.0, value=1500.0 - (i*500), key=f"pk_{i}")
        with col_p2:
            dr = st.number_input(f"Déplacement rel. Δk (m) :", min_value=0.001, max_value=0.5, value=0.015, format="%.4f", key=f"dr_{i}")
        with col_p3:
            vk = st.number_input(f"Effort Tranchant Vk (kN) :", min_value=1.0, value=122.73 / (i+1), key=f"vk_{i}")
        with col_p4:
            hk = st.number_input(f"Hauteur Étage hk (m) :", min_value=1.0, value=3.0, key=f"hk_{i}")
            
        # Formule de l'indice de stabilité (RPA 2024)
        theta_k = (pk * dr) / (vk * hk)
        list_theta.append(theta_k)

    st.markdown("---")
    
    if st.button("🔍 Lancer la Vérification de Stabilité", type="primary"):
        st.markdown("### 📊 Résultats de l'analyse P-Delta :")
        
        tout_conforme = True
        
        for i in range(int(nb_niveaux)):
            tk = list_theta[i]
            st.write(f"*Niveau {i+1} :*")
            
            if tk < 0.10:
                st.success(f"✅ Conforme | θ = {tk:.4f} < 0.10 (Effet P-Delta négligeable)")
            elif 0.10 <= tk <= 0.20:
                st.warning(f"⚠️ Attention | θ = {tk:.4f} [0.10 - 0.20] (Amplification requise de {1/(1-tk):.2f})")
            else:
                st.error(f"❌ NON CONFORME | θ = {tk:.4f} > 0.20 (Structure Instable, Augmenter la rigidité !)")
                tout_conforme = False
        
        st.markdown("---")
        if tout_conforme:
            st.balloons()
            st.success("🏆 Félicitations ! La structure globale respecte parfaitement les exigences de sécurité du RPA 2024.")
        else:
            st.error("🚨 Recommandation : Veuillez réviser le système de contreventement (ajouter des voiles ou augmenter les sections)เพื่อ réduire les déplacements.")
