## Item Catalog Project

Udacity - Full Stack Web Developer Nanodegree

Project 4: Build a web application that provides a list of items within a variety of categories and integrate third party user registration and authentication. Authenticated users have the ability to post, edit and delete their own items.

### How to run

1. Download and install [Vagrant](https://www.vagrantup.com/downloads.html) and [Virtual Box](https://www.virtualbox.org/wiki/Downloads) for your operating system.

2. Use Github to clone the repository [https://github.com/udacity/fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm).

3. Using your terminal, cd into the vagrant directory, run ```vagrant up```, then log into it with ```vagrant ssh```.

4. Clone the GitHub repository inside the vagrant folder. 

5. The categoryitems.db database is prepopulated with default categories and items and ready to use. If you need to reinitialize the database, delete the existing categoryitems.db then run the following commands:
	
	python database_setup.py
	python lotsofitems.py 

6. Run the application with python application.py from within the directory.

7. Go to http://localhost:5000/ to access the application.


### JSON Endpoints

**http://localhost:5000/category/JSON**

```
Return JSON of all the categories

```

**http://localhost:5000/category/<int:category_id>/item/JSON**

```
Return JSON of all items in a category

```

**http://localhost:5000//category/<int:category_id>/item/<int:item_id>/JSON**

```
Return JSON of an item in a category

```
