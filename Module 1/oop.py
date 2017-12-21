class myclass:
 sample=0
 w=0
 b=0
 g=0
 o=0
 color_list=['black','white','gray']
 def __init__(self):

   print("What's your name ?")
   myclass.name=input()
   print("What's the color of your car?")
   myclass.color=input()
   myclass.sample=myclass.sample+1

       def check_color(self):
            if myclass.color in myclass.color_list:
               if myclass.color==myclass.color_list[0]:
                   myclass.b=myclass.b+1
                    elif myclass.color==myclass.color_list[1]:
                         myclass.w=myclass.w+1
                             else:
                                 myclass.g=myclass.g+1
                                     else:
                                         myclass.o=myclass.o+1
         def display_result(self):
         print("Hello",myclass.name)         
         print("Total number of black Cars:",myclass.b)
	 print("Total number of white Cars:",myclass.w)
	 print("Total number of gray Cars:",myclass.g)
	 print("Other",myclass.o)
	 print("Sample Size:",myclass.sample)
  var=0
  mylist[]
  while var<4;
  mylist.append(myclass())
  mylist[var].check_color()
  mylist[var].display_result()
  var=var+1
