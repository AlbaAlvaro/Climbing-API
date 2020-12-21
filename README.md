# Climbing API
![Alt text]("/static/images/img.jpg")

## Aim of the project
Create an API that gives information about the routes of a desired area in Spain giving to the API, the area of interest and the grade of the route. It has also a webpage to interact more easily with the API.

## Process
1. **Webscraping**

With **Selenium** and **requests** obtain the information from the webpage 8a.nu. The information about the routes including the route name, the sector, the grade and the punctuation based on the number of stars was extracted.

2. Insert data to **MongoDB**

In order to store all the information from the webscraping it was saved into MongoDB

3. **API** creation

Create the endpoints of the API to extract the desired information from MongoDB using **Flask**. The API has two endpoints to connect to MongoDB.

4. **Webpage**

Using **HTML** and **CSS** create a simple webpage to get the information from the API in an easier way.

![Alt_text]("static/images/web_img.PNG")

## Further development
Improvements for the future include adding more areas to the database, showing in the webpage an interactive map to see where the determined areas are and adding the sector depending on the area to the selection menu.