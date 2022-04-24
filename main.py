# Hopefully I rmbr how python works
import streamlit as st
import pandas as pd

st.title('Companion App Metrics Prototype')
st.markdown("ME 533 - EPE Group 8")
#st.subheader("Mihir Nadig, Meryl Suresh, Nicholas Robinson, Chris Jurkiewics")
st.markdown("")
st.subheader("Metrics")
col1, col2, col3, = st.columns(3)
with col1:
    st.metric(label="Percentage Correct", value="70 %", delta="5 %")
with col2:
    st.metric(label="Elapsed Time", value="12 m", delta="-1 m")
with col3:
    st.metric(label="Accuracy", value="90 %", delta="7 %")

data = [["User1","Auscultation", "Fail", 5],["User1","Auscultation", "Pass", 8],["User1","Auscultation", "Pass", 9]]
data2 = [["User1","Suture", "Fail", 6.0],["User1","Suture", "Fail", 7.2],["User1","Suture", "Pass", 14.3]]
df1 = pd.DataFrame(data, columns = ['User', 'Procedure/Module', "Pass/Fail", "0-10 Score"])
df2 = pd.DataFrame(data, columns = ['User', 'Procedure/Module', "Pass/Fail", "Tensile Strength"])

st.subheader("Suturing Analytics")
st.table(df2)

st.subheader("Auscultation Analytics")
st.table(df1)

