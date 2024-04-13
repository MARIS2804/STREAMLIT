import streamlit as st 
import numpy as np
a=st.slider("1st operator",1,100)
b=st.slider("2nd operator",1,100)
c=st.selectbox("SELECT OPERATION",["+","-","*","/","%","^","sin","cos","tan"])
if c=="+":
    d=a+b
elif c=="-":
    d=a-b 
elif c=="*":
    d=a*b 
elif c=="/":
    d=a/b 
elif c=="%":
    d=a%b
elif c=="^":
    d= (int)(a) **(int)(b)
elif c=="sin":
    d=np.sin(a)
elif c=="cos":
    d=np.cos(a)
elif c=="tan":
    d=np.tan(a)
st.write("RESULT ",d)
    