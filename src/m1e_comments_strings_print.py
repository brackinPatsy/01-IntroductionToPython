###############################################################################
#
#   Do this WITH YOUR INSTRUCTOR (live in class):
#
#   Read the code below.  Predict (in your head)
#   what will get printed (i.e., displayed) when the code runs.
#
#   Then run this module by right clicking anywhere in this window
#   and then selecting:
#        Run 'name of file'
#   (i.e.  Run 'm1e_comments_strings...')  Or, use the Windows keyboard
#   shortcut:  Control + Shift + Function-F10.  (That is, hold the
#   Control, Shift and Function keys down and press the F10 key.)
#
#   Confirm that you see the output in the  "Run"  window that appears.
#   Confirm that the output is what you expected, asking questions as desired.
#
#   This module is just an example (m1e, note the 'e').
#   After you have read and run the code,
#   feel free to play with it briefly, then move on to m2.
#
###############################################################################


print('Hello, Brackin')
print('hi there')
print('one', 'two', 'buckle my shoe')

print(3 + 9)
print('3 + 9', 'versus', 3 + 9)

def mystery(x,y):
    result = (x+y)/(y-x)
    return result

print('mystery 2,3 =',mystery(2,3))
print('mystery 3,2 = ',mystery(3,2))
print('mystery -1,3 = ',mystery(-1,3))

def countEvans(n):
    count = 0
    for k in range(n):
        # the % sign means "take the remainder"
        if k % 2 == 0:
            count = count +1
        print(k, count)
    return count

def countOdds(n):
    count = 0
    for k in range(n):
        # the % sign means "take the remainder"
        if k % 2 != 0:
            count = count +1
        print(k, count)
    return count

def printOdds(n):
    for k in range(n):
        # the % sign means "take the remainder"
        if k % 2 != 0:
            print(k)

def fastprintOdds(n):
    for k in range(1,n,2):
        print(k)

print(countEvans(5))
print(countOdds(5))
printOdds(5)
fastprintOdds(5)
