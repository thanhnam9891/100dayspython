import tkinter as tk

#variables
label = 0

def updateLabel():
    #label = "bye world"
    #hello["text"]=label # Subroutine that updates the text in the label
    global label
    number = text.get("1.0","end") # Gets the number from the text box (starting at the first position and going to the end.) and stores in the number variable
    number = int(number) #Casts to an integer. I've done this on a separate line to prevent the line above getting too complex, but you can combine the two.
    label += number # Adds the number from the text box to the one in the label.
    hello["text"] = label

window = tk.Tk()
window.title("Hello World") # Sets the name of the window in the border
window.geometry("300x300") # Sets the size of the window in pixels

#hello = tk.Label(text = label) # Creates a text box
hello = tk.Label(text = label)
hello.grid(row=0,column=1) # Creates a text box
#hello.pack() # 'pack' places the element on the screen

#text = tk.Text(window ,height=1, width = 50)
text = tk.Text(window ,height=1, width = 50)
text.grid(row=1,column=1)
# Three arguments, name of the window to place the text box in, height & width.
#text.pack()

# Creates a button
button = tk.Button(text = "Click me!", command=updateLabel)
button.grid(row=2,column=0)
#button.pack(side=tk.BOTTOM) #add the button to the bottom of the window

#button = tk.Button(text = "Another Button", command = updateLabel)
#button.grid(row=2, column=1)
#button.pack()

tk.mainloop()