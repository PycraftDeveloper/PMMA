
Open G L (``pmma.OpenGL``)
=======

Object
++++++
.. py:class:: OpenGL

Methods
++++++
.. py:method:: OpenGL.quit() -> NYD:

.. py:method:: OpenGL.get_simple_texture_rendering_program() -> NYD:

.. py:method:: OpenGL.get_texture_aggregation_program() -> NYD:

.. py:method:: OpenGL.get_context() -> NYD:

.. py:method:: OpenGL.create_fbo(width, height, texture=None, color_format=Constants.RGBA) -> NYD:

.. py:method:: OpenGL.create_texture(width, height, color_format=Constants.RGBA, x_scaling_method=moderngl.LINEAR, y_scaling_method=moderngl.LINEAR) -> NYD:

.. py:method:: OpenGL.blit_image_to_texture(image, texture) -> NYD:

.. py:method:: OpenGL.create_vbo(data) -> NYD:

.. py:method:: OpenGL.create_ibo(data) -> NYD:

.. py:method:: OpenGL.create_vao(program, data_or_vbo, attributes=None, index_buffer=None) -> NYD:
