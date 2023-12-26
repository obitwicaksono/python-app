import tkinter as tk

def usd_to_idr():
    angka = textbox.get()
    dollar = float(angka) * 15407
    text.set('Rp' + str(dollar))
    label2.config(font=('helvetica', 20, 'bold'), fg='green')

window = tk.Tk()
window.title('USD TO IDR CONVERTER')
window.geometry('500x180')

label1 = tk.Label(window, text="USD", font=('helvetica', 20, 'bold'))
label1.pack()

textbox = tk.Entry(window, font=('helvetica', 20, 'bold'), width='14', justify=tk.CENTER)
textbox.pack()

btn = tk.Button(window, text='TO', font=('helvetica', 18, 'bold'), command=usd_to_idr)
btn.pack()

text = tk.StringVar()
text.set('IDR')

label2 = tk.Label(window, font=('helvetica', 20, 'bold'), textvariable=text)
label2.pack()

window.mainloop()