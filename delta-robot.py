import pyglet
from pyglet.gl import *
from pyglet.window import key

INCREMENT = 5

class Triangle:
    def __init__(self):

        self.vertices = pyglet.graphics.vertex_list(4, ('v3f', [1, 1, 3, 1, -1, -1, -1, 1, -1, -1, -1, 1]),
                                            ('c3B', [100, 200, 220, 200, 110, 100, 100, 250, 100, 100, 250, 100]))

class DeltaWindow(pyglet.window.Window):
    xRotation = yRotation = 30

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(400, 300)

        self.triangle = Triangle()

    def on_draw(self):
        glRotatef(self.xRotation, 1, 0, 0)
        glRotatef(self.yRotation, 0, 1, 0)
        self.triangle.vertices.draw(GL_TRIANGLES)


    def on_resize(self, width, height):
       # set the Viewport
       glViewport(0, 0, width, height)

       # using Projection mode
       glMatrixMode(GL_PROJECTION)
       glLoadIdentity()

       aspectRatio = width / height
       gluPerspective(35, aspectRatio, 1, 1000)

       glMatrixMode(GL_MODELVIEW)
       glLoadIdentity()
       glTranslatef(0, 0, -10)

    def on_text_motion(self, motion):
       if motion == key.UP:
            self.xRotation -= INCREMENT
       elif motion == key.DOWN:
           self.xRotation += INCREMENT
       elif motion == key.LEFT:
           self.yRotation -= INCREMENT
       elif motion == key.RIGHT:
           self.yRotation += INCREMENT


if __name__ == "__main__":
    window = DeltaWindow(1280, 720, "Delta Robot Simulation", resizable=True)
    pyglet.app.run()
