# import pprint
# from pprint import pprint
# student_data = {
#     'name': 'Gentle Inyang',
#     'age' : 30,
#     'school': "Heritage polytechinc",
#     'regNo': 23015008
# }
# assign = student_data.copy()
# newlist = {}
# newlist.update(student_data)
#
# pprint(student_data)
# print(student_data['name'], "is ", student_data['age'], "years old")
# student_data.update({"Department ":"computer engineering"})
# pprint(student_data)
# pprint(newlist)
#
#
#
# storage = {}
# def store(**kwargs):
#     tempdict = {}
#     for key,value in kwargs.items():
#         tempdict[key] = value
#     storage.update(tempdict)
# def collectpasskey(name,link):
#     for key, value in storage.items():
#         if name == key and link == value[0]:
#             return value[1]
#
# name = input('Enter name $ ')
# link = input('Enter link_name $')
# password = input('Enter a password $ ')
# storage[name] = [link, password]
# password = collectpasskey('lucy','facebook')
# print(password)
# # file = {}
# file.update(name = [link,password])
# store(**file)

mylist = ['prince', 'value', 'precious', 'prince', 'peace', 'prince', 'precious', 'prince', "lucy"]
new_list = []
for x in mylist:
    if x in new_list:
        continue
    else:
        new_list.append(x)
print(new_list)


