from turtle import *
import pickle
import keyboard as key
import os
# when the input function used turtle window is minimised so this func is used
def bring_turtle_to_front():
    
    Screen()._root.attributes('-topmost', True)
    Screen()._root.attributes('-topmost', False)


'''These boolan value are used to track the previous key press value.
These are updated in further program according to the keypressed
'''
up_tap=False
down_tap=False
left_tap=False
right_tap=True

steps=[]
print('\nThe drawings can be made using the navigation key on your keyboard like left, right, up and down')
a=input('Enter:\n1. To load the data\n2. To create data\n')


if a=='2':
    filename=input("Enter a filename: ")
    #The forward of 0.001 is used to just start the window of turtle
    forward(0.001)
    #The speed is used further as a parameter in forward
    speed=5
    
    bring_turtle_to_front()
    while True:
        #steps[] is used to record the steps
        if key.is_pressed('left'):
            ''' The circle is used to rotate the pen of the turtle.
             The angles of the circle is adjusted to rotate the pen such that when left key(or any other keys used in program) is pressed the pen points left(or the key specified) irrespective of the previous key'''
            if right_tap:
                circle(0,180) 
                steps.append(['c',180])
                
            elif up_tap:
                circle(0,90)
                steps.append(['c',90])
                
            elif down_tap:
                circle(0,-90)   
                steps.append(['c',-90])
                
            
            
            right_tap=False
            left_tap=True
            up_tap=False
            down_tap=False 
            
            forward(speed)
            steps.append(['f',speed]) 

        elif key.is_pressed('right'):
            
            if up_tap:
                circle(0,-90)
                steps.append(['c',-90])
                
            elif down_tap:
                circle(0,90)
                steps.append(['c',90])
                
            elif left_tap:
                circle(0,180) 
                steps.append(['c',180])
                
            
            right_tap=True
            left_tap=False
            up_tap=False
            down_tap=False
            
            forward(speed)
            steps.append(['f',speed])    
        
        elif key.is_pressed('up'):
            if down_tap:
                circle(0,180)
                steps.append(['c',180])
                
            elif right_tap:
                circle(0,90)
                steps.append(['c',90])
                
            elif left_tap:
                circle(0,-90)  
                steps.append(['c',-90])
                
            

            up_tap=True
            right_tap=False
            left_tap=False
            down_tap=False
            forward(speed)
            steps.append(['f',speed])

        elif key.is_pressed('down'):
            if up_tap:
                circle(0,180)
                steps.append(['c',180])
                
            elif left_tap:
                circle(0,90)
                steps.append(['c',90])
                
            elif right_tap:
                circle(0,-90) 
                steps.append(['c',-90])
                
                
            up_tap=False
            right_tap=False
            left_tap=False 
            down_tap=True
            
            
            forward(speed)
            steps.append(['f',speed]) 
        
        elif key.is_pressed('enter'):
            break 
        
        
    
    
    with open(f'{filename}.dat','wb') as file:
        pickle.dump(steps,file)
    print('File saved\n')
elif a=='1':
    
    # Gets all the files in the directory with extension .dat
    files=[file for file in os.listdir() if file.endswith('.dat')]
    i=0
    if len(files) !=0:
        print("\nSelct your files among these:")
        while i<len(files):
            print(f'{i+1}. {files[i].rsplit(".",1)[0]}') # prints the files without extension
            i+=1
        selected_file=int(input(""))

        with open(files[selected_file-1],'rb') as file: # Takes the selected file and loads
            a=pickle.load(file)
            

        bring_turtle_to_front()
        for i,j in a: # 'a' is a multi-dimensional array so i,j are used
            if i == 'f':
                forward(j)
            elif i=='c':
                circle(0,j)
        
        input('Press Enter to close') # The file waits till the enter is pressed and doesn't close immediately
    
    else:
        print("No drawings present. First create some drawings")

        
