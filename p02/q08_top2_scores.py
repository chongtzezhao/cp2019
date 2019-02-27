a = int(input("Enter number of students: "))
class_dict = {}
count = 0
while count<a:
    score = eval(input('Enter score: '))
    name = input("Enter name: ")
    class_dict[score]=name
    count += 1

x=[]
for i in class_dict:
    x.append(i)
x.sort(reverse=True)
print("Student with highest score: " + class_dict.get(x[0]))
print("Student with second highest score: " + class_dict.get(x[1]))

'''for i in dictList:
x.append(int(i))
x.sort()
largest = x[-1]
print('Number One: {}'.format(class_list[str(largest)]))
second = x[-2]
print('Number Two: {}'.format(class_list[str(second)]))

s
Send a message'''

