import streamlit as st

st.set_page_config(page_title="AI Mammogram Analysis", page_icon="🎗️", layout="centered")

st.markdown("""
<style>

.stApp {
    background-color: #FDF8FB;
}

div[data-testid="stFileUploader"] {
    background-color: #FCE4EC !important;
    border: 2px solid #E91E8C !important;
    border-radius: 25px !important;
    padding: 60px 20px !important;
    text-align: center !important;
}

div[data-testid="stFileUploader"] label {
    color: #C2185B !important;
    font-size: 24px !important;
    font-weight: bold !important;
    font-family: 'Arial', sans-serif !important;
    margin-bottom: 20px !important;
    display: block !important;
}

div[data-testid="stFileUploader"] section {
    background-color: transparent !important;
    border: none !important;
}

div[data-testid="stFileUploader"] span {
    color: #880E4F !important;
}

div[data-testid="stFileUploader"] button {
    background-color: #E91E8C !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: bold !important;
}

div[data-testid="stFileUploader"] button:hover {
    background-color: #AD1457 !important;
    color: #FFFFFF !important;
}

/* ✅ أزرار Back و Next: وردي طوخ + حواف مربعة */
div.stButton > button {
    background-color: #E91E8C !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px !important;        /* حواف مربعة شوي */
    padding: 10px 10px !important;
    font-size: 17px !important;
    font-weight: bold !important;
    white-space: nowrap !important;
    width: 100% !important;
}

div.stButton > button:hover {
    background-color: #AD1457 !important;
    color: #FFFFFF !important;
}

div[data-testid="stAlert"] {
    background-color: #FCE4EC !important;
    border-left: 4px solid #E91E8C !important;
    color: #880E4F !important;
    border-radius: 10px !important;
}

</style>
""", unsafe_allow_html=True)

st.write("<br><br><br>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "UPLOAD IMAGE\n(DICOM)",
    type=["dcm"],
    accept_multiple_files=False
)

if uploaded_file is not None:
    st.success(f"✅ تم رفع ملف الأشعة بنجاح: {uploaded_file.name}")

st.write("<br>", unsafe_allow_html=True)

# ✅ تقريب الأزرار من بعض بتقليل المسافة بينهم
col_back, col_space, col_next = st.columns([3, 1, 3])

with col_back:
    if st.button("« Back"):
        st.info("الرجوع للواجهة الثانية...")

with col_next:
    if st.button("Next »"):
        st.info("الانتقال للواجهة الرابعة...")
