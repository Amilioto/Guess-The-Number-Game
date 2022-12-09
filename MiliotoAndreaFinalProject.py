#Guess the number game 
#Created by: Andrea Milioto 
#Using Python with Tkinter, Pillow, and Random imports 
#Finished on December 9th, 2022


#Imports
from tkinter import * 
import random
from PIL import Image, ImageTk


#Initializations

root = Tk()
root.title('Guess the number game!')
root.geometry('1500x900')
root.iconbitmap(r'icon.ico')


#Attempts counter
attempts = 0   #Track how many times the user compares their answer to the Hidden variable


#Hidden number generator function
def innit_Hidden_Number():
    global hiddenNumber
    hiddenNumber = random.randint(1, 100)   #Main variable that, once created, is the objective of the game for the user to reach 
    return hiddenNumber 
innit_Hidden_Number()


#displayed number generator function
def innit_Displayed_Number():
    global displayedNumber
    displayedNumber = random.randint(1, 100)   #Main number presented to user that may be changed in order to play the game
    return displayedNumber
innit_Displayed_Number()


#Clear Label Function - Used with other functions throughout the program to clear the answer label for de-cluttering
def clear_Label():
    answerLabel.config(text='')


#Framing for widgets - Establish basic framing for grid posiitioning of widgets that may use .pack() function
buttonframe = Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)


#Main window Images
image = Image.open("numbers.png")
imageNew = ImageTk.PhotoImage(image)

imageLabel = Label(root, image=imageNew)
imageLabel.pack(pady=10)


#Title label text

title_Label = Label(root, text='Use the buttons below to change and compare the number you see to a mystery number generated randomly from 1 to 100!', font=('Ariel', 16))
title_Label.pack(padx=20, pady=20)

#Generated number label

generated_number_Label = Label(root, text=displayedNumber, font=('Ariel', 26))
generated_number_Label.pack(padx=20, pady=20)


#~~~~~~~~~~~~Second Window~~~~~~~~~~~~


def Second_Window():
    #Second window initializations
    second = Toplevel()
    second.title('Congratulations!')
    second.geometry('900x600')
    second.iconbitmap(r'icon.ico')

    #Main end screen label using 'attempts' variable
    endinglabel = Label(second, text='Congrats you won! It took you '+ str(attempts) + ' tries to guess the correct the number.', font=('Ariel', 20))
    endinglabel.pack()
    

    #Images for second window, opening and resizing functions used
    global secondImage
    global newPic
    secondImage = Image.open('ranking.png')

    resized = secondImage.resize((256, 256), Image.ANTIALIAS)

    newPic = ImageTk.PhotoImage(resized)
    
    imageLabel = Label(second, image=newPic).pack()

    #Restart button and function in second window 
    def Restart_Button_Second():
        global reset_displayed_number
        reset_displayed_number()
        second.destroy()


    restartButton = Button(second, text='Restart game!', font=('Ariel', 20), command=Restart_Button_Second)
    restartButton.pack()
    

    #Exit button and function in second window 
    def Exit_Action_Second():
        second.destroy()
        global root
        root.destroy()

    
    exitButton = Button(second, text='Exit program', font=('Ariel', 15), command=Exit_Action_Second)
    exitButton.pack()



#~~~~~~~~~~~~~Buttons~~~~~~~~~~~~~~~

#~~~~Increase Displayed Number buttons and respective functions 

#Increase Displayed number by 1
def Button_plus1():
    global displayedNumber
    if displayedNumber <= 99:
        displayedNumber = displayedNumber + 1
        generated_number_Label.config(text=displayedNumber)
    else:
        answerLabel.config(text='Cannot have numbers greater than 100!', font=('Ariel', 15))
        answerLabel.after(2000, clear_Label)

#Increase Displayed number by 5
def Button_plus5():
    global displayedNumber
    if displayedNumber <= 95:
        displayedNumber = displayedNumber + 5
        generated_number_Label.config(text=displayedNumber)
    else:
        answerLabel.config(text='Cannot have numbers greater than 100!', font=('Ariel', 15))
        answerLabel.after(2000, clear_Label)

#Increase Displayed number by 10
def Button_plus10():
    global displayedNumber
    if displayedNumber <= 90:
        displayedNumber = displayedNumber + 10
        generated_number_Label.config(text=displayedNumber)
    else:
        answerLabel.config(text='Cannot have numbers greater than 100!', font=('Ariel', 15))
        answerLabel.after(2000, clear_Label)

#Increment raise Buttons 
def higher_button1():
    higherButton = Button(buttonframe, text='+1', font=('Ariel', 15), command=Button_plus1)
    higherButton.grid(row=2, column=0, sticky=W + E)
higher_button1()

def higher_button5():
    higherButton = Button(buttonframe, text='+5', font=('Ariel', 15), command=Button_plus5)
    higherButton.grid(row=2, column=1, sticky=W + E)
higher_button5()

def higher_button10():
    higherButton = Button(buttonframe, text='+10', font=('Ariel', 15), command=Button_plus10)
    higherButton.grid(row=2, column=2, sticky=W + E)
higher_button10()


#~~~~Check Button and respective functions 

#Initial creation of answer label 
answerLabel = Label(buttonframe, text='')
answerLabel.grid(row=5, column=1, pady=10)

#Check Displayed number function
def check_number():
    global hiddenNumber
    global attempts
    attempts = attempts + 1
    
    if displayedNumber == hiddenNumber:
        answerLabel.config(text='Correct!', font=('Ariel', 15))
        Second_Window()
            
            
    elif displayedNumber > hiddenNumber:
        answerLabel.config(text='Incorrect! Too high!', font=('Ariel', 15))
           
    else:
        answerLabel.config(text='Incorrect! Too low!', font=('Ariel', 15))

    answerLabel.after(2000, clear_Label)

#Check number button creation
def check_button():
    checkButton = Button(buttonframe, text='Check', font=('Ariel', 15), command=check_number)
    checkButton.grid(row=4, column=1, sticky=W+E, pady=10)  
check_button()


#~~~~Lower buttons and functions 

#Decrease Displayed number by 1
def Button_minus1():
    global displayedNumber
    if displayedNumber >= 1:
        displayedNumber = displayedNumber - 1
        generated_number_Label.config(text=displayedNumber)
    else:
        answerLabel.config(text='Cannot have negative numbers!', font=('Ariel', 15))
        answerLabel.after(2000, clear_Label)

#Decrease Displayed number by 5
def Button_minus5():
    global displayedNumber
    if displayedNumber >= 5:
        displayedNumber = displayedNumber - 5
        generated_number_Label.config(text=displayedNumber)
    else:
        answerLabel.config(text='Cannot have negative numbers!', font=('Ariel', 15))
        answerLabel.after(2000, clear_Label)

#Decrease Displayed number by 10
def Button_minus10():
    global displayedNumber
    if displayedNumber >= 10:
        displayedNumber = displayedNumber - 10
        generated_number_Label.config(text=displayedNumber)
    else:
        answerLabel.config(text='Cannot have negative numbers!', font=('Ariel', 15))
        answerLabel.after(2000, clear_Label)


#Increment Lower Buttons
def lower_button1():
    lowerButton = Button(buttonframe, text='-1', font=('Ariel', 15), command=Button_minus1)
    lowerButton.grid(row=3, column=0, sticky=W + E)
lower_button1()

def lower_button5():
    lowerButton = Button(buttonframe, text='-5', font=('Ariel', 15), command=Button_minus5)
    lowerButton.grid(row=3, column=1, sticky=W + E)
lower_button5()

def lower_button10():
    lowerButton = Button(buttonframe, text='-10', font=('Ariel', 15), command= Button_minus10)
    lowerButton.grid(row=3, column=2, sticky=W + E)
lower_button10()



#reset button and function

def reset_displayed_number():
    global attempts
    attempts = 0
    innit_Hidden_Number()
    innit_Displayed_Number()
    generated_number_Label.config(text=displayedNumber)

def reset_button():
    resetButton = Button(buttonframe, text='Reset', font=('Ariel', 15), command=reset_displayed_number)
    resetButton.grid(row=6, column=1, pady=20)
reset_button()


#Exit Button and function 

exitButton = Button(buttonframe, text='Exit program', font=('Ariel', 20), command=root.quit)
exitButton.grid(row=10, column=1)


#Frame pack and main window function call

buttonframe.pack(fill = 'x')
root.mainloop()