# flask-web-template
A standard template we can use as a starting point for any web based projects we decide to use.

##Usage
To use this repo as the starting point for a new project, follow these steps:

1) clone this repository: `git clone git@github.com:8451-CS-Club/flask-web-template.git new_project`

2) cd to new repo: `cd new_project`

3) remove the origin: `git remote rm origin`

4) Create the new project on GitHub's site

5) add the new origin: `git remote add origin git@github.com:8451-CS-Club/new-project.git`

6) now you can run: `git push origin master` and it will update the project


Here's a quick breakdown for flask projects for those who are interested in learning more.

##run.py
Execute this file to actually run the website locally. You can either navigate to the directory it's in and run `python run.py`, or run it from an IDE.

##app
A high level directory where most of the projects code will live under.

##static
A directory to keep any static files. This will usually have subdirectories like css or js, to keep those files in.

##templates
A directory to keep all html files in.

##views.py
This is where you define your url routes. For example, `@app.route('/')` creates my home url. I can create anything here, and the code below will run when that endpoint is hit.
