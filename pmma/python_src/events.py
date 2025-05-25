from pmma.python_src.utility.module_utils import ModuleManager as _ModuleManager
from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.constant_utils import InternalConstants as _InternalConstants

class Events:
    """
    🟩 **R** -
    """
    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self, unique_instance=_InternalConstants.EVENTS_OBJECT, add_to_pmma_module_spine=True)

        self._pygame__module = _ModuleManager.import_module("pygame")

        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")
        self._controller__module = _ModuleManager.import_module("pmma.python_src.controller")
        self._backpack__module = _ModuleManager.import_module("pmma.python_src.backpack")

        self._logger = self._logging_utils__module.InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            _Registry.pmma_module_spine[_InternalConstants.LOGGING_INTERMEDIARY_OBJECT].log_information(_Registry.pygame_launch_message)
            self._pygame__module.init()

        self.iteration_id = 0

        self.controllers = self._controller__module.Controllers()

    def handle(self, handle_full_screen_events=True, handle_exit_events=True, grab_extended_keyboard_events=False):
        """
        🟩 **R** -
        """
        if self.iteration_id == _Registry.iteration_id and _Registry.compute_component_called:
            self._logger.log_development("You have called the 'handle()' method from events \
multiple times within a single game loop. Whilst this isn't always a bad thing, \
it can lead to unexpected behavior a some events might not be captured reliably \
at each method call. For instance, one event might appear randomly between two \
different event loops, instead of consistently at one you might be expecting to \
find it at. If this isn't something you where intending to do, changing this will \
potentially save a lot of headaches later down the line.")
        self.iteration_id = _Registry.iteration_id

        if grab_extended_keyboard_events:
            self._logger.log_development("You have set up PMMA's events system to handle a \
wider range of keyboard events. This means that the application will take control of \
keyboard events that are otherwise reserved for the operating system. This is useful for \
example when creating Virtual Desktop applications usig PMMA, but should NOT be needed in \
most applications. We advise you make and test your application with this feature disabled, \
then enable it to see if it fixes or improves a desired feature.")

            self._pygame__module.set_keyboard_grab(True)

        _Registry.handled_events = True

        if _InternalConstants.APPTERMINATING_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.APPTERMINATING_EVENT_OBJECT].set_value(False)

        if _InternalConstants.APPLOWMEMORY_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.APPLOWMEMORY_EVENT_OBJECT].set_value(False)

        if _InternalConstants.APPWILLENTERBACKGROUND_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.APPWILLENTERBACKGROUND_EVENT_OBJECT].set_value(False)

        if _InternalConstants.APPDIDENTERBACKGROUND_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.APPDIDENTERBACKGROUND_EVENT_OBJECT].set_value(False)

        if _InternalConstants.APPWILLENTERFOREGROUND_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.APPWILLENTERFOREGROUND_EVENT_OBJECT].set_value(False)

        if _InternalConstants.APPDIDENTERFOREGROUND_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.APPDIDENTERFOREGROUND_EVENT_OBJECT].set_value(False)

        if _InternalConstants.AUDIODEVICEADDED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.AUDIODEVICEADDED_EVENT_OBJECT].set_value(False)

        if _InternalConstants.AUDIODEVICEREMOVED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.AUDIODEVICEREMOVED_EVENT_OBJECT].set_value(False)

        if _InternalConstants.CLIPBOARDUPDATE_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.CLIPBOARDUPDATE_EVENT_OBJECT].set_value(False)

        if _InternalConstants.DROPFILE_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.DROPFILE_EVENT_OBJECT].set_file(False)

        if _InternalConstants.DROPTEXT_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.DROPTEXT_EVENT_OBJECT].set_text(None)

        if _InternalConstants.DROPBEGIN_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.DROPBEGIN_EVENT_OBJECT].set_value(False)

        if _InternalConstants.DROPCOMPLETE_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.DROPCOMPLETE_EVENT_OBJECT].set_value(False)

        if _InternalConstants.FINGERMOTION_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.FINGERMOTION_EVENT_OBJECT].set_value(False)

        if _InternalConstants.FINGERDOWN_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.FINGERDOWN_EVENT_OBJECT].set_value(False)

        if _InternalConstants.FINGERUP_EVENT_OBJECT in _Registry.pmma_module_spine:
           _Registry.pmma_module_spine[_InternalConstants.FINGERUP_EVENT_OBJECT].set_value(False)

        if _InternalConstants.KEYMAPCHANGED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.KEYMAPCHANGED_EVENT_OBJECT].set_value(False)

        if _InternalConstants.LOCALECHANGED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.LOCALECHANGED_EVENT_OBJECT].set_value(False)

        if _InternalConstants.MULTIGESTURE_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.MULTIGESTURE_EVENT_OBJECT].set_gesture_center_x(None)
            _Registry.pmma_module_spine[_InternalConstants.MULTIGESTURE_EVENT_OBJECT].set_gesture_center_y(None)
            _Registry.pmma_module_spine[_InternalConstants.MULTIGESTURE_EVENT_OBJECT].set_number_of_fingers(None)
            _Registry.pmma_module_spine[_InternalConstants.MULTIGESTURE_EVENT_OBJECT].set_rotated_value(None)
            _Registry.pmma_module_spine[_InternalConstants.MULTIGESTURE_EVENT_OBJECT].set_pinched_value(None)

        if _InternalConstants.QUIT_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.QUIT_EVENT_OBJECT].set_value(False)

        if _InternalConstants.RENDERTARGETSRESET_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.RENDERTARGETSRESET_EVENT_OBJECT].set_value(False)

        if _InternalConstants.RENDERDEVICERESET_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.RENDERDEVICERESET_EVENT_OBJECT].set_value(False)

        if _InternalConstants.SYSWMEVENT_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.SYSWMEVENT_EVENT_OBJECT].set_value(False)

        if _InternalConstants.WINDOWSHOWN_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.WINDOWSHOWN_EVENT_OBJECT].set_value(False)

        if _InternalConstants.WINDOWHIDDEN_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.WINDOWHIDDEN_EVENT_OBJECT].set_value(False)

        if _InternalConstants.WINDOWEXPOSED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.WINDOWEXPOSED_EVENT_OBJECT].set_value(False)

        if _InternalConstants.WINDOWMOVED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.WINDOWMOVED_EVENT_OBJECT].set_value(False)

        if _InternalConstants.WINDOWRESIZED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.WINDOWRESIZED_EVENT_OBJECT].set_value(False)

        if _InternalConstants.WINDOWMINIMIZED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.WINDOWMINIMIZED_EVENT_OBJECT].set_value(False)

        if _InternalConstants.WINDOWMAXIMIZED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.WINDOWMAXIMIZED_EVENT_OBJECT].set_value(False)

        if _InternalConstants.WINDOWRESTORED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.WINDOWRESTORED_EVENT_OBJECT].set_value(False)

        if _InternalConstants.WINDOWENTER_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.WINDOWENTER_EVENT_OBJECT].set_value(False)

        if _InternalConstants.WINDOWLEAVE_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.WINDOWLEAVE_EVENT_OBJECT].set_value(False)

        if _InternalConstants.WINDOWFOCUSGAINED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.WINDOWFOCUSGAINED_EVENT_OBJECT].set_value(False)

        if _InternalConstants.WINDOWFOCUSLOST_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.WINDOWFOCUSLOST_EVENT_OBJECT].set_value(False)

        if _InternalConstants.WINDOWCLOSE_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.WINDOWCLOSE_EVENT_OBJECT].set_value(False)

        if _InternalConstants.WINDOWTAKEFOCUS_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.WINDOWTAKEFOCUS_EVENT_OBJECT].set_value(False)

        if _InternalConstants.WINDOWHITTEST_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.WINDOWHITTEST_EVENT_OBJECT].set_value(False)

        if _InternalConstants.WINDOWICCPROFCHANGED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.WINDOWICCPROFCHANGED_EVENT_OBJECT].set_value(False)

        if _InternalConstants.WINDOWDISPLAYCHANGED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.WINDOWDISPLAYCHANGED_EVENT_OBJECT].set_value(False)

        if _InternalConstants.JOYDEVICEADDED_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.JOYDEVICEADDED_OBJECT].set_value(False)

        if _InternalConstants.JOYDEVICEREMOVED_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.JOYDEVICEREMOVED_OBJECT].set_value(False)

        if _InternalConstants.MOUSE_SCROLL_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.MOUSE_SCROLL_OBJECT].set_x_displacement(0)
            _Registry.pmma_module_spine[_InternalConstants.MOUSE_SCROLL_OBJECT].set_y_displacement(0)

        if _InternalConstants.MOUSE_POSITION_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_InternalConstants.MOUSE_POSITION_OBJECT].set_x_axis_displacement(0)
            _Registry.pmma_module_spine[_InternalConstants.MOUSE_POSITION_OBJECT].set_y_axis_displacement(0)

        raw_events = self._pygame__module.event.get()
        for event in raw_events:
            if event.type == self._pygame__module.APP_TERMINATING:
                if _InternalConstants.APPTERMINATING_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.APPTERMINATING_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.APP_LOWMEMORY:
                if _InternalConstants.APPLOWMEMORY_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.APPLOWMEMORY_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.APP_WILLENTERBACKGROUND:
                if _InternalConstants.APPWILLENTERBACKGROUND_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.APPWILLENTERBACKGROUND_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.APP_DIDENTERBACKGROUND:
                if _InternalConstants.APPDIDENTERBACKGROUND_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.APPDIDENTERBACKGROUND_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.APP_WILLENTERFOREGROUND:
                if _InternalConstants.APPWILLENTERFOREGROUND_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.APPWILLENTERFOREGROUND_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.APP_DIDENTERFOREGROUND:
                if _InternalConstants.APPDIDENTERFOREGROUND_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.APPDIDENTERFOREGROUND_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.AUDIODEVICEADDED:
                if _InternalConstants.AUDIODEVICEADDED_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.AUDIODEVICEADDED_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.AUDIODEVICEREMOVED:
                if _InternalConstants.AUDIODEVICEREMOVED_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.AUDIODEVICEREMOVED_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.CLIPBOARDUPDATE:
                if _InternalConstants.CLIPBOARDUPDATE_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.CLIPBOARDUPDATE_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.DROPFILE:
                if _InternalConstants.DROPFILE_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.DROPFILE_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.DROPTEXT:
                if _InternalConstants.DROPTEXT_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.DROPTEXT_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.DROPBEGIN:
                if _InternalConstants.DROPBEGIN_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.DROPBEGIN_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.DROPCOMPLETE:
                if _InternalConstants.DROPCOMPLETE_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.DROPCOMPLETE_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.FINGERMOTION:
                if _InternalConstants.FINGERMOTION_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.FINGERMOTION_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.FINGERDOWN:
                if _InternalConstants.FINGERDOWN_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.FINGERDOWN_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.FINGERUP:
                if _InternalConstants.FINGERUP_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.FINGERUP_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.KEYMAPCHANGED:
                if _InternalConstants.KEYMAPCHANGED_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.KEYMAPCHANGED_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.JOYAXISMOTION:
                controller = self.controllers.get_controller(event.joy)
                if event.axis == 0:
                    controller.set_left_joystick_axis_x_axis(event.value)

                elif event.axis == 1:
                    controller.set_left_joystick_axis_y_axis(event.value)

                elif event.axis == 2:
                    controller.set_right_joystick_axis_x_axis(event.value)

                elif event.axis == 3:
                    controller.set_right_joystick_axis_y_axis(event.value)

                elif event.axis == 4:
                    controller.set_left_trigger_value(event.value)

                elif event.axis == 5:
                    controller.set_right_trigger_value(event.value)

            elif event.type == self._pygame__module.JOYBALLMOTION:
                controller = self.controllers.get_controller(event.joy)
                trackball = controller.get_track_ball_from_id(event.ball)
                x_motion, y_motion = event.rel
                trackball.set_x_motion(x_motion)
                trackball.set_y_motion(y_motion)

            elif event.type == self._pygame__module.JOYBUTTONDOWN:
                controller = self.controllers.get_controller(event.joy)
                if event.button == 2:
                    controller.set_x_button_pressed(True)
                elif event.button == 0:
                    controller.set_a_button_pressed(True)
                elif event.button == 1:
                    controller.set_b_button_pressed(True)
                elif event.button == 3:
                    controller.set_y_button_pressed(True)
                elif event.button == 9:
                    controller.set_left_bumper_pressed(True)
                elif event.button == 10:
                    controller.set_right_bumper_pressed(True)
                elif event.button == 4:
                    controller.set_share_button_pressed(True)
                elif event.button == 6:
                    controller.set_options_button_pressed(True)
                elif event.button == 7:
                    controller.set_left_joystick_button_pressed(True)
                elif event.button == 8:
                    controller.set_right_joystick_button_pressed(True)
                elif event.button == 11:
                    controller.set_up_hat_button_pressed(True)
                elif event.button == 12:
                    controller.set_down_hat_button_pressed(True)
                elif event.button == 13:
                    controller.set_left_hat_button_pressed(True)
                elif event.button == 14:
                    controller.set_right_hat_button_pressed(True)
                elif event.button == 15:
                    controller.set_center_button_pressed(True)

            elif event.type == self._pygame__module.JOYBUTTONUP:
                controller = self.controllers.get_controller(event.joy)
                if event.button == 2:
                    controller.set_x_button_pressed(False)
                elif event.button == 0:
                    controller.set_a_button_pressed(False)
                elif event.button == 1:
                    controller.set_b_button_pressed(False)
                elif event.button == 3:
                    controller.set_y_button_pressed(False)
                elif event.button == 9:
                    controller.set_left_bumper_pressed(False)
                elif event.button == 10:
                    controller.set_right_bumper_pressed(False)
                elif event.button == 4:
                    controller.set_share_button_pressed(False)
                elif event.button == 6:
                    controller.set_options_button_pressed(False)
                elif event.button == 7:
                    controller.set_left_joystick_button_pressed(False)
                elif event.button == 8:
                    controller.set_right_joystick_button_pressed(False)
                elif event.button == 11:
                    controller.set_up_hat_button_pressed(False)
                elif event.button == 12:
                    controller.set_down_hat_button_pressed(False)
                elif event.button == 13:
                    controller.set_left_hat_button_pressed(False)
                elif event.button == 14:
                    controller.set_right_hat_button_pressed(False)
                elif event.button == 15:
                    controller.set_center_button_pressed(False)

            elif event.type == self._pygame__module.JOYDEVICEADDED:
                if _InternalConstants.JOYDEVICEADDED_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.JOYDEVICEADDED_OBJECT].set_value(True)
                self.controllers.update_controllers()

            elif event.type == self._pygame__module.JOYDEVICEREMOVED:
                if _InternalConstants.JOYDEVICEREMOVED_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.JOYDEVICEREMOVED_OBJECT].set_value(True)
                self.controllers.update_controllers()

            elif event.type == self._pygame__module.LOCALECHANGED:
                if _InternalConstants.LOCALECHANGED_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.LOCALECHANGED_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.MOUSEMOTION:
                if _InternalConstants.MOUSE_POSITION_OBJECT in _Registry.pmma_module_spine:
                    mouse_x_position, mouse_y_position = event.pos
                    mouse_x_displacement, mouse_y_displacement = event.rel
                    _Registry.pmma_module_spine[_InternalConstants.MOUSE_POSITION_OBJECT].set_x_axis(mouse_x_position)
                    _Registry.pmma_module_spine[_InternalConstants.MOUSE_POSITION_OBJECT].set_y_axis(mouse_y_position)
                    _Registry.pmma_module_spine[_InternalConstants.MOUSE_POSITION_OBJECT].set_x_axis_displacement(mouse_x_displacement)
                    _Registry.pmma_module_spine[_InternalConstants.MOUSE_POSITION_OBJECT].set_y_axis_displacement(mouse_y_displacement)

            elif event.type == self._pygame__module.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if _InternalConstants.LEFTBUTTON_MOUSE_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LEFTBUTTON_MOUSE_OBJECT].set_pressed(True)

                elif event.button == 2:
                    if _InternalConstants.MIDDLEBUTTON_MOUSE_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.MIDDLEBUTTON_MOUSE_OBJECT].set_pressed(True)

                elif event.button == 3:
                    if _InternalConstants.RIGHTBUTTON_MOUSE_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RIGHTBUTTON_MOUSE_OBJECT].set_pressed(True)

            elif event.type == self._pygame__module.MOUSEBUTTONUP:
                if event.button == 1:
                    if _InternalConstants.LEFTBUTTON_MOUSE_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LEFTBUTTON_MOUSE_OBJECT].set_pressed(False)

                elif event.button == 2:
                    if _InternalConstants.MIDDLEBUTTON_MOUSE_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.MIDDLEBUTTON_MOUSE_OBJECT].set_pressed(False)

                elif event.button == 3:
                    if _InternalConstants.RIGHTBUTTON_MOUSE_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RIGHTBUTTON_MOUSE_OBJECT].set_pressed(False)

            elif event.type == self._pygame__module.MOUSEWHEEL:
                if _InternalConstants.MOUSE_SCROLL_OBJECT in _Registry.pmma_module_spine:
                    x_displacement = event.precise_x
                    y_displacement = event.precise_y
                    if event.flipped:
                        x_displacement *= -1
                        y_displacement *= -1
                    _Registry.pmma_module_spine[_InternalConstants.MOUSE_SCROLL_OBJECT].set_x_displacement(x_displacement)
                    _Registry.pmma_module_spine[_InternalConstants.MOUSE_SCROLL_OBJECT].set_y_displacement(y_displacement)
                    total_x = _Registry.pmma_module_spine[_InternalConstants.MOUSE_SCROLL_OBJECT].get_x_value()
                    total_y = _Registry.pmma_module_spine[_InternalConstants.MOUSE_SCROLL_OBJECT].get_y_value()
                    _Registry.pmma_module_spine[_InternalConstants.MOUSE_SCROLL_OBJECT].set_x_value(total_x + x_displacement)
                    _Registry.pmma_module_spine[_InternalConstants.MOUSE_SCROLL_OBJECT].set_y_value(total_y + y_displacement)

            elif event.type == self._pygame__module.KEYDOWN:
                if event.key == self._pygame__module.K_BACKSPACE:
                    if _InternalConstants.BACKSPACE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.BACKSPACE_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_TAB:
                    if _InternalConstants.TAB_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.TAB_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_CLEAR:
                    if _InternalConstants.CLEAR_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.CLEAR_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_RETURN:
                    if _InternalConstants.RETURN_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RETURN_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_PAUSE:
                    if _InternalConstants.PAUSE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PAUSE_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_ESCAPE:
                    if _InternalConstants.ESCAPE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.ESCAPE_KEY_OBJECT].set_pressed(True)
                    if handle_exit_events:
                        _Registry.running = False
                        self._backpack__module.Backpack.running = False

                elif event.key == self._pygame__module.K_SPACE:
                    if _InternalConstants.SPACE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.SPACE_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_EXCLAIM:
                    if _InternalConstants.EXCLAMATIONMARK_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.EXCLAMATIONMARK_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_QUOTEDBL:
                    if _InternalConstants.DOUBLEQUOTE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.DOUBLEQUOTE_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_HASH:
                    if _InternalConstants.HASHTAG_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.HASHTAG_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_DOLLAR:
                    if _InternalConstants.DOLLAR_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.DOLLAR_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_AMPERSAND:
                    if _InternalConstants.AMPERSAND_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.AMPERSAND_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_QUOTE:
                    if _InternalConstants.SINGLEQUOTE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.SINGLEQUOTE_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_LEFTPAREN:
                    if _InternalConstants.LEFTPARENTHESIS_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LEFTPARENTHESIS_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_RIGHTPAREN:
                    if _InternalConstants.RIGHTPARENTHESIS_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RIGHTPARENTHESIS_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_ASTERISK:
                    if _InternalConstants.ASTERISK_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.ASTERISK_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_PLUS:
                    if _InternalConstants.PLUS_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PLUS_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_COMMA:
                    if _InternalConstants.COMMA_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.COMMA_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_MINUS:
                    if _InternalConstants.MINUS_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.MINUS_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_PERIOD:
                    if _InternalConstants.PERIOD_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PERIOD_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_SLASH:
                    if _InternalConstants.FORWARDSLASH_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FORWARDSLASH_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_0:
                    if _InternalConstants.PRIMARY0_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY0_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_1:
                    if _InternalConstants.PRIMARY1_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY1_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_2:
                    if _InternalConstants.PRIMARY2_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY2_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_3:
                    if _InternalConstants.PRIMARY3_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY3_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_4:
                    if _InternalConstants.PRIMARY4_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY4_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_5:
                    if _InternalConstants.PRIMARY5_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY5_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_6:
                    if _InternalConstants.PRIMARY6_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY6_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_7:
                    if _InternalConstants.PRIMARY7_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY7_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_8:
                    if _InternalConstants.PRIMARY8_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY8_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_9:
                    if _InternalConstants.PRIMARY9_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY9_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_COLON:
                    if _InternalConstants.COLON_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.COLON_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_SEMICOLON:
                    if _InternalConstants.SEMICOLON_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.SEMICOLON_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_LESS:
                    if _InternalConstants.LESSTHAN_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LESSTHAN_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_EQUALS:
                    if _InternalConstants.EQUALS_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.EQUALS_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_GREATER:
                    if _InternalConstants.GREATERTHAN_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.GREATERTHAN_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_QUESTION:
                    if _InternalConstants.QUESTIONMARK_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.QUESTIONMARK_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_AT:
                    if _InternalConstants.AT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.AT_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_LEFTBRACKET:
                    if _InternalConstants.LEFTBRACKET_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LEFTBRACKET_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_BACKSLASH:
                    if _InternalConstants.BACKSLASH_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.BACKSLASH_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_RIGHTBRACKET:
                    if _InternalConstants.RIGHTBRACKET_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RIGHTBRACKET_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_CARET:
                    if _InternalConstants.CARET_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.CARET_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_UNDERSCORE:
                    if _InternalConstants.UNDERSCORE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.UNDERSCORE_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_BACKQUOTE:
                    if _InternalConstants.GRAVE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.GRAVE_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_a:
                    if _InternalConstants.PRIMARYA_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYA_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_b:
                    if _InternalConstants.PRIMARYB_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYB_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_c:
                    if _InternalConstants.PRIMARYC_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYC_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_d:
                    if _InternalConstants.PRIMARYD_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYD_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_e:
                    if _InternalConstants.PRIMARYE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYE_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_f:
                    if _InternalConstants.PRIMARYF_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYF_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_g:
                    if _InternalConstants.PRIMARYG_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYG_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_h:
                    if _InternalConstants.PRIMARYH_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYH_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_i:
                    if _InternalConstants.PRIMARYI_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYI_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_j:
                    if _InternalConstants.PRIMARYJ_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYJ_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_k:
                    if _InternalConstants.PRIMARYK_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYK_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_l:
                    if _InternalConstants.PRIMARYL_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYL_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_m:
                    if _InternalConstants.PRIMARYM_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYM_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_n:
                    if _InternalConstants.PRIMARYN_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYN_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_o:
                    if _InternalConstants.PRIMARYO_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYO_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_p:
                    if _InternalConstants.PRIMARYP_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYP_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_q:
                    if _InternalConstants.PRIMARYQ_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYQ_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_r:
                    if _InternalConstants.PRIMARYR_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYR_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_s:
                    if _InternalConstants.PRIMARYS_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYS_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_t:
                    if _InternalConstants.PRIMARYT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYT_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_u:
                    if _InternalConstants.PRIMARYU_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYU_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_v:
                    if _InternalConstants.PRIMARYV_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYV_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_w:
                    if _InternalConstants.PRIMARYW_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYW_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_x:
                    if _InternalConstants.PRIMARYX_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYX_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_y:
                    if _InternalConstants.PRIMARYY_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYY_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_z:
                    if _InternalConstants.PRIMARYZ_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYZ_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_DELETE:
                    if _InternalConstants.DELETE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.DELETE_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_KP0:
                    if _InternalConstants.NUMPAD0_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD0_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_KP1:
                    if _InternalConstants.NUMPAD1_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD1_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_KP2:
                    if _InternalConstants.NUMPAD2_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD2_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_KP3:
                    if _InternalConstants.NUMPAD3_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD3_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_KP4:
                    if _InternalConstants.NUMPAD4_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD4_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_KP5:
                    if _InternalConstants.NUMPAD5_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD5_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_KP6:
                    if _InternalConstants.NUMPAD6_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD6_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_KP7:
                    if _InternalConstants.NUMPAD7_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD7_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_KP8:
                    if _InternalConstants.NUMPAD8_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD8_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_KP9:
                    if _InternalConstants.NUMPAD9_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD9_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_KP_PERIOD:
                    if _InternalConstants.NUMPADPERIOD_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPADPERIOD_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_KP_DIVIDE:
                    if _InternalConstants.NUMPADDIVIDE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPADDIVIDE_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_KP_MULTIPLY:
                    if _InternalConstants.NUMPADMULTIPLY_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPADMULTIPLY_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_KP_MINUS:
                    if _InternalConstants.NUMPADMINUS_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPADMINUS_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_KP_PLUS:
                    if _InternalConstants.NUMPADPLUS_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPADPLUS_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_KP_ENTER:
                    if _InternalConstants.NUMPADENTER_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPADENTER_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_KP_EQUALS:
                    if _InternalConstants.NUMPADEQUALS_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPADEQUALS_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_UP:
                    if _InternalConstants.UP_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.UP_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_DOWN:
                    if _InternalConstants.DOWN_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.DOWN_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_RIGHT:
                    if _InternalConstants.RIGHT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RIGHT_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_LEFT:
                    if _InternalConstants.LEFT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LEFT_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_INSERT:
                    if _InternalConstants.INSERT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.INSERT_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_HOME:
                    if _InternalConstants.HOME_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.HOME_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_END:
                    if _InternalConstants.END_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.END_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_PAGEUP:
                    if _InternalConstants.PAGEUP_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PAGEUP_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_PAGEDOWN:
                    if _InternalConstants.PAGEDOWN_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PAGEDOWN_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_F1:
                    if _InternalConstants.FUNCTION1_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION1_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_F2:
                    if _InternalConstants.FUNCTION2_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION2_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_F3:
                    if _InternalConstants.FUNCTION3_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION3_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_F4:
                    if _InternalConstants.FUNCTION4_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION4_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_F5:
                    if _InternalConstants.FUNCTION5_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION5_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_F6:
                    if _InternalConstants.FUNCTION6_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION6_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_F7:
                    if _InternalConstants.FUNCTION7_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION7_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_F8:
                    if _InternalConstants.FUNCTION8_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION8_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_F9:
                    if _InternalConstants.FUNCTION9_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION9_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_F10:
                    if _InternalConstants.FUNCTION10_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION10_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_F11:
                    if _InternalConstants.FUNCTION11_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION11_KEY_OBJECT].set_pressed(True)
                    if handle_full_screen_events:
                        if _Registry.display_initialized:
                            _Registry.pmma_module_spine[_InternalConstants.DISPLAY_OBJECT].toggle_full_screen()
                            if _InternalConstants.WINDOWRESIZED_EVENT_OBJECT in _Registry.pmma_module_spine:
                                _Registry.pmma_module_spine[_InternalConstants.WINDOWRESIZED_EVENT_OBJECT].set_value(True)

                elif event.key == self._pygame__module.K_F12:
                    if _InternalConstants.FUNCTION12_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION12_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_F13:
                    if _InternalConstants.FUNCTION13_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION13_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_F14:
                    if _InternalConstants.FUNCTION14_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION14_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_F15:
                    if _InternalConstants.FUNCTION15_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION15_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_NUMLOCK:
                    if _InternalConstants.NUMLOCK_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMLOCK_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_CAPSLOCK:
                    if _InternalConstants.CAPSLOCK_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.CAPSLOCK_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_SCROLLOCK:
                    if _InternalConstants.SCROLLLOCK_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.SCROLLLOCK_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_RSHIFT:
                    if _InternalConstants.RIGHTSHIFT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RIGHTSHIFT_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_LSHIFT:
                    if _InternalConstants.LEFTSHIFT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LEFTSHIFT_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_RCTRL:
                    if _InternalConstants.RIGHTCONTROL_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RIGHTCONTROL_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_LCTRL:
                    if _InternalConstants.LEFTCONTROL_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LEFTCONTROL_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_RALT:
                    if _InternalConstants.RIGHTALT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RIGHTALT_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_LALT:
                    if _InternalConstants.LEFTALT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LEFTALT_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_RMETA:
                    if _InternalConstants.RIGHTMETA_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RIGHTMETA_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_LMETA:
                    if _InternalConstants.LEFTMETA_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LEFTMETA_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_LSUPER:
                    if _InternalConstants.LEFTSUPER_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LEFTSUPER_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_RSUPER:
                    if _InternalConstants.RIGHTSUPER_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RIGHTSUPER_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_MODE:
                    if _InternalConstants.MODE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.MODE_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_HELP:
                    if _InternalConstants.HELP_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.HELP_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_PRINT:
                    if _InternalConstants.PRINT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRINT_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_SYSREQ:
                    if _InternalConstants.SYSTEMREQUEST_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.SYSTEMREQUEST_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_BREAK:
                    if _InternalConstants.BREAK_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.BREAK_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_MENU:
                    if _InternalConstants.MENU_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.MENU_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_POWER:
                    if _InternalConstants.POWER_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.POWER_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_EURO:
                    if _InternalConstants.EURO_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.EURO_KEY_OBJECT].set_pressed(True)

                elif event.key == self._pygame__module.K_AC_BACK:
                    if _InternalConstants.ANDROIDBACK_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.ANDROIDBACK_KEY_OBJECT].set_pressed(True)

            elif event.type == self._pygame__module.KEYUP:
                if event.key == self._pygame__module.K_BACKSPACE:
                    if _InternalConstants.BACKSPACE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.BACKSPACE_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_TAB:
                    if _InternalConstants.TAB_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.TAB_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_CLEAR:
                    if _InternalConstants.CLEAR_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.CLEAR_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_RETURN:
                    if _InternalConstants.RETURN_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RETURN_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_PAUSE:
                    if _InternalConstants.PAUSE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PAUSE_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_ESCAPE:
                    if _InternalConstants.ESCAPE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.ESCAPE_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_SPACE:
                    if _InternalConstants.SPACE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.SPACE_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_EXCLAIM:
                    if _InternalConstants.EXCLAMATIONMARK_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.EXCLAMATIONMARK_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_QUOTEDBL:
                    if _InternalConstants.DOUBLEQUOTE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.DOUBLEQUOTE_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_HASH:
                    if _InternalConstants.HASHTAG_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.HASHTAG_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_DOLLAR:
                    if _InternalConstants.DOLLAR_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.DOLLAR_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_AMPERSAND:
                    if _InternalConstants.AMPERSAND_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.AMPERSAND_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_QUOTE:
                    if _InternalConstants.SINGLEQUOTE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.SINGLEQUOTE_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_LEFTPAREN:
                    if _InternalConstants.LEFTPARENTHESIS_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LEFTPARENTHESIS_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_RIGHTPAREN:
                    if _InternalConstants.RIGHTPARENTHESIS_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RIGHTPARENTHESIS_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_ASTERISK:
                    if _InternalConstants.ASTERISK_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.ASTERISK_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_PLUS:
                    if _InternalConstants.PLUS_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PLUS_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_COMMA:
                    if _InternalConstants.COMMA_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.COMMA_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_MINUS:
                    if _InternalConstants.MINUS_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.MINUS_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_PERIOD:
                    if _InternalConstants.PERIOD_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PERIOD_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_SLASH:
                    if _InternalConstants.FORWARDSLASH_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FORWARDSLASH_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_0:
                    if _InternalConstants.PRIMARY0_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY0_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_1:
                    if _InternalConstants.PRIMARY1_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY1_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_2:
                    if _InternalConstants.PRIMARY2_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY2_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_3:
                    if _InternalConstants.PRIMARY3_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY3_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_4:
                    if _InternalConstants.PRIMARY4_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY4_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_5:
                    if _InternalConstants.PRIMARY5_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY5_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_6:
                    if _InternalConstants.PRIMARY6_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY6_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_7:
                    if _InternalConstants.PRIMARY7_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY7_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_8:
                    if _InternalConstants.PRIMARY8_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY8_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_9:
                    if _InternalConstants.PRIMARY9_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARY9_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_COLON:
                    if _InternalConstants.COLON_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.COLON_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_SEMICOLON:
                    if _InternalConstants.SEMICOLON_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.SEMICOLON_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_LESS:
                    if _InternalConstants.LESSTHAN_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LESSTHAN_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_EQUALS:
                    if _InternalConstants.EQUALS_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.EQUALS_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_GREATER:
                    if _InternalConstants.GREATERTHAN_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.GREATERTHAN_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_QUESTION:
                    if _InternalConstants.QUESTIONMARK_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.QUESTIONMARK_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_AT:
                    if _InternalConstants.AT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.AT_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_LEFTBRACKET:
                    if _InternalConstants.LEFTBRACKET_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LEFTBRACKET_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_BACKSLASH:
                    if _InternalConstants.BACKSLASH_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.BACKSLASH_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_RIGHTBRACKET:
                    if _InternalConstants.RIGHTBRACKET_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RIGHTBRACKET_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_CARET:
                    if _InternalConstants.CARET_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.CARET_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_UNDERSCORE:
                    if _InternalConstants.UNDERSCORE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.UNDERSCORE_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_BACKQUOTE:
                    if _InternalConstants.GRAVE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.GRAVE_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_a:
                    if _InternalConstants.PRIMARYA_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYA_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_b:
                    if _InternalConstants.PRIMARYB_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYB_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_c:
                    if _InternalConstants.PRIMARYC_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYC_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_d:
                    if _InternalConstants.PRIMARYD_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYD_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_e:
                    if _InternalConstants.PRIMARYE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYE_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_f:
                    if _InternalConstants.PRIMARYF_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYF_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_g:
                    if _InternalConstants.PRIMARYG_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYG_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_h:
                    if _InternalConstants.PRIMARYH_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYH_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_i:
                    if _InternalConstants.PRIMARYI_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYI_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_j:
                    if _InternalConstants.PRIMARYJ_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYJ_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_k:
                    if _InternalConstants.PRIMARYK_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYK_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_l:
                    if _InternalConstants.PRIMARYL_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYL_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_m:
                    if _InternalConstants.PRIMARYM_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYM_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_n:
                    if _InternalConstants.PRIMARYN_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYN_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_o:
                    if _InternalConstants.PRIMARYO_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYO_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_p:
                    if _InternalConstants.PRIMARYP_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYP_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_q:
                    if _InternalConstants.PRIMARYQ_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYQ_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_r:
                    if _InternalConstants.PRIMARYR_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYR_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_s:
                    if _InternalConstants.PRIMARYS_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYS_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_t:
                    if _InternalConstants.PRIMARYT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYT_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_u:
                    if _InternalConstants.PRIMARYU_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYU_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_v:
                    if _InternalConstants.PRIMARYV_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYV_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_w:
                    if _InternalConstants.PRIMARYW_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYW_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_x:
                    if _InternalConstants.PRIMARYX_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYX_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_y:
                    if _InternalConstants.PRIMARYY_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYY_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_z:
                    if _InternalConstants.PRIMARYZ_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRIMARYZ_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_DELETE:
                    if _InternalConstants.DELETE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.DELETE_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_KP0:
                    if _InternalConstants.NUMPAD0_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD0_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_KP1:
                    if _InternalConstants.NUMPAD1_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD1_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_KP2:
                    if _InternalConstants.NUMPAD2_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD2_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_KP3:
                    if _InternalConstants.NUMPAD3_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD3_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_KP4:
                    if _InternalConstants.NUMPAD4_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD4_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_KP5:
                    if _InternalConstants.NUMPAD5_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD5_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_KP6:
                    if _InternalConstants.NUMPAD6_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD6_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_KP7:
                    if _InternalConstants.NUMPAD7_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD7_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_KP8:
                    if _InternalConstants.NUMPAD8_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD8_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_KP9:
                    if _InternalConstants.NUMPAD9_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPAD9_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_KP_PERIOD:
                    if _InternalConstants.NUMPADPERIOD_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPADPERIOD_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_KP_DIVIDE:
                    if _InternalConstants.NUMPADDIVIDE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPADDIVIDE_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_KP_MULTIPLY:
                    if _InternalConstants.NUMPADMULTIPLY_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPADMULTIPLY_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_KP_MINUS:
                    if _InternalConstants.NUMPADMINUS_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPADMINUS_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_KP_PLUS:
                    if _InternalConstants.NUMPADPLUS_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPADPLUS_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_KP_ENTER:
                    if _InternalConstants.NUMPADENTER_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPADENTER_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_KP_EQUALS:
                    if _InternalConstants.NUMPADEQUALS_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMPADEQUALS_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_UP:
                    if _InternalConstants.UP_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.UP_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_DOWN:
                    if _InternalConstants.DOWN_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.DOWN_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_RIGHT:
                    if _InternalConstants.RIGHT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RIGHT_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_LEFT:
                    if _InternalConstants.LEFT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LEFT_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_INSERT:
                    if _InternalConstants.INSERT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.INSERT_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_HOME:
                    if _InternalConstants.HOME_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.HOME_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_END:
                    if _InternalConstants.END_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.END_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_PAGEUP:
                    if _InternalConstants.PAGEUP_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PAGEUP_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_PAGEDOWN:
                    if _InternalConstants.PAGEDOWN_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PAGEDOWN_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_F1:
                    if _InternalConstants.FUNCTION1_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION1_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_F2:
                    if _InternalConstants.FUNCTION2_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION2_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_F3:
                    if _InternalConstants.FUNCTION3_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION3_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_F4:
                    if _InternalConstants.FUNCTION4_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION4_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_F5:
                    if _InternalConstants.FUNCTION5_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION5_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_F6:
                    if _InternalConstants.FUNCTION6_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION6_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_F7:
                    if _InternalConstants.FUNCTION7_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION7_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_F8:
                    if _InternalConstants.FUNCTION8_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION8_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_F9:
                    if _InternalConstants.FUNCTION9_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION9_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_F10:
                    if _InternalConstants.FUNCTION10_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION10_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_F11:
                    if _InternalConstants.FUNCTION11_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION11_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_F12:
                    if _InternalConstants.FUNCTION12_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION12_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_F13:
                    if _InternalConstants.FUNCTION13_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION13_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_F14:
                    if _InternalConstants.FUNCTION14_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION14_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_F15:
                    if _InternalConstants.FUNCTION15_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.FUNCTION15_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_NUMLOCK:
                    if _InternalConstants.NUMLOCK_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.NUMLOCK_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_CAPSLOCK:
                    if _InternalConstants.CAPSLOCK_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.CAPSLOCK_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_SCROLLOCK:
                    if _InternalConstants.SCROLLLOCK_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.SCROLLLOCK_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_RSHIFT:
                    if _InternalConstants.RIGHTSHIFT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RIGHTSHIFT_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_LSHIFT:
                    if _InternalConstants.LEFTSHIFT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LEFTSHIFT_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_RCTRL:
                    if _InternalConstants.RIGHTCONTROL_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RIGHTCONTROL_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_LCTRL:
                    if _InternalConstants.LEFTCONTROL_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LEFTCONTROL_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_RALT:
                    if _InternalConstants.RIGHTALT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RIGHTALT_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_LALT:
                    if _InternalConstants.LEFTALT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LEFTALT_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_RMETA:
                    if _InternalConstants.RIGHTMETA_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RIGHTMETA_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_LMETA:
                    if _InternalConstants.LEFTMETA_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LEFTMETA_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_LSUPER:
                    if _InternalConstants.LEFTSUPER_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.LEFTSUPER_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_RSUPER:
                    if _InternalConstants.RIGHTSUPER_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.RIGHTSUPER_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_MODE:
                    if _InternalConstants.MODE_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.MODE_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_HELP:
                    if _InternalConstants.HELP_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.HELP_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_PRINT:
                    if _InternalConstants.PRINT_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.PRINT_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_SYSREQ:
                    if _InternalConstants.SYSTEMREQUEST_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.SYSTEMREQUEST_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_BREAK:
                    if _InternalConstants.BREAK_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.BREAK_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_MENU:
                    if _InternalConstants.MENU_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.MENU_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_POWER:
                    if _InternalConstants.POWER_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.POWER_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_EURO:
                    if _InternalConstants.EURO_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.EURO_KEY_OBJECT].set_pressed(False)

                elif event.key == self._pygame__module.K_AC_BACK:
                    if _InternalConstants.ANDROIDBACK_KEY_OBJECT in _Registry.pmma_module_spine:
                        _Registry.pmma_module_spine[_InternalConstants.ANDROIDBACK_KEY_OBJECT].set_pressed(False)

            elif event.type == self._pygame__module.MULTIGESTURE:
                if _InternalConstants.MULTIGESTURE_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.MULTIGESTURE_EVENT_OBJECT].set_gesture_center_x(event.x)
                    _Registry.pmma_module_spine[_InternalConstants.MULTIGESTURE_EVENT_OBJECT].set_gesture_center_y(event.y)
                    _Registry.pmma_module_spine[_InternalConstants.MULTIGESTURE_EVENT_OBJECT].set_number_of_fingers(event.num_fingers)
                    _Registry.pmma_module_spine[_InternalConstants.MULTIGESTURE_EVENT_OBJECT].set_rotated_value(event.rotated)
                    _Registry.pmma_module_spine[_InternalConstants.MULTIGESTURE_EVENT_OBJECT].set_pinched_value(event.pinched)

            elif event.type == self._pygame__module.QUIT:
                if _InternalConstants.QUIT_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.QUIT_EVENT_OBJECT].set_value(True)
                if handle_exit_events:
                    _Registry.running = False
                    self._backpack__module.Backpack.running = False

            elif event.type == self._pygame__module.RENDER_TARGETS_RESET:
                if _InternalConstants.RENDERTARGETSRESET_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.RENDERTARGETSRESET_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.RENDER_DEVICE_RESET:
                if _InternalConstants.RENDERDEVICERESET_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.RENDERDEVICERESET_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.SYSWMEVENT:
                if _InternalConstants.SYSWMEVENT_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.SYSWMEVENT_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.WINDOWSHOWN:
                if _InternalConstants.WINDOWSHOWN_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.WINDOWSHOWN_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.WINDOWHIDDEN:
                if _InternalConstants.WINDOWHIDDEN_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.WINDOWHIDDEN_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.WINDOWEXPOSED:
                if _InternalConstants.WINDOWEXPOSED_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.WINDOWEXPOSED_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.WINDOWMOVED:
                if _InternalConstants.WINDOWMOVED_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.WINDOWMOVED_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.WINDOWRESIZED or event.type == self._pygame__module.WINDOWSIZECHANGED:
                if _InternalConstants.WINDOWRESIZED_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.WINDOWRESIZED_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.WINDOWMINIMIZED:
                if _InternalConstants.WINDOWMINIMIZED_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.WINDOWMINIMIZED_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.WINDOWMAXIMIZED:
                if _InternalConstants.WINDOWMAXIMIZED_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.WINDOWMAXIMIZED_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.WINDOWRESTORED:
                if _InternalConstants.WINDOWRESTORED_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.WINDOWRESTORED_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.WINDOWENTER:
                if _InternalConstants.WINDOWENTER_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.WINDOWENTER_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.WINDOWLEAVE:
                if _InternalConstants.WINDOWLEAVE_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.WINDOWLEAVE_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.WINDOWFOCUSGAINED:
                if _InternalConstants.WINDOWFOCUSGAINED_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.WINDOWFOCUSGAINED_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.WINDOWFOCUSLOST:
                if _InternalConstants.WINDOWFOCUSLOST_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.WINDOWFOCUSLOST_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.WINDOWCLOSE:
                if _InternalConstants.WINDOWCLOSE_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.WINDOWCLOSE_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.WINDOWTAKEFOCUS:
                if _InternalConstants.WINDOWTAKEFOCUS_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.WINDOWTAKEFOCUS_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.WINDOWHITTEST:
                if _InternalConstants.WINDOWHITTEST_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.WINDOWHITTEST_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.WINDOWICCPROFCHANGED:
                if _InternalConstants.WINDOWICCPROFCHANGED_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.WINDOWICCPROFCHANGED_EVENT_OBJECT].set_value(True)

            elif event.type == self._pygame__module.WINDOWDISPLAYCHANGED:
                if _InternalConstants.WINDOWDISPLAYCHANGED_EVENT_OBJECT in _Registry.pmma_module_spine:
                    _Registry.pmma_module_spine[_InternalConstants.WINDOWDISPLAYCHANGED_EVENT_OBJECT].set_value(True)

class Backspace_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.BACKSPACE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.BACKSPACE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Backspace_KEY as _Backspace_KEY
            _Backspace_KEY()

        self._backspace_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.BACKSPACE_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._backspace_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._backspace_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._backspace_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._backspace_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._backspace_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._backspace_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._backspace_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._backspace_key_object_intermediary.set_double_tap_timing(value)

class Tab_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.TAB_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.TAB_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Tab_KEY as _Tab_KEY
            _Tab_KEY()

        self._tab_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.TAB_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._tab_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._tab_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._tab_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._tab_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._tab_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._tab_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._tab_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._tab_key_object_intermediary.set_double_tap_timing(value)

class Clear_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.CLEAR_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.CLEAR_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Clear_KEY as _Clear_KEY
            _Clear_KEY()

        self._clear_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.CLEAR_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._clear_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._clear_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._clear_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._clear_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._clear_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._clear_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._clear_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._clear_key_object_intermediary.set_double_tap_timing(value)

class Return_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.RETURN_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.RETURN_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Return_KEY as _Return_KEY
            _Return_KEY()

        self._return_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.RETURN_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._return_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._return_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._return_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._return_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._return_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._return_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._return_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._return_key_object_intermediary.set_double_tap_timing(value)

class Pause_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PAUSE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PAUSE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Pause_KEY as _Pause_KEY
            _Pause_KEY()

        self._pause_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PAUSE_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._pause_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._pause_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._pause_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._pause_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._pause_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._pause_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._pause_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._pause_key_object_intermediary.set_double_tap_timing(value)

class Escape_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.ESCAPE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.ESCAPE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Escape_KEY as _Escape_KEY
            _Escape_KEY()

        self._escape_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.ESCAPE_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._escape_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._escape_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._escape_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._escape_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._escape_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._escape_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._escape_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._escape_key_object_intermediary.set_double_tap_timing(value)

class Space_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.SPACE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.SPACE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Space_KEY as _Space_KEY
            _Space_KEY()

        self._space_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.SPACE_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._space_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._space_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._space_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._space_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._space_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._space_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._space_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._space_key_object_intermediary.set_double_tap_timing(value)

class ExclamationMark_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.EXCLAMATIONMARK_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.EXCLAMATIONMARK_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import ExclamationMark_KEY as _ExclamationMark_KEY
            _ExclamationMark_KEY()

        self._exclamationmark_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.EXCLAMATIONMARK_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._exclamationmark_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._exclamationmark_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._exclamationmark_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._exclamationmark_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._exclamationmark_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._exclamationmark_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._exclamationmark_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._exclamationmark_key_object_intermediary.set_double_tap_timing(value)

class DoubleQuote_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.DOUBLEQUOTE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.DOUBLEQUOTE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import DoubleQuote_KEY as _DoubleQuote_KEY
            _DoubleQuote_KEY()

        self._doublequote_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.DOUBLEQUOTE_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._doublequote_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._doublequote_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._doublequote_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._doublequote_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._doublequote_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._doublequote_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._doublequote_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._doublequote_key_object_intermediary.set_double_tap_timing(value)

class Hashtag_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.HASHTAG_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.HASHTAG_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Hashtag_KEY as _Hashtag_KEY
            _Hashtag_KEY()

        self._hashtag_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.HASHTAG_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._hashtag_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._hashtag_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._hashtag_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._hashtag_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._hashtag_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._hashtag_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._hashtag_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._hashtag_key_object_intermediary.set_double_tap_timing(value)

class Dollar_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.DOLLAR_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.DOLLAR_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Dollar_KEY as _Dollar_KEY
            _Dollar_KEY()

        self._dollar_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.DOLLAR_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._dollar_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._dollar_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._dollar_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._dollar_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._dollar_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._dollar_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._dollar_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._dollar_key_object_intermediary.set_double_tap_timing(value)

class Ampersand_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.AMPERSAND_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.AMPERSAND_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Ampersand_KEY as _Ampersand_KEY
            _Ampersand_KEY()

        self._ampersand_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.AMPERSAND_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._ampersand_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._ampersand_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._ampersand_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._ampersand_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._ampersand_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._ampersand_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._ampersand_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._ampersand_key_object_intermediary.set_double_tap_timing(value)

class SingleQuote_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.SINGLEQUOTE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.SINGLEQUOTE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import SingleQuote_KEY as _SingleQuote_KEY
            _SingleQuote_KEY()

        self._singlequote_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.SINGLEQUOTE_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._singlequote_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._singlequote_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._singlequote_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._singlequote_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._singlequote_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._singlequote_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._singlequote_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._singlequote_key_object_intermediary.set_double_tap_timing(value)

class LeftParenthesis_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.LEFTPARENTHESIS_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.LEFTPARENTHESIS_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import LeftParenthesis_KEY as _LeftParenthesis_KEY
            _LeftParenthesis_KEY()

        self._leftparenthesis_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.LEFTPARENTHESIS_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._leftparenthesis_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._leftparenthesis_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._leftparenthesis_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._leftparenthesis_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._leftparenthesis_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._leftparenthesis_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._leftparenthesis_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._leftparenthesis_key_object_intermediary.set_double_tap_timing(value)

class RightParenthesis_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.RIGHTPARENTHESIS_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.RIGHTPARENTHESIS_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import RightParenthesis_KEY as _RightParenthesis_KEY
            _RightParenthesis_KEY()

        self._rightparenthesis_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.RIGHTPARENTHESIS_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._rightparenthesis_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._rightparenthesis_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._rightparenthesis_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._rightparenthesis_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._rightparenthesis_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._rightparenthesis_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._rightparenthesis_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._rightparenthesis_key_object_intermediary.set_double_tap_timing(value)

class Asterisk_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.ASTERISK_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.ASTERISK_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Asterisk_KEY as _Asterisk_KEY
            _Asterisk_KEY()

        self._asterisk_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.ASTERISK_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._asterisk_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._asterisk_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._asterisk_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._asterisk_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._asterisk_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._asterisk_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._asterisk_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._asterisk_key_object_intermediary.set_double_tap_timing(value)

class Plus_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PLUS_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PLUS_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Plus_KEY as _Plus_KEY
            _Plus_KEY()

        self._plus_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PLUS_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._plus_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._plus_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._plus_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._plus_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._plus_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._plus_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._plus_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._plus_key_object_intermediary.set_double_tap_timing(value)

class Comma_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.COMMA_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.COMMA_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Comma_KEY as _Comma_KEY
            _Comma_KEY()

        self._comma_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.COMMA_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._comma_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._comma_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._comma_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._comma_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._comma_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._comma_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._comma_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._comma_key_object_intermediary.set_double_tap_timing(value)

class Minus_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.MINUS_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.MINUS_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Minus_KEY as _Minus_KEY
            _Minus_KEY()

        self._minus_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.MINUS_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._minus_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._minus_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._minus_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._minus_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._minus_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._minus_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._minus_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._minus_key_object_intermediary.set_double_tap_timing(value)

class Period_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PERIOD_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PERIOD_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Period_KEY as _Period_KEY
            _Period_KEY()

        self._period_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PERIOD_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._period_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._period_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._period_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._period_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._period_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._period_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._period_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._period_key_object_intermediary.set_double_tap_timing(value)

class ForwardSlash_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.FORWARDSLASH_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.FORWARDSLASH_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import ForwardSlash_KEY as _ForwardSlash_KEY
            _ForwardSlash_KEY()

        self._forwardslash_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.FORWARDSLASH_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._forwardslash_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._forwardslash_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._forwardslash_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._forwardslash_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._forwardslash_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._forwardslash_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._forwardslash_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._forwardslash_key_object_intermediary.set_double_tap_timing(value)

class Primary0_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARY0_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARY0_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary0_KEY as _Primary0_KEY
            _Primary0_KEY()

        self._primary0_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARY0_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primary0_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primary0_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primary0_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primary0_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primary0_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primary0_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primary0_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primary0_key_object_intermediary.set_double_tap_timing(value)

class Primary1_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARY1_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARY1_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary1_KEY as _Primary1_KEY
            _Primary1_KEY()

        self._primary1_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARY1_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primary1_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primary1_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primary1_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primary1_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primary1_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primary1_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primary1_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primary1_key_object_intermediary.set_double_tap_timing(value)

class Primary2_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARY2_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARY2_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary2_KEY as _Primary2_KEY
            _Primary2_KEY()

        self._primary2_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARY2_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primary2_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primary2_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primary2_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primary2_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primary2_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primary2_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primary2_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primary2_key_object_intermediary.set_double_tap_timing(value)

class Primary3_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARY3_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARY3_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary3_KEY as _Primary3_KEY
            _Primary3_KEY()

        self._primary3_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARY3_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primary3_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primary3_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primary3_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primary3_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primary3_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primary3_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primary3_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primary3_key_object_intermediary.set_double_tap_timing(value)

class Primary4_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARY4_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARY4_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary4_KEY as _Primary4_KEY
            _Primary4_KEY()

        self._primary4_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARY4_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primary4_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primary4_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primary4_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primary4_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primary4_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primary4_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primary4_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primary4_key_object_intermediary.set_double_tap_timing(value)

class Primary5_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARY5_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARY5_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary5_KEY as _Primary5_KEY
            _Primary5_KEY()

        self._primary5_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARY5_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primary5_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primary5_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primary5_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primary5_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primary5_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primary5_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primary5_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primary5_key_object_intermediary.set_double_tap_timing(value)

class Primary6_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARY6_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARY6_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary6_KEY as _Primary6_KEY
            _Primary6_KEY()

        self._primary6_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARY6_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primary6_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primary6_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primary6_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primary6_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primary6_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primary6_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primary6_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primary6_key_object_intermediary.set_double_tap_timing(value)

class Primary7_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARY7_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARY7_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary7_KEY as _Primary7_KEY
            _Primary7_KEY()

        self._primary7_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARY7_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primary7_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primary7_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primary7_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primary7_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primary7_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primary7_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primary7_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primary7_key_object_intermediary.set_double_tap_timing(value)

class Primary8_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARY8_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARY8_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary8_KEY as _Primary8_KEY
            _Primary8_KEY()

        self._primary8_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARY8_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primary8_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primary8_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primary8_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primary8_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primary8_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primary8_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primary8_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primary8_key_object_intermediary.set_double_tap_timing(value)

class Primary9_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARY9_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARY9_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary9_KEY as _Primary9_KEY
            _Primary9_KEY()

        self._primary9_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARY9_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primary9_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primary9_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primary9_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primary9_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primary9_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primary9_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primary9_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primary9_key_object_intermediary.set_double_tap_timing(value)

class Colon_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.COLON_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.COLON_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Colon_KEY as _Colon_KEY
            _Colon_KEY()

        self._colon_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.COLON_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._colon_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._colon_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._colon_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._colon_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._colon_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._colon_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._colon_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._colon_key_object_intermediary.set_double_tap_timing(value)

class SemiColon_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.SEMICOLON_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.SEMICOLON_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import SemiColon_KEY as _SemiColon_KEY
            _SemiColon_KEY()

        self._semicolon_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.SEMICOLON_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._semicolon_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._semicolon_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._semicolon_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._semicolon_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._semicolon_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._semicolon_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._semicolon_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._semicolon_key_object_intermediary.set_double_tap_timing(value)

class LessThan_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.LESSTHAN_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.LESSTHAN_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import LessThan_KEY as _LessThan_KEY
            _LessThan_KEY()

        self._lessthan_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.LESSTHAN_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._lessthan_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._lessthan_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._lessthan_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._lessthan_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._lessthan_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._lessthan_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._lessthan_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._lessthan_key_object_intermediary.set_double_tap_timing(value)

class Equals_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.EQUALS_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.EQUALS_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Equals_KEY as _Equals_KEY
            _Equals_KEY()

        self._equals_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.EQUALS_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._equals_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._equals_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._equals_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._equals_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._equals_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._equals_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._equals_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._equals_key_object_intermediary.set_double_tap_timing(value)

class GreaterThan_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.GREATERTHAN_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.GREATERTHAN_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import GreaterThan_KEY as _GreaterThan_KEY
            _GreaterThan_KEY()

        self._greaterthan_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.GREATERTHAN_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._greaterthan_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._greaterthan_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._greaterthan_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._greaterthan_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._greaterthan_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._greaterthan_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._greaterthan_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._greaterthan_key_object_intermediary.set_double_tap_timing(value)

class QuestionMark_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.QUESTIONMARK_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.QUESTIONMARK_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import QuestionMark_KEY as _QuestionMark_KEY
            _QuestionMark_KEY()

        self._questionmark_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.QUESTIONMARK_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._questionmark_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._questionmark_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._questionmark_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._questionmark_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._questionmark_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._questionmark_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._questionmark_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._questionmark_key_object_intermediary.set_double_tap_timing(value)

class At_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.AT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.AT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import At_KEY as _At_KEY
            _At_KEY()

        self._at_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.AT_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._at_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._at_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._at_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._at_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._at_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._at_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._at_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._at_key_object_intermediary.set_double_tap_timing(value)

class LeftBracket_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.LEFTBRACKET_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.LEFTBRACKET_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import LeftBracket_KEY as _LeftBracket_KEY
            _LeftBracket_KEY()

        self._leftbracket_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.LEFTBRACKET_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._leftbracket_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._leftbracket_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._leftbracket_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._leftbracket_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._leftbracket_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._leftbracket_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._leftbracket_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._leftbracket_key_object_intermediary.set_double_tap_timing(value)

class BackSlash_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.BACKSLASH_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.BACKSLASH_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import BackSlash_KEY as _BackSlash_KEY
            _BackSlash_KEY()

        self._backslash_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.BACKSLASH_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._backslash_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._backslash_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._backslash_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._backslash_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._backslash_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._backslash_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._backslash_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._backslash_key_object_intermediary.set_double_tap_timing(value)

class RightBracket_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.RIGHTBRACKET_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.RIGHTBRACKET_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import RightBracket_KEY as _RightBracket_KEY
            _RightBracket_KEY()

        self._rightbracket_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.RIGHTBRACKET_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._rightbracket_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._rightbracket_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._rightbracket_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._rightbracket_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._rightbracket_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._rightbracket_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._rightbracket_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._rightbracket_key_object_intermediary.set_double_tap_timing(value)

class Caret_KEY: # ^
    """
    🟩 **R** -
    """


    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.CARET_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.CARET_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Caret_KEY as _Caret_KEY
            _Caret_KEY()

        self._caret_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.CARET_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._caret_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._caret_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._caret_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._caret_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._caret_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._caret_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._caret_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._caret_key_object_intermediary.set_double_tap_timing(value)

class Underscore_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.UNDERSCORE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.UNDERSCORE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Underscore_KEY as _Underscore_KEY
            _Underscore_KEY()

        self._underscore_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.UNDERSCORE_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._underscore_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._underscore_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._underscore_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._underscore_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._underscore_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._underscore_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._underscore_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._underscore_key_object_intermediary.set_double_tap_timing(value)

class Grave_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.GRAVE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.GRAVE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Grave_KEY as _Grave_KEY
            _Grave_KEY()

        self._grave_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.GRAVE_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._grave_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._grave_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._grave_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._grave_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._grave_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._grave_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._grave_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._grave_key_object_intermediary.set_double_tap_timing(value)

class PrimaryA_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYA_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYA_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryA_KEY as _PrimaryA_KEY
            _PrimaryA_KEY()

        self._primarya_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYA_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primarya_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primarya_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primarya_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primarya_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primarya_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primarya_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primarya_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primarya_key_object_intermediary.set_double_tap_timing(value)

class PrimaryB_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYB_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYB_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryB_KEY as _PrimaryB_KEY
            _PrimaryB_KEY()

        self._primaryb_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYB_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryb_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryb_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryb_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryb_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryb_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryb_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryb_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryb_key_object_intermediary.set_double_tap_timing(value)

class PrimaryC_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYC_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYC_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryC_KEY as _PrimaryC_KEY
            _PrimaryC_KEY()

        self._primaryc_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYC_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryc_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryc_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryc_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryc_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryc_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryc_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryc_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryc_key_object_intermediary.set_double_tap_timing(value)

class PrimaryD_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYD_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYD_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryD_KEY as _PrimaryD_KEY
            _PrimaryD_KEY()

        self._primaryd_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYD_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryd_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryd_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryd_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryd_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryd_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryd_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryd_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryd_key_object_intermediary.set_double_tap_timing(value)

class PrimaryE_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryE_KEY as _PrimaryE_KEY
            _PrimaryE_KEY()

        self._primarye_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYE_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primarye_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primarye_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primarye_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primarye_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primarye_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primarye_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primarye_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primarye_key_object_intermediary.set_double_tap_timing(value)

class PrimaryF_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYF_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYF_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryF_KEY as _PrimaryF_KEY
            _PrimaryF_KEY()

        self._primaryf_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYF_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryf_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryf_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryf_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryf_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryf_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryf_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryf_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryf_key_object_intermediary.set_double_tap_timing(value)

class PrimaryG_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYG_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYG_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryG_KEY as _PrimaryG_KEY
            _PrimaryG_KEY()

        self._primaryg_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYG_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryg_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryg_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryg_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryg_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryg_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryg_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryg_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryg_key_object_intermediary.set_double_tap_timing(value)

class PrimaryH_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYH_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYH_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryH_KEY as _PrimaryH_KEY
            _PrimaryH_KEY()

        self._primaryh_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYH_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryh_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryh_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryh_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryh_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryh_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryh_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryh_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryh_key_object_intermediary.set_double_tap_timing(value)

class PrimaryI_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYI_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYI_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryI_KEY as _PrimaryI_KEY
            _PrimaryI_KEY()

        self._primaryi_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYI_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryi_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryi_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryi_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryi_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryi_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryi_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryi_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryi_key_object_intermediary.set_double_tap_timing(value)

class PrimaryJ_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYJ_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYJ_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryJ_KEY as _PrimaryJ_KEY
            _PrimaryJ_KEY()

        self._primaryj_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYJ_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryj_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryj_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryj_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryj_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryj_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryj_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryj_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryj_key_object_intermediary.set_double_tap_timing(value)

class PrimaryK_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYK_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYK_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryK_KEY as _PrimaryK_KEY
            _PrimaryK_KEY()

        self._primaryk_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYK_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryk_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryk_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryk_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryk_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryk_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryk_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryk_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryk_key_object_intermediary.set_double_tap_timing(value)

class PrimaryL_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYL_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYL_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryL_KEY as _PrimaryL_KEY
            _PrimaryL_KEY()

        self._primaryl_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYL_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryl_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryl_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryl_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryl_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryl_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryl_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryl_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryl_key_object_intermediary.set_double_tap_timing(value)

class PrimaryM_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYM_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYM_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryM_KEY as _PrimaryM_KEY
            _PrimaryM_KEY()

        self._primarym_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYM_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primarym_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primarym_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primarym_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primarym_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primarym_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primarym_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primarym_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primarym_key_object_intermediary.set_double_tap_timing(value)

class PrimaryN_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYN_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYN_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryN_KEY as _PrimaryN_KEY
            _PrimaryN_KEY()

        self._primaryn_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYN_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryn_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryn_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryn_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryn_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryn_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryn_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryn_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryn_key_object_intermediary.set_double_tap_timing(value)

class PrimaryO_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYO_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYO_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryO_KEY as _PrimaryO_KEY
            _PrimaryO_KEY()

        self._primaryo_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYO_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryo_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryo_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryo_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryo_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryo_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryo_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryo_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryo_key_object_intermediary.set_double_tap_timing(value)

class PrimaryP_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYP_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYP_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryP_KEY as _PrimaryP_KEY
            _PrimaryP_KEY()

        self._primaryp_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYP_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryp_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryp_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryp_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryp_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryp_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryp_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryp_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryp_key_object_intermediary.set_double_tap_timing(value)

class PrimaryQ_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYQ_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYQ_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryQ_KEY as _PrimaryQ_KEY
            _PrimaryQ_KEY()

        self._primaryq_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYQ_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryq_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryq_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryq_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryq_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryq_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryq_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryq_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryq_key_object_intermediary.set_double_tap_timing(value)

class PrimaryR_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYR_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYR_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryR_KEY as _PrimaryR_KEY
            _PrimaryR_KEY()

        self._primaryr_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYR_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryr_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryr_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryr_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryr_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryr_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryr_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryr_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryr_key_object_intermediary.set_double_tap_timing(value)

class PrimaryS_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYS_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYS_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryS_KEY as _PrimaryS_KEY
            _PrimaryS_KEY()

        self._primarys_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYS_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primarys_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primarys_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primarys_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primarys_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primarys_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primarys_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primarys_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primarys_key_object_intermediary.set_double_tap_timing(value)

class PrimaryT_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryT_KEY as _PrimaryT_KEY
            _PrimaryT_KEY()

        self._primaryt_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYT_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryt_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryt_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryt_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryt_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryt_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryt_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryt_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryt_key_object_intermediary.set_double_tap_timing(value)

class PrimaryU_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYU_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYU_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryU_KEY as _PrimaryU_KEY
            _PrimaryU_KEY()

        self._primaryu_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYU_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryu_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryu_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryu_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryu_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryu_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryu_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryu_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryu_key_object_intermediary.set_double_tap_timing(value)

class PrimaryV_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYV_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYV_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryV_KEY as _PrimaryV_KEY
            _PrimaryV_KEY()

        self._primaryv_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYV_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryv_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryv_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryv_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryv_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryv_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryv_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryv_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryv_key_object_intermediary.set_double_tap_timing(value)

class PrimaryW_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYW_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYW_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryW_KEY as _PrimaryW_KEY
            _PrimaryW_KEY()

        self._primaryw_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYW_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryw_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryw_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryw_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryw_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryw_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryw_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryw_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryw_key_object_intermediary.set_double_tap_timing(value)

class PrimaryX_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYX_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYX_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryX_KEY as _PrimaryX_KEY
            _PrimaryX_KEY()

        self._primaryx_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYX_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryx_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryx_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryx_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryx_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryx_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryx_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryx_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryx_key_object_intermediary.set_double_tap_timing(value)

class PrimaryY_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYY_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYY_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryY_KEY as _PrimaryY_KEY
            _PrimaryY_KEY()

        self._primaryy_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYY_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryy_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryy_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryy_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryy_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryy_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryy_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryy_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryy_key_object_intermediary.set_double_tap_timing(value)

class PrimaryZ_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRIMARYZ_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRIMARYZ_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryZ_KEY as _PrimaryZ_KEY
            _PrimaryZ_KEY()

        self._primaryz_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRIMARYZ_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._primaryz_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._primaryz_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._primaryz_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._primaryz_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._primaryz_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._primaryz_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._primaryz_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._primaryz_key_object_intermediary.set_double_tap_timing(value)

class Delete_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.DELETE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.DELETE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Delete_KEY as _Delete_KEY
            _Delete_KEY()

        self._delete_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.DELETE_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._delete_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._delete_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._delete_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._delete_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._delete_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._delete_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._delete_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._delete_key_object_intermediary.set_double_tap_timing(value)

class Numpad0_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.NUMPAD0_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.NUMPAD0_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad0_KEY as _Numpad0_KEY
            _Numpad0_KEY()

        self._numpad0_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.NUMPAD0_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._numpad0_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._numpad0_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._numpad0_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._numpad0_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._numpad0_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._numpad0_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._numpad0_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._numpad0_key_object_intermediary.set_double_tap_timing(value)

class Numpad1_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.NUMPAD1_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.NUMPAD1_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad1_KEY as _Numpad1_KEY
            _Numpad1_KEY()

        self._numpad1_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.NUMPAD1_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._numpad1_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._numpad1_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._numpad1_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._numpad1_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._numpad1_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._numpad1_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._numpad1_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._numpad1_key_object_intermediary.set_double_tap_timing(value)

class Numpad2_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.NUMPAD2_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.NUMPAD2_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad2_KEY as _Numpad2_KEY
            _Numpad2_KEY()

        self._numpad2_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.NUMPAD2_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._numpad2_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._numpad2_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._numpad2_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._numpad2_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._numpad2_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._numpad2_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._numpad2_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._numpad2_key_object_intermediary.set_double_tap_timing(value)

class Numpad3_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.NUMPAD3_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.NUMPAD3_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad3_KEY as _Numpad3_KEY
            _Numpad3_KEY()

        self._numpad3_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.NUMPAD3_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._numpad3_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._numpad3_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._numpad3_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._numpad3_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._numpad3_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._numpad3_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._numpad3_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._numpad3_key_object_intermediary.set_double_tap_timing(value)

class Numpad4_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.NUMPAD4_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.NUMPAD4_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad4_KEY as _Numpad4_KEY
            _Numpad4_KEY()

        self._numpad4_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.NUMPAD4_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._numpad4_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._numpad4_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._numpad4_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._numpad4_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._numpad4_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._numpad4_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._numpad4_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._numpad4_key_object_intermediary.set_double_tap_timing(value)

class Numpad5_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.NUMPAD5_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.NUMPAD5_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad5_KEY as _Numpad5_KEY
            _Numpad5_KEY()

        self._numpad5_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.NUMPAD5_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._numpad5_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._numpad5_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._numpad5_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._numpad5_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._numpad5_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._numpad5_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._numpad5_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._numpad5_key_object_intermediary.set_double_tap_timing(value)

class Numpad6_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.NUMPAD6_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.NUMPAD6_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad6_KEY as _Numpad6_KEY
            _Numpad6_KEY()

        self._numpad6_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.NUMPAD6_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._numpad6_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._numpad6_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._numpad6_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._numpad6_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._numpad6_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._numpad6_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._numpad6_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._numpad6_key_object_intermediary.set_double_tap_timing(value)

class Numpad7_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.NUMPAD7_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.NUMPAD7_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad7_KEY as _Numpad7_KEY
            _Numpad7_KEY()

        self._numpad7_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.NUMPAD7_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._numpad7_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._numpad7_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._numpad7_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._numpad7_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._numpad7_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._numpad7_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._numpad7_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._numpad7_key_object_intermediary.set_double_tap_timing(value)

class Numpad8_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.NUMPAD8_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.NUMPAD8_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad8_KEY as _Numpad8_KEY
            _Numpad8_KEY()

        self._numpad8_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.NUMPAD8_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._numpad8_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._numpad8_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._numpad8_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._numpad8_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._numpad8_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._numpad8_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._numpad8_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._numpad8_key_object_intermediary.set_double_tap_timing(value)

class Numpad9_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.NUMPAD9_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.NUMPAD9_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad9_KEY as _Numpad9_KEY
            _Numpad9_KEY()

        self._numpad9_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.NUMPAD9_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._numpad9_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._numpad9_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._numpad9_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._numpad9_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._numpad9_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._numpad9_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._numpad9_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._numpad9_key_object_intermediary.set_double_tap_timing(value)

class NumpadPeriod_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.NUMPADPERIOD_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.NUMPADPERIOD_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import NumpadPeriod_KEY as _NumpadPeriod_KEY
            _NumpadPeriod_KEY()

        self._numpadperiod_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.NUMPADPERIOD_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._numpadperiod_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._numpadperiod_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._numpadperiod_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._numpadperiod_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._numpadperiod_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._numpadperiod_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._numpadperiod_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._numpadperiod_key_object_intermediary.set_double_tap_timing(value)

class NumpadDivide_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.NUMPADDIVIDE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.NUMPADDIVIDE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import NumpadDivide_KEY as _NumpadDivide_KEY
            _NumpadDivide_KEY()

        self._numpaddivide_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.NUMPADDIVIDE_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._numpaddivide_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._numpaddivide_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._numpaddivide_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._numpaddivide_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._numpaddivide_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._numpaddivide_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._numpaddivide_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._numpaddivide_key_object_intermediary.set_double_tap_timing(value)

class NumpadMultiply_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.NUMPADMULTIPLY_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.NUMPADMULTIPLY_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import NumpadMultiply_KEY as _NumpadMultiply_KEY
            _NumpadMultiply_KEY()

        self._numpadmultiply_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.NUMPADMULTIPLY_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._numpadmultiply_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._numpadmultiply_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._numpadmultiply_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._numpadmultiply_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._numpadmultiply_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._numpadmultiply_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._numpadmultiply_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._numpadmultiply_key_object_intermediary.set_double_tap_timing(value)

class NumpadMinus_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.NUMPADMINUS_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.NUMPADMINUS_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import NumpadMinus_KEY as _NumpadMinus_KEY
            _NumpadMinus_KEY()

        self._numpadminus_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.NUMPADMINUS_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._numpadminus_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._numpadminus_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._numpadminus_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._numpadminus_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._numpadminus_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._numpadminus_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._numpadminus_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._numpadminus_key_object_intermediary.set_double_tap_timing(value)

class NumpadPlus_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.NUMPADPLUS_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.NUMPADPLUS_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import NumpadPlus_KEY as _NumpadPlus_KEY
            _NumpadPlus_KEY()

        self._numpadplus_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.NUMPADPLUS_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._numpadplus_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._numpadplus_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._numpadplus_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._numpadplus_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._numpadplus_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._numpadplus_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._numpadplus_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._numpadplus_key_object_intermediary.set_double_tap_timing(value)

class NumpadEnter_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.NUMPADENTER_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.NUMPADENTER_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import NumpadEnter_KEY as _NumpadEnter_KEY
            _NumpadEnter_KEY()

        self._numpadenter_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.NUMPADENTER_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._numpadenter_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._numpadenter_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._numpadenter_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._numpadenter_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._numpadenter_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._numpadenter_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._numpadenter_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._numpadenter_key_object_intermediary.set_double_tap_timing(value)

class NumpadEquals_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.NUMPADEQUALS_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.NUMPADEQUALS_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import NumpadEquals_KEY as _NumpadEquals_KEY
            _NumpadEquals_KEY()

        self._numpadequals_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.NUMPADEQUALS_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._numpadequals_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._numpadequals_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._numpadequals_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._numpadequals_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._numpadequals_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._numpadequals_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._numpadequals_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._numpadequals_key_object_intermediary.set_double_tap_timing(value)

class Up_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.UP_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.UP_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Up_KEY as _Up_KEY
            _Up_KEY()

        self._up_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.UP_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._up_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._up_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._up_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._up_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._up_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._up_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._up_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._up_key_object_intermediary.set_double_tap_timing(value)

class Down_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.DOWN_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.DOWN_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Down_KEY as _Down_KEY
            _Down_KEY()

        self._down_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.DOWN_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._down_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._down_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._down_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._down_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._down_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._down_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._down_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._down_key_object_intermediary.set_double_tap_timing(value)

class Right_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.RIGHT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.RIGHT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Right_KEY as _Right_KEY
            _Right_KEY()

        self._right_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.RIGHT_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._right_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._right_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._right_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._right_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._right_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._right_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._right_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._right_key_object_intermediary.set_double_tap_timing(value)

class Left_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.LEFT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.LEFT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Left_KEY as _Left_KEY
            _Left_KEY()

        self._left_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.LEFT_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._left_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._left_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._left_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._left_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._left_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._left_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._left_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._left_key_object_intermediary.set_double_tap_timing(value)

class Insert_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.INSERT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.INSERT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Insert_KEY as _Insert_KEY
            _Insert_KEY()

        self._insert_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.INSERT_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._insert_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._insert_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._insert_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._insert_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._insert_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._insert_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._insert_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._insert_key_object_intermediary.set_double_tap_timing(value)

class Home_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.HOME_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.HOME_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Home_KEY as _Home_KEY
            _Home_KEY()

        self._home_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.HOME_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._home_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._home_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._home_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._home_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._home_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._home_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._home_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._home_key_object_intermediary.set_double_tap_timing(value)

class End_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.END_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.END_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import End_KEY as _End_KEY
            _End_KEY()

        self._end_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.END_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._end_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._end_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._end_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._end_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._end_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._end_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._end_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._end_key_object_intermediary.set_double_tap_timing(value)

class PageUp_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PAGEUP_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PAGEUP_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PageUp_KEY as _PageUp_KEY
            _PageUp_KEY()

        self._pageup_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PAGEUP_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._pageup_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._pageup_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._pageup_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._pageup_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._pageup_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._pageup_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._pageup_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._pageup_key_object_intermediary.set_double_tap_timing(value)

class PageDown_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PAGEDOWN_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PAGEDOWN_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PageDown_KEY as _PageDown_KEY
            _PageDown_KEY()

        self._pagedown_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PAGEDOWN_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._pagedown_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._pagedown_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._pagedown_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._pagedown_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._pagedown_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._pagedown_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._pagedown_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._pagedown_key_object_intermediary.set_double_tap_timing(value)

class Function1_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.FUNCTION1_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.FUNCTION1_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function1_KEY as _Function1_KEY
            _Function1_KEY()

        self._function1_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.FUNCTION1_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._function1_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._function1_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._function1_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._function1_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._function1_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._function1_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._function1_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._function1_key_object_intermediary.set_double_tap_timing(value)

class Function2_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.FUNCTION2_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.FUNCTION2_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function2_KEY as _Function2_KEY
            _Function2_KEY()

        self._function2_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.FUNCTION2_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._function2_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._function2_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._function2_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._function2_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._function2_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._function2_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._function2_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._function2_key_object_intermediary.set_double_tap_timing(value)

class Function3_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.FUNCTION3_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.FUNCTION3_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function3_KEY as _Function3_KEY
            _Function3_KEY()

        self._function3_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.FUNCTION3_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._function3_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._function3_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._function3_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._function3_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._function3_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._function3_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._function3_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._function3_key_object_intermediary.set_double_tap_timing(value)

class Function4_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.FUNCTION4_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.FUNCTION4_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function4_KEY as _Function4_KEY
            _Function4_KEY()

        self._function4_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.FUNCTION4_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._function4_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._function4_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._function4_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._function4_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._function4_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._function4_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._function4_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._function4_key_object_intermediary.set_double_tap_timing(value)

class Function5_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.FUNCTION5_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.FUNCTION5_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function5_KEY as _Function5_KEY
            _Function5_KEY()

        self._function5_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.FUNCTION5_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._function5_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._function5_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._function5_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._function5_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._function5_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._function5_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._function5_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._function5_key_object_intermediary.set_double_tap_timing(value)

class Function6_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.FUNCTION6_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.FUNCTION6_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function6_KEY as _Function6_KEY
            _Function6_KEY()

        self._function6_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.FUNCTION6_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._function6_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._function6_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._function6_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._function6_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._function6_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._function6_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._function6_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._function6_key_object_intermediary.set_double_tap_timing(value)

class Function7_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.FUNCTION7_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.FUNCTION7_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function7_KEY as _Function7_KEY
            _Function7_KEY()

        self._function7_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.FUNCTION7_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._function7_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._function7_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._function7_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._function7_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._function7_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._function7_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._function7_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._function7_key_object_intermediary.set_double_tap_timing(value)

class Function8_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.FUNCTION8_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.FUNCTION8_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function8_KEY as _Function8_KEY
            _Function8_KEY()

        self._function8_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.FUNCTION8_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._function8_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._function8_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._function8_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._function8_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._function8_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._function8_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._function8_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._function8_key_object_intermediary.set_double_tap_timing(value)

class Function9_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.FUNCTION9_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.FUNCTION9_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function9_KEY as _Function9_KEY
            _Function9_KEY()

        self._function9_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.FUNCTION9_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._function9_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._function9_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._function9_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._function9_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._function9_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._function9_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._function9_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._function9_key_object_intermediary.set_double_tap_timing(value)

class Function10_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.FUNCTION10_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.FUNCTION10_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function10_KEY as _Function10_KEY
            _Function10_KEY()

        self._function10_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.FUNCTION10_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._function10_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._function10_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._function10_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._function10_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._function10_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._function10_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._function10_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._function10_key_object_intermediary.set_double_tap_timing(value)

class Function11_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.FUNCTION11_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.FUNCTION11_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function11_KEY as _Function11_KEY
            _Function11_KEY()

        self._function11_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.FUNCTION11_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._function11_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._function11_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._function11_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._function11_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._function11_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._function11_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._function11_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._function11_key_object_intermediary.set_double_tap_timing(value)

class Function12_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.FUNCTION12_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.FUNCTION12_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function12_KEY as _Function12_KEY
            _Function12_KEY()

        self._function12_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.FUNCTION12_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._function12_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._function12_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._function12_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._function12_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._function12_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._function12_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._function12_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._function12_key_object_intermediary.set_double_tap_timing(value)

class Function13_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.FUNCTION13_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.FUNCTION13_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function13_KEY as _Function13_KEY
            _Function13_KEY()

        self._function13_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.FUNCTION13_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._function13_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._function13_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._function13_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._function13_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._function13_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._function13_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._function13_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._function13_key_object_intermediary.set_double_tap_timing(value)

class Function14_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.FUNCTION14_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.FUNCTION14_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function14_KEY as _Function14_KEY
            _Function14_KEY()

        self._function14_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.FUNCTION14_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._function14_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._function14_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._function14_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._function14_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._function14_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._function14_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._function14_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._function14_key_object_intermediary.set_double_tap_timing(value)

class Function15_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.FUNCTION15_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.FUNCTION15_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function15_KEY as _Function15_KEY
            _Function15_KEY()

        self._function15_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.FUNCTION15_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._function15_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._function15_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._function15_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._function15_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._function15_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._function15_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._function15_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._function15_key_object_intermediary.set_double_tap_timing(value)

class NumLock_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.NUMLOCK_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.NUMLOCK_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import NumLock_KEY as _NumLock_KEY
            _NumLock_KEY()

        self._numlock_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.NUMLOCK_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._numlock_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._numlock_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._numlock_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._numlock_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._numlock_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._numlock_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._numlock_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._numlock_key_object_intermediary.set_double_tap_timing(value)

class CapsLock_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.CAPSLOCK_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.CAPSLOCK_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import CapsLock_KEY as _CapsLock_KEY
            _CapsLock_KEY()

        self._capslock_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.CAPSLOCK_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._capslock_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._capslock_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._capslock_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._capslock_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._capslock_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._capslock_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._capslock_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._capslock_key_object_intermediary.set_double_tap_timing(value)

class ScrollLock_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.SCROLLLOCK_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.SCROLLLOCK_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import ScrollLock_KEY as _ScrollLock_KEY
            _ScrollLock_KEY()

        self._scrolllock_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.SCROLLLOCK_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._scrolllock_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._scrolllock_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._scrolllock_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._scrolllock_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._scrolllock_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._scrolllock_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._scrolllock_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._scrolllock_key_object_intermediary.set_double_tap_timing(value)

class RightShift_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.RIGHTSHIFT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.RIGHTSHIFT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import RightShift_KEY as _RightShift_KEY
            _RightShift_KEY()

        self._rightshift_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.RIGHTSHIFT_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._rightshift_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._rightshift_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._rightshift_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._rightshift_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._rightshift_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._rightshift_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._rightshift_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._rightshift_key_object_intermediary.set_double_tap_timing(value)

class LeftShift_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.LEFTSHIFT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.LEFTSHIFT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import LeftShift_KEY as _LeftShift_KEY
            _LeftShift_KEY()

        self._leftshift_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.LEFTSHIFT_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._leftshift_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._leftshift_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._leftshift_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._leftshift_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._leftshift_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._leftshift_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._leftshift_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._leftshift_key_object_intermediary.set_double_tap_timing(value)

class Shift_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.SHIFT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.SHIFT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Shift_KEY as _Shift_KEY
            _Shift_KEY()

        self._shift_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.SHIFT_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._shift_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._shift_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._shift_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._shift_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._shift_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._shift_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._shift_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._shift_key_object_intermediary.set_double_tap_timing(value)

class RightControl_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.RIGHTCONTROL_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.RIGHTCONTROL_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import RightControl_KEY as _RightControl_KEY
            _RightControl_KEY()

        self._rightcontrol_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.RIGHTCONTROL_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._rightcontrol_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._rightcontrol_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._rightcontrol_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._rightcontrol_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._rightcontrol_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._rightcontrol_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._rightcontrol_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._rightcontrol_key_object_intermediary.set_double_tap_timing(value)

class LeftControl_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.LEFTCONTROL_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.LEFTCONTROL_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import LeftControl_KEY as _LeftControl_KEY
            _LeftControl_KEY()

        self._leftcontrol_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.LEFTCONTROL_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._leftcontrol_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._leftcontrol_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._leftcontrol_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._leftcontrol_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._leftcontrol_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._leftcontrol_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._leftcontrol_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._leftcontrol_key_object_intermediary.set_double_tap_timing(value)

class Control_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.CONTROL_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.CONTROL_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Control_KEY as _Control_KEY
            _Control_KEY()

        self._control_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.CONTROL_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._control_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._control_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._control_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._control_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._control_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._control_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._control_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._control_key_object_intermediary.set_double_tap_timing(value)

class RightAlt_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.RIGHTALT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.RIGHTALT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import RightAlt_KEY as _RightAlt_KEY
            _RightAlt_KEY()

        self._rightalt_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.RIGHTALT_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._rightalt_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._rightalt_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._rightalt_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._rightalt_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._rightalt_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._rightalt_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._rightalt_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._rightalt_key_object_intermediary.set_double_tap_timing(value)

class LeftAlt_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.LEFTALT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.LEFTALT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import LeftAlt_KEY as _LeftAlt_KEY
            _LeftAlt_KEY()

        self._leftalt_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.LEFTALT_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._leftalt_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._leftalt_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._leftalt_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._leftalt_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._leftalt_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._leftalt_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._leftalt_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._leftalt_key_object_intermediary.set_double_tap_timing(value)

class Alt_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.ALT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.ALT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Alt_KEY as _Alt_KEY
            _Alt_KEY()

        self._alt_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.ALT_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._alt_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._alt_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._alt_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._alt_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._alt_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._alt_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._alt_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._alt_key_object_intermediary.set_double_tap_timing(value)

class RightMeta_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.RIGHTMETA_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.RIGHTMETA_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import RightMeta_KEY as _RightMeta_KEY
            _RightMeta_KEY()

        self._rightmeta_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.RIGHTMETA_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._rightmeta_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._rightmeta_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._rightmeta_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._rightmeta_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._rightmeta_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._rightmeta_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._rightmeta_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._rightmeta_key_object_intermediary.set_double_tap_timing(value)

class LeftMeta_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.LEFTMETA_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.LEFTMETA_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import LeftMeta_KEY as _LeftMeta_KEY
            _LeftMeta_KEY()

        self._leftmeta_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.LEFTMETA_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._leftmeta_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._leftmeta_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._leftmeta_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._leftmeta_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._leftmeta_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._leftmeta_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._leftmeta_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._leftmeta_key_object_intermediary.set_double_tap_timing(value)

class Meta_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.META_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.META_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Meta_KEY as _Meta_KEY
            _Meta_KEY()

        self._meta_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.META_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._meta_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._meta_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._meta_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._meta_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._meta_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._meta_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._meta_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._meta_key_object_intermediary.set_double_tap_timing(value)

class LeftSuper_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.LEFTSUPER_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.LEFTSUPER_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import LeftSuper_KEY as _LeftSuper_KEY
            _LeftSuper_KEY()

        self._leftsuper_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.LEFTSUPER_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._leftsuper_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._leftsuper_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._leftsuper_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._leftsuper_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._leftsuper_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._leftsuper_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._leftsuper_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._leftsuper_key_object_intermediary.set_double_tap_timing(value)

class RightSuper_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.RIGHTSUPER_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.RIGHTSUPER_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import RightSuper_KEY as _RightSuper_KEY
            _RightSuper_KEY()

        self._rightsuper_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.RIGHTSUPER_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._rightsuper_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._rightsuper_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._rightsuper_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._rightsuper_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._rightsuper_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._rightsuper_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._rightsuper_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._rightsuper_key_object_intermediary.set_double_tap_timing(value)

class Super_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.SUPER_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.SUPER_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Super_KEY as _Super_KEY
            _Super_KEY()

        self._super_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.SUPER_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._super_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._super_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._super_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._super_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._super_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._super_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._super_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._super_key_object_intermediary.set_double_tap_timing(value)

class Mode_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.MODE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.MODE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Mode_KEY as _Mode_KEY
            _Mode_KEY()

        self._mode_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.MODE_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._mode_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._mode_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._mode_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._mode_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._mode_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._mode_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._mode_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._mode_key_object_intermediary.set_double_tap_timing(value)

class Help_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.HELP_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.HELP_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Help_KEY as _Help_KEY
            _Help_KEY()

        self._help_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.HELP_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._help_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._help_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._help_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._help_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._help_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._help_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._help_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._help_key_object_intermediary.set_double_tap_timing(value)

class Print_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.PRINT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.PRINT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Print_KEY as _Print_KEY
            _Print_KEY()

        self._print_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.PRINT_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._print_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._print_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._print_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._print_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._print_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._print_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._print_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._print_key_object_intermediary.set_double_tap_timing(value)

class SystemRequest_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.SYSTEMREQUEST_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.SYSTEMREQUEST_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import SystemRequest_KEY as _SystemRequest_KEY
            _SystemRequest_KEY()

        self._systemrequest_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.SYSTEMREQUEST_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._systemrequest_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._systemrequest_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._systemrequest_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._systemrequest_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._systemrequest_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._systemrequest_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._systemrequest_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._systemrequest_key_object_intermediary.set_double_tap_timing(value)

class Break_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.BREAK_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.BREAK_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Break_KEY as _Break_KEY
            _Break_KEY()

        self._break_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.BREAK_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._break_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._break_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._break_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._break_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._break_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._break_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._break_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._break_key_object_intermediary.set_double_tap_timing(value)

class Menu_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.MENU_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.MENU_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Menu_KEY as _Menu_KEY
            _Menu_KEY()

        self._menu_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.MENU_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._menu_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._menu_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._menu_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._menu_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._menu_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._menu_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._menu_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._menu_key_object_intermediary.set_double_tap_timing(value)

class Power_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.POWER_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.POWER_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Power_KEY as _Power_KEY
            _Power_KEY()

        self._power_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.POWER_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._power_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._power_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._power_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._power_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._power_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._power_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._power_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._power_key_object_intermediary.set_double_tap_timing(value)

class Euro_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.EURO_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.EURO_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Euro_KEY as _Euro_KEY
            _Euro_KEY()

        self._euro_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.EURO_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._euro_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._euro_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._euro_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._euro_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._euro_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._euro_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._euro_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._euro_key_object_intermediary.set_double_tap_timing(value)

class AndroidBack_KEY:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.ANDROIDBACK_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.ANDROIDBACK_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import AndroidBack_KEY as _AndroidBack_KEY
            _AndroidBack_KEY()

        self._androidback_key_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.ANDROIDBACK_KEY_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._androidback_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._androidback_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._androidback_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._androidback_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._androidback_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._androidback_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._androidback_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._androidback_key_object_intermediary.set_double_tap_timing(value)

class LeftButton_MOUSE:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.LEFTBUTTON_MOUSE_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.LEFTBUTTON_MOUSE_OBJECT)
            from pmma.python_src.utility.event_utils import LeftButton_MOUSE as _LeftButton_MOUSE
            _LeftButton_MOUSE()

        self._leftbutton_mouse_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.LEFTBUTTON_MOUSE_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._leftbutton_mouse_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._leftbutton_mouse_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._leftbutton_mouse_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._leftbutton_mouse_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._leftbutton_mouse_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._leftbutton_mouse_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._leftbutton_mouse_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._leftbutton_mouse_object_intermediary.set_double_tap_timing(value)

class MiddleButton_MOUSE:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.MIDDLEBUTTON_MOUSE_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.MIDDLEBUTTON_MOUSE_OBJECT)
            from pmma.python_src.utility.event_utils import MiddleButton_MOUSE as _MiddleButton_MOUSE
            _MiddleButton_MOUSE()

        self._middlebutton_mouse_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.MIDDLEBUTTON_MOUSE_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._middlebutton_mouse_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._middlebutton_mouse_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._middlebutton_mouse_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._middlebutton_mouse_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._middlebutton_mouse_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._middlebutton_mouse_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._middlebutton_mouse_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._middlebutton_mouse_object_intermediary.set_double_tap_timing(value)

class RightButton_MOUSE:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.RIGHTBUTTON_MOUSE_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.RIGHTBUTTON_MOUSE_OBJECT)
            from pmma.python_src.utility.event_utils import RightButton_MOUSE as _RightButton_MOUSE
            _RightButton_MOUSE()

        self._rightbutton_mouse_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.RIGHTBUTTON_MOUSE_OBJECT]

    def set_double_tapped(self, value):
        """
        🟩 **R** -
        """
        self._rightbutton_mouse_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        """
        🟩 **R** -
        """
        return self._rightbutton_mouse_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        """
        🟩 **R** -
        """
        return self._rightbutton_mouse_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        """
        🟩 **R** -
        """
        self._rightbutton_mouse_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        """
        🟩 **R** -
        """
        return self._rightbutton_mouse_object_intermediary.get_pressed()

    def set_pressed(self, value):
        """
        🟩 **R** -
        """
        self._rightbutton_mouse_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        """
        🟩 **R** -
        """
        return self._rightbutton_mouse_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        """
        🟩 **R** -
        """
        self._rightbutton_mouse_object_intermediary.set_double_tap_timing(value)

class Mouse_SCROLL:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.MOUSE_SCROLL_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.MOUSE_SCROLL_OBJECT)
            from pmma.python_src.utility.event_utils import Mouse_SCROLL as _Mouse_SCROLL
            _Mouse_SCROLL()

        self._mouse_scroll_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.MOUSE_SCROLL_OBJECT]

    def get_x_displacement(self):
        """
        🟩 **R** -
        """
        return self._mouse_scroll_object_intermediary.get_x_displacement()

    def set_x_displacement(self, value):
        """
        🟩 **R** -
        """
        self._mouse_scroll_object_intermediary.set_x_displacement(value)

    def get_x_value(self):
        """
        🟩 **R** -
        """
        return self._mouse_scroll_object_intermediary.get_x_value()

    def set_x_value(self, value):
        """
        🟩 **R** -
        """
        self._mouse_scroll_object_intermediary.set_x_value(value)

    def get_y_displacement(self):
        """
        🟩 **R** -
        """
        return self._mouse_scroll_object_intermediary.get_y_displacement()

    def set_y_displacement(self, value):
        """
        🟩 **R** -
        """
        self._mouse_scroll_object_intermediary.set_y_displacement(value)

    def get_y_value(self):
        """
        🟩 **R** -
        """
        return self._mouse_scroll_object_intermediary.get_y_value()

    def set_y_value(self, value):
        """
        🟩 **R** -
        """
        self._mouse_scroll_object_intermediary.set_y_value(value)

class Mouse_POSITION:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.MOUSE_POSITION_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.MOUSE_POSITION_OBJECT)
            from pmma.python_src.utility.event_utils import Mouse_POSITION as _Mouse_POSITION
            _Mouse_POSITION()

        self._mouse_position_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.MOUSE_POSITION_OBJECT]

    def get_axis_displacement(self):
        """
        🟩 **R** -
        """
        return self._mouse_position_object_intermediary.get_axis_displacement()

    def get_x_axis_displacement(self):
        """
        🟩 **R** -
        """
        return self._mouse_position_object_intermediary.get_x_axis_displacement()

    def get_y_axis_displacement(self):
        """
        🟩 **R** -
        """
        return self._mouse_position_object_intermediary.get_y_axis_displacement()

    def get_x_axis(self):
        """
        🟩 **R** -
        """
        return self._mouse_position_object_intermediary.get_x_axis()

    def get_y_axis(self):
        """
        🟩 **R** -
        """
        return self._mouse_position_object_intermediary.get_y_axis()

    def set_x_axis(self, value):
        """
        🟩 **R** -
        """
        self._mouse_position_object_intermediary.set_x_axis(value)

    def set_y_axis(self, value):
        """
        🟩 **R** -
        """
        self._mouse_position_object_intermediary.set_y_axis(value)

    def set_x_axis_displacement(self, value):
        """
        🟩 **R** -
        """
        self._mouse_position_object_intermediary.set_x_axis_displacement(value)

    def set_y_axis_displacement(self, value):
        """
        🟩 **R** -
        """
        self._mouse_position_object_intermediary.set_y_axis_displacement(value)

class Active_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.ACTIVE_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.ACTIVE_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import Active_EVENT as _Active_EVENT
            _Active_EVENT()

        self._active_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.ACTIVE_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._active_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._active_event_object_intermediary.get_value()

class AppTerminating_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")
        self._general_utils__module = _ModuleManager.import_module("pmma.python_src.utility.general_utils")
        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        self._logger = self._logging_utils__module.InternalLogger()
        self._internal_general_utils = self._general_utils__module.GeneralIntermediary()

        if not _InternalConstants.APPTERMINATING_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.APPTERMINATING_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import AppTerminating_EVENT as _AppTerminating_EVENT
            _AppTerminating_EVENT()

        self._appterminatingevent_intermediary = _Registry.pmma_module_spine[_InternalConstants.APPTERMINATING_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._appterminatingevent_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        if self._internal_general_utils.get_operating_system() != _InternalConstants.ANDROID:
            self._logger.log_development("This event is exclusive to the Android operating system. Instead please use: 'Quit_EVENT' as this works across all platforms.")
        return self._appterminatingevent_intermediary.get_value()

class AppLowMemory_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")
        self._general_utils__module = _ModuleManager.import_module("pmma.python_src.utility.general_utils")
        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        self._logger = self._logging_utils__module.InternalLogger()
        self._internal_general_utils = self._general_utils__module.GeneralIntermediary()

        if not _InternalConstants.APPLOWMEMORY_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.APPLOWMEMORY_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import AppLowMemory_EVENT as _AppLowMemory_EVENT
            _AppLowMemory_EVENT()

        self._applowmemory_intermediary = _Registry.pmma_module_spine[_InternalConstants.APPLOWMEMORY_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._applowmemory_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        if self._internal_general_utils.get_operating_system() != _InternalConstants.ANDROID:
            self._logger.log_development("This event is exclusive to the Android operating system. There is no alternative \
to this on other operating systems due to how memory is allocated. If you are interested in getting information about memory, \
I'd recommend checking out PSUtil: https://pypi.org/project/psutil/")
        return self._applowmemory_intermediary.get_value()

class AppWillEnterBackground_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")
        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        self._logger = self._logging_utils__module.InternalLogger()

        if not _InternalConstants.APPWILLENTERBACKGROUND_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.APPWILLENTERBACKGROUND_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import AppWillEnterBackground_EVENT as _AppWillEnterBackground_EVENT
            _AppWillEnterBackground_EVENT()

        self._appwillenterbackground_intermediary = _Registry.pmma_module_spine[_InternalConstants.APPWILLENTERBACKGROUND_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._appwillenterbackground_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        self._logger.log_development("This event is exclusive to the Android operating system. \
There is no alternative to this on other operating systems.")
        return self._appwillenterbackground_intermediary.get_value()

class AppDidEnterBackground_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")
        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        self._logger = self._logging_utils__module.InternalLogger()

        if not _InternalConstants.APPDIDENTERBACKGROUND_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.APPDIDENTERBACKGROUND_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import AppDidEnterBackground_EVENT as _AppDidEnterBackground_EVENT
            _AppDidEnterBackground_EVENT()

        self._appdidenterbackground_intermediary = _Registry.pmma_module_spine[_InternalConstants.APPDIDENTERBACKGROUND_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._appdidenterbackground_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        self._logger.log_development("This event is exclusive to the Android operating system. \
Instead please use: 'WindowFocusLost' as this works across all platforms.")
        return self._appdidenterbackground_intermediary.get_value()

class AppWillEnterForeground_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")
        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        self._logger = self._logging_utils__module.InternalLogger()

        if not _InternalConstants.APPWILLENTERFOREGROUND_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.APPWILLENTERFOREGROUND_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import AppWillEnterForeground_EVENT as _AppWillEnterForeground_EVENT
            _AppWillEnterForeground_EVENT()

        self._appwillenterforeground_intermediary = _Registry.pmma_module_spine[_InternalConstants.APPWILLENTERFOREGROUND_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._appwillenterforeground_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        self._logger.log_development("This event is exclusive to the Android operating system. There is no \
alternative to this on other operating systems.")
        return self._appwillenterforeground_intermediary.get_value()

class AppDidEnterForeground_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")
        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        self._logger = self._logging_utils__module.InternalLogger()

        if not _InternalConstants.APPDIDENTERFOREGROUND_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.APPDIDENTERFOREGROUND_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import AppDidEnterForeground_EVENT as _AppDidEnterForeground_EVENT
            _AppDidEnterForeground_EVENT()

        self._appdidenterforeground_intermediary = _Registry.pmma_module_spine[_InternalConstants.APPDIDENTERFOREGROUND_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._appdidenterforeground_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        self._logger.log_development("This event is exclusive to the Android operating system. Instead please use: 'WindowFocusGained' \
as this works across all platforms.")
        return self._appdidenterforeground_intermediary.get_value()

class AudioDeviceAdded_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.AUDIODEVICEADDED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.AUDIODEVICEADDED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import AudioDeviceAdded_EVENT as _AudioDeviceAdded_EVENT
            _AudioDeviceAdded_EVENT()

        self._audiodeviceadded_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.AUDIODEVICEADDED_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._audiodeviceadded_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._audiodeviceadded_event_object_intermediary.get_value()

class AudioDeviceRemoved_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.AUDIODEVICEREMOVED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.AUDIODEVICEREMOVED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import AudioDeviceRemoved_EVENT as _AudioDeviceRemoved_EVENT
            _AudioDeviceRemoved_EVENT()

        self._audiodeviceremoved_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.AUDIODEVICEREMOVED_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._audiodeviceremoved_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._audiodeviceremoved_event_object_intermediary.get_value()

class ClipBoardUpdate_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.CLIPBOARDUPDATE_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.CLIPBOARDUPDATE_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import ClipBoardUpdate_EVENT as _ClipBoardUpdate_EVENT
            _ClipBoardUpdate_EVENT()

        self._clipboardupdate_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.CLIPBOARDUPDATE_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._clipboardupdate_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._clipboardupdate_event_object_intermediary.get_value()

class DropFile_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.DROPFILE_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.DROPFILE_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import DropFile_EVENT as _DropFile_EVENT
            _DropFile_EVENT()

        self._dropfile_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.DROPFILE_EVENT_OBJECT]

    def set_file(self, file):
        """
        🟩 **R** -
        """
        self._dropfile_event_object_intermediary.set_file(file)

    def get_file(self):
        """
        🟩 **R** -
        """
        return self._dropfile_event_object_intermediary.get_file()

class DropText_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._logging_utils__module = _ModuleManager.import_module("pmma.python_src.utility.logging_utils")
        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        self._logger = self._logging_utils__module.InternalLogger()

        if not _InternalConstants.DROPTEXT_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.DROPTEXT_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import DropText_EVENT as _DropText_EVENT
            _DropText_EVENT()

        self._deoptext_intermediary = _Registry.pmma_module_spine[_InternalConstants.DROPTEXT_EVENT_OBJECT]

    def set_text(self, text):
        """
        🟩 **R** -
        """
        self._deoptext_intermediary.set_text(text)

    def get_text(self):
        """
        🟩 **R** -
        """
        self._logger.log_development("Please note that this event is not yet reliably supported across all \
operating systems. Windows compatability is generally mixed, MacOS compatability is generally good, Linux \
compatability varies based on what desktop envioment is being used and Android support being unofficial and \
limited. Effectively this means that your milage may vary when using this event if it is triggered reliably. \
Generally speaking however, if your developing your application to run on specific hardware - like a games \
console - you can try and use this event, if the event works and the software/hardware is the same, it should \
work more reliably. ALTERNATIVELY, use the 'DropFile_EVENT' event with the user dropping a text file, then \
open and read that for text inputs instead. In short - this event is not known to work reliably, using other \
events instead is recommended!")

        return self._deoptext_intermediary.get_text()

class DropBegin_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.DROPBEGIN_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.DROPBEGIN_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import DropBegin_EVENT as _DropBegin_EVENT
            _DropBegin_EVENT()

        self._dropbegin_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.DROPBEGIN_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._dropbegin_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._dropbegin_event_object_intermediary.get_value()

class DropComplete_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.DROPCOMPLETE_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.DROPCOMPLETE_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import DropComplete_EVENT as _DropComplete_EVENT
            _DropComplete_EVENT()

        self._dropcomplete_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.DROPCOMPLETE_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._dropcomplete_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._dropcomplete_event_object_intermediary.get_value()

class FingerMotion_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.FINGERMOTION_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.FINGERMOTION_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import FingerMotion_EVENT as _FingerMotion_EVENT
            _FingerMotion_EVENT()

        self._fingermotion_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.FINGERMOTION_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._fingermotion_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._fingermotion_event_object_intermediary.get_value()

class FingerDown_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.FINGERDOWN_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.FINGERDOWN_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import FingerDown_EVENT as _FingerDown_EVENT
            _FingerDown_EVENT()

        self._fingerdown_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.FINGERDOWN_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._fingerdown_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._fingerdown_event_object_intermediary.get_value()

class FingerUp_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.FINGERUP_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.FINGERUP_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import FingerUp_EVENT as _FingerUp_EVENT
            _FingerUp_EVENT()

        self._fingerup_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.FINGERUP_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._fingerup_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._fingerup_event_object_intermediary.get_value()

class KeyMapChanged_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.KEYMAPCHANGED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.KEYMAPCHANGED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import KeyMapChanged_EVENT as _KeyMapChanged_EVENT
            _KeyMapChanged_EVENT()

        self._keymapchanged_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.KEYMAPCHANGED_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._keymapchanged_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._keymapchanged_event_object_intermediary.get_value()

class LocaleChanged_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.LOCALECHANGED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.LOCALECHANGED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import LocaleChanged_EVENT as _LocaleChanged_EVENT
            _LocaleChanged_EVENT()

        self._localechanged_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.LOCALECHANGED_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._localechanged_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._localechanged_event_object_intermediary.get_value()

class MultiGesture_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.MULTIGESTURE_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.MULTIGESTURE_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import MultiGesture_EVENT as _MultiGesture_EVENT
            _MultiGesture_EVENT()

        self._multigesture_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.MULTIGESTURE_EVENT_OBJECT]

    def get_gesture_center_x(self):
        """
        🟩 **R** -
        """
        return self._multigesture_event_object_intermediary.get_gesture_center_x()

    def get_gesture_center_y(self):
        """
        🟩 **R** -
        """
        return self._multigesture_event_object_intermediary.get_gesture_center_y()

    def get_pinched_value(self):
        """
        🟩 **R** -
        """
        return self._multigesture_event_object_intermediary.get_pinched_value()

    def get_rotated_value(self):
        """
        🟩 **R** -
        """
        return self._multigesture_event_object_intermediary.get_rotated_value()

    def get_number_of_fingers(self):
        """
        🟩 **R** -
        """
        return self._multigesture_event_object_intermediary.get_number_of_fingers()

    def set_gesture_center_x(self, value):
        """
        🟩 **R** -
        """
        self._multigesture_event_object_intermediary.set_gesture_center_x(value)

    def set_gesture_center_y(self, value):
        """
        🟩 **R** -
        """
        self._multigesture_event_object_intermediary.set_gesture_center_y(value)

    def set_pinched_value(self, value):
        """
        🟩 **R** -
        """
        self._multigesture_event_object_intermediary.set_pinched_value(value)

    def set_rotated_value(self, value):
        """
        🟩 **R** -
        """
        self._multigesture_event_object_intermediary.set_rotated_value(value)

    def set_number_of_fingers(self, value):
        """
        🟩 **R** -
        """
        self._multigesture_event_object_intermediary.set_number_of_fingers(value)

class Quit_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.QUIT_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.QUIT_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import Quit_EVENT as _Quit_EVENT
            _Quit_EVENT()

        self._quit_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.QUIT_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._quit_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._quit_event_object_intermediary.get_value()

class RenderTargetsReset_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.RENDERTARGETSRESET_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.RENDERTARGETSRESET_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import RenderTargetsReset_EVENT as _RenderTargetsReset_EVENT
            _RenderTargetsReset_EVENT()

        self._rendertargetsreset_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.RENDERTARGETSRESET_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._rendertargetsreset_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._rendertargetsreset_event_object_intermediary.get_value()

class RenderDeviceReset_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.RENDERDEVICERESET_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.RENDERDEVICERESET_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import RenderDeviceReset_EVENT as _RenderDeviceReset_EVENT
            _RenderDeviceReset_EVENT()

        self._renderdevicereset_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.RENDERDEVICERESET_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._renderdevicereset_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._renderdevicereset_event_object_intermediary.get_value()

class SysWMEvent_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.SYSWMEVENT_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.SYSWMEVENT_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import SysWMEvent_EVENT as _SysWMEvent_EVENT
            _SysWMEvent_EVENT()

        self._syswmevent_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.SYSWMEVENT_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._syswmevent_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._syswmevent_event_object_intermediary.get_value()

class VideoResize_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.VIDEORESIZE_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.VIDEORESIZE_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import VideoResize_EVENT as _VideoResize_EVENT
            _VideoResize_EVENT()

        self._videoresize_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.VIDEORESIZE_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._videoresize_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._videoresize_event_object_intermediary.get_value()

class VideoExpose_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.VIDEOEXPOSE_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.VIDEOEXPOSE_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import VideoExpose_EVENT as _VideoExpose_EVENT
            _VideoExpose_EVENT()

        self._videoexpose_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.VIDEOEXPOSE_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._videoexpose_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._videoexpose_event_object_intermediary.get_value()

class WindowShown_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.WINDOWSHOWN_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.WINDOWSHOWN_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowShown_EVENT as _WindowShown_EVENT
            _WindowShown_EVENT()

        self._windowshown_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.WINDOWSHOWN_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._windowshown_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._windowshown_event_object_intermediary.get_value()

class WindowHidden_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.WINDOWHIDDEN_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.WINDOWHIDDEN_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowHidden_EVENT as _WindowHidden_EVENT
            _WindowHidden_EVENT()

        self._windowhidden_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.WINDOWHIDDEN_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._windowhidden_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._windowhidden_event_object_intermediary.get_value()

class WindowExposed_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.WINDOWEXPOSED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.WINDOWEXPOSED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowExposed_EVENT as _WindowExposed_EVENT
            _WindowExposed_EVENT()

        self._windowexposed_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.WINDOWEXPOSED_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._windowexposed_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._windowexposed_event_object_intermediary.get_value()

class WindowMoved_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.WINDOWMOVED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.WINDOWMOVED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowMoved_EVENT as _WindowMoved_EVENT
            _WindowMoved_EVENT()

        self._windowmoved_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.WINDOWMOVED_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._windowmoved_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._windowmoved_event_object_intermediary.get_value()

class WindowResized_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.WINDOWRESIZED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.WINDOWRESIZED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowResized_EVENT as _WindowResized_EVENT
            _WindowResized_EVENT()

        self._windowresized_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.WINDOWRESIZED_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._windowresized_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._windowresized_event_object_intermediary.get_value()

class WindowMinimized_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.WINDOWMINIMIZED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.WINDOWMINIMIZED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowMinimized_EVENT as _WindowMinimized_EVENT
            _WindowMinimized_EVENT()

        self._windowminimized_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.WINDOWMINIMIZED_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._windowminimized_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._windowminimized_event_object_intermediary.get_value()

class WindowMaximized_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.WINDOWMAXIMIZED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.WINDOWMAXIMIZED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowMaximized_EVENT as _WindowMaximized_EVENT
            _WindowMaximized_EVENT()

        self._windowmaximized_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.WINDOWMAXIMIZED_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._windowmaximized_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._windowmaximized_event_object_intermediary.get_value()

class WindowRestored_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.WINDOWRESTORED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.WINDOWRESTORED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowRestored_EVENT as _WindowRestored_EVENT
            _WindowRestored_EVENT()

        self._windowrestored_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.WINDOWRESTORED_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._windowrestored_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._windowrestored_event_object_intermediary.get_value()

class WindowEnter_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.WINDOWENTER_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.WINDOWENTER_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowEnter_EVENT as _WindowEnter_EVENT
            _WindowEnter_EVENT()

        self._windowenter_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.WINDOWENTER_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._windowenter_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._windowenter_event_object_intermediary.get_value()

class WindowLeave_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.WINDOWLEAVE_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.WINDOWLEAVE_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowLeave_EVENT as _WindowLeave_EVENT
            _WindowLeave_EVENT()

        self._windowleave_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.WINDOWLEAVE_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._windowleave_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._windowleave_event_object_intermediary.get_value()

class WindowFocusGained_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.WINDOWFOCUSGAINED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.WINDOWFOCUSGAINED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowFocusGained_EVENT as _WindowFocusGained_EVENT
            _WindowFocusGained_EVENT()

        self._windowfocusgained_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.WINDOWFOCUSGAINED_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._windowfocusgained_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._windowfocusgained_event_object_intermediary.get_value()

class WindowFocusLost_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.WINDOWFOCUSLOST_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.WINDOWFOCUSLOST_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowFocusLost_EVENT as _WindowFocusLost_EVENT
            _WindowFocusLost_EVENT()

        self._windowfocuslost_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.WINDOWFOCUSLOST_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._windowfocuslost_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._windowfocuslost_event_object_intermediary.get_value()

class WindowClose_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.WINDOWCLOSE_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.WINDOWCLOSE_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowClose_EVENT as _WindowClose_EVENT
            _WindowClose_EVENT()

        self._windowclose_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.WINDOWCLOSE_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._windowclose_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._windowclose_event_object_intermediary.get_value()

class WindowTakeFocus_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.WINDOWTAKEFOCUS_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.WINDOWTAKEFOCUS_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowTakeFocus_EVENT as _WindowTakeFocus_EVENT
            _WindowTakeFocus_EVENT()

        self._windowtakefocus_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.WINDOWTAKEFOCUS_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._windowtakefocus_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._windowtakefocus_event_object_intermediary.get_value()

class WindowHitTest_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.WINDOWHITTEST_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.WINDOWHITTEST_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowHitTest_EVENT as _WindowHitTest_EVENT
            _WindowHitTest_EVENT()

        self._windowhittest_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.WINDOWHITTEST_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._windowhittest_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._windowhittest_event_object_intermediary.get_value()

class WindowICCPROFChanged_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.WINDOWICCPROFCHANGED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.WINDOWICCPROFCHANGED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowICCPROFChanged_EVENT as _WindowICCPROFChanged_EVENT
            _WindowICCPROFChanged_EVENT()

        self._windowiccprofchanged_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.WINDOWICCPROFCHANGED_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._windowiccprofchanged_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._windowiccprofchanged_event_object_intermediary.get_value()

class WindowDisplayChanged_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.WINDOWDISPLAYCHANGED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.WINDOWDISPLAYCHANGED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowDisplayChanged_EVENT as _WindowDisplayChanged_EVENT
            _WindowDisplayChanged_EVENT()

        self._windowdisplaychanged_event_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.WINDOWDISPLAYCHANGED_EVENT_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._windowdisplaychanged_event_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._windowdisplaychanged_event_object_intermediary.get_value()

class JoyDeviceAdded_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.JOYDEVICEADDED_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.JOYDEVICEADDED_OBJECT)
            from pmma.python_src.utility.event_utils import JoyDeviceAdded_EVENT as _JoyDeviceAdded_EVENT
            _JoyDeviceAdded_EVENT()

        self._joydeviceadded_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.JOYDEVICEADDED_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._joydeviceadded_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._joydeviceadded_object_intermediary.get_value()

class JoyDeviceRemoved_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.JOYDEVICEREMOVED_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.JOYDEVICEREMOVED_OBJECT)
            from pmma.python_src.utility.event_utils import JoyDeviceRemoved_EVENT as _JoyDeviceRemoved_EVENT
            _JoyDeviceRemoved_EVENT()

        self._joydeviceremoved_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.JOYDEVICEREMOVED_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._joydeviceremoved_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._joydeviceremoved_object_intermediary.get_value()

class WindowFullScreenStatusChanged_EVENT:
    """
    🟩 **R** -
    """

    def quit(self):
        """
        🟩 **R** -
        """
        self._shut_down = True

    def __init__(self):
        """
        🟩 **R** -
        """
        _initialize(self)

        self._passport_utils__module = _ModuleManager.import_module("pmma.python_src.utility.passport_utils")

        if not _InternalConstants.WINDOWFULLSCREENSTATECHANGED_OBJECT in _Registry.pmma_module_spine.keys():
            self._passport_utils__module.PassportIntermediary.components_used.append(_InternalConstants.WINDOWFULLSCREENSTATECHANGED_OBJECT)
            from pmma.python_src.utility.event_utils import WindowFullScreenStatusChanged_EVENT as _WindowFullScreenStatusChanged_EVENT
            _WindowFullScreenStatusChanged_EVENT()

        self._windowfullscreenstatechanged_object_intermediary = _Registry.pmma_module_spine[_InternalConstants.WINDOWFULLSCREENSTATECHANGED_OBJECT]

    def set_value(self, value):
        """
        🟩 **R** -
        """
        self._windowfullscreenstatechanged_object_intermediary.set_value(value)

    def get_value(self):
        """
        🟩 **R** -
        """
        return self._windowfullscreenstatechanged_object_intermediary.get_value()