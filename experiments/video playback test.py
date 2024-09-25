import pygame
import moderngl
import numpy as np
import av
from pygame.locals import DOUBLEBUF, OPENGL

# Initialize Pygame with an OpenGL context
pygame.init()
screen = pygame.display.set_mode((1280, 720), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Video Playback with OpenGL")

# Create ModernGL context
ctx = moderngl.create_context()

# Load the video file with manually specified hardware decoding
input_container = av.open(r"H:\Videos\Drivin'.mp4")
# Loop through the streams to find the video stream
for stream in input_container.streams:
    if stream.type == 'video':
        print(f"Codec Name: {stream.codec.name}")
        print(f"Codec Long Name: {stream.codec.long_name}")

# Manually specify a hardware decoder if available
# Example decoders: 'h264_cuvid' for NVIDIA, 'h264_vaapi' for VAAPI, 'h264_qsv' for Intel
hardware_decoder = "h264_cuvid"  # Change based on your platform and availability

# Set the video stream
input_stream = next(s for s in input_container.streams if s.type == 'video')

# Try to set the codec to a hardware-accelerated one
try:
    input_stream.codec_context.options = {'hwaccel': hardware_decoder}
except Exception as e:
    print(f"Failed to set hardware decoder: {e}")
    # Fallback to software decoding
    hardware_decoder = None

# Get video frame rate and calculate the duration of each frame
frame_rate = input_stream.average_rate
frame_time = 1.0 / float(frame_rate)  # Duration for each frame in seconds

# Initialize the first frame to get video dimensions
frame = next(input_container.decode(video=0))
width, height = frame.width, frame.height

# Create OpenGL texture
texture = ctx.texture((width, height), 3)

# Setup ModernGL shaders
prog = ctx.program(
    vertex_shader="""
    #version 330
    in vec2 in_vert;
    in vec2 in_text;
    out vec2 v_text;
    uniform vec2 scale;
    uniform vec2 offset;
    void main() {
        gl_Position = vec4(in_vert * scale + offset, 0.0, 1.0);
        v_text = vec2(in_text.x, 1.0 - in_text.y);  // Flip the y-coordinate
    }
    """,
    fragment_shader="""
    #version 330
    uniform sampler2D Texture;
    in vec2 v_text;
    out vec4 f_color;
    void main() {
        f_color = texture(Texture, v_text);
    }
    """,
)

# Quad vertices and texture coordinates
vertices = np.array([
    -1.0,  1.0, 0.0, 1.0,
    -1.0, -1.0, 0.0, 0.0,
     1.0,  1.0, 1.0, 1.0,
     1.0, -1.0, 1.0, 0.0,
], dtype='f4')

vbo = ctx.buffer(vertices)
vao = ctx.simple_vertex_array(prog, vbo, 'in_vert', 'in_text')

# Initial scale and offset
scale = [1.0, 1.0]
offset = [0.0, 0.0]

clock = pygame.time.Clock()
running = True

# Time tracking variables
time_since_last_frame = 0.0

# Main game loop
while running:
    # Track the time elapsed in the loop
    elapsed_time = clock.tick(500) / 1000.0  # Time since last tick in seconds
    time_since_last_frame += elapsed_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Handle key events to adjust scale and position
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                scale[1] += 0.1
            elif event.key == pygame.K_DOWN:
                scale[1] -= 0.1
            elif event.key == pygame.K_LEFT:
                scale[0] -= 0.1
            elif event.key == pygame.K_RIGHT:
                scale[0] += 0.1
            elif event.key == pygame.K_w:
                offset[1] += 0.1
            elif event.key == pygame.K_s:
                offset[1] -= 0.1
            elif event.key == pygame.K_a:
                offset[0] -= 0.1
            elif event.key == pygame.K_d:
                offset[0] += 0.1

    # Update video frame if enough time has passed
    if time_since_last_frame >= frame_time:
        try:
            frame = next(input_container.decode(video=0))
        except StopIteration:
            # Loop the video for demonstration purposes
            input_container.seek(0)
            frame = next(input_container.decode(video=0))

        # Convert frame to RGB for OpenGL
        img = frame.to_ndarray(format='rgb24')
        texture.write(img)

        time_since_last_frame -= frame_time  # Reset the time counter

    # Update the shader uniforms for scale and offset
    prog['scale'].value = tuple(scale)
    prog['offset'].value = tuple(offset)

    # Render the frame
    ctx.clear(0.0, 0.0, 0.0)
    texture.use()
    vao.render(moderngl.TRIANGLE_STRIP)

    # Swap buffers
    pygame.display.flip()

# Cleanup
input_container.close()
pygame.quit()
