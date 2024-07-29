import moderngl
import pygame
from pygame.locals import DOUBLEBUF, OPENGL
import shapes  # This imports the compiled Cython module
import time
import random

def init_pygame():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

def init_moderngl():
    return moderngl.create_context()

def gen():
    return (random.random()*2)-1

def cleanup(vao, vbo, cbo, ibo):
    vao.release()
    vbo.release()
    cbo.release()
    ibo.release()

def rect():
    return (0, gen(), gen(), random.random(), random.random(), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0), (1.0, 1.0, 0.0))

def main():
    init_pygame()
    ctx = init_moderngl()

    vertex_shader = '''
    #version 330
    in vec2 in_vert;
    in vec3 in_color;
    out vec3 v_color;
    void main() {
        gl_Position = vec4(in_vert, 0.0, 1.0);
        v_color = in_color;
    }
    '''

    fragment_shader = '''
    #version 330
    in vec3 v_color;
    out vec4 fragColor;
    void main() {
        fragColor = vec4(v_color, 1.0);
    }
    '''

    program = ctx.program(
        vertex_shader=vertex_shader,
        fragment_shader=fragment_shader,
    )

    shapes_data = []

    clock = pygame.time.Clock()
    points = []
    while len(shapes_data) < 50_000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        shapes_data.append(rect())

        ctx.clear(0.0, 0.0, 0.0, 1.0)

        tt = 0
        vao, vbo, cbo, ibo = shapes.create_batch_shapes(ctx, program, shapes_data)
        for _ in range(10):
            start = time.perf_counter()
            vao.render(moderngl.TRIANGLES)
            end = time.perf_counter()
            tt += end-start

        tt = tt/10
        print((len(shapes_data), 1/tt))
        points.append((len(shapes_data), 1/tt))

        #del shape_vao
        cleanup(vao, vbo, cbo, ibo)

        pygame.display.flip()
        clock.tick(60)

    print(points)

if __name__ == "__main__":
    main()
