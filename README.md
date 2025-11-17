# Candidate Profile Management Application

This is a web application built using **Streamlit**, **MongoDB**, and **Gemini API** for extracting and managing vital candidate information from resumes. The application allows users to upload resumes, extract essential details, store them in a MongoDB database, and view the profiles on the application interface. The application also enables downloading the uploaded resumes.

## Features

1. **Resume Upload**: 
    - Users can upload their resumes in PDF format.
    
2. **Automated Information Extraction**: 
    - The application uses the Gemini API to extract key information from the resume, including:
      - Name
      - Email
      - Phone Number
      - College Name
      - Skills

3. **MongoDB Storage**: 
    - The extracted information along with the uploaded resume (PDF) is stored in a MongoDB collection.

4. **Profile Viewing**: 
    - A list of all uploaded candidate profiles is displayed on the left sidebar.
    - Selecting a candidate from the sidebar displays their extracted profile details and allows users to view or download their resume.

5. **Resume Download**: 
    - The uploaded PDF resumes are stored in the MongoDB database using GridFS, and users can view or download the resumes directly from the web application.

## Technologies Used

- **Python**: The application logic is implemented in Python.
- **Streamlit**: A fast way to create custom web apps for ML and data science.
- **MongoDB**: NoSQL database for storing extracted candidate information and resumes.
- **GridFS**: Used to store and retrieve the resume PDFs from MongoDB.
- **Gemini API**: Used to retrieve specific information from the text extracted from resumes.
- **PyPDF2**: For extracting raw text from uploaded PDF resumes.

## Installation

### Prerequisites
- Python 3.x
- MongoDB Atlas account or local MongoDB instance
- Streamlit (`pip install streamlit`)
- Required Python packages: 
    ```bash
    pip -r requirements

## Usage
    streamlit run app.py

## Installation
