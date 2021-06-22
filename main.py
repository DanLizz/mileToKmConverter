import tkinter


def mile_km():
    mile = float(mile_input.get())
    km = mile*1.60934
    km_result.config(text=f"{km}")


window = tkinter.Tk()
window.title("Mile to KM Converter")
window.minsize(width=200, height=100)
window.config(padx=25, pady=25)

mile_input = tkinter.Entry(width=8)
mile_input.grid(column=1, row=0)
mile_label = tkinter.Label(text="Miles")
mile_label.grid(column=2, row=0)
mid_label = tkinter.Label(text="is equal to")
mid_label.grid(column=0, row=1)
km_result = tkinter.Label(text="0")
km_result.grid(column=1, row=1)
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

result = tkinter.Button(text="Calculate", command=mile_km)
result.grid(column=1, row=2)

window.mainloop()
