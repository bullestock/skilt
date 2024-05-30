import drawsvg as draw

width = 318
height = 159
insetx = 11
insety = 11
cc1 = 91
cc2 = 63
cc3 = 85
studinset = 89.3

r1 = 5/2 # screw hole
r2 = 3/2 # stud hole

d = draw.Drawing(width, height, origin=(0, 0))

d.append(draw.Rectangle(0, 0, width, height, fill='none', stroke='black'))

# top row

x = (width - 2*cc1 - cc2)/2
d.append(draw.Circle(x, insety, r1, fill='none', stroke='black'))
x += cc1
d.append(draw.Circle(x, insety, r1, fill='none', stroke='black'))
x += cc2
d.append(draw.Circle(x, insety, r1, fill='none', stroke='black'))
x += cc1
d.append(draw.Circle(x, insety, r1, fill='none', stroke='black'))

# bottom row

x = (width - 2*cc1 - cc2)/2
d.append(draw.Circle(x, height - insety, r1, fill='none', stroke='black'))
x += cc1
d.append(draw.Circle(x, height - insety, r1, fill='none', stroke='black'))
x += cc2
d.append(draw.Circle(x, height - insety, r1, fill='none', stroke='black'))
x += cc1
d.append(draw.Circle(x, height - insety, r1, fill='none', stroke='black'))

# left
y = (height - cc3)/2
d.append(draw.Circle(insetx, y, r1, fill='none', stroke='black'))
y += cc3
d.append(draw.Circle(insetx, y, r1, fill='none', stroke='black'))

# right
y = (height - cc3)/2
d.append(draw.Circle(width - insetx, y, r1, fill='none', stroke='black'))
y += cc3
d.append(draw.Circle(width - insetx, y, r1, fill='none', stroke='black'))

# stud holes
d.append(draw.Circle(width - studinset, insety, r2, fill='none', stroke='black'))
d.append(draw.Circle(studinset, height - insety, r2, fill='none', stroke='black'))

d.save_svg('templ.svg')
