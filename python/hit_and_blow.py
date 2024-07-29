import random
import tkinter as tk
import tkinter.messagebox as tmsg
#button clicked handler
def ButtonClick():
    #get entry value
    b=editbox1.get*(
    #4 digit number?
    isok=False
    if len(b)!=4:tmsg.showerror("error","please input a four-digit number")
    else:
        kazuok=True
        for i in range(4):
            if not "0"<b<"9":
                tmsg.showerror("error","not number")
                kazuok=False
                break
        if kazuok:isok=True
    if isok:
        #hit
        hit=0
        for i in range(4):if a[i]==int(b[i]):hit+=1
        #blow
        blow=0
        for j in range(4):
            for i in range(4):
                if a[j]!=int(b[j])==a[i]!=int(b[i]):
                    blow+=1
                    break
        #hit==4?
        if hit==4:
            tmsg.showinfo("guess right","Congratulations!You guessed it right!")
            root.destroy()
        else:
            #show hit and blow
            rirekibox.insert(tk.END,b+" /H: "+str(hit)+" B: "+str(blow)+"\n")
#main
#random 4 numbers
a=[random.randint(0,9),
   random.randint(0,9),
   random.randint(0,9),
   random.randint(0,9)]
#make window
root=tk.Tk()
root.geometry("600x400")
root.title("guess number game")
#make game history text box
rirekibox=tk.Text(root,font=("Helvetica",14))
rirekibox.place(x=400,y=0,width=200,height=400)
#make label
label1=tk.Label(root,text="input number",font=("Helvetica",14))
label1.place(x=20,y=20)
#make entry
editbox1=tk.Entry(width=4,font=("Helvetica",28))
editbox1.place(x=120,y=60)
#make button
button1=tk.Button(root,text="confirm",font=("Helvetica",14),command=ButtonClick)
button1.place(x=220,y=60)
#show window
root.mainloop()