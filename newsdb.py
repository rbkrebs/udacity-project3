#!/usr/bin/env python2
# "Database code" for the DB Forum.
import psycopg2

DBNAME = "news"


def get_popular_articles():

    """Return the most popular three articles of all time."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select a.title,  count(a.title) from articles as a inner join log as l on l.path like '%'||a.slug and l.status = '200 OK' group by a.title order by count desc limit 3;")
    articles = c.fetchall()
    return articles


def get_popular_author():

    """Return the most popular article authors of all time."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select au.name,  count(au.name) from articles as a inner join log as l on l.path like '%'||a.slug inner join authors as au on au.id = a.author  and l.status = '200 OK' group by au.name order by count desc limit 4;")
    authors = c.fetchall()
    return authors


def get_worse_day():

    """Return which days did more than 1% of requests lead to errors."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select date(time) as data, cast(COUNT(case when status <> '200 OK' then 1 end) as decimal)/COUNT(case when status = '200 OK' then 1 end)*100 from log group by data having cast(COUNT(case when status <> '200 OK' then 1 end)as decimal)/COUNT(case when status = '200 OK' then 1 end)*100>=1;")
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
percentage = round(get_worse_day()[0][1], 1)

print('On which days did more than 1% of requests lead to errors?\n')
print('{} -- {}%\n'.format(data, percentage))
