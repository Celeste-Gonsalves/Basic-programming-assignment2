#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Write a Python program to convert kilometers to miles?
km=input("Enter kilometres:")
miles= 0.621371192 * int(km)
print(miles,"miles")


# In[8]:


#Write a Python program to convert Celsius to Fahrenheit?
celsius=input("Enter celsius degree:")
far= ((9/5) * float(celsius))+32
print(far)


# In[9]:


#Write a Python program to display calendar?
import calendar
#if we write tuesday the calendar will start with tuesday 
c= calendar.TextCalendar(calendar.SUNDAY)
calendar = c.formatmonth(int(input("Enter the year: ")),int(input("Enter the month number: ")))
print(calendar)


# In[15]:


#Write a Python program to solve quadratic equation?
a=int(input("Enter number:"))
b=int(input("Enter number:"))
c=int(input("Enter number:"))
#to find the roots of the equation
x1= (-b + (b**2-4*a*c)**0.5)/2*a
x2= (-b - (b**2-4*a*c)**0.5)/2*a
print(x1,x2)


# In[20]:


#Write a Python program to swap two variables without temp variable?
a=int(input("Enter number:"))
b=int(input("Enter number:"))
a,b=b,a
print("swap",a)
print("swap",b)

