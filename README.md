# flask-web-template
A standard template we can use as a starting point for any web based projects we decide to use.


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
