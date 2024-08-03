#Employee database-------------------------------------------------------------------------------
This is a python project based GUI application that handles employee data like unique emmployee id(integer), Employee name (without spaces) and salary.
This application has made use of modules in python like tkinter for GUI, sqlite3 for handling data in database file linked to it, requests, json, pandas, matplolib, and use of API.

The home page of the application shows five tabs namely Add data, View data, Update data, Delete data and Graph. It also shows location and temperature at that time.
Here is an image of Main window:  ![Python_projhome](https://github.com/user-attachments/assets/80093171-64e5-4eab-a271-3f8c42c36475)

Upon clicking on "Add data" a new window opens and one can add Employee id , Name and Salary and then click on "Add" button. It wil raise an issue if user makes any mistake in entering data like entering wrong datatype than permitted in given section. Clicking on "Back" button will take one back to main window.
Here is an image of Add data window: ![Python_projadd](https://github.com/user-attachments/assets/2aced130-667c-42a5-b2fa-e7469bdc94b4)

Upon clicking on "View data" a new window opens and one can view all the data in database. Clicking on back button will take you "Back" to home window.
Here is an image of View data window based on available data: ![Python_projview](https://github.com/user-attachments/assets/f5568cf2-8ebe-41ef-a26e-c9b723956b9f)

Upon clicking on "Update data" a new window opens and one can update Name and Salary with reference to employee id and then click on "Update" button. It will raise issue similarly like add window upon any mistake by user in data entry. Clicking on "Back" button will take one back to main window.
Here is an image of Update data window: ![Python_projupdate](https://github.com/user-attachments/assets/7ce6aeed-1d32-4d64-a20c-a33761a13bd3)
                                        ![Python_projupdatedone](https://github.com/user-attachments/assets/e57df39a-3edf-40f1-b7c4-7df674a8b13b)

Upon clicking on "Delete data" a new window opens and one can enter corresponding employee id which data is to be deleted. All the data of the corressponding employee will be deleted from the database. Clicking on "Back" button will take one back to main window.
Here is an image of Delete data window: ![Python_projdelete](https://github.com/user-attachments/assets/4078f026-0c65-4d7b-a7e0-8507c161506d)
                                        ![Python_projdeletedone](https://github.com/user-attachments/assets/df5778ff-0d7b-4f16-9311-9d74b550fce3)

Upon clicking on "Graph" button a graph pops up which is a bar graph representation of top five salaries present in the database with the corresponding employee name. 
Here is an image of Graph window based on availale data:![Python_projgraph](https://github.com/user-attachments/assets/b573aba3-9586-4f53-bb2c-139b37306b47)

#Prerequisites:------------------------------------------------------------------------------------
Needs installation of Python software of suitable version.
Needs installation of matplotlib, pandas in the system.
