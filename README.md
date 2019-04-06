# Logs Analysis Project

This is the third project of Full Stack Web Developer Nanodegree Program from `Udacity`.
It has just `one` python file: newsdb.py.

## Configuration

To run this project, you must have installed in your computer the python 2. Follow the instructions
according to this [link](https://www.python.org/downloads/).

The project use `PostgreSQL` database.Follow the instructions according to this [link](https://www.postgresql.org/download/)

The tables and inserts can be done by running the newsdata.sql, which can be downloaded directly on Udacity site. After running, use this command:

```psql -d news -f newsdata.sql```


The file `newsdb.py` has the three functions which make some queries to the `news` database. The return must answer the three follw questions:

```What are the most popular three articles of all time?```
```Who are the most popular article authors of all time?```
```On which days did more than 1% of requests lead to errors?```


## Run

To run this project follow the next steps forward:

1. Clone the directory or download as a zip file. If you download, unpack the zip first.
2. Navigate to the directory cd repository_name or folder name.
3. Inside the repository or folder, run python newsdb.py. You can see [here](http://www.cs.bu.edu/courses/cs108/guides/runpython.html) how to run python according to your OS system.



## License

This project is under [MIT License](https://opensource.org/licenses/MIT)


