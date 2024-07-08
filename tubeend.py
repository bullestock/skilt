import cadquery as cq

w = 26.8
h = 10

res = (cq.Workplane("XY")
       .tag("o")
       # Body
       .box(w, w, h)
       .faces(">Z")
       # Insert hole
       .circle(4.5/2)
       .cutBlind(-4)
       # Screw hole
       .circle(4.3/2)
       .cutThruAll()
       # Ridges, 1
       .workplaneFromTagged("o")
       .transformed(offset=(0, w/2, 0))
       .rarray(5, 1, 4, 1)
       .circle(1)
       .cutThruAll()
       # Ridges, 2
       .workplaneFromTagged("o")
       .transformed(offset=(0, -w/2, 0))
       .rarray(5, 1, 4, 1)
       .circle(1)
       .cutThruAll()
       # Ridges, 3
       .workplaneFromTagged("o")
       .transformed(offset=(w/2, 0, 0))
       .rarray(1, 5, 1, 4)
       .circle(1)
       .cutThruAll()
       # Ridges, 4
       .workplaneFromTagged("o")
       .transformed(offset=(-w/2, 0, 0))
       .rarray(1, 5, 1, 4)
       .circle(1)
       .cutThruAll()
       )

show_object(res)
