# Created by: Scarlett Gao
# Created on: Oct 2017
# Created for: ICS3U
# This program is use for selling egg waffle.

import ui

user_egg_waffle = None
user_ice_cream = None
user_toppings = None

def original_button_touch_up_inside(sender):
    # choose the original egg waffle
	  global user_egg_waffle
	  user_egg_waffle = 5
	  
def matcha_button_touch_up_inside(sender):
	  # choose the matcha egg waffle
	  global user_egg_waffle
	  user_egg_waffle = 6
	  
def vanilla_button_touch_up_inside(sender):
	  # choose the vanilla ice cream
	  global user_ice_cream
	  user_ice_cream = 1.50
	  
def chocolate_button_touch_up_inside(sender):
	  # choose the chocolate ice cream
	  global user_ice_cream
	  user_ice_cream = 2
	  
def strawberry_button_touch_up_inside(sender):
	  # choose the strawberry ice cream
	  global user_ice_cream
	  user_ice_cream = 2.50
	  
def mango_button_touch_up_inside(sender):
	  # choose the mango ice cream
	  global user_ice_cream
	  user_ice_cream = 2.50
	  
def m_and_m_button_touch_up_inside(sender):
	  # choose the M&M topping
	  global user_topping
	  user_topping = 1
	  
def marshmallow_button_touch_up_inside(sender):
	  # choose the marshmallow topping
	  global user_topping
	  user_topping = 1.5
	  
def no_topping_button_touch_up_inside(sender):
	  # choose no topping for egg waffle
	  global user_topping
	  user_topping = 0
	  
def calculate_button_touch_up_inside(sender):
    
    if user_egg_waffle == 5 and user_topping == 0 and user_ice_cream == 2:
        subtotal = user_egg_waffle + user_topping + user_ice_cream
        view['tax_label'].text = 'tax: ' + str(subtotal)
        HST = subtotal*0.13
        view['subtotal_label'].text = 'subtotal: ' + str(HST)
        tax = subtotal*0.13
        view['total_price_label'].text = 'total price: ' + str(tax)
        total_price = subtotal + tax
    elif user_egg_waffle == 6 and user_topping == 1 and user_ice_cream == 2.50:
        subtotal = user_egg_waffle + user_topping + user_ice_cream
        view['tax_label'].text = 'tax: ' + str(subtotal)
        HST = subtotal*0.13
        view['subtotal_label'].text = 'subtotal: ' + str(HST)
        tax = subtotal*0.13
        view['total_price_label'].text = 'total price: ' + str(tax)
        total_price = subtotal + tax
    elif user_egg_waffle == 6 and user_topping == 1.5 and user_ice_cream == 1.5:
        subtotal = user_egg_waffle + user_topping + user_ice_cream
        view['tax_label'].text = 'tax: ' + str(subtotal)
        HST = subtotal*0.13
        view['subtotal_label'].text = 'subtotal: ' + str(HST)
        tax = subtotal*0.13
        view['total_price_label'].text = 'total price: ' + str(tax)
        total_price = subtotal + tax
    elif  user_egg_waffle == 6 and user_topping == 0 and user_ice_cream == 2:
        subtotal = user_egg_waffle + user_topping + user_ice_cream
        view['tax_label'].text = 'tax: ' + str(subtotal)
        HST = subtotal*0.13
        view['subtotal_label'].text = 'subtotal: ' + str(HST)
        tax = subtotal*0.13
        view['total_price_label'].text = 'total price: ' + str(tax)
        total_price = subtotal + tax
      
view = ui.load_view()
view.present('sheet')
