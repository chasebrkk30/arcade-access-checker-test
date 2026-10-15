#The variables for the person attempting to enter
age = ? #output for person depends on the age inputed into this value
has_ticket = True #output for person depends on ticket holding
is_vip = False #input on this boolean only contributes to var 'vip_louge_entry'
is_banned = False #this kind of explains itself

#The logic rules
can_enter_arcade = age >= 13 and has_ticket and not is_banned
vip_lounge_entry = (is_vip or age > 18) and not is_banned

#Printing in output
print("Can Enter Arcade =", can_enter_arcade)
print("Vip Lounge Entry =", vip_lounge_entry)
