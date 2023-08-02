from tkinter import *

root = Tk()
root.title("Multidimensional Arrays")
root.geometry("500x500")

label = Label(root)

array_1d = ["John", "James", "Thomson"]
print(array_1d[0])

array_2d = [["John", "A"],["James", "B"], ["Thomson", "C"]]
print(array_2d[0][1])

array_3d = [[["John", "A+", "Excellent"],["James", "A", "Very Good"],["Thomson", "B", "Good"]]]
print(array_3d[0][0][2])

array_4d = [[[["John", "A+", "Excellent", "Math"],["James", "A", "Very Good", "Math"]["Thomson", "B", "Good", "Math"]]]]
print(array_4d[0][0][0][3])

def report():
    label["text"] = array_3d[0][1][0] + " got grade " + array_3d[0][1][1] + " and he is doing " + array_3d[0][1][2]
    label["text"] = array_3d[1][1][0] + " got grade " + array_3d[1][1][1] + " and he is doing " + array_3d1[0][1][2]
    label["text"] = array_3d[2][1][0] + " got grade " + array_3d[2][1][1] + " and he is doing " + array_3d[2][1][2]

btn = Button(root, text="Show Report", command=report)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
label.place(relx = 0.5, rely=0.6, anchor = CENTER)

root.mainloop()