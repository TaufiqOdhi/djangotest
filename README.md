# Documentation
Python version : 3.12.0

This docummentation provide to run using linux os.

## How to Install
1. create python environment using conda or python venv
```
# if using conda
conda create -n pythontest python=3.12

# if using python venv
python -m venv pythontest
```
2. activate python environment
```
# if using conda
conda activate pythontest

# if using python venv
source pythontest/bin/activate
```
3. install requirements
```
pip install -r requirements.txt
```
4. migrate the migrations file
```
python manage.py migrate
```
5. load seeder data
```
bash scripts/load_seeder_data.sh
```

## How to Run
```
python manage.py runserver
```