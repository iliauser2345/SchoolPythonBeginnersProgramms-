print("--------------------------------------------")
print("What kind of problem you wish to solve?")
print("[1]Precentage of a amount")
print("[2]Amount which is a percentage of a nubmer")
print("[3]Growth per certain percentage")
print("[4]Decline per certain percentage")
print("[5]Growth from one amount to another")
print("[6]Decline from one amount to another")
print("[7] Growth by certain percentage")
print("[8]Decline by certain percentage")
choice=int(input("your choice(nubmer)>>>"))

def calculate_choice_1():
    origin_number=int(input("Your origin number>>>"))
    percentage=int(input("percentage(no %)>>>"))*0.01
    print("result", int(origin_number*percentage), "is", int(percentage/0.01),"% of", origin_number)
    quit()

def calculate_choice_2():
    origin_number=int(input("Your origin number>>>"))
    result=int(input("Your result number>>>"))
    print(int(result/origin_number*100),"% of",origin_number, "is", result)
    quit()

def calculate_choice_3():
    origin_number=int(input("Your origin number>>>"))
    percentage=(int(input("Growth percentage(no %)>>>"))*0.01)+1.0
    print(origin_number, "has grown by",int((percentage-1.0)*100),"%","to",int(origin_number*percentage))
    quit()

def calculate_choice_4():
    origin_number=int(input("Your origin number>>>"))
    percentage=1.0-(int(input("Decline percentage(no %)>>>"))*0.01)
    print(origin_number, "has decline by",int((percentage-1.0)*100),"%","to",int(origin_number*percentage))
    quit()

def calculate_choice_5():
    origin_number=int(input("Your origin number>>>"))
    result=int(input("Your result number>>>"))
    print(origin_number,"has grown to", result, "by",int(((result/origin_number)-1.0)*100),"%")
    quit()

def calculate_choice_6():
    origin_number=int(input("Your origin number>>>"))
    result=int(input("Your result number>>>"))
    print(origin_number,"has declined to", result, "by",int(((result/origin_number-1.0)*-1)*100),"%")
    quit()

def calculate_choice_7():
    result=int(input("Your result number>>>"))
    percentage=int(input("Growth percentage>>>"))
    print(int(result*((percentage*0.01)+1.0)),"has grown by", percentage,"% to",result)
    quit()

def calculate_choice_8():
    result=int(input("Your result number>>>"))
    percentage=int(input("Decline percentage>>>"))
    print(int(result*((percentage*0.01)+1.0)),"has declined by",percentage,"% to",result)
    quit()

selector=[
    calculate_choice_1,
    calculate_choice_2,
    calculate_choice_3,
    calculate_choice_4,
    calculate_choice_5,
    calculate_choice_6,
    calculate_choice_7,
    calculate_choice_8
]
selector[choice-1]()
