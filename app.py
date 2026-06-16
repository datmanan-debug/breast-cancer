import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="AI Mammogram Analysis", layout="centered")

# --- إضافة تنسيقات CSS لتخصيص الألوان الوردية المطابقة لواجهاتك ---
st.markdown("""
    <style>
    /* 1. تخصيص حاوية رفع الملفات (المستطيل الوردي المريح) */
    div[data-testid="stFileUploader"] {
        background-color: #FCE4EC !important; /* وردي فاتح ناعم جداً مطابق لخلفياتك */
        border: 2px solid #E91E63 !important; /* إطار وردي حيوي وواضح */
        border-radius: 25px !important;
        padding: 60px 20px !important;
        text-align: center !important;
    }
    
    /* 2. تعديل نصوص وعنوان صندوق الرفع */
    div[data-testid="stFileUploader"] label {
        color: #C2185B !important; /* نص وردي غامق متناسق */
        font-size: 24px !important;
        font-weight: bold !important;
        font-family: 'Arial', sans-serif !important;
        margin-bottom: 20px !important;
        display: block !important;
    }
    
    /* إلغاء حواف التنسيق الافتراضي لـ streamlit داخل الصندوق */
    div[data-testid="stFileUploader"] section {
        background-color: transparent !important;
        border: none !important;
    }

    /* تعديل لون نص حجم الملف الافتراضي ليكون واضحاً */
    div[data-testid="stFileUploader"] span {
        color: #880E4F !important;
    }

    /* 3. تخصيص أزرار التحكم (Next) باللون الوردي المتناسق */
    div.stButton > button {
        background-color: #FCE4EC !important;
        color: #C2185B !important;
        border: 2px solid #E91E63 !important;
        border-radius: 12px !important;
        padding: 8px 35px !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }
    
    /* تأثير عند تمرير الماوس فوق الزر (ينعكس اللون) */
    div.stButton > button:hover {
        background-color: #E91E63 !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- محتوى الواجهة الثالثة ---

# مسافة علوية لضبط موقع الصندوق في المنتصف
st.write("<br><br><br>", unsafe_allow_html=True)

# أداة رفع الملفات مخصصة لملفات الأشعة الطبية DICOM
uploaded_file = st.file_uploader(
    "UPLOAD IMAGE\n(DICOM)", 
    type=["dcm"], 
    accept_multiple_files=False
)

# عرض رسالة تأكيد عند رفع ملف جديد بنجاح
if uploaded_file is not None:
    st.success(f"📂 تم رفع ملف الأشعة بنجاح: {uploaded_file.name}")

# مسافة قبل زر التالي
st.write("<br><br>", unsafe_allow_html=True)

# --- زر الانتقال (Next) في أسفل اليمين ---
col1, col2 = st.columns([6, 1])
with col2:
    if st.button("Next"):
        st.info("سيتم الانتقال للواجهة الرابعة...")
