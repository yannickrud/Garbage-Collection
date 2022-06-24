import streamlit as st
import os
import pandas as pd
from PIL import Image
import tensorflow as tf
from PIL.Image import Resampling
import numpy as np
import pathlib

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)




dir = './dataSources/'
data_dir = pathlib.Path(os.path.join(dir, './Garbage classification/Garbage classification/'))

st.title('Garbage-Classification ML4B')


with st.expander("Team Presentation"):
    "Hi, we are Yannick Rudolf, Nico Schunk and Christoph Lehr. We are creating this app as part of our Machine Learning for Business course."
    col1, col2, col3 = st.columns(3)
with col1:
    # Yannick Rudolf
    st.markdown("Yannick Rudolf", unsafe_allow_html=True)
with col2:
    # Nico Schunk
    st.markdown("Nico Schunk", unsafe_allow_html=True)
with col3:
    # Christoph Lehr
    st.markdown("Christoph Lehr", unsafe_allow_html=True)



'''
This app is a tutorial: How to build your own computer vision model following the CRISP-DM Process Model. 

The example used for this tutorial is a garbage classification problem. The data used for this problem can be found on kaggle:
https://www.kaggle.com/datasets/asdasdasasdas/garbage-classification
'''

img = st.camera_input('Welche Art von Müll bist du? Mache jetzt den Test!')
img = st.file_uploader("Upload Image",type=["png","jpg","jpeg"])

model = tf.keras.models.load_model('./model/cv_model.h5')


batch_size = 32
img_height = 384
img_width = 512

train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

# print(model.predict())
if img:
    class_names = train_ds.class_names
    img = Image.open(img)
    img = img.resize((512, 384), Resampling.LANCZOS)
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.convert_to_tensor(img_array[:, :, :3])
    img_array.shape

    img_array = tf.expand_dims(img_array, 0)  # Create a batch
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    print("This image most likely belongs to {} with a {:.2f} percent confidence."
          .format(class_names[np.argmax(score)], 100 * np.max(score)))