import sqlite3


def get_result(query: str):
    """

    :param query:
    :return:
    """
    with sqlite3.connect("netflix.db") as conn:
        conn.row_factory = sqlite3.Row
        result = []
        print()

        for item in conn.execute(query).fetchall():
            print(item)
            s = dict(item)

            result.append(s)

        return result


def get_all(query: str):
    """

    :param query:
    :return:
    """
    with sqlite3.connect("netflix.db") as conn:
        conn.row_factory = sqlite3.Row
        result = []

        for item in conn.execute(query).fetchall():
            print(item)
            s = dict(item)

            result.append(s)

        return result


def get_one(query: str):
    """

    :param query:
    :return:
    """
    with sqlite3.connect('netflix.db') as conn:
        conn.row_factory = sqlite3.Row
        res = conn.execute(query).fetchall()

        if res is None:
            return None
        else:
            return dict(res)


def search_by_cast(name1: str = 'Rose McIver', name2: str = 'Ben Lamb'):
    qery = f"""
    SELECT * FROM netflix
    WHERE "cast" like '%{name1}%' and "cast" like '%{name2}%'
    """

    cast = []

    result = get_all(qery)

    for item in result:
        ...
