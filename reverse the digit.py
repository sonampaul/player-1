def reverse_integer(x);
sign=-1 if x<0 else 1
x*=sign
while x;
if x%10==0;
x/=10
else:
	break
x=str(x)
1st=list(x)
1st.reverse()
x="".join(1st)
x=int(x)
return sign**
print(reverse_integer(234))
print(reverse_integer(-234))