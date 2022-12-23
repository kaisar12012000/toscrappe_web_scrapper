# Web scrapping with python

## Dependencies

- Python
- Beautiful soup
- Requests
- xlsxwriter
- uuid

## What is web scrapping

**Web scrapping** is an efficient technique that is used to get data from websites. Usually we use web scrapping to get data from large data sets over the internet. Imagine you are to create a project that gets information of players of a specific team. Web scrapping would be an excellent solution to this. We can target the elements on that web page and get the details from them.

## About the project

- The project comprises of a ```scrapper.py``` file.
- The workflow of the project is very simple. We use the ```requests``` library to make a get request to [Toscrappe Books Page](http://books.toscrape.com/).
- We use ```Beautiful soup``` library to find all the ```article``` tags.
- We fetch the data of each book  from this ```article``` tag and then store this value in an excel spreadsheet.
- We are using ```xlsxwriter``` library to write our data into an excel sheet and save the file in th root directory.
- We use ```uuid`` to get a unique string that will serve as the name of the file.
