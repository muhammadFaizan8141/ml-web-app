import joblib
import streamlit as st

st.header("jhfafhl  fhffhl fsgfoaya fh ahqo ")
st.text("pata nai kya likhna heh")


def main():
    html_temp="""
    <div style="background-color:lightblue;padding:18px">
    <h2 style="color:black";text-align:center> Health insurance cost prediction using ml </h2>  
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    model=joblib.load("model_joblib_gr")
    p1=st.slider("Enter your age",18,100)
    s1=st.selectbox("Sex" , ("male","female"))

    if s1=="female":
          p2=0
    else:
          p2=0
    p3=st.number_input("enter your bmi value")

    p4=st.selectbox("enter number of childern",(0,1,2,3,4))

    s2=st.selectbox("smoker",("yes","no"))

    if s2=="yes":
          p5=1
    else:
          p5=0
    p6=st.selectbox("enter your region",(1,2,3,4))

    if st.button("predict"):
            #result=
            st.success(f"your insurance cost is {model.predict([[p1,p2,p3,p4,p5,p6]])}")
            







if __name__=="__main__":
        main()
