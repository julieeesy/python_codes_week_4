# Help Desk Ticketing System Prototype
import random

ticketID = 2000

creator = []
email = []
staff = []
desc = []

while True:
    print("Welcome to the Help Desk!\n")
    print("Choose your course of action...")
    print("Ask for help [1]")
    print("Respond to help [2]")

    section_choice = input("Enter choice: ")
    section_choice = section_choice[0]
    section_choice = section_choice.lower()

    match section_choice:
        case "1": # asking for help
            print("\nPrinting Tickets...")

            print(f"Ticket Number: {ticketID}")

            creator = creator.append(ticket_creator)
            ticket_creator = input("Enter Ticket Creator: ")

            staff = staff.append(staff_id)
            staff_id = input("Enter Staff ID [in caps]: ")

            email = email.append(email_add)
            email_add = input("Email Address: ")

            desc = desc.append(description)
            description = input("Description: ")

            # response = input("Response: Not Yet provided")
            print("Response: Not Yet provided")
            print("Ticket status: Open")

        case "2": # responding for help
            print("banana")
        case _:
            break
    break