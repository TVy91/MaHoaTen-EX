text = input()
array = text.split()
if len(array) !=3:
    print('Loi')
    quit()
a = None
b = None
c = None
for i in range(0, len(array)):
    if i==0:
        a = float(array[i])
    if i==1:
        b = array[i]
    if i==2:
        c = float(array[i])
if b=='+':
    result=a+c
    formatted_result = "{:.2f}".format(result)
    print(formatted_result)
elif b=='-':
    result=a-c
    formatted_result = "{:.2f}".format(result)
    print(formatted_result)
elif b =='*':
    result= a*c
    formatted_result = "{:.2f}".format(result)
    print(formatted_result)
else:
    if b =='/' and c==0:
        print('Math Error')
    else:
        result= a/c
        formatted_result = "{:.2f}".format(result)
        print(formatted_result)