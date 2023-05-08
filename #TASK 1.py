#TASK 1

organization_name = input("Enter the full name of the organization: ")

words = organization_name.split()
abbrev = ""
for word in words:
     abbrev += word[0].upper()

print("The abbreviation for", organization_name, "is", abbrev)