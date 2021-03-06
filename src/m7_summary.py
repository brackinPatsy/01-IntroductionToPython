"""
An exercise that summarizes what you have learned in this Session.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Patsy.
"""
########################################################################
# done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
#
# done: 2.
#   Write code that accomplishes the following (and ONLY the following),
#   in the order listed:
#
#    - Constructs a SimpleTurtle with a  'blue'  Pen.
#
#    - Makes the SimpleTurtle go straight UP 200 pixels.
#
#    - Makes the SimpleTurtle lift its pen UP
#         (so that the next movements do NOT leave a "trail")
#         HINT: Use the "dot trick" to figure out how to do this.
#
#    - Makes the SimpleTurtle go to the Point at (100, -40).
#
#    - Makes the SimpleTurtle put its pen DOWN
#         (so that the next movements will return to leaving a "trail").
#
#    - Makes the SimpleTurtle's pen have color 'green' and thickness 10.
#
#    - Makes the SimpleTurtle go 150 pixels straight DOWN.
#
#   Don't forget to:
#     - import rosegraphics and construct a TurtleWindow
#          at the BEGINNING of your code, and to
#     - ask your TurtleWindow to   close_on_mouse_click
#          as the LAST line of your code.
#   See the beginning and end of m4e_loopy_turtles for an example.
#
#   As always, test by running the module.
#   As always, COMMIT-and-PUSH when you are done with this module.
#
########################################################################
#answers to quiz 2
import rosegraphics as rg
window = rg.TurtleWindow()
window.delay(20)
nadia=rg.SimpleTurtle
import math
x = 4 + 8
print(x)
x = (4 + 2) * 3
print(x)
x = 42**(1./3.)
print(x)
x = 42**(1/3)
print(x)
x=42**(0.3333333)
print(x)
x =15.
x = x+5.0
x=x*3
print(type(x))
print(x)
x = 52
print(type(x))
x = -27.235
print(type(x))
x =  x + 10
print(type(x))
x ='hello'*3
print(type(x))
print(x)
p =math.pi
print(p)

def main():
    a=alpha()
    print()
    b = beta()
    print()
    g = gamma()
    print()
    print('main!',a,b,g)

def alpha():
    print('Alpha!')
    return 7

def beta():
    print('Beta')
    return 15 +alpha()

def gamma():
    print('Gamma!', alpha(),beta())
    return alpha() + beta() +alpha()
main()