# Flask is-up

To run:

- First create the database: `python create_schema.py`.
- Run the checker periodically: `watch -n 20 python check.py`.
- Run the flask server: `flask run`.


To add a domain using curl:

    curl -XPOST -H"Content-Type: application/json" http://127.0.0.1:5000/domains/ -d '{"name": "https://discuss.afpy.org"}'


## TODO

- Add a `message` explaining why a domain is down.
- Add a `/domains/{domain_name}` endpoint to get infos for a single
  domain.
- Add a `/domains/{domain_name}/history` endoint to get the full
  history of checks (you'll need another dedicated table to store each
  checks).
- Add a `?q=` query string to `/domains/` to filter domains by a name
  pattern, like `GET /domains/?q=.fr`.
- Add a `?is_up=` query string to filter by status, like `GET
  /domains/?is_up=False`.
- Paginate the `/domains/{domain_name}/history` endpoint.
- Enhance `check.py` to only check a limited number of domains
  (prioritizing the last recently checked ones and the never checked
  ones), via a `--limit` argument.  domains should always be checked,
  though.
- Add a paginated `/checks/` showing all checks, antechronologically.
- Add query strings `q` and `is_up` to the `/checks/` endpoint.
- Add meta-informations to the `/domains/{domain_name}/`:
  - Computed uptime, in %, from the domain checks history.
  - Top 10 errors with error counts.
  - Last error details.
