import pandas as pd
import gradio as gr
import streamlit as st
from pickle import load
from sklearn.preprocessing import StandardScaler

def Admission_Prediction(n1, n2, n3, n4,  n5, n6, n7):
    loaded_scaler = load(open('./model/scaler.pkl', 'rb'))
    loaded_model  = load(open('./model/Admission_Predict_SGDC_model.pkl', 'rb'))
    Research_bin = 1 if n7 == "Yes" else 0

    columns = ['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA', 'Research']
    lst = [[n1, n2, n3, n4, n5, n6, Research_bin]]
    df_input = pd.DataFrame(lst, columns=columns)

    list_scaled = loaded_scaler.transform(df_input)
    pred = loaded_model.predict(list_scaled)
    return 'student will be admitted' if pred[0] == 1 else 'student will not be admitted'

def deploy_gradio():
    In = gr.Interface( fn=Admission_Prediction,
                       inputs=[ gr.Slider(minimum=260,  maximum=340,  step=1,   label='GRE Score'),
                                gr.Slider(minimum=0,    maximum=120,  step=1,   label='TOEFL Score'),
                                gr.Slider(minimum=0,    maximum=5,    step=1,   label='University Rating'),
                                gr.Slider(minimum=0.0,  maximum=5.0,  step=0.5, label='SOP'),
                                gr.Slider(minimum=0.0,  maximum=5.0,  step=0.5, label='LOR'),
                                gr.Slider(minimum=0.0,  maximum=10.0, step=0.1, label='CGPA'),
                                gr.Dropdown(choices=['Yes', 'No'], label='Research')
                        ],
                       outputs=gr.Textbox(label="result") )
    In.launch()

def deploy_streamlit():
    st.markdown("""
        <div style="background-color:yellow;padding:13px"> 
            <h1 style="color:black;text-align:center;">Streamlit Admission Prediction ML App</h1> 
        </div>
    """, unsafe_allow_html=True)

    GRE        = st.slider('GRE Score',         min_value=260, max_value=340,  step=1)
    TOEFL      = st.slider('TOEFL Score',       min_value=0,   max_value=120,  step=1)
    UnivRating = st.slider("University Rating", min_value=0,   max_value=5,    step=1)
    SOP        = st.slider("SOP",               min_value=0.0, max_value=5.0,  step=0.5)
    LOR        = st.slider("LOR",               min_value=0.0, max_value=5.0,  step=0.5)
    CGPA       = st.slider("CGPA",              min_value=0.0, max_value=10.0, step=0.1)
    Research   = st.selectbox('Research',       ("Yes", "No"))

    if st.button("Predict"):
        result = Admission_Prediction(GRE, TOEFL, UnivRating, SOP, LOR, CGPA, Research)
        st.success(result)
