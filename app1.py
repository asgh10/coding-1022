import streamlit as st

'''
if st.button("on"):
    st.success("활성화")
elif st.button("off"):
    st.error("비활성화")
'''

is_active = st.toggle("상태 전환")

if is_active:
    st.success("활성화")
else:
    st.error("비활성화")


'''
import streamlit as st

status = st.pills("상태 선택", ["on", "off"], default="off")

if status == "on":
    st.success("활성화")
else:
    st.error("비활성화")
'''
