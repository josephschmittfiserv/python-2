# define and/or call your methods here:
def ex1():
    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    sort_people(people_list, 'weight', 'sex')
    print(people_list)
    
def sort_people(people, x, y):
    return sorted(people, key=lambda person: (person[x], person[y]))

    
# ex2()
# ex3()
# ex4()
# ex5()
# ex6()
# ex7()
# ex8()
# ex9()
# ex10()

if __name__ == '__main__':
    ex1()