import pygame
import moderngl
import numpy as np

# Pygame and ModernGL setup
pygame.init()
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)

# Create a Pygame window with OpenGL context
screen = pygame.display.set_mode((800, 800), pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE)
clock = pygame.time.Clock()
ctx = moderngl.create_context()

# Vertex Shader
vertex_shader = """
#version 330
in vec2 in_vert;

void main() {
    gl_Position = vec4(in_vert, 0.0, 1.0);
}
"""

# Fragment Shader
fragment_shader = """
#version 330
out vec4 fragColor;

void main() {
    fragColor = vec4(1.0, 0.0, 0.0, 1.0);  // Red color
}
"""

# Compile shaders and link into a program
prog = ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)

# Define a line from (-0.5, -0.5) to (0.5, 0.5)
vertices = np.array([
    -0.5, -0.5,  # Start point
    0.5, 0.5     # End point
], dtype='f4')

# Create a Vertex Buffer Object (VBO) and bind it to the program
vbo = ctx.buffer(vertices.tobytes())
vao = ctx.simple_vertex_array(prog, vbo, 'in_vert')

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    ctx.clear(0.1, 0.1, 0.1)

    # Render the line
    vao.render(mode=moderngl.LINES)

    # Swap the buffers
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
