
Methods
++++++
.. py:method:: path_builder(*args) -> NYD:

File (``pmma.File``)
=======

Object
++++++
.. py:class:: File

Methods
++++++
.. py:method:: File.quit() -> NYD:

.. py:method:: File.exists() -> NYD:

.. py:method:: File.get_path() -> NYD:

.. py:method:: File.get_directory() -> NYD:

.. py:method:: File.get_file_name_and_type() -> NYD:

.. py:method:: File.get_file_name() -> NYD:

.. py:method:: File.get_file_type() -> NYD:

.. py:method:: File.move(new_path) -> NYD:

.. py:method:: File.delete() -> NYD:

.. py:method:: File.recycle() -> NYD:

.. py:method:: File.rename(new_name) -> NYD:

.. py:method:: File.read() -> NYD:

.. py:method:: File.write(content) -> NYD:

File Core (``pmma.FileCore``)
=======

Object
++++++
.. py:class:: FileCore

Methods
++++++
.. py:method:: FileCore.quit() -> NYD:

.. py:method:: FileCore.update_locations(project_directory=None, force_refresh=True) -> NYD:

.. py:method:: FileCore.scan() -> NYD:

.. py:method:: FileCore.refresh(force=False) -> NYD:

.. py:method:: FileCore.stop_passively_refreshing() -> NYD:

.. py:method:: FileCore.start_passively_refreshing() -> NYD:

.. py:method:: FileCore.identify(identifier) -> NYD:
