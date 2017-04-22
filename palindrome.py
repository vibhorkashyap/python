def is_palindrome(n):
    return str(n) == str(n)[::-1]

n = raw_input('Enter a number: ')
if is_palindrome(n):
   print('Congratulations! {0} is a palindrome.'.format(n))
else:
   n1 = n
   n2 = n
   while not is_palindrome(n1):
       n1 = int(n1)+1
   while not is_palindrome(n2):
   		n2 = int(n2)-1

   if int(n) - int(n2) < int(n1) - int(n) :
   		nx = n2
   else:
   		nx = n1
   print('You entered {0}, but the nearest palindrome is {1}'.format(n, nx))