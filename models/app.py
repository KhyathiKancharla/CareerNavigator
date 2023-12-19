import re
import cohere as co

import webbrowser

def clean_resume(resume_text):
    clean_text = re.sub('http\S+\s*', ' ', resume_text)
    clean_text = re.sub('RT|cc', ' ', clean_text)
    clean_text = re.sub('#\S+', '', clean_text)
    clean_text = re.sub('@\S+', '  ', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text)
    return clean_text

def camel_case_with_spaces(input_text):
    words = input_text.split()
    camel_case_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    final = ''.join(camel_case_words) 
    return final

def cohereLLM(resumedata):
    coApi = co.Client('ut8qQIUABIpJ3LfXmL1wkgMxqyySgbbksQrcKe4f')
    response = coApi.generate (
    model = 'command',
 
   #prompt = f"{resumedata}. Given is the resume data. predict only one job domain role the resume belongs to in one keyword and no further explanation required.",
   # prompt = f"{resumedata}. predict overall job role the resume belongs in one keyword (NO SPECIAL CHARACTERS SHOULD BE INCLUDED)",
    prompt= f"{resumedata}. Given is the resume data. predict job domain role the resume belongs to in one keyword.",
    max_tokens = 1000,
    temperature = 0.99,
    k = 0,
    stop_sequences=[],
    return_likelihoods='NONE'
    )
    
    return camel_case_with_spaces(response.generations[0].text)

def openJobListing(domain):
    url= f'https://www.linkedin.com/jobs/search/?keywords={domain}'  
    webbrowser.open_new_tab(url)  


def main(profileParagraph):
    if profileParagraph == ' ':
        return "No resume data found"
    
    resumeData = clean_resume(profileParagraph)
    domain =  cohereLLM(resumeData)
    # openJobListing(domain)
    return domain
