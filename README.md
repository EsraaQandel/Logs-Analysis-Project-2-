# Log-Analysis Project

## Introduction 

> In this project you will build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
You will get practice interacting with a live database both from the command line and from your code.

 You will be working with a database that includes three tables:
 * The authors table includes information about the authors of articles.
 * The articles table includes the articles themselves.
 * The log table includes one entry for each time a user has accessed the site.


## How to Run?

### PreRequisites:
  [Python3](https://www.python.org/) , [VirtualBox](https://www.virtualbox.org/), [Vagrant](https://www.vagrantup.com/)
   

### Prepare the software and data:
 
  1. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository and Download the data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
  2. Copy the newsdata.sql file -from the zip file you just downloaded - and content of this current repository
  3. launch the VM and install all the dependencies by running:
  
  ```
    $ vagrant up
  ```
  4. Log using command:
  
  ```
    $ vagrant ssh
  ```

  5. Use `psql -d news -f newsdata.sql` to Load the data in local database.

  6. Use `psql -d news` to connect to database.
  
  7. Create view error_calc using:
  ```
  create view error_calc as select day, round((error::decimal / normal)*100,2) as error_rate from (
   select time::date as day , count(*) as normal , count(case when status NOT LIKE '200 OK' then 1 end) as error from log GROUP BY day
  ) as error_percentage; 
  ```

### Run the reporting tool:

  ```
    $ python3 my_tool.py
  ```
  