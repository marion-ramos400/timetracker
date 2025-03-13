# Time Tracker App
##  Run everything via Docker
### Clone the repository
```
git clone https://github.com/marion-ramos400/timetracker.git
```
### Go to project folder
```
cd timetracker
```
### Run docker compose build and run
```
sudo docker compose up --build
```
### Access the app via browser in http://localhost:3000
> frontend is running at localhost:3000
> backend is running at localhost:8000
## Run backend without docker
### Go to backend folder
```
cd timetracker/backend
```
### Install python packages
```
pip install -r requirements.txt
```
### Migrate app
```
python manage.py makemigrations timetracker
python manage.py migrate
```
### Run backend app
```
python manage.py runserver
```
> this will run at localhost:8000
## Run frontend without docker
### Go to frontend folder
```
cd timetracker/frontend
```
### Install npm packages
```
npm install
```
### Run frontend app
```
npm start
```
> this will run at localhost:3000
## Running pytest
### Prerequisites
> make sure you have pytest and requests installed in your python environment
```
pip install pytest
pip install requests
```
> make sure that backend app is running
### Go to test folder
```
cd timetracker/test
```
### Run pytest
```
pytest
```
###  Or run pytest in a single file
```
pytest test_signup.py
```

## Backend Endpoints:
##### usage on the following endpoints can be found in test/ files
> /api/signup

> /api/login

> /api/createtask

> /api/gettasks
