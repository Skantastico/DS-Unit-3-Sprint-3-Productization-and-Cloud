#

Soon to be adding a lot of useful info



'''sh
cd web_app

FLASK_APP=app.py flask db init #> generates app/migrations dir

# run both when changing the schema:
FLASK_APP=app.py flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=app.py flask db upgrade #> creates the "users" table
'''

## Run

'''sh
FLASK_APP=app.py flask run
'''
