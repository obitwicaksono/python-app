import tkinter as tk

def usd_to_idr():
    angka = textbox.get()
    dollar = float(angka) * 15407
    text.set('Rp' + str(dollar))
    label2.config(font=('helvetica', 20, 'bold'))

window = tk.Tk()
window.title('USD TO IDR CONVERTER')
window.geometry('500x270')
window.resizable(False, False)
window.config(bg="#e5ff61")

column_space = tk.Label(text="", bg="#e5ff61")
column_space.pack()

label1 = tk.Label(window, text="USD", font=('helvetica', 20, 'bold'), bg="#e5ff61")
label1.pack()

column_space = tk.Label(text="", bg="#e5ff61")
column_space.pack()

textbox = tk.Entry(window, font=('helvetica', 20, 'bold'), width='14', justify=tk.CENTER)
textbox.pack()

column_space = tk.Label(text="", bg="#e5ff61")
column_space.pack()

btn = tk.Button(window, text='TO', font=('helvetica', 18, 'bold'), bg="#e5ff61", command=usd_to_idr)
btn.pack()

column_space = tk.Label(text="", bg="#e5ff61")
column_space.pack()

text = tk.StringVar()
text.set('IDR')

label2 = tk.Label(window, font=('helvetica', 20, 'bold'), textvariable=text, bg="#e5ff61")
label2.pack()

window.mainloop()