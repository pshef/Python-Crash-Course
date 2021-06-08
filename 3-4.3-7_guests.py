guests = ['person1','person2','person3','person4']
for person in guests:
    print(f"{person.title()}, you are invited to dinner!") 
    
print(f"\n{guests[1].title()} cant' make it anymore, so...")

del guests[1]
guests.insert(1, 'person5')

print("\n")

for person in guests:
    print(f"{person.title()}, you are invited to dinner!")

print(f"\n{guests[0].title()}, {guests[1].title()}, {guests[2].title()}, and {guests[3].title()}, we have found a bigger table! Who should we invite now?")

guests.insert(0, 'person2')
guests.insert(2, 'person6')
guests.append('person7')

print("\n")

for person in guests:
    print(f"{person.title()}, you are invited to dinner!")

print(f"\nSorry {guests[0].title()}, {guests[1].title()}, {guests[2].title()}, {guests[3].title()}, {guests[4].title()}, {guests[5].title()}, and {guests[6].title()}, it looks like the new table won't get here in time so some of you won't be invited after all.")

guests_gone0 = guests.pop()
guests_gone1 = guests.pop()
guests_gone2 = guests.pop()
guests_gone3 = guests.pop()
guests_gone4 = guests.pop()

print("\n" + guests_gone0.title() + ", " + guests_gone1 + ", " + guests_gone2 + ", " + guests_gone3 + ", and " + guests_gone4 + ", I'm sorry to say you're uninvited.")

del guests[0]
del guests[0]

print(guests)

print("As of now, there are " + str(len(guests)) + " guests invited. Good job! This is why you have so many friends.")

# Originally 46 lines of code, after changing to loops it's only 41
