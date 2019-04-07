#!/usr/bin/env python2

import psycopg2

DBNAME = "news"


def get_popular_articles():

    """Return the most popular three articles of all time."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''SELECT a.title,
                    COUNT(a.title)
                FROM articles AS a
                INNER JOIN log AS l ON l.path LIKE '%'||a.slug
                AND l.status = '200 OK'
                GROUP BY a.title
                ORDER BY COUNT DESC
                LIMIT 3;''')
    articles = c.fetchall()
    return articles


def get_popular_author():

    """Return the most popular article authors of all time."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''SELECT au.name,
                    COUNT(au.name)
                FROM articles AS a
                INNER JOIN log AS l ON l.path LIKE '%'||a.slug
                INNER JOIN authors AS au ON au.id = a.author
                AND l.status = '200 OK'
                GROUP BY au.name
                ORDER BY COUNT DESC
                LIMIT 4;''')
    authors = c.fetchall()
    return authors


def get_worse_day():

    """Return which days did more than 1% of requests lead to errors."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''SELECT date(TIME) AS DATA,
                    CAST(COUNT(CASE
                            WHEN status <> '200 OK' THEN 1
                                END) AS DECIMAL)/COUNT(*)*100
                FROM log
                GROUP BY DATA
                HAVING cast(COUNT(CASE
                            WHEN status <> '200 OK' THEN 1
                                END)AS DECIMAL)/COUNT(*)*100>=1;''')
    data = c.fetchall()
    return data


articles = get_popular_articles()
print('What are the most popular three articles of all time?\n')
for article in articles:

    print('{} -- {} views\n'.format(article[0], article[1]))

authors = get_popular_author()
print('Who are the most popular article authors of all time?\n')

for author in authors:
    print('{} -- {} views\n'.format(author[0], author[1]))


data = get_worse_day()[0][0].strftime('%B %d, %Y')
percentage = round(get_worse_day()[0][1], 2)

print('On which days did more than 1% of requests lead to errors?\n')
print('{} -- {}%\n'.format(data, percentage))
