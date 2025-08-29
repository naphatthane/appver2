import streamlit as st

# --- เปลี่ยนหัวข้อใหญ่ด้านบน ---
st.title("🏋️ โปรแกรมสุขภาพและฟิตเนสเฉพาะคุณ")

# --- Slider น้ำหนักและส่วนสูง ---
weight = st.slider("น้ำหนัก (kg)", 30, 200, 70, 1)
height = st.slider("ส่วนสูง (cm)", 100, 220, 170, 1)

# --- Slider รอบเอวและสะโพก (นิ้ว) ---
waist_in = st.slider("รอบเอว (นิ้ว)", 20, 60, 31, 1)
hip_in = st.slider("รอบสะโพก (นิ้ว)", 20, 60, 37, 1)

# --- แปลงนิ้วเป็นเซนติเมตร ---
waist_cm = waist_in * 2.54
hip_cm = hip_in * 2.54

# --- BMI + WHR ---
bmi = weight / ((height / 100) ** 2)
bmi = round(bmi, 1)
whr = waist_cm / hip_cm
whr = round(whr, 2)

# --- แสดงผลพร้อมสีโซนที่ปรับใหม่ ---
st.subheader("📌 วิเคราะห์ร่างกายเฉพาะคุณ")
if bmi < 18.5:
    st.markdown(f"<h3 style='color:#1E90FF'>BMI: {bmi} (น้ำหนักต่ำ)</h3>", unsafe_allow_html=True)
elif 18.5 <= bmi < 25:
    st.markdown(f"<h3 style='color:#32CD32'>BMI: {bmi} (น้ำหนักปกติ)</h3>", unsafe_allow_html=True)
else:
    st.markdown(f"<h3 style='color:#FF4500'>BMI: {bmi} (น้ำหนักเกิน)</h3>", unsafe_allow_html=True)

if whr < 0.85:
    st.markdown(f"<h3 style='color:#32CD32'>WHR: {whr} (สัดส่วนดี)</h3>", unsafe_allow_html=True)
else:
    st.markdown(f"<h3 style='color:#FF4500'>WHR: {whr} (ไขมันรอบเอวสูง)</h3>", unsafe_allow_html=True)

# --- ตารางออกกำลังกายและอาหารเหมือนเดิม ---
st.subheader("📆 ตารางออกกำลังกาย")
workout_plan = [
    "วันจันทร์: เดินเร็ว 30 นาที + เวทเบา 20 นาที",
    "วันอังคาร: HIIT 20 นาที + เวทเบา 20 นาที",
    "วันพุธ: ว่ายน้ำ 30 นาที",
    "วันพฤหัสบดี: เดินเร็ว 30 นาที + เวทเบา 15 นาที",
    "วันศุกร์: HIIT 20 นาที",
    "วันเสาร์: กีฬา/กิจกรรมกลางแจ้ง 40 นาที",
    "วันอาทิตย์: พักผ่อน/โยคะ 20-30 นาที"
]

st.subheader("🍽 คำแนะนำอาหาร")
meal_plan = [
    "อาหารเช้า: ข้าวโอ๊ต + นม + ผลไม้",
    "อาหารว่างเช้า: ถั่วหรือโยเกิร์ต",
    "อาหารกลางวัน: ข้าวกล้อง + ไก่/ปลา + ผักเยอะ",
    "อาหารว่างบ่าย: ผลไม้+โปรตีนเชค",
    "อาหารเย็น: ผัก + โปรตีน (ปลา/ไข่/ไก่)",
]
for day in workout_plan:
    st.write(f"- {day}")
for meal in meal_plan:
    st.write(f"- {meal}")