import database_mgr
from database_mgr import Book
from database_mgr import Member
from database_mgr import Issue_History


dbMgr = database_mgr

def add_book():																	#func to enter a new book
	book_title = input('Enter the book title: ')
	book_author = input('Enter the book author: ')
	book_publication = input('Enter the book publication: ')
	book_pub_year = input('Enter the year of publication of book: ')
	book_isbn = input('Enter the ISBN code of book: ')
	#book_no = number of books having same ISBN
	

def add_book_to_db(comment, TableName=Book):									#func to actually save books to db
	book_data = book(title=book_title,
						author=book_author,
						publication=book_publication,
						pub_year=book_pub_year,
						isbn=book_isbn,
						current_status=current_status)
	book_data.save()


def add_member():																#func to add a new member
	user_id = input('Enter the user_id: ')
	member_name = input('Enter the member name: ')
	member_phone_no = input('Enter the phone number of the member: ')

def add_member_to_db(TableName=Member):								#func to actually save a new member to db
	member_data = book(user_id=user_id,
						name=member_name,
						phone_no=member_phone_no)
	member_data.save()


def allocate():																	#func to allocate a book
	alloc_book_isbn = input('Enter book isbn to be allocated: ')
	#check alloc_book_id with actual book id in database
	if alloc_book_id in book_isbn:
		alloc_member_id = input('Enter member id receving the book:')
		#checks if correct user_id is entered
		if alloc_member_id in user_id:
			issue_date = input('Enter issueing date:')
			return_date = input('Enter return date:')
			#checks if date is properly entered or not
			if start_date > return_date:
				print ('Issueing date cannot be after return date')
				#go to line 37
			
			else :
				issue_id = issue_date + user_id + return_date 
				issue_data.save()
				issue.append(sr_no)
				current_status = 'issued'

				print("This is your issue id: {0}").format(issue_id) 
				print('Your return date is: {0}').format(return_date)

		else:
			print ('user_id entered does not exist')
			#go to line line 35
		
	else:
		print ('ISBN entered is not present in the database')
		#go to line 32
	

def save_allocate_to_db(comment, TableName=Issue_History):								#func to save the new allocation data to db
	issue_data = book(user_id=alloc_member_id,
						isbn=alloc_book_isbn,
						issue_id=issue_id,
						issue_date=issue_date,
						return_date=return_date,
						num_of_books=book_no)
	issue_data.save()


def de_allocate():																#func to de-allocate a book
	de_alloc_issue_id = input('Enter the issue id provided to you:')
	#check alloc_book_id with actual book id in database
	if de_alloc_issue_id in issue_data:
		if today_date == return_date in issue_data:
			print ('Book received')
			book_no += 1
			current_status = 'returned'

		elif today_date < return_date:
			overdue_days = return_date - today_date
			fine = 5*overdue_days
			print("Your fine is Rs", fine)
			current_status = 'returned'

		else:
			book_no+= 1
			print ('Thank you for choosing Python Library')

#def update_de_allocate_to_db():
	#function to add returned status to book


def remove_book():																
	check_isbn = input('Enter the ISBN code of the book you want to remove: ')
	
	for check_isbn in book_isbn(1,10):
		#remove book action
		book = book.get(book_isbn == check_isbn)
		book.delete_instance()

		print ('The book',check_isbn,'has been deleted.')
	

def remove_member():															#func to remove member from db
	rem_member_id = input("Enter member's user_id : ")
	# remove member action
	member = member.get(user_id == rem_member_id)
	member.delete_instance()

	print ('Member',rem_member_id,'has been removed.')
