N = int(input())

person = []
ageList = []
nameList = []

answerPerson = []

for i in range(0, N):
    age, name = map(str, input().split())
    age = int(age)
    person.append([age, name, i])

sortedPerson = sorted(person, key=lambda x:(x[0], x[2]))

for i in range(0, N):
    answerPerson.append([sortedPerson[i][0], sortedPerson[i][1]])

for i in range(0, N):
    print(answerPerson[i][0], answerPerson[i][1])