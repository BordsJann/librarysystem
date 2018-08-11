import peewee
from peewee import *;

db = peewee.SqliteDatabase('library.db')

class Book(Model):
    title = CharField()
    author = CharField()
    publication = CharField();
    pub_year = IntegerField()
    isbn = CharField();
    num_of_books = IntegerField()

    class Meta:
        database = db

class Member(Model):
    user_id = IntegerField()
    name = CharField()
    phone_no = CharField()

    class Meta:
        database = db

class Issue_History(Model):														
	user_id = ForeignKeyField(Member, related_name='pets')
	isbn = ForeignKeyField(Book, related_name='library')
	issue_id = CharField()
	issue_date = DateField()
	return_date = DateField()
	current_status = TextField()

	class Meta:
		database = db

def initialize_db():
	db.connect()
	try:
		db.create_tables([Book, Member, Issue_History])
	except OperationalError:
		pass

def deinit():
	db.close()


