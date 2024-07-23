import pygame
from pygame.locals import DOUBLEBUF, OPENGL
import moderngl
import numpy as np
import math
import shapes

def init_pygame():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

def init_moderngl():
    return moderngl.create_context()

def rect(ctx, program, top_left, width, height, color):
    x, y = top_left
    vertices = np.array([
        x, y,
        x + width, y,
        x + width, y + height,
        x, y + height
    ], dtype='f4')

    indices = np.array([0, 1, 2, 2, 3, 0], dtype='i4')

    program['color'].value = color
    vbo = ctx.buffer(vertices)
    ibo = ctx.buffer(indices)
    vao = ctx.vertex_array(program, [(vbo, '2f', 'in_vert')], ibo)
    return vao

def render(vao):
    vao.render(moderngl.TRIANGLES)

import time
def main():
    init_pygame()
    ctx = init_moderngl()
    program = ctx.program(
        vertex_shader='''
        #version 330
        in vec2 in_vert;
        void main() {
            gl_Position = vec4(in_vert, 0.0, 1.0);
        }
        ''',
        fragment_shader='''
        #version 330
        out vec4 fragColor;
        uniform vec3 color;
        void main() {
            fragColor = vec4(color, 1.0);
        }
        ''',
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        ctx.clear(0.0, 0.0, 0.0)

        rect_vao = shapes.create_rect(ctx, program, (-0.5, -0.5), 1.0, 1.0, (1.0, 0.0, 0.0))

        s = time.perf_counter()
        for i in range(1_000_000):
            shapes.render_vao(rect_vao, moderngl.TRIANGLES)
        e = time.perf_counter()
        print((1/(e-s)))

        # Call drawing functions here

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
