# TrackTC

# Django React Stack
### REMINDER TO PUSH TO YOUR OWN BRANCH AND PULL REQUEST BEFORE MERGING TO MAIN
*Since I added this ReadMe, remember to*`git pull origin main` *to update your local files*


## How to start up the `venv`
`cd` into your djangoreact dir, and then execute the `activate` script
for Mac/Linux: `. venv/bin/activate`
for Windows: do what you guys did last time lol

## Do not add the `venv` file to git
I’ve already added the `venv/` directory to the .gitignore, so make sure the `venv` directory is not tracked. Having it greyed out on VSCode is not a mistake 
-> TLDR: you can safely use `git add *`, just don’t go out of your way to add `venv` to the commit

## Some resources:
[Developers - MyTTC](https://myttc.ca/developers) Station/Stop API in json format
[Google Maps Platform Documentation  |  Google Developers](https://developers.google.com/maps/documentation)	Google Maps API

Django/React API
[How to get Django and ReactJS to work together? - Stack Overflow](https://stackoverflow.com/questions/41867055/how-to-get-django-and-reactjs-to-work-together)  Top answer here

Django (Backend) -> Django Rest Framework (Interface) -> React (Frontend)

## Django workflow/customs
*  Run live server `python3 map_project/manage.py runserver` from root folder
*  `views.py` are different pages, so like `admin/` or `profile/`
*  `urls.py` directs the url to the given view in`views.py`
*  Logic heavy coding for views goes into `models.py`, this is basically a database/tables system for views to pull information out of
*  `serializers.py` is part of the REST framework, this sends and recieves data, you will use this system to communicate between frontend and backend
*  `frontend/src` is for react, javascript
*  `frontend/static` is for CSS, images
*  `frontend/templates/frontend` is for HTML pages
* If you change `models.py` or `views.py`,  run `python3 map_project/manage.py makemigrations` from the djangoreact root folder, then run `python3 map_project/manage.py migrate` to update the database. This is similar to committing then pushing

## Packages that were downloaded
```
npm i webpack webpack-cli --save-dev
npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
npm i react react-dom --save-dev
npm install @material-ui/core
npm install @babel/plugin-proposal-class-properties
npm install react-router-dom
npm install @material-ui/icons

pip install requests
```
