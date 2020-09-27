# BrainSkills!

A system student/teacher website.

The aim of BrainSkills is to help the student to get confident speaking in English helping them to reach their goals. Implementing many techniques of conversation, writing, and grammar.

At BrainSkills website, the user can choose between a guest, student, or teacher account. Base on the user selection, the user will be able to create a profile with different characteristics. If is `student` the user will have to choose a service, level of English, and time schedule for his class. Also will be able to send a message to the teacher or administration with inquiries. If is `teacher` the user will be able to select a time schedule and also will have access to the messages that the students could have sent, as well as the student contact information.

This project is base on users' role and data models manipulation. Having one site with different status for the users makes the application powerful and effective.

Web Programming with Python and JavaScript.

Built with `Python`/`Django`/`JavaScript`/ `Bootstrap4`/ `JQuery`.

## Setup

```
# views.py -the core of the project structure, connects the app with the database, and all the corresponding paths for each web page.
# urls.py -determines the paths for each view function. Connects the HTTPrequest waiting for a matching response from views.py. Here we define the routes and arguments that we would need in order to fetch a call to our db.
# models.py -gives a perspective of how each table of the database looks like and what data types are referring to.
# templates folder -contains all HTML files.
# static folder -contains ` brainSkills ` folder which contains the css file with the stylesheet, all images using in the application, javascript file and a `readme` folder which contains the images for the readme file.
# main.js -connects the client-side with the server-side, here all the APIs calls are made to fetch information from our database. The path using in our fetch request has to match with the path on our urls.py to connect with the view function and retrieve information. AJAX calls are also to prevent refresh/ reloading the webpage which makes our app run fast.

```

## Enviroment

- `$ . venv/bin/activate`
- `cd project5`
- `python manage.py makemigrations brainSkills`
- `python manage.py migrate`
- `python manage.py runserver`

## DB SCHEMA

![](/project5/brainSkills/static/brainSkills/readme/db_schema_brainskills.png)

## Home page for all users

![](/project5/brainSkills/static/brainSkills/readme/home_brainskills.png)

## Home page for a registered user

![](/project5/brainSkills/static/brainSkills/readme/home3_nrainskills.png)

## Mobile responsive design with toggle navbar and scrolling down the page, using the bootstrap grid system.

![](/project5/brainSkills/static/brainSkills/readme/mobile_responsive.png)

## User will be prompted to choose an account

![](/project5/brainSkills/static/brainSkills/readme/user_status_brainSkills.png)

## Student profile - shows the user information if the user is a student. Allows students to send messages to teachers.

![](/project5/brainSkills/static/brainSkills/readme/student_profile.png)

## Teacher profile - shows the messages from students to handle, student's contact, and let the teacher choose for a time schedule.

![](/project5/brainSkills/static/brainSkills/readme/teacher_profile1.png)

![](/project5/brainSkills/static/brainSkills/readme/teacher_profile2.png)
