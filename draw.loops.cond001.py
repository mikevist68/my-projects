import turtle
t = turtle.Pen()

t.color('blue','green')
t.begin_fill()

count = 0

#draw a star
for x in range(1,9):
    t.forward(300)
    t.left(225)
    count = count+1
    print("Count is: " + str(count))

    #stop drawing after 8 loops
    if count > 7 and count < 9:
    #if count > 7:
        print("the star pattern is complete!")
        break

    

t.end_fill()
print("A star is born!")
