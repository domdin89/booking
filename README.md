### Create a virtual evironment

`python3 -m venv project_env`

### Check with ls that is created the folder

`ls`

### Activate virtual environment

`source project_env/bin/activate`

### Install requirements

`pip install -r requirements.txt`

### Start the project

`python3 manage.py runserver`


## All in one

```bash
python3 -m venv project_env && source project_env/bin/activate &&  pip install -r requirements.txt && python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver
```

## ENV variables

## Author

- [@domdin89](https://www.github.com/domdin89)