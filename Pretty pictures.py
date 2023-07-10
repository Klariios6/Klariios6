from gasp import *
begin_graphics() 


Circle((300, 300), 100)
Line((220, 345), (260, 340))#eyebrow from left to right
Line((300,320), (280, 280))#nose 
Line((280,280), (300, 280)) #bottom of the nose 
Line((340, 340), (380, 345)) #left eyebrow
Circle((240, 320), 17)#left eye 
Circle((235, 315), 8.5)#pupil 
Circle((360, 320), 17)#right eye
Circle((355, 315), 8.5)#right pupil 

Arc((300, 265), 30, 225, 315)
Arc((195, 265), 50, 270, 315)
Arc((190, 270), 50, 270, 315)
update_when('key_pressed')   # This keeps the graphics window open until
                             # you press a key.
end_graphics()

