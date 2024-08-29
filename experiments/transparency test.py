import pyglet
from pyglet.gl import *  # This imports OpenGL functions including glColor4f

# Set up a window with transparency
config = pyglet.gl.Config(double_buffer=True, sample_buffers=1, samples=4)
window = pyglet.window.Window(width=800, height=600, config=config, style=pyglet.window.Window.WINDOW_STYLE_BORDERLESS)

# Set the window background color to transparent
window.set_location(100, 100)
window.clear()

# Enable blending for transparency
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

# Function to draw something
@window.event
def on_draw():
    window.clear()
    glColor4f(1.0, 0.0, 0.0, 0.5)  # Semi-transparent red
    pyglet.graphics.draw(4, GL_QUADS, ('v2i', [100, 100, 200, 100, 200, 200, 100, 200]))

# Run the application
pyglet.app.run()
