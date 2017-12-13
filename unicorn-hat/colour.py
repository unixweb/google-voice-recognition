def red():
   import unicornhat as unicorn
   import time
   unicorn.set_layout(unicorn.AUTO)
   unicorn.rotation(0)
   unicorn.brightness(0.2)
   width,height=unicorn.get_shape()
   for y in range(height):
       for x in range(width):
           unicorn.set_pixel(x,y,255,10,25)
           unicorn.show()
           time.sleep(0.05)

def blue():
   import unicornhat as unicorn
   import time
   unicorn.set_layout(unicorn.AUTO)
   unicorn.rotation(0)
   unicorn.brightness(0.5)
   width,height=unicorn.get_shape()
   for y in range(height):
       for x in range(width):
           unicorn.set_pixel(x,y,124,0,255)
           unicorn.show()
           time.sleep(0.05)

def green():
   import unicornhat as unicorn
   import time
   unicorn.set_layout(unicorn.AUTO)
   unicorn.rotation(0)
   unicorn.brightness(0.7)
   width,height=unicorn.get_shape()
   for y in range(height):
       for x in range(width):
           unicorn.set_pixel(x,y,100,100,25)
           unicorn.show()
           time.sleep(0.05)


def clear():
   import unicornhat as unicorn
   import time
   unicorn.set_layout(unicorn.AUTO)
   unicorn.rotation(0)
   unicorn.brightness(0.0)
   width,height=unicorn.get_shape()
   for y in range(height):
       for x in range(width):
           unicorn.set_pixel(x,y,0,0,0)
           unicorn.show()
           time.sleep(0.05)

