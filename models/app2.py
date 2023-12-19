import os
import pickle
import re
import streamlit as st
from django.conf import settings

clf_path = os.path.join(settings.BASE_DIR, 'clf.pkl')
tfidf_path = os.path.join(settings.BASE_DIR, 'tfidf.pkl')

clf = pickle.load(open(clf_path, 'rb'))
tfidf = pickle.load(open(tfidf_path, 'rb'))

def clean_resume(resume_text):
    clean_text = re.sub('http\S+\s*', ' ', resume_text)
    clean_text = re.sub('RT|cc', ' ', clean_text)
    clean_text = re.sub('#\S+', '', clean_text)
    clean_text = re.sub('@\S+', '  ', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text)
    return clean_text

def main(profileParagraph):
    global resume_bytes
    upload_Resume= profileParagraph
    if upload_Resume is not None:
        cleanedResume = clean_resume(upload_Resume)
        vectorised = tfidf.transform([cleanedResume])
        prediction_id = clf.predict(vectorised)[0]

        print("Predicted Job Category ID: ", prediction_id)

        category_mapping = {
            15: "Java Developer",
            23: "Testing",
            8: "DevOps Engineer",
            20: "Python Developer",
            24: "Web Designing - MERN, MEVN, MEAN",
            12: "HR",
            13: "Hadoop",
            3: "Blockchain",
            10: "ETL Developer",
            18: "Operations Manager",
            6: "Data Science",
            22: "Sales",
            16: "Mechanical Engineer",
            1: "Arts",
            7: "Database",
            11: "Electrical Engineering",
            14: "Health and fitness",
            19: "PMO",
            4: "Business Analyst",
            9: "DotNet Developer",
            2: "Automation Testing",
            17: "Network Security Engineer",
            21: "SAP Developer",
            5: "Civil Engineer",
            0: "Advocate",
        }

        category_name = category_mapping.get(prediction_id, "Unknown")
        print("Predicted Job Category: ", category_name)
        return category_name