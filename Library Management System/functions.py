################################### problem analysis ###############################

# add book
# list of books -> add books 
# books = ['book1', 'book2', 'book3'] # unique
# any change here -> availbale books

# register a member
# dictionary of members -> add members
# members = {ID:'name', ID:'name'} # ID : national ID 
# members = {1:'mohamed', 2:'ali', 3:'mostafa'} 

# members_details -> borrowed books and returned books -> processes : borrow and retrun 
# member_details = { 'id_name':{borrowed:[book1, book2], return:[book2]} }  -> dictioanry has key[name], value: dictionary of list
# member_details = { '1_mohamed':{borrowed:[book1, book2], return:[book2]} }

# in case of reports -> showing borrowed books, available books, and member details.
# borrowed_books = ['book1']
# available_books = ['book2', 'book3'] # include the rest books in this list 
# just print member details

# process of borrow and return 
# add book -> avialble books -> add 
# borrow book -> available books -> remove
# return book -> availble books -> add

###############################################################

# Data structures
books = list()
borrowed_books = list()
available_books = list()
members = dict()
members_details = dict()

# Functions 

# add book
def add_book(book_name:str):
    # check if the book name already exists or not
    if book_name not in books:
        # add the new book to the books of the library
        books.append(book_name)
        # add the new book to the avialble books that can be borrowed
        available_books.append(book_name)
        return True
    else:
        return False


# register a memeber
def register_member(member_id:str, member_name:str):
    # check if the id of the member is already exist or not
    if member_id not in members:
        # add the new member to the member list
        members[member_id] = member_name
        # add the new member to the member_details dictionary to track its transaction
        members_details[f'{member_id}_{member_name}'] = {'borrowed':list(), 'returned':list()}
        return True
    else:
        return False

# borrow a book 
def borrow_book(member_id:str, member_name:str, book_name:str):
    # check if the book is actually found in the system of the library
    if book_name not in books:
        print('The borrowing process failed.')
        print(f'{book_name} is not on the system.')
        print(f'Books on the system = {books}')
    # check if the book is avilable or not
    elif book_name not in available_books:
        print('The borrowing process failed.')
        print(f'{book_name} is on the system, but not available right now.')
        print(f'Available Books to be borrowed = {available_books}')
    # check if the name and id of the member are found
    elif (member_id not in members) or (member_name != members[member_id]):
        print('The borrowing process failed.')
        print(f'Member ID or Member name or both is incorrect.')
    # all is good
    else:
        # remove from the available books
        available_books.remove(book_name)
        # add to the borrowed books
        borrowed_books.append(book_name)
        # add the process to the member details -> transaction
        # member_details = { '1_mohamed':{borrowed:[book1, book2], return:[book2]} }
        members_details[f'{member_id}_{member_name}']['borrowed'].append(book_name)
        return True

# return a book : book_name on the system? / book_name from the borrowed books? / name? / id? [any damage he will responsible for, clear transactions]
def return_book(member_id:str, member_name:str, book_name:str):
    # check if the book on the system
    if book_name not in books:
        print('The returning process failed.')
        print(f"{book_name} is not recorded on the system at all. So, We can't receive this book.")
        print(f'Books on the system = {books}')
    # check if the book is borrowed or not
    elif book_name not in borrowed_books:
        print('The returning process failed.')
        print(f"{book_name} is not borrowed from any one. So, We can't receive this book.")
        print(f'Borrowed books on the system = {borrowed_books}')

    # check if it is the same member that borrow the book
    elif (member_id not in members) or (member_name != members[member_id]):
        print('The returning process failed.')
        print(f'Member ID or Member name or both is in correct.')
    
    elif book_name not in members_details[f'{member_id}_{member_name}']['borrowed']:
        print('The returning process failed.')
        print('The same member has to retrun the book.')
    # all is good
    else:
        # remove the book from the borrowed_books
        borrowed_books.remove(book_name)
        # add the book to the available books
        available_books.append(book_name)
        # record this transcation in the member details
        members_details[f'{member_id}_{member_name}']['returned'].append(book_name)
        return True
    
# generate report
def generate_report():
    print(f' - Books on the system = {books}')
    print(f' - Borrowed books = {borrowed_books}')
    print(f' - Available books = {available_books}')
    print(' - Member details :')
    for i in members_details:
        print('\t', '-', i, ' -> ', members_details[i])

# # function to check if the input is integer or not -> true / false
# def to_integer(x:str):
#     if x.isdecimal() == True:
#        x = int(x)
#        return x
#     else:
#         return 'Invalid Input, Expected integer value'



# add_book('book1')
# add_book('book2')
# add_book('book3')
# print(books)

# register_member('1', 'mohamed')
# register_member('2', 'mohamed')
# register_member('3', 'ali')
# register_member('3', 'mahmoud')
# print(members)

# print(f'before borrow available_books = {available_books}')
# print(f'before borrow borrowed_books = {borrowed_books}')
# borrow_book('1', 'mohamed', 'book1')
# borrow_book('2', 'mohamed', 'book2')
# borrow_book('3', 'ali', 'book3')
# print(f'after borrow available_books = {available_books}')
# print(f'after borrow borrowed_books = {borrowed_books}')
# print(members_details)


# print(f'before return available_books = {available_books}')
# print(f'before return borrowed_books = {borrowed_books}')
# # return_book('1', 'mohamed', 'book1')
# return_book('2', 'mohamed', 'book2')
# return_book('1', 'mohamed', 'book3')
# print(f'after return available_books = {available_books}')
# print(f'after return borrowed_books = {borrowed_books}')
# print(members_details)
# borrow_book('3', 'ali', 'book1')


# generate_report()






