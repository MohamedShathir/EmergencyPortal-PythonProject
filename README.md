# EmergencyPortal-PythonProject
This is a project developed for recording the details of students who were admitted to hospital from school. This was made as school project. This project can be used as a basic template for creating similar projects. This project uses Python as front-end development tool and MySQL as back-end development tool. Hope you guys like my project, hit the Star if you like it &lt;3.



Python Setting
~~~~~~~~~~~
Be sure to install these python packages
>>>	pip install matplotlib
>>>	pip install mysql-connector
>>>	pip install pillow
>>>	pip install tk
>>>	pip install messagebox

Current Username - Admin
Current Password - Admin

#TO EDIT THE USERNAME & PASSWORD
	Go to line 14 and change 
>>>	entry1.get() == '<Username>' and entry2.get() == "<Password>":
	entry1.get() == 'Admin' and entry2.get() == 'Admin'

#TO CHANGE THE BACKROUND
	Go to line 266 and paste your image location over there (be sure to use \\)
>>>	load = Image.open("<File Directory>")
	load= Image.open("C:\\Users\\shath\\Desktop\\EmergencyPortal\\Backpic.jpg")
	
	I have provided additional images and an extra icon in the "Extra Pics" Folder
	Install the fonts from the "Fonts" folder

~~~~~~~~~~~
MySQL Setting
~~~~~~~~~~~
Create database named Emergency_Portal and table named PatientData
>>>	create table PatientData(
	e_Eid int(15) primary key,
	e_FN varchar(30) not null,
	e_LN varchar(30) not null,
	e_PH varchar(10) not null,
	cond varchar(10) not null,
	Time_Stamp timestamp);
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Star if you like the project <3
