# CareerNavigator
## Functions
- If the student want to change his/her domain there is a roadmap of what skills are required and how to study.
- The student can attempt different types of quizes.
- In the learner module the student can do a profile screening to know what job roles he can get with the skills he/she accquires.
- The learner gets a detailed roadmap with the resources links that are free to access

### Admin
- Create Admin account using command
```
py manage.py createsuperuser
```
- After Login, can see Total Number Of Student, Teacher, Course, Questions are there in system on Dashboard.
- Can View, Update, Delete, Approve Teacher.
- Can View, Update, Delete Student.
- Can Also See Student Marks.
- Can Add, View, Delete Course/Exams.
- Can Add Questions To Respective Courses With Options, Correct Answer, And Marks.
- Can View And Delete Questions Too.

### Teacher
- Apply for job in System. Then Login (Approval required by system admin, Then only teacher can login).
- After Login, can see Total Number Of Student, Course, Questions are there in system on Dashboard.
- Can Add, View, Delete Course/Exams.
- Can Add Questions To Respective Courses With Options, Correct Answer, And Marks.
- Can View And Delete Questions Too.
> **_NOTE:_**  Basically Admin Will Hire Teachers To Manage Courses and Questions.

### Student
- Create account (No Approval Required By Admin, Can Login After Signup)
- After Login, Can See How Many Courses/Exam And Questions Are There In System On Dashboard.
- Can Give Exam Any Time, There Is No Limit On Number Of Attempt.
- Can View Marks Of Each Attempt Of Each Exam.
- Question Pattern Is MCQ With 4 Options And 1 Correct Answer.
- get few roles suggested from the users skills

## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Open Terminal and Execute Following Commands :
```
python -m pip install -r requirements. txt
```
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```


## CHANGES REQUIRED FOR CONTACT US PAGE
- In settins.py file, You have to give your email and password

```

EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'your email password'
EMAIL_RECEIVING_USER = 'youremail@gmail.com'
```
## Screenshots

![index](https://github.com/KhyathiKancharla/CareerNavigator/assets/110332342/c8ffc4f0-c3cb-4654-b7df-247e1469fd29 )


![domainchange](https://github.com/KhyathiKancharla/CareerNavigator/assets/110332342/484bff85-dfa5-449f-856c-87407dacd792)


   

![exams](https://github.com/KhyathiKancharla/CareerNavigator/assets/110332342/c8392e88-f358-41f5-bfc5-dc047ff1eb44)

## Drawbacks/LoopHoles
- Need to make the application responsive.
- The user interface of the website is basic which should be improved.

## Team 
- Khyathi Kancharla 
- Salman Khan
- Teja Sai
- Pujitha Sayana
