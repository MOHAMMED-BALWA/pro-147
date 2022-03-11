from tkinter import *
root = Tk()
root.title("ASCII")
root.geometry("400x400")
root.configure(background="lightgreen")

enter_word=Entry(root)
enter_word.place(relx=0.5 , rely=0.2 , anchor=CENTER)

label=Label(root , text="NAME IN ASCII : ", bg="orange" , fg="black")
label1=Label(root , text="ENCRYPTED NAME : ", bg="orange" , fg="black")




def show():
    input_name=enter_word.get()
   

   
    
   
    for letter in input_name:
        asciii = int(ord(letter))
        encrypted = asciii - 1
        label["text"] +=  str(ord(letter))+" "
        label1["text"] +=  str(chr(encrypted))


btn=Button(root, text="SHOW NAME IN ASCII" , command=show , bg="gold" , fg="black"  )
btn.place(relx=0.5 , rely=0.3 , anchor=CENTER)

label.place(relx=0.5 , rely=0.4 , anchor=CENTER)
label1.place(relx=0.5 , rely=0.5 , anchor=CENTER)

root.mainloop()

