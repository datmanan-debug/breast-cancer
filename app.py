import streamlit as st
import os

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="AI Mammogram Analysis", layout="centered")

# --- إضافة تنسيقات CSS لتخصيص الألوان والأشكال لتطابق التصميم ---
st.markdown("""
    <style>
    /* 1. تخصيص حاوية رفع الملفات (المستطيل الوردي الكبير) */
    div[data-testid="stFileUploader"] {
        background-color: #F6D6EC !important; /* اللون الوردي الفاتح بالخلفية */
        border: 2px solid #A24B88 !important; /* الإطار الوردي الغامق */
        border-radius: 25px !important;
        padding: 40px 20px !important;
        text-align: center !important;
    }
    
    /* 2. تعديل نصوص وعنوان صندوق الرفع */
    div[data-testid="stFileUploader"] label {
        color: #4A154B !important;
        font-size: 24px !important;
        font-weight: bold !important;
        font-family: 'Arial', sans-serif !important;
        margin-bottom: 15px !important;
    }
    
    /* إلغاء حواف التنسيق الافتراضي لـ streamlit داخل الصندوق */
    div[data-testid="stFileUploader"] section {
        background-color: transparent !important;
        border: none !important;
    }

    /* تنسيق اسم الصورة بالأسفل */
    .image-caption {
        font-size: 20px !important;
        font-weight: bold !important;
        color: black !important;
        margin-top: 5px;
    }

    /* 3. تخصيص أزرار التحكم (Next) لتشبه التصميم */
    div.stButton > button {
        background-color: #F6D6EC !important;
        color: black !important;
        border: 2px solid #A24B88 !important;
        border-radius: 12px !important;
        padding: 8px 35px !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }
    
    /* تأثير عند تمرير الماوس فوق الزر */
    div.stButton > button:hover {
        background-color: #A24B88 !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- محتوى الواجهة الثالثة ---

# مسافة علوية لضبط موقع الصندوق في المنتصف
st.write("<br><br><br>", unsafe_allow_html=True)

# استخدام الـ container لتجميع عناصر صندوق الرفع والصورة الثابتة بداخله
with st.container():
    # أداة رفع الملفات مخصصة لملفات الأشعة الطبية DICOM
    uploaded_file = st.file_uploader(
        "UPLOAD IMAGE\n(DICOM)", 
        type=["dcm"], 
        accept_multiple_files=False
    )
    
    # هنا نقوم بعرض الصورة m.jpg كجزء مدمج أسفل نص الرفع إذا كانت موجودة في الفولدر
    image_path = "m.jpg"
    if os.path.exists(image_path):
        # عرض الصورة بعرض مناسب (مثلاً 120 بكسل) وتوسيطها
        st.image(image_path, width=120)
        st.markdown('<p class="image-caption">m</p>', unsafe_allow_html=True)

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