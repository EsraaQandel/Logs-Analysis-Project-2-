#! /usr/bin/env python3

import psycopg2

db_name = "news"

q1 = """ select title , count(*) as views from articles,log
where (path like '%' || slug) GROUP BY title order by views DESC limit 3 ;"""

q2 = """ select name , count(*) as views from authors,articles,log
where (path like '%' || slug) and authors.id = articles.author
GROUP BY name order by views DESC ;"""

q3 = """ select * from error_calc where error_rate > 1 """


def connect(query):
    """ connect to postgresql db """
    conn = psycopg2.connect(dbname=db_name)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return(results)
    conn.close()


# store results for each query
results_1 = connect(q1)
results_2 = connect(q2)
results_3 = connect(q3)

# format results


def get_q1_answers():
    print("\n The most popular three articles of all time are : \n")
    for eachObject in results_1:
        print( '%s --- %s views'%(eachObject[0],eachObject[1]))


def get_q2_answers():
    print("\n The most popular article authors of all time are : \n")
    for eachObject in results_2:
        print( '%s --- %s views'%(eachObject[0],eachObject[1]))


def get_q3_answers():
    print("""\n The days with more than 1% of errors are : \n""")
    for eachObject in results_3:
        print( '%s --- %s %% errors'%(eachObject[0],eachObject[1]))


# print formatted results
get_q1_answers()
get_q2_answers()
get_q3_answers()
