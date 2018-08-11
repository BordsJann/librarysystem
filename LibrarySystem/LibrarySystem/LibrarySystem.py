import sys
import peewee
import database_mgr

import functions
from functions import *;
from peewee import *
from database_mgr import *

action = functions
dbMgr = database_mgr

print ("""							  		
	 	Welcome to Python Library System.
	  	a To add a book
	  	b To add a member
	  	c To allocate a book
	 	d To return a book
	 	e To remove a book from the collection
	  	f To remove a member from the book
	 """)

user_option = input('Enter your choice now:')
user_option = user_option.lower()


if user_option == 'a':
	action.add_book()

elif user_option == 'b':
	action.add_member();
	
elif user_option == 'c':
	action.allocate()
	
elif user_option == 'd':
	action.de_allocate()
	
elif user_option == 'e':
	action.remove_book()
	
elif user_option == 'f':
	action.remove_member()
else:
	action.print("Invalid choice")

if __name__ == '__main__':
	dbMgr.initialize_db()

