import os
import streamlit as st
from dotenv import load_dotenv

# 讀取 .env 檔案內容
load_dotenv()

# 從環境變數中取得密碼，如果找不到則給予預設值
PASSWORD = os.getenv("APP_PASSWORD", "defaultpassword")

st.set_page_config(page_title="登入系統", page_icon="🔒")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

## ---------------- 登入介面 ----------------
if not st.session_state.logged_in:
    st.title("🔑 請先登入")
    
    password_input = st.text_input("請輸入密碼：", type="password")
    
    if st.button("登入"):
        if password_input == PASSWORD:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("❌ 密碼錯誤，請再試一次！")

## ---------------- 登入成功介面 ----------------
else:
    st.title("🎉 登入成功！")
    st.subheader("歡迎來到你的專屬空間")
    
    st.divider()
    
    st.markdown("""
    ### 📜 《春曉》
    > **孟浩然**
    > 
    > 春眠不覺曉，處處聞啼鳥。  
    > 夜來風雨聲，花落知多少。
    """)
    
    st.divider()
    
    if st.button("登出"):
        st.session_state.logged_in = False
        st.rerun()
