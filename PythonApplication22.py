a=int(input("정수를 입력하시오. "))

if(a<0):
    print("음수입니다. ", a, "입니다. ", sep="")
elif(a==0):
    print("0입니다. ")
else:
    print("양수입니다. ", a, "입니다. ", sep="")
