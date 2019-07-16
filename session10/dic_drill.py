# person = {
#     "name": "PMD",
#     "age": 19,
# }
# print(person)
# if "name" in person:
#     print("name does exist")
# if not "nationality" in person:
#     print("nationality does not exist")   



# salary = []

# p1 = {
#     "name": "huy",
#     "role": "waiter",
#     "hours": 12,
#     "salary/hour": 0.8,
# }
# p2 = {
#     "name": "tung",
#     "role": "cook",
#     "hours": 24,
#     "salary/hour": 1.5, 
# }
# p3 = {
#     "name": "m.duc",
#     "role": "manager",
#     "hours": 20,
#     "salary/hour": 2,
# }

# salary = [p1, p2, p3]


# p4 = {
#     "name": "don",
#     "role": "waitor",
#     "hours": 12,
#     "salary/hour": 0.9
# }
# p5 = {
#     "name": "h.duc",
#     "role": "waitor",
#     "hour": 14,
#     "salary/hour": 0.7,
# }

# salary.append(p4)
# salary.append(p5)

# salary["p1"] ={
#     "name": "huyen",
#     "role": "waitress",
#     "hour": 14,
#     "salary/hour": 1
# }

# # salary.pop()



# print(salary)



            #   ///////////////////////////

question = {
    "question": "How many legs an octopus has:",
    "a": "a: 1",
    "b": "b: 2",
    "c": "c: 4",
    "d": "d: 8" ,
    "answer": "d"
}
for i in question:
    if i != "answer":
        print(question[i])
aws = input("your answer: ")
if aws == question['answer']:
        print("correct")
else:
        print("false")





