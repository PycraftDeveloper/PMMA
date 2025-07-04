from typing import Union

Numerical = Union[float, int]

class ButtonPressedEvent:
    def get_pressed(self) -> bool: ...
    def get_pressed_toggle(self) -> bool: ...
    def get_double_pressed(self) -> bool: ...
    def get_long_pressed(self) -> bool: ...

    def poll_long_pressed(self) -> bool: ...

    def get_repeat_press_duration(self) -> Numerical: ...
    def get_long_press_duration(self) -> Numerical: ...
    def get_double_press_duration(self) -> Numerical: ...

    def set_repeat_press_duration(self, duration: Numerical) -> None: ...
    def set_double_press_duration(self, duration: Numerical) -> None: ...
    def set_long_press_duration(self, duration: Numerical) -> None: ...

class Zero(ButtonPressedEvent):
    def __init__(self) -> None: ...

class One(ButtonPressedEvent):
    def __init__(self) -> None: ...

class Two(ButtonPressedEvent):
    def __init__(self) -> None: ...

class Three(ButtonPressedEvent):
    def __init__(self) -> None: ...

class Four(ButtonPressedEvent):
    def __init__(self) -> None: ...

class Five(ButtonPressedEvent):
    def __init__(self) -> None: ...

class Siz(ButtonPressedEvent):
    def __init__(self) -> None: ...

class Seven(ButtonPressedEvent):
    def __init__(self) -> None: ...

class Eight(ButtonPressedEvent):
    def __init__(self) -> None: ...

class Nine(ButtonPressedEvent):
    def __init__(self) -> None: ...

class Decimal(ButtonPressedEvent):
    def __init__(self) -> None: ...

class Divide(ButtonPressedEvent):
    def __init__(self) -> None: ...

class Multiply(ButtonPressedEvent):
    def __init__(self) -> None: ...

class Subtract(ButtonPressedEvent):
    def __init__(self) -> None: ...

class Add(ButtonPressedEvent):
    def __init__(self) -> None: ...

class Enter(ButtonPressedEvent):
    def __init__(self) -> None: ...

class Equal(ButtonPressedEvent):
    def __init__(self) -> None: ...