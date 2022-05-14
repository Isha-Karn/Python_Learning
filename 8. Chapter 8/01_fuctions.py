def percent(marks):
    p= ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p

marks1= [45,65,45,78]
percentage1= percent(marks1)

marks2= [55,35,65,97]
percentage2= percent(marks2)
print(percentage1, percentage2) 