import cadquery as cq

res = (cq.Workplane("XY")
       .circle(7/2)
       .extrude(4)
       .circle(4.2/2)
       .cutThruAll()
       )
show_object(res)
