from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("Project 146")
enter_number = Entry(root)
label_series = Label(root, text = "Fibonacci Series")
label_sum = Label(root, text = "Fibonacci Sum")

def fibonacci() :
    input_num = int(enter_no.get())
    first_number = 0
    second_number = 1
    sum = 0
    counter = 1
    sum_2 = 0
    
    while(counter <= input_num) :
        label_series["text"] += str(sum) + " "
        label_sum["text"] += "Fibonacci Sum = " + str(sum_2)
        counter += 1
        first_number = second_number
        second_number = sum
        sum = first_number + second_number
        sum_2 = sum_2 + sum
        
btn = Button(root, text = "Fibonacci Series", command = fibonacci)
enter_number.pack()
label_series.pack()
label_sum.pack()
btn.pack()
root.mainloop()