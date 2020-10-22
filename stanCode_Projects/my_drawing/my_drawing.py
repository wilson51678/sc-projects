"""
File: my_drawing
Name: Wilson Wang
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    Accidentally watched movie 'Minions' on HBO , so I decide to let it join stanCode's class
    """
    window = GWindow(width=800, height=800, title= 'minion')

    # hair
    hair1 = GOval(100,30,x=280,y=120)
    window.add(hair1)

    cover = GOval(100,30,x=280, y=122)
    cover.filled = True
    cover.fill_color = 'white'
    cover.color = 'white'
    window.add(cover)

    hair2 = GOval(100,30,x=380,y=120)
    window.add(hair2)

    cover2 = GOval(100,30,x=380, y=122)
    cover2.filled = True
    cover2.fill_color = 'white'
    cover2.color = 'white'
    window.add(cover2)

    body = GRect(250,300,x=250,y=200)
    body.filled = True
    body.fill_color = 'khaki'
    window.add(body)

    head = GOval(250,140,x=250,y=130)
    head.filled = True
    head.fill_color = 'khaki'
    window.add(head)

    adjust_head = GOval(248,100,x=251,y=160)
    adjust_head.filled = True
    adjust_head.fill_color = 'khaki'
    adjust_head.color = 'khaki'
    window.add(adjust_head)

    r_glass = GOval(120,120,x=260,y=200)
    r_glass.filled = True
    window.add(r_glass)

    l_glass = GOval(120,120,x=370,y=200)
    l_glass.filled = True
    window.add(l_glass)

    r_glass1 = GRect(40,40, x=250,y=230)
    r_glass1.filled = True
    window.add(r_glass1)

    l_glass1 = GRect(40,40, x=460,y=230)
    l_glass1.filled = True
    window.add(l_glass1)

    r_eye = GOval(100,100, x=270, y=210)
    r_eye.filled = True
    r_eye.fill_color = 'white'
    window.add(r_eye)

    l_eye = GOval(100,100, x=380, y=210)
    l_eye.filled = True
    l_eye.fill_color = 'white'
    window.add(l_eye)

    r_inner_eye = GOval(30,30,x=310, y=250)
    r_inner_eye.filled = True
    window.add(r_inner_eye)

    l_inner_eye = GOval(30,30,x=410, y=250)
    l_inner_eye.filled = True
    window.add(l_inner_eye)

    # This start from the mid part of body
    mouth = GOval(100,40, x=323, y=330)
    mouth.filled = True
    window.add(mouth)

    oval1 = GOval(100, 30, x=323, y=330)
    oval1.filled = True
    oval1.fill_color = 'khaki'
    oval1.color = 'khaki'
    window.add(oval1)

    # This start from the bottom part of body
    belly = GOval(250,130,x=250,y=430)
    belly.filled = True
    belly.fill_color = 'steelblue'
    window.add(belly)

    rect2 = GRect(248, 60, x=251, y=430)
    rect2.filled = True
    rect2.fill_color = 'khaki'
    rect2.color = 'khaki'
    window.add(rect2)

    pants = GRect(180, 90, x=285, y=400)
    pants.filled = True
    pants.fill_color = 'steelblue'
    pants.color = 'steelblue'
    window.add(pants)

    l_sling = GRect(60, 30, x=250, y=400)
    l_sling.filled = True
    l_sling.fill_color = 'steelblue'
    window.add(l_sling)

    l_button = GOval(15,15, x=290, y=405)
    l_button.filled = True
    window.add(l_button)

    r_sling = GRect(60, 30, x=440, y=400)
    r_sling.filled = True
    r_sling.fill_color = 'steelblue'
    window.add(r_sling)

    adjust_line = GLine(250,400,500,400)
    window.add(adjust_line)

    r_button = GOval(15,15, x=450, y=405)
    r_button.filled = True
    window.add(r_button)

    # arms
    l_arm = GRect(80,35,x=170,y=400)
    l_arm.filled = True
    l_arm.fill_color = 'Khaki'
    window.add(l_arm)

    l_hand = GOval(50,50,x=150,y=390)
    l_hand.filled = True
    window.add(l_hand)

    r_arm = GRect(80,35,x=500,y=400)
    r_arm.filled = True
    r_arm.fill_color = 'Khaki'
    window.add(r_arm)

    r_hand = GOval(50,50,x=550,y=390)
    r_hand.filled = True
    window.add(r_hand)

    #feet
    l_foot = GRect(40,50,x=330,y=550)
    l_foot.filled = True
    l_foot.fill_color = 'steelblue'
    window.add(l_foot)

    l_shoe = GOval(30,30,x=315,y=570)
    l_shoe.filled = True
    window.add(l_shoe)

    l_shoe2 = GRect(40,30,x=330,y=570)
    l_shoe2.filled = True
    window.add(l_shoe2)

    r_foot = GRect(40,50,x=380,y=550)
    r_foot.filled = True
    r_foot.fill_color = 'steelblue'
    window.add(r_foot)

    r_shoe = GOval(30,30,x=405,y=570)
    r_shoe.filled = True
    window.add(r_shoe)

    r_shoe2 = GRect(40,30,x=380,y=570)
    r_shoe2.filled = True
    window.add(r_shoe2)

    oval2 = GOval(170,50,x=290, y=510)
    oval2.filled = True
    oval2.fill_color = 'steelblue'
    oval2.color = 'steelblue'
    window.add(oval2)

    #pocket
    pocket = GRect(70,70,x=340, y=420)
    window.add(pocket)

    circle = GOval(50,50,x=350,y=430)
    circle.filled = True
    window.add(circle)

    small_pocket = GRect(32,32, x= 359, y=438)
    small_pocket.filled = True
    small_pocket.fill_color = 'steelblue'
    window.add(small_pocket)






if __name__ == '__main__':
    main()
