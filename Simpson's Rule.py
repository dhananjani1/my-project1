#Question 01 part 04
#Python implementation of Simpson's 1/3 Rule
#To obtain the total profit of the beverage company over the nine-month period
def Simpsons(x,y):
   #to find the value of h
   h = (x[-1]-x[0])/(len(x)-1) 
   Sum = y[0]+y[-1]
   
   #to apply Simpson’s 1/3 Rule formula
   for i ,val in enumerate(y[1:-1]) :
      if i%2 ==0:
         Sum = Sum + 4.0*val   #for odd numbers
      else:
         Sum = Sum + 2.0*val   #for even numbers

   #to get the final answer
   S = (h/3)*Sum
   print("The total profit of the company over 9 month period is",round(S*1000,1),"in dollars.")

#Driver code
x = (1,2,3,4,5,6,7,8,9)
y = (3.1,4.4,6.4,6.6,5.9,5.6,5.1,4.9,4.6)
Simpsons(x,y)















