class DB(object):
    def __init__(self, **credentials):
        self._connect = partial(pymysql.connect, **credentials)

    def query(self, q_str, params):
        with self._connect as conn:
            with conn.cursor() as cur:
                cur.execute(q_str, params)
                return cur.fetchall()

# now for usage

test_credentials = {
    # use credentials to a fake database
}

test_db = DB(**test_credentials)
test_db.query(write_query, list_of_fake_params)
results = test_db.query(read_query)
assert results = what_the_results_should_be
