import streamlit as st

st.set_page_config(page_title="AI Mammogram Analysis", page_icon="🎗️", layout="centered")

st.markdown("""
<style>

.stApp {
    background-color: #FDF8FB;
}

/* إخفاء label الافتراضي لأداة الرفع */
div[data-testid="stFileUploader"] label {
    display: none !important;
}

/* تصغير وتنظيم صندوق الرفع */
div[data-testid="stFileUploader"] {
    background-color: #FCE4EC !important;
    border: 2px solid #E91E8C !important;
    border-radius: 16px !important;
    padding: 25px 20px !important;
    text-align: center !important;
    max-width: 320px !important;
    margin: 0 auto !important;
}

div[data-testid="stFileUploader"] section {
    background-color: transparent !important;
    border: none !important;
}

div[data-testid="stFileUploader"] span {
    color: #880E4F !important;
    font-size: 13px !important;
}

div[data-testid="stFileUploader"] button {
    background-color: #E91E8C !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: bold !important;
    font-size: 13px !important;
    padding: 6px 18px !important;
}

div[data-testid="stFileUploader"] button:hover {
    background-color: #AD1457 !important;
    color: #FFFFFF !important;
}

/* أزرار Back و Next */
div.stButton > button {
    background-color: #E91E8C !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px !important;
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

/* العنوان الخارجي فوق الصندوق */
.upload-title {
    color: #C2185B;
    font-size: 22px;
    font-weight: bold;
    font-family: 'Arial', sans-serif;
    text-align: center;
    margin-bottom: 12px;
}

</style>
""", unsafe_allow_html=True)

st.write("<br><br>", unsafe_allow_html=True)

# ✅ العنوان خارج المربع
st.markdown("<div class='upload-title'>UPLOAD DICOM</div>", unsafe_allow_html=True)

# ✅ صندوق الرفع مصغر ومرتب
uploaded_file = st.file_uploader(
    "",
    type=["dcm"],
    accept_multiple_files=False
)

if uploaded_file is not None:
    st.success(f"✅ تم رفع الملف بنجاح: {uploaded_file.name}")

st.write("<br>", unsafe_allow_html=True)

col_back, col_space, col_next = st.columns([3, 1, 3])

with col_back:
    if st.button("« Back"):
        st.info("الرجوع للواجهة الثانية...")

with col_next:
    if st.button("Next »"):
        st.info("الانتقال للواجهة الرابعة...")
