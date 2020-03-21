class Student:
    roll_no = 0;
    name = "";
    age = 0
    total_mark = 0
    def __init__(self,roll_no,name,age,total_mark):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.total_mark = total_mark
    def display(self):
        print(self.roll_no," ",self.name," ",self.age," ",self.total_mark);
    def __eq__(self,other):
        if(self.total_mark == other.total_mark):
            print(self.roll_no," ",self.name," ",self.age," ",self.total_mark);
            print(other.roll_no," ",other.name," ",other.age," ",other.total_mark);
        
            
N = int(input("Enter Total Number of Students: "))
my_student=[];
i=0;
roll_no = 0;
name = "";
age = 0
total_mark = 0
while(i<N):
    roll_no = int(input("Enter Roll_No"))
    name = input("Enter Name");
    age = int(input("Enter Age"))
    total_mark = int(input("Enter Total Mark"))
    my_student.append(Student(roll_no,name,age,total_mark));
    i = i+1;

i=0;
j=0;
flag = 0;
while(i<N):
    j=i+1;
    while(j<N):
        if(my_student[i] == my_student[j]):
            flag = 1;            
        j = j+1;
    i=i+1;
    #print(flag)
    flag = flag

print("Thank You");

