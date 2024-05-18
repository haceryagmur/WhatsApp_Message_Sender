import pywhatkit 

# contact
phone_number = input("Enter phone number: ")
pywhatkit.sendwhatmsg(phone_number, "Test", 1, 00, 15, True, 3) # also closes the tab


# group
group_id = input("Enter group id: ")
pywhatkit.sendwhatmsg_to_group(group_id, "Test Group", 1, 00)




