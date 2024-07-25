from functions import *
import os

while True:
    # list of process
    print('========== Library Management System ==========')
    print('1. Add Book')
    print('2. Register Member')
    print('3. Borrow Book')
    print('4. Return Book')
    print('5. Generate Report')
    print('6. Exit')
    print()

    # choose the process with the number
    process_num = input("Please, Enter the number of the process = ")

    # check if the use input is a number
    if process_num.isdecimal() == False:
        # clear terminal
        os.system('cls')
        print('Error: Please, Enter an integer number.\n')
        continue

    # check if the use input is a number from 1 to 6
    elif int(process_num) not in range(1,7):
        # clear terminal
        os.system('cls')
        print('Error: Please, Choose a number from 1 to 6. \n')
        continue

    # it is number and we choose a process
    else:
        
        # clear terminal
        os.system('cls')
        # add book
        if process_num == '1':
            print('========== Adding a book ==========\n')
            book_name = input("Please, Enter the book name = ")
            print()
            adding_result = add_book(book_name)
            if adding_result == True:
                print(f'{book_name} added sucessfully to the system.')
                print(f'Books on the system = {books}\n')
                input('*** Press any key to return home')
                # clear terminal
                os.system('cls')
            else:
                print('This book is already exist on the system.')
                print(f'Books on the system = {books}\n')
                input('*** Press any key to return home')
                # clear terminal
                os.system('cls')
        
        # register member
        elif process_num == '2':
            print('========== Registering a member ==========\n')
            member_id = input("Please, Enter member id = ")
            member_name = input("Please, Enter member name = ")
            print()
            registering_result = register_member(member_id, member_name)
            if registering_result == True:
                print(f'{member_name} registered sucessfully to the system with the ID {member_id}.')
                print(f'Members on the system = {members}\n')
                input('*** Press any key to return home')
                # clear terminal
                os.system('cls')
            else:
                print('Member ID has to be unique')
                print(f'Members on the system = {members}\n')
                input('*** Press any key to return home')
                # clear terminal
                os.system('cls')

        # borrow book
        elif process_num == '3':
            print('========== borrowing a book ==========\n')
            print(f'Available books = {available_books}\n')
            member_id = input("Please, Enter member id = ")
            member_name = input("Please, Enter member name = ")
            book_name = input("Please, Enter book name = ")
            print()
            borrowing_result = borrow_book(member_id, member_name, book_name)
            if borrowing_result == True:
                print(f'The process of borrowing {book_name} is completed successfully.')
                member_transaction = members_details[f'{member_id}_{member_name}']
                print(f'Your Transactions = {member_transaction}\n')
                input('*** Press any key to return home')
                # clear terminal
                os.system('cls')
            else:
                print()
                input('*** Press any key to return home')
                # clear terminal
                os.system('cls')

        # return book
        elif process_num == '4':
            print('========== Returning a book ==========\n')
            member_id = input("Please, Enter member id = ")
            member_name = input("Please, Enter member name = ")
            book_name = input("Please, Enter book name = ")
            print()
            returning_result = return_book(member_id, member_name, book_name)
            if returning_result == True:
                print(f'The process of returning {book_name} is completed successfully.')
                member_transaction = members_details[f'{member_id}_{member_name}']
                print(f'Your Transactions = {member_transaction}\n')
                input('*** Press any key to return home')
                # clear terminal
                os.system('cls')
            else:
                print()
                input('*** Press any key to return home')
                # clear terminal
                os.system('cls')
        
        # generate report
        elif process_num == '5':
            print('========== Generating a report ==========\n')
            generate_report()
            input('*** Press any key to return home')
            # clear terminal
            os.system('cls')
        
        # Exit 
        else:
            break
