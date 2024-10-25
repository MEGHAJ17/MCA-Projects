
import streamlit as st
import numpy as np
from PIL import Image
import pickle as pk
import tensorflow as tf
from keras.models import Sequential
from keras.models import load_model
import cv2

 
def predict_catagory(test_model, data):
    import os 
    os.chdir('/content/drive/My Drive/Projects/untitled')
    from dump import Test

    output = Test.Predict(data)  
    
    return output

def mapping_data(val):
    if (val.lower() == 'yes') or (val.lower() == 'male') :
        return 1
    elif (val.lower() == 'no') or (val.lower() == 'female'):
        return 0
    else:
        return 0
                
def main():
    st.set_page_config(layout="wide")
    test_model = r'/content/drive/My Drive/Projects/untitled/Model_file.pkl'
    
    #models = [classifier_logistic, classifier_naive, classifier_rf]    
    
    st.title('''
             My Pocket Tracker
             ''')
    
    st.text('''
            We looked at easy to build open-source techniques leveraging AI 
            which can give us state-of-the-art accuracy in detecting the Novel 
            COVID-19 virus thus enabling AI for social good.

            ''')  
    
    try:
        fever = st.radio('Do You Feel Any Fever ? ',('Yes','No'))
        tiredness = st.radio('Do You Feel Any Tiredness ? ',('Yes','No'))
        dry_cough = st.radio('Do You Feel Any Dry Cough ? ',('Yes','No'))
        breathing = st.radio('Do You Feel Any Difficulty-in-Breathing ? ',('Yes','No'))
        throat = st.radio('Do You Feel Any Sore-Throat ? ',('Yes','No'))
        nasal = st.radio('Is there Nasal-Congestion ? ',('Yes','No'))
        nose = st.radio('Do You Feel Runny Nose ? ',('Yes','No'))
        diarrhea = st.radio('Any Diarrhea related issue ? ',('Yes','No'))
        gender = st.radio('Male or Female ? ',('Male','Female','Others'))
        contact = st.radio('Any Contact with any Covid +ve patient ? ',('Yes','No','Dont Know'))
        age = st.text_input('Your Age : ')
            
        data = [fever, tiredness, dry_cough, breathing, throat, nasal, nose, diarrhea, gender, contact, age]
        data = list(map(mapping_data,data))

        if st.button('Make a Test'):
            output = predict_catagory(test_model, data)
            st.success("<br>The Output Label is &nbsp : &nbsp {} :sunglasses:".format(output))

            st.write('Recommendations')
            
        
    
    except AttributeError:
        pass

if __name__=='__main__':
    main()