from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

root = Tk()
root.geometry("900x600")
root.title("Rdonalds")

burger = ImageTk.PhotoImage(Image.open ("burger1.png"))

lbl_heading = Label(root, text="Rdonalds", font=("Heventica", 18, "bold"), fg = "orange")
lbl_heading.place(relx=0.1, rely=0.1, anchor=CENTER)

burger_img = Label(root, image=burger)
burger_img.place(relx=0.7, rely=0.5, anchor=CENTER)

lbl_dish = Label(root, text="Dish: ", font=("Arial", 16))
lbl_dish.place(relx=0.12, rely=0.2, anchor=CENTER)

dish = ["Burger", "Iced_Americano"]
drp_dish = ttk.Combobox(root, state="readonly", values=dish)
drp_dish.place(relx=0.25, rely=0.2, anchor=CENTER)

lbl_Add_Ons = Label(root, text="Add-Ons: ", font=("Arial", 16))
lbl_Add_Ons.place(relx=0.12, rely=0.5, anchor=CENTER)

Add_ons = []
drp_add_ons = ttk.Combobox(root, state="readonly", values=Add_ons)
drp_add_ons.place(relx=0.25, rely=0.5, anchor=CENTER)

lbl_result = Label(root, font=("Arial", 17))
lbl_result.place(relx=0.12, rely=0.7, anchor=CENTER)

class parent():
    def __init__(self):
        print("This is parent class")
        
    def menu(dish):
        if dish == "Burger":
            print("\n You can choose following toppings \n Cheese | Jalapenos")
            lst_toppings = ["Cheese", "Jalapenos"]
            drp_add_ons["values"] = lst_toppings
        elif dish == "Iced_Americano":
            print("\n You can choose following toppings \n Chocolate Flavour | Caramel Flavour")
            lst_toppings = ["Chocolate", "Caramel"]
            drp_add_ons["values"] = lst_toppings
        else:
            print("Invalid Option")
            
    def final_amount(dish, add_ons):
        
        if dish == 'Burger' and add_ons == 'Cheese':
            lbl_result['text'] = "Your final price is ₹250"
            
        elif dish == 'Burger' and add_ons == 'Jalapeno':
            lbl_result['text'] = "Your final price is ₹350"
            
        elif dish == 'Iced_Americano' and add_ons == 'Chocolate':
            lbl_result['text'] = "Your final price is ₹250"

        elif dish == 'Iced_Americano' and add_ons == 'Caramel':
            lbl_result['text'] = "Your final price is ₹250"
        
        elif dish == 'Burger':
            lbl_result['text'] = "Your final price is ₹200"
        
        elif dish == 'Iced_Americano':
            lbl_result['text'] = "Your final price is ₹200"
        
class child1(parent):
    def __init__(self, dish):
        self.new_dish = dish
    def get_menu(self):
        new_dish = drp_dish.get()
        parent.menu(self.new_dish)
        
class child2(parent):
    def __init__(self, dish, add_ons):
        self.new_dish = dish
        self.add_ons = add_ons
    def  get_final_amount(self):
        new_dish = drp_dish.get()
        add_ons = drp_add_ons.get()
        parent.final_amount(self.new_dish, self.add_ons)
        
obj1 = child1(drp_dish.get())
obj1.get_menu()

obj2 = child2(drp_dish.get(), drp_add_ons.get())
obj2.get_final_amount()


btn_dish = Button(root, text="Add Dish Name", relief=FLAT, command=obj1.get_menu)
btn_dish.place(relx=0.12, rely=0.4, anchor=CENTER)


btn_Add_ons = Button(root, text="Add Add-Ons Name", relief=FLAT, command=obj2.get_final_amount)
btn_Add_ons.place(relx=0.12, rely=0.6, anchor=CENTER)


root.mainloop()