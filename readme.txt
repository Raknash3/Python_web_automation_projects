This repository contains the following assignments. The following software is recommended for running the programs
 1. Jupyter Notebooks
 2. Spyder IDE ( Recent version )
 
 The following libraries are required to run the programs:
 1. Selenium
 2. Beautiful Soup
 3. Tkinter
 4. Tesseract
 5. Pytesseract
 6. Flask
 7. Flask SQLalchemy
 8. libtiff= 4.0.10 ( assgn 6 works only with this version)
 
 
 Assignments

 1. Assign 1 : Web scrapping

              The program opens the mentioned website and collects the following details
                i Total products

                ii The name of the products in the list

                iii The mardown price and the actual price
                   ( If there is no markdown price then both the actual and markdown price are the same)

                iv Ratings

                v The link that contains the image

               The collected details are made into a dataframe containg the following columns: Id, Name, Markdown Price, Actual Price, Rating, Image link. Then they are exported to tsv file
               
2. Assign 2: Web Automation

             The program opens big basket website searches for the items mentioned in the assignments, takes the screenshot and saves them in the mentioned name format.(Note: Though the process of searching the products and taking screenshot is automated, updating the location has to be done manually, the class or the id for setting the location couldn't be found. Hence making this code semi-automated)
             
3.  Assign 5: Creating a table and editing it using Flask framework

              The program does the basic function like creating a database, adding, editing, deleting, sorting, filtering of the data given using Flask SQLalchemy and finally it is also exported into a Excel file. 

4. Assign 6: Image OCR

              The program is divided in to two parts, 6b for non-tiff files and 6a for other image types like jpg,jpeg,png. Using the teserract library's image_to_string function, this program reads the image and writes the extracted information into a text file. For tiff files, however the image must be first converted into "RGBA" format before passing the image_to_string function. The funstion image_to_string performs mediocrely on the images, provided that the date in the image is clear and visible. Sample outputs is provided. CNN can be used to acquire more accurate extraction of data from scanned copies but it is computationally expensive. 
              
5. Assign 7: Application

             The application is built using python, upon running it a simple GUI opens with three buttons, pressing on any of the buttons will display the respective information on the application.
