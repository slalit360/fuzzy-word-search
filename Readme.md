Write a HTTP service that provides an endpoint for fuzzy search / autocomplete of English words.


You are given a dataset that contains 333,333 English words and the frequency of their usage in some corpus. A very small sample is shown below:


track   		112385243
australia		112197265
discussion		111973466
archive		111971865
once			111882023
others		111397714
entertainment	111394818
agreement		111356320
format		111279626


Let us assume we’re building a web app where the user types in a single word from this list in a search box. We wish to autocomplete the input in the search box. 


Your objective is to write a Python app using Django framework that exposes a single endpoint:


GET /search?word=<input>


where input is the (partial) word that the user has typed so far. For example, if the user is looking up procrastination, the service might receive this sequence of requests:


GET /search?word=pro
GET /search?word=procr
GET /search?word=procra


and so on.


The response should be a JSON array containing upto 25 results, ranked by some criteria (see below).
Constraints

1.	Matches can occur anywhere in the string, not just at the beginning. For example, eryx should match archaeopteryx (among others).
2.	The ranking of results should satisfy the following:
a.	We assume that the user is typing the beginning of the word. Thus, matches at the start of a word should be ranked higher. For example, for the input pract, the result practical should be ranked higher than impractical.
b.	Common words (those with a higher usage count) should rank higher than rare words.
c.	Short words should rank higher than long words. For example, given the input environ, the result environment should rank higher than environmentalism.
i.	As a corollary to the above, an exact match should always be ranked as the first result.
The search algorithm you develop should ideally incorporate some form of a weighted average of all qualifying parameters. The perfect weights, in production systems, are however derived through the use of ML algorithms.


Steps:

1> install python and 		> 	pip install virtualenv or pipenv
2> cd to project dir and 	>	vitualenv .
3> activate virtualenv   	>	.\Script\activate
4> install django 	   		>	pip install Django
5> move to django project   > 	cd WordSearchDjango 
   complete django code dev finishes here
6> run django				>	python manage.py runserver 8080
7> install server			> 	pip install gunicorn
   django-heroku install	> 	pip install django-heroku
8> save to requirements		> 	pip freeze > requirements.txt

9> create heroku app 
	install heroku cli
							> 	heroku login
							>   heroku create fuzzy-word-search
10> git setup				> 	git init
							>	git add . or git add --all
							>	git commit -m "final upload"
							> 	heroku git:remote -a fuzzy-word-search
11> deploy and setup		>	git push heroku master
							>	heroku run bash
							>	python manage.py migrate
							>	python manage.py createsuperuser
12 > visit app 			https://fuzzy-word-search.herokuapp.com/

	
dir tree:-
	
<DIR>	+ Include
<DIR>   + Lib
<DIR>   + Scripts	
<DIR>   - WordSearchDjango							
<FILE>		+ Procfile
<DIR> 		+ SearchApp/
<DIR> 		+ WordSearchDjango/
<FILE>		+ db.sqlite3
<FILE>		+ manage.py
<FILE>		+ requirements.txt
<FILE>		+ word_search.tsv
