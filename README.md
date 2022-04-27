# Flask is-up

To run:

- First create the database: `python create_schema.py`.
- Run the checker periodically: `watch -n 20 python check.py`.
- Run the flask server: `flask run`.


To add a domain using curl:

    curl -XPOST -H"Content-Type: application/json" http://127.0.0.1:5000/domains/ -d '{"name": "https://discuss.afpy.org"}'
