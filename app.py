import streamlit as st
import pickle
import numpy as np

final_model = pickle.load(open('saved_model.pkl', 'rb'))
selected_attributes = ['V4', 'V7', 'V8', 'V10', 'V12', 'V14', 'V16', 'V17', 'V18', 'V20', 'V21', 'V23', 'V24', 'V26', 'V27', 'Hour']
scaler = None # pickle your standard scaler and reload it here

def predict(inputs):
    arr = np.array([inputs])
    arr = arr.astype(float)
    scaled_arr = scaler.transform(arr)
    output = final_model.predict(scaled_arr)
    return output

def main():
    st.title('GAN Model Deployment')
    inputs = []
    for attr in selected_attributes:
        inputs.append(st.text_input(attr, value="0"))

    button = st.button("Predict")

    if button:
        output = predict(inputs)
        if output == 1:
            st.error('The transaction is {}'.format(output))
        elif output == 0:
            st.success('The transaction is {}'.format(output))

    

if __name__ == "__main__":
    main()