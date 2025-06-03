import streamlit as st
import bcrypt
import json

# Load user database dari file
def load_users():
    with open("users.json", "r") as f:
        return json.load(f)

# Verifikasi username dan password
def verify_user(username, password, users_db):
    if username in users_db:
        hashed_pw = users_db[username].encode('utf-8')
        return bcrypt.checkpw(password.encode('utf-8'), hashed_pw)
    return False

# Login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Fungsi logout
def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.success("Anda berhasil logout.")

# Jika sudah login
if st.session_state.logged_in:
    st.success(f"Halo, {st.session_state.username} 👋")
    if st.button("Logout"):
        logout()
    # Tambahkan aplikasi utama di bawah ini
    st.write("Ini adalah isi aplikasi setelah login.")
else:
    st.title("Login Page")
    users = load_users()

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")

    if login_button:
        if verify_user(username, password, users):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Selamat datang, {username}!")
        else:
            st.error("Username atau password salah.")
