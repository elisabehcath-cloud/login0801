import streamlit as st

# 設定頁面標題
st.set_page_config(page_title="登入系統", page_icon="🔒")

# 初始化 session_state 用來紀錄登入狀態（修正：使用 st.session_state）
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 設定預設密碼 (可自行修改)
PASSWORD = "APP_PASSWORD"

## ---------------- 登入介面 ----------------
if not st.session_state.logged_in:
    st.title("🔑 請先登入")
    
    # 密碼輸入框 (type="password" 會隱藏輸入字元)
    password_input = st.text_input("請輸入密碼：", type="password")
    
    if st.button("登入"):
        if password_input == PASSWORD:
            st.session_state.logged_in = True
            st.rerun()  # 重新整理頁面以顯示登入後內容
        else:
            st.error("❌ 密碼錯誤，請再試一次！")

## ---------------- 登入成功介面 ----------------
else:
    st.title("🎉 登入成功！")
    st.subheader("歡迎來到你的專屬空間")
    
    st.divider()
    
    # 顯示詩作
    st.markdown("""
    ### 📜 《春曉》
    > **孟浩然**
    > 
    > 春眠不覺曉，處處聞啼鳥。  
    > 夜來風雨聲，花落知多少。
    """)
    
    st.divider()
    
    # 登出按鈕
    if st.button("登出"):
        st.session_state.logged_in = False
        st.rerun()
