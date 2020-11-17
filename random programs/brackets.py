import sys
string= "[{(){}]"
open_list=["[", "{", "("]
close_list=["]", "}", ")"]
stack=[]
for i in string:
    if i in open_list:
        stack.append(i)
    elif i in close_list:
        pos=close_list.index(i)
        if ((len(stack)>0) and (open_list[pos] == stack[len(stack) - 1])):
            stack.pop()
        else:
            print("unbalanced")
            sys.exit(0)

print ("Balanced") if len(stack)==0 else print ("Unbalanced")