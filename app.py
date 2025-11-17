from typing import Any, List
import asyncio
import json
import logging
import os
import streamlit as st
import numpy as np
import PyPDF2
import google.generativeai as genai
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import base64
from streamlit_pdf_viewer import pdf_viewer

# Connecting to the mongoDB
uri = "mongodb+srv://Ramkumar:Ram%402004@ramcluster.c6j2p.mongodb.net/?retryWrites=true&w=majority&appName=RamCluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.candidate
profileData = db.profileData

st.sidebar.title("About")


# Retriving all the documents
all_candidate_info = profileData.find()
all_candidate_info = list(all_candidate_info)

st.sidebar.info(
    "This application identifies the crop health in the picture.")
st.sidebar.write("candidate_names")
for data in all_candidate_info:
    if st.sidebar.button(data.get('Name')):
        candidate_pdf_file_bytes = base64.b64decode(data.get('resume'))

        candidate_pdf_file = open('file.pdf', 'wb')
        candidate_pdf_file.write(candidate_pdf_file_bytes)

        st.download_button('Download pdf', candidate_pdf_file)
        # container_pdf, container_chat = st.columns([50, 50])

        # with container_pdf:

        #     if candidate_pdf_file:
        #         binary_data = candidate_pdf_file.getvalue()
        #         pdf_viewer(input=binary_data,
        #                 width=700)




st.title('Wheat Rust Identification')

st.write("Upload your resume")
uploaded_file = st.file_uploader("", type="pdf")

if uploaded_file is not None:
    # Initialize an empty string to store the text
    text_extracted_from_pdf = ''

    # Create a PdfReader object instead of PdfFileReader
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text_extracted_from_pdf += page.extract_text()

    
    # Import the Python SDK
    # Used to securely store your API key
    genai.configure(api_key="AIzaSyBVQbVwbK8GvhwTOTBWsVDKlcUtMmPNKDM")
    model = genai.GenerativeModel('gemini-pro')

    # Name
    prompt = text_extracted_from_pdf + "\n Give me the name of this profile bearer"
    response = model.generate_content(prompt)
    #print(response.text)
    name = response.text  

    # Email
    prompt = text_extracted_from_pdf + "\n Give me the email of this profile bearer"
    response = model.generate_content(prompt)
    #print(response.text)
    email = response.text

    # Phone Number
    prompt = text_extracted_from_pdf + "\n Give me the phone number of this profile bearer"
    response = model.generate_content(prompt)
    #print(response.text)
    phoneNo = response.text

    # College Name
    prompt = text_extracted_from_pdf + "\n Give me the college name of this profile bearer"
    response = model.generate_content(prompt)
    #print(response.text)
    collegeName = response.text

    # skills
    prompt = text_extracted_from_pdf + "\n Give me all the skill sets of this profile bearer as a whole"
    response = model.generate_content(prompt)
    #print(response.text)
    skills = response.text



    # Procesing the pdf file to insert into db
    file_bytes = base64.b64encode(uploaded_file.read())

    candidate_data = {
    'Name': name,
    'E-mail': email,
    'Phone Number': phoneNo,
    'College': collegeName,
    'Skills': skills,
    'resume': file_bytes
    }

    profileData.insert_one(candidate_data)
