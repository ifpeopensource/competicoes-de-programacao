total_people, total_meets = [int(value) for value in input().split()]
infected, infected_first_meet = [int(value) for value in input().split()]

infected_list = [infected]

for meet in range(1, total_meets + 1):
    atendees = [int(value) for value in input().split()]
    atendees = atendees[1:]
    if (meet < infected_first_meet):
        continue

    contamined = False
    for infected in infected_list:
        if infected in atendees:
            contamined = True
    
    if contamined:
        for atendee in atendees:
            if atendee not in infected_list:
                infected_list.append(atendee)
    
print(len(infected_list))



