#functions with outputs

def format_name(f_name, l_name):
    name = str(f_name).title() + " " + str(l_name).title()
    return name


def format_name2(f_name, l_name):
    first = (f_name).title() 
    last= (l_name).title()
    return f"{first} {last}"

def format_name3(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs."
    first = (f_name).title() 
    last= (l_name).title()
    return f"{first} {last}"

output = format_name("SANmuel", "BonGHanoy")

print(output)