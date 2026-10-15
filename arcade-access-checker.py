#The variables for the person attempting to enter
age = 16
has_ticket = True
is_vip = False
is_banned = False

#The logic rules
can_enter_arcade = age >= 13 and has_ticket and not is_banned
vip_lounge_entry = (is_vip or age > 18) and not is_banned

#Printing in output
print("Can Enter Arcade =", can_enter_arcade)
print("Vip Lounge Entry =", vip_lounge_entry)
