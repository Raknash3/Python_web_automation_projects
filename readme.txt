## Project Name: Python web automation assignments

This repository contains a series of assignments that cover various topics, including web scraping, web automation, data manipulation, image processing, and application development. To effectively run and explore these assignments, it's recommended to use the following tools and libraries:

### Recommended Tools and Software
1. Jupyter Notebooks
2. Spyder IDE (Recent version)

### Required Libraries
1. Selenium
2. Beautiful Soup
3. Tkinter
4. Tesseract
5. Pytesseract
6. Flask
7. Flask SQLAlchemy
8. libtiff 4.0.10 (required for Assignment 6)
9. Openpyxl

## Assignments

### Assignment 1: Web Scraping

This assignment focuses on web scraping. The program navigates to a specified website and gathers the following information:
- Total number of products
- Names of the products
- Markdown price and actual price (if no markdown, both prices are the same)
- Ratings
- Links to product images

The collected details are organized into a dataframe with columns: Id, Name, Markdown Price, Actual Price, Rating, and Image Link. The data is then exported to a TSV file.

### Assignment 2: Web Automation

In this assignment, the program automates web interactions on the Big Basket website. It searches for specified items and takes screenshots, saving them in a predefined format. Note that although searching and screenshot processes are automated, manual updating of the location is required due to difficulties in identifying specific elements on the webpage.

### Assignment 4: Spreadsheet Automation

This assignment involves editing a given file based on specific conditions. Rows that violate the conditions are removed, and their unique identifiers are logged and saved in a text file. Once all conditions are met, blank spaces in the file are replaced with 'N/A'. The output Excel file and the log text file are provided in the repository.

### Assignment 5: Data Manipulation with Flask

In this assignment, a Flask application is used to perform basic database operations, including adding, editing, deleting, sorting, and filtering data. The Flask SQLAlchemy library is utilized to achieve these tasks. The data can be interactively manipulated through a GUI, and the final results can be exported to an Excel file.

### Assignment 6: Image OCR

The assignment is split into two parts: 6a for non-TIFF files and 6b for TIFF files. The program utilizes the Tesseract library to extract text information from images. For TIFF files, an additional step of converting the image to "RGBA" format is required before extraction. The accuracy of text extraction depends on the clarity of the image. While the program provides sample outputs, using a CNN model could potentially improve accuracy at the cost of higher computational resources.

### Assignment 7: Application Development

This assignment involves building a Python application with a graphical user interface (GUI). Upon running the application, a simple GUI with three buttons is displayed. Clicking on a button reveals relevant information within the application.
