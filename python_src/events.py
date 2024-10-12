from gc import collect as _gc__collect

import pygame as _pygame

from pmma.python_src.general import get_operating_system as _get_operating_system
from pmma.python_src.constants import Constants as _Constants
from pmma.python_src.backpack import Backpack as _Backpack
from pmma.python_src.controller import Controllers as _Controllers

from pmma.python_src.utility.registry_utils import Registry as _Registry
from pmma.python_src.utility.initialization_utils import initialize as _initialize
from pmma.python_src.utility.logging_utils import InternalLogger as _InternalLogger
from pmma.python_src.utility.passport_utils import PassportIntermediary as _PassportIntermediary

class Events:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self, unique_instance=_Constants.EVENTS_OBJECT, add_to_pmma_module_spine=True)

        self._logger = _InternalLogger()

        if _Registry.displayed_pygame_start_message is False:
            _Registry.displayed_pygame_start_message = True
            _Registry.pmma_module_spine[_Constants.LOGGING_INTERMEDIARY_OBJECT].log_information(_Registry.pygame_launch_message)
            _pygame.init()

        self.iteration_id = 0

        self.controllers = _Controllers()

    def handle(self, handle_full_screen_events=True, handle_exit_events=True, grab_extended_keyboard_events=False):
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

            _pygame.event.set_keyboard_grab(True)

        _Registry.handled_events = True

        if _Constants.APPTERMINATING_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.APPTERMINATING_EVENT_OBJECT].set_value(False)

        if _Constants.APPLOWMEMORY_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.APPLOWMEMORY_EVENT_OBJECT].set_value(False)

        if _Constants.APPWILLENTERBACKGROUND_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.APPWILLENTERBACKGROUND_EVENT_OBJECT].set_value(False)

        if _Constants.APPDIDENTERBACKGROUND_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.APPDIDENTERBACKGROUND_EVENT_OBJECT].set_value(False)

        if _Constants.APPWILLENTERFOREGROUND_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.APPWILLENTERFOREGROUND_EVENT_OBJECT].set_value(False)

        if _Constants.APPDIDENTERFOREGROUND_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.APPDIDENTERFOREGROUND_EVENT_OBJECT].set_value(False)

        if _Constants.AUDIODEVICEADDED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.AUDIODEVICEADDED_EVENT_OBJECT].set_value(False)

        if _Constants.AUDIODEVICEREMOVED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.AUDIODEVICEREMOVED_EVENT_OBJECT].set_value(False)

        if _Constants.CLIPBOARDUPDATE_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.CLIPBOARDUPDATE_EVENT_OBJECT].set_value(False)

        if _Constants.DROPFILE_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.DROPFILE_EVENT_OBJECT].set_file(False)

        if _Constants.DROPTEXT_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.DROPTEXT_EVENT_OBJECT].set_text(None)

        if _Constants.DROPBEGIN_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.DROPBEGIN_EVENT_OBJECT].set_value(False)

        if _Constants.DROPCOMPLETE_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.DROPCOMPLETE_EVENT_OBJECT].set_value(False)

        if _Constants.FINGERMOTION_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.FINGERMOTION_EVENT_OBJECT].set_value(False)

        if _Constants.FINGERDOWN_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.FINGERDOWN_EVENT_OBJECT].set_value(False)

        if _Constants.FINGERUP_EVENT_OBJECT in _Registry.pmma_module_spine:
           _Registry.pmma_module_spine[_Constants.FINGERUP_EVENT_OBJECT].set_value(False)

        if _Constants.KEYMAPCHANGED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.KEYMAPCHANGED_EVENT_OBJECT].set_value(False)

        if _Constants.LOCALECHANGED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.LOCALECHANGED_EVENT_OBJECT].set_value(False)

        if _Constants.MULTIGESTURE_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.MULTIGESTURE_EVENT_OBJECT].set_gesture_center_x(None)
            _Registry.pmma_module_spine[_Constants.MULTIGESTURE_EVENT_OBJECT].set_gesture_center_y(None)
            _Registry.pmma_module_spine[_Constants.MULTIGESTURE_EVENT_OBJECT].set_number_of_fingers(None)
            _Registry.pmma_module_spine[_Constants.MULTIGESTURE_EVENT_OBJECT].set_rotated_value(None)
            _Registry.pmma_module_spine[_Constants.MULTIGESTURE_EVENT_OBJECT].set_pinched_value(None)

        if _Constants.QUIT_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.QUIT_EVENT_OBJECT].set_value(False)

        if _Constants.RENDERTARGETSRESET_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.RENDERTARGETSRESET_EVENT_OBJECT].set_value(False)

        if _Constants.RENDERDEVICERESET_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.RENDERDEVICERESET_EVENT_OBJECT].set_value(False)

        if _Constants.SYSWMEVENT_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.SYSWMEVENT_EVENT_OBJECT].set_value(False)

        if _Constants.WINDOWSHOWN_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.WINDOWSHOWN_EVENT_OBJECT].set_value(False)

        if _Constants.WINDOWHIDDEN_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.WINDOWHIDDEN_EVENT_OBJECT].set_value(False)

        if _Constants.WINDOWEXPOSED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.WINDOWEXPOSED_EVENT_OBJECT].set_value(False)

        if _Constants.WINDOWMOVED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.WINDOWMOVED_EVENT_OBJECT].set_value(False)

        if _Constants.WINDOWRESIZED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.WINDOWRESIZED_EVENT_OBJECT].set_value(False)

        if _Constants.WINDOWMINIMIZED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.WINDOWMINIMIZED_EVENT_OBJECT].set_value(False)

        if _Constants.WINDOWMAXIMIZED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.WINDOWMAXIMIZED_EVENT_OBJECT].set_value(False)

        if _Constants.WINDOWRESTORED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.WINDOWRESTORED_EVENT_OBJECT].set_value(False)

        if _Constants.WINDOWENTER_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.WINDOWENTER_EVENT_OBJECT].set_value(False)

        if _Constants.WINDOWLEAVE_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.WINDOWLEAVE_EVENT_OBJECT].set_value(False)

        if _Constants.WINDOWFOCUSGAINED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.WINDOWFOCUSGAINED_EVENT_OBJECT].set_value(False)

        if _Constants.WINDOWFOCUSLOST_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.WINDOWFOCUSLOST_EVENT_OBJECT].set_value(False)

        if _Constants.WINDOWCLOSE_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.WINDOWCLOSE_EVENT_OBJECT].set_value(False)

        if _Constants.WINDOWTAKEFOCUS_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.WINDOWTAKEFOCUS_EVENT_OBJECT].set_value(False)

        if _Constants.WINDOWHITTEST_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.WINDOWHITTEST_EVENT_OBJECT].set_value(False)

        if _Constants.WINDOWICCPROFCHANGED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.WINDOWICCPROFCHANGED_EVENT_OBJECT].set_value(False)

        if _Constants.WINDOWDISPLAYCHANGED_EVENT_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.WINDOWDISPLAYCHANGED_EVENT_OBJECT].set_value(False)

        if _Constants.JOYDEVICEADDED_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.JOYDEVICEADDED_OBJECT].set_value(False)

        if _Constants.JOYDEVICEREMOVED_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.JOYDEVICEREMOVED_OBJECT].set_value(False)

        if _Constants.MOUSE_SCROLL_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.MOUSE_SCROLL_OBJECT].set_x_displacement(0)
            _Registry.pmma_module_spine[_Constants.MOUSE_SCROLL_OBJECT].set_y_displacement(0)

        if _Constants.MOUSE_POSITION_OBJECT in _Registry.pmma_module_spine:
            _Registry.pmma_module_spine[_Constants.MOUSE_POSITION_OBJECT].set_x_axis_displacement(0)
            _Registry.pmma_module_spine[_Constants.MOUSE_POSITION_OBJECT].set_y_axis_displacement(0)

        raw_events = _pygame.event.get()
        for event in raw_events:
            if event.type == _pygame.APP_TERMINATING:
                _Registry.pmma_module_spine[_Constants.APPTERMINATING_EVENT_OBJECT].set_value(True)

            elif event.type == _pygame.APP_LOWMEMORY:
                _Registry.pmma_module_spine[_Constants.APPLOWMEMORY_EVENT_OBJECT].set_value(True)

            elif event.type == _pygame.APP_WILLENTERBACKGROUND:
                _Registry.pmma_module_spine[_Constants.APPWILLENTERBACKGROUND_EVENT_OBJECT].set_value(True)

            elif event.type == _pygame.APP_DIDENTERBACKGROUND:
                _Registry.pmma_module_spine[_Constants.APPDIDENTERBACKGROUND_EVENT_OBJECT].set_value(True)

            elif event.type == _pygame.APP_WILLENTERFOREGROUND:
                _Registry.pmma_module_spine[_Constants.APPWILLENTERFOREGROUND_EVENT_OBJECT].set_value(True)

            elif event.type == _pygame.APP_DIDENTERFOREGROUND:
                _Registry.pmma_module_spine[_Constants.APPDIDENTERFOREGROUND_EVENT_OBJECT].set_value(True)

            elif event.type == _pygame.AUDIODEVICEADDED:
                _Registry.pmma_module_spine[_Constants.AUDIODEVICEADDED_EVENT_OBJECT].set_value(True)

            elif event.type == _pygame.AUDIODEVICEREMOVED:
                _Registry.pmma_module_spine[_Constants.AUDIODEVICEREMOVED_EVENT_OBJECT].set_value(True)

            elif event.type == _pygame.CLIPBOARDUPDATE:
                _Registry.pmma_module_spine[_Constants.CLIPBOARDUPDATE_EVENT_OBJECT].set_value(True)

            elif event.type == _pygame.DROPFILE:
                _Registry.pmma_module_spine[_Constants.DROPFILE_EVENT_OBJECT].set_value(True)

            elif event.type == _pygame.DROPTEXT:
                _Registry.pmma_module_spine[_Constants.DROPTEXT_EVENT_OBJECT].set_value(True)

            elif event.type == _pygame.DROPBEGIN:
                _Registry.pmma_module_spine[_Constants.DROPBEGIN_EVENT_OBJECT].set_value(True)

            elif event.type == _pygame.DROPCOMPLETE:
                _Registry.pmma_module_spine[_Constants.DROPCOMPLETE_EVENT_OBJECT].set_value(True)

            elif event.type == _pygame.FINGERMOTION:
                _Registry.pmma_module_spine[_Constants.FINGERMOTION_EVENT_OBJECT].set_value(True)

            elif event.type == _pygame.FINGERDOWN:
                _Registry.pmma_module_spine[_Constants.FINGERDOWN_EVENT_OBJECT].set_value(True)

            elif event.type == _pygame.FINGERUP:
                _Registry.pmma_module_spine[_Constants.FINGERUP_EVENT_OBJECT].set_value(True)

            elif event.type == _pygame.KEYMAPCHANGED:
                _Registry.pmma_module_spine[_Constants.KEYMAPCHANGED_EVENT_OBJECT].set_value(True)

            elif event.type == _pygame.JOYAXISMOTION:
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

            elif event.type == _pygame.JOYBALLMOTION:
                controller = self.controllers.get_controller(event.joy)
                trackball = controller.get_track_ball_from_id(event.ball)
                x_motion, y_motion = event.rel
                trackball.set_x_motion(x_motion)
                trackball.set_y_motion(y_motion)

            elif event.type == _pygame.JOYBUTTONDOWN:
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

            elif event.type == _pygame.JOYBUTTONUP:
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

            elif event.type == _pygame.JOYDEVICEADDED:
                _Registry.pmma_module_spine[_Constants.JOYDEVICEADDED_OBJECT].set_value(True)
                self.controllers.update_controllers()

            elif event.type == _pygame.JOYDEVICEREMOVED:
                _Registry.pmma_module_spine[_Constants.JOYDEVICEREMOVED_OBJECT].set_value(True)
                self.controllers.update_controllers()

            elif event.type == _pygame.LOCALECHANGED:
                _Registry.pmma_module_spine[_Constants.LOCALECHANGED_EVENT_OBJECT].set_value(True)

            elif event.type == _pygame.MOUSEMOTION:
                mouse_x_position, mouse_y_position = event.pos
                mouse_x_displacement, mouse_y_displacement = event.rel
                _Registry.pmma_module_spine[_Constants.MOUSE_POSITION_OBJECT].set_x_axis(mouse_x_position)
                _Registry.pmma_module_spine[_Constants.MOUSE_POSITION_OBJECT].set_y_axis(mouse_y_position)
                _Registry.pmma_module_spine[_Constants.MOUSE_POSITION_OBJECT].set_x_axis_displacement(mouse_x_displacement)
                _Registry.pmma_module_spine[_Constants.MOUSE_POSITION_OBJECT].set_y_axis_displacement(mouse_y_displacement)

            elif event.type == _pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    _Registry.pmma_module_spine[_Constants.LEFTBUTTON_MOUSE_OBJECT].set_pressed(True)

                elif event.button == 2:
                    _Registry.pmma_module_spine[_Constants.MIDDLEBUTTON_MOUSE_OBJECT].set_pressed(True)

                elif event.button == 3:
                    _Registry.pmma_module_spine[_Constants.RIGHTBUTTON_MOUSE_OBJECT].set_pressed(True)

            elif event.type == _pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    _Registry.pmma_module_spine[_Constants.LEFTBUTTON_MOUSE_OBJECT].set_pressed(False)

                elif event.button == 2:
                    _Registry.pmma_module_spine[_Constants.MIDDLEBUTTON_MOUSE_OBJECT].set_pressed(False)

                elif event.button == 3:
                    _Registry.pmma_module_spine[_Constants.RIGHTBUTTON_MOUSE_OBJECT].set_pressed(False)

            elif event.type == _pygame.MOUSEWHEEL:
                x_displacement = event.precise_x
                y_displacement = event.precise_y
                if event.flipped:
                    x_displacement *= -1
                    y_displacement *= -1
                _Registry.pmma_module_spine[_Constants.MOUSE_SCROLL_OBJECT].set_x_displacement(x_displacement)
                _Registry.pmma_module_spine[_Constants.MOUSE_SCROLL_OBJECT].set_y_displacement(y_displacement)
                total_x = _Registry.pmma_module_spine[_Constants.MOUSE_SCROLL_OBJECT].get_x_value()
                total_y = _Registry.pmma_module_spine[_Constants.MOUSE_SCROLL_OBJECT].get_y_value()
                _Registry.pmma_module_spine[_Constants.MOUSE_SCROLL_OBJECT].set_x_value(total_x + x_displacement)
                _Registry.pmma_module_spine[_Constants.MOUSE_SCROLL_OBJECT].set_y_value(total_y + y_displacement)

            elif event.type == _pygame.KEYDOWN:
                if event.key == _pygame.K_BACKSPACE:
                    _Registry.pmma_module_spine[_Constants.BACKSPACE_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_TAB:
                    _Registry.pmma_module_spine[_Constants.TAB_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_CLEAR:
                    _Registry.pmma_module_spine[_Constants.CLEAR_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_RETURN:
                    _Registry.pmma_module_spine[_Constants.RETURN_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_PAUSE:
                    _Registry.pmma_module_spine[_Constants.PAUSE_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_ESCAPE:
                    _Registry.pmma_module_spine[_Constants.ESCAPE_KEY_OBJECT].set_pressed(True)
                    if handle_exit_events:
                        _Registry.running = False
                        _Backpack.running = False

                elif event.key == _pygame.K_SPACE:
                    _Registry.pmma_module_spine[_Constants.SPACE_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_EXCLAIM:
                    _Registry.pmma_module_spine[_Constants.EXCLAMATIONMARK_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_QUOTEDBL:
                    _Registry.pmma_module_spine[_Constants.DOUBLEQUOTE_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_HASH:
                    _Registry.pmma_module_spine[_Constants.HASHTAG_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_DOLLAR:
                    _Registry.pmma_module_spine[_Constants.DOLLAR_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_AMPERSAND:
                    _Registry.pmma_module_spine[_Constants.AMPERSAND_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_QUOTE:
                    _Registry.pmma_module_spine[_Constants.SINGLEQUOTE_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_LEFTPAREN:
                    _Registry.pmma_module_spine[_Constants.LEFTPARENTHESIS_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_RIGHTPAREN:
                    _Registry.pmma_module_spine[_Constants.RIGHTPARENTHESIS_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_ASTERISK:
                    _Registry.pmma_module_spine[_Constants.ASTERISK_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_PLUS:
                    _Registry.pmma_module_spine[_Constants.PLUS_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_COMMA:
                    _Registry.pmma_module_spine[_Constants.COMMA_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_MINUS:
                    _Registry.pmma_module_spine[_Constants.MINUS_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_PERIOD:
                    _Registry.pmma_module_spine[_Constants.PERIOD_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_SLASH:
                    _Registry.pmma_module_spine[_Constants.FORWARDSLASH_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_0:
                    _Registry.pmma_module_spine[_Constants.PRIMARY0_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_1:
                    _Registry.pmma_module_spine[_Constants.PRIMARY1_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_2:
                    _Registry.pmma_module_spine[_Constants.PRIMARY2_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_3:
                    _Registry.pmma_module_spine[_Constants.PRIMARY3_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_4:
                    _Registry.pmma_module_spine[_Constants.PRIMARY4_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_5:
                    _Registry.pmma_module_spine[_Constants.PRIMARY5_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_6:
                    _Registry.pmma_module_spine[_Constants.PRIMARY6_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_7:
                    _Registry.pmma_module_spine[_Constants.PRIMARY7_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_8:
                    _Registry.pmma_module_spine[_Constants.PRIMARY8_KEY_OBJECT].set_pressed(True)

                elif event.key == _pygame.K_9:
                    self.primary9_key.set_pressed(True)

                elif event.key == _pygame.K_COLON:
                    self.colon_key.set_pressed(True)

                elif event.key == _pygame.K_SEMICOLON:
                    self.semicolon_key.set_pressed(True)

                elif event.key == _pygame.K_LESS:
                    self.lessthan_key.set_pressed(True)

                elif event.key == _pygame.K_EQUALS:
                    self.equals_key.set_pressed(True)

                elif event.key == _pygame.K_GREATER:
                    self.greaterthan_key.set_pressed(True)

                elif event.key == _pygame.K_QUESTION:
                    self.questionmark_key.set_pressed(True)

                elif event.key == _pygame.K_AT:
                    self.at_key.set_pressed(True)

                elif event.key == _pygame.K_LEFTBRACKET:
                    self.leftbracket_key.set_pressed(True)

                elif event.key == _pygame.K_BACKSLASH:
                    self.backslash_key.set_pressed(True)

                elif event.key == _pygame.K_RIGHTBRACKET:
                    self.rightbracket_key.set_pressed(True)

                elif event.key == _pygame.K_CARET:
                    self.caret_key.set_pressed(True)

                elif event.key == _pygame.K_UNDERSCORE:
                    self.underscore_key.set_pressed(True)

                elif event.key == _pygame.K_BACKQUOTE:
                    self.grave_key.set_pressed(True)

                elif event.key == _pygame.K_a:
                    self.primarya_key.set_pressed(True)

                elif event.key == _pygame.K_b:
                    self.primaryb_key.set_pressed(True)

                elif event.key == _pygame.K_c:
                    self.primaryc_key.set_pressed(True)

                elif event.key == _pygame.K_d:
                    self.primaryd_key.set_pressed(True)

                elif event.key == _pygame.K_e:
                    self.primarye_key.set_pressed(True)

                elif event.key == _pygame.K_f:
                    self.primaryf_key.set_pressed(True)

                elif event.key == _pygame.K_g:
                    self.primaryg_key.set_pressed(True)

                elif event.key == _pygame.K_h:
                    self.primaryh_key.set_pressed(True)

                elif event.key == _pygame.K_i:
                    self.primaryi_key.set_pressed(True)

                elif event.key == _pygame.K_j:
                    self.primaryj_key.set_pressed(True)

                elif event.key == _pygame.K_k:
                    self.primaryk_key.set_pressed(True)

                elif event.key == _pygame.K_l:
                    self.primaryl_key.set_pressed(True)

                elif event.key == _pygame.K_m:
                    self.primarym_key.set_pressed(True)

                elif event.key == _pygame.K_n:
                    self.primaryn_key.set_pressed(True)

                elif event.key == _pygame.K_o:
                    self.primaryo_key.set_pressed(True)

                elif event.key == _pygame.K_p:
                    self.primaryp_key.set_pressed(True)

                elif event.key == _pygame.K_q:
                    self.primaryq_key.set_pressed(True)

                elif event.key == _pygame.K_r:
                    self.primaryr_key.set_pressed(True)

                elif event.key == _pygame.K_s:
                    self.primarys_key.set_pressed(True)

                elif event.key == _pygame.K_t:
                    self.primaryt_key.set_pressed(True)

                elif event.key == _pygame.K_u:
                    self.primaryu_key.set_pressed(True)

                elif event.key == _pygame.K_v:
                    self.primaryv_key.set_pressed(True)

                elif event.key == _pygame.K_w:
                    self.primaryw_key.set_pressed(True)

                elif event.key == _pygame.K_x:
                    self.primaryx_key.set_pressed(True)

                elif event.key == _pygame.K_y:
                    self.primaryy_key.set_pressed(True)

                elif event.key == _pygame.K_z:
                    self.primaryz_key.set_pressed(True)

                elif event.key == _pygame.K_DELETE:
                    self.delete_key.set_pressed(True)

                elif event.key == _pygame.K_KP0:
                    self.numpad0_key.set_pressed(True)

                elif event.key == _pygame.K_KP1:
                    self.numpad1_key.set_pressed(True)

                elif event.key == _pygame.K_KP2:
                    self.numpad2_key.set_pressed(True)

                elif event.key == _pygame.K_KP3:
                    self.numpad3_key.set_pressed(True)

                elif event.key == _pygame.K_KP4:
                    self.numpad4_key.set_pressed(True)

                elif event.key == _pygame.K_KP5:
                    self.numpad5_key.set_pressed(True)

                elif event.key == _pygame.K_KP6:
                    self.numpad6_key.set_pressed(True)

                elif event.key == _pygame.K_KP7:
                    self.numpad7_key.set_pressed(True)

                elif event.key == _pygame.K_KP8:
                    self.numpad8_key.set_pressed(True)

                elif event.key == _pygame.K_KP9:
                    self.numpad9_key.set_pressed(True)

                elif event.key == _pygame.K_KP_PERIOD:
                    self.numpadperiod_key.set_pressed(True)

                elif event.key == _pygame.K_KP_DIVIDE:
                    self.numpaddivide_key.set_pressed(True)

                elif event.key == _pygame.K_KP_MULTIPLY:
                    self.numpadmultiply_key.set_pressed(True)

                elif event.key == _pygame.K_KP_MINUS:
                    self.numpadminus_key.set_pressed(True)

                elif event.key == _pygame.K_KP_PLUS:
                    self.numpadplus_key.set_pressed(True)

                elif event.key == _pygame.K_KP_ENTER:
                    self.numpadenter_key.set_pressed(True)

                elif event.key == _pygame.K_KP_EQUALS:
                    self.numpadequals_key.set_pressed(True)

                elif event.key == _pygame.K_UP:
                    self.up_key.set_pressed(True)

                elif event.key == _pygame.K_DOWN:
                    self.down_key.set_pressed(True)

                elif event.key == _pygame.K_RIGHT:
                    self.right_key.set_pressed(True)

                elif event.key == _pygame.K_LEFT:
                    self.left_key.set_pressed(True)

                elif event.key == _pygame.K_INSERT:
                    self.insert_key.set_pressed(True)

                elif event.key == _pygame.K_HOME:
                    self.home_key.set_pressed(True)

                elif event.key == _pygame.K_END:
                    self.end_key.set_pressed(True)

                elif event.key == _pygame.K_PAGEUP:
                    self.pageup_key.set_pressed(True)

                elif event.key == _pygame.K_PAGEDOWN:
                    self.pagedown_key.set_pressed(True)

                elif event.key == _pygame.K_F1:
                    self.function1_key.set_pressed(True)

                elif event.key == _pygame.K_F2:
                    self.function2_key.set_pressed(True)

                elif event.key == _pygame.K_F3:
                    self.function3_key.set_pressed(True)

                elif event.key == _pygame.K_F4:
                    self.function4_key.set_pressed(True)

                elif event.key == _pygame.K_F5:
                    self.function5_key.set_pressed(True)

                elif event.key == _pygame.K_F6:
                    self.function6_key.set_pressed(True)

                elif event.key == _pygame.K_F7:
                    self.function7_key.set_pressed(True)

                elif event.key == _pygame.K_F8:
                    self.function8_key.set_pressed(True)

                elif event.key == _pygame.K_F9:
                    self.function9_key.set_pressed(True)

                elif event.key == _pygame.K_F10:
                    self.function10_key.set_pressed(True)

                elif event.key == _pygame.K_F11:
                    self.function11_key.set_pressed(True)
                    if handle_full_screen_events:
                        if _Registry.display_initialized:
                            _Registry.pmma_module_spine[_Constants.DISPLAY_OBJECT].toggle_full_screen()
                            self.windowresized_event.set_value(True)

                elif event.key == _pygame.K_F12:
                    self.function12_key.set_pressed(True)

                elif event.key == _pygame.K_F13:
                    self.function13_key.set_pressed(True)

                elif event.key == _pygame.K_F14:
                    self.function14_key.set_pressed(True)

                elif event.key == _pygame.K_F15:
                    self.function15_key.set_pressed(True)

                elif event.key == _pygame.K_NUMLOCK:
                    self.numlock_key.set_pressed(True)

                elif event.key == _pygame.K_CAPSLOCK:
                    self.capslock_key.set_pressed(True)

                elif event.key == _pygame.K_SCROLLOCK:
                    self.scrolllock_key.set_pressed(True)

                elif event.key == _pygame.K_RSHIFT:
                    self.rightshift_key.set_pressed(True)

                elif event.key == _pygame.K_LSHIFT:
                    self.leftshift_key.set_pressed(True)

                elif event.key == _pygame.K_RCTRL:
                    self.rightcontrol_key.set_pressed(True)

                elif event.key == _pygame.K_LCTRL:
                    self.leftcontrol_key.set_pressed(True)

                elif event.key == _pygame.K_RALT:
                    self.rightalt_key.set_pressed(True)

                elif event.key == _pygame.K_LALT:
                    self.leftalt_key.set_pressed(True)

                elif event.key == _pygame.K_RMETA:
                    self.rightmeta_key.set_pressed(True)

                elif event.key == _pygame.K_LMETA:
                    self.leftmeta_key.set_pressed(True)

                elif event.key == _pygame.K_LSUPER:
                    self.leftsuper_key.set_pressed(True)

                elif event.key == _pygame.K_RSUPER:
                    self.rightsuper_key.set_pressed(True)

                elif event.key == _pygame.K_MODE:
                    self.mode_key.set_pressed(True)

                elif event.key == _pygame.K_HELP:
                    self.help_key.set_pressed(True)

                elif event.key == _pygame.K_PRINT:
                    self.print_key.set_pressed(True)

                elif event.key == _pygame.K_SYSREQ:
                    self.systemrequest_key.set_pressed(True)

                elif event.key == _pygame.K_BREAK:
                    self.break_key.set_pressed(True)

                elif event.key == _pygame.K_MENU:
                    self.menu_key.set_pressed(True)

                elif event.key == _pygame.K_POWER:
                    self.power_key.set_pressed(True)

                elif event.key == _pygame.K_EURO:
                    self.euro_key.set_pressed(True)

                elif event.key == _pygame.K_AC_BACK:
                    self.androidback_key.set_pressed(True)

            elif event.type == _pygame.KEYUP:
                if event.key == _pygame.K_BACKSPACE:
                    self.backspace_key.set_pressed(False)

                elif event.key == _pygame.K_TAB:
                    self.tab_key.set_pressed(False)

                elif event.key == _pygame.K_CLEAR:
                    self.clear_key.set_pressed(False)

                elif event.key == _pygame.K_RETURN:
                    self.return_key.set_pressed(False)

                elif event.key == _pygame.K_PAUSE:
                    self.pause_key.set_pressed(False)

                elif event.key == _pygame.K_ESCAPE:
                    self.escape_key.set_pressed(False)

                elif event.key == _pygame.K_SPACE:
                    self.space_key.set_pressed(False)

                elif event.key == _pygame.K_EXCLAIM:
                    self.exclamationmark_key.set_pressed(False)

                elif event.key == _pygame.K_QUOTEDBL:
                    self.doublequote_key.set_pressed(False)

                elif event.key == _pygame.K_HASH:
                    self.hash_key.set_pressed(False)

                elif event.key == _pygame.K_DOLLAR:
                    self.dollar_key.set_pressed(False)

                elif event.key == _pygame.K_AMPERSAND:
                    self.ampersand_key.set_pressed(False)

                elif event.key == _pygame.K_QUOTE:
                    self.singlequote_key.set_pressed(False)

                elif event.key == _pygame.K_LEFTPAREN:
                    self.leftparenthesis_key.set_pressed(False)

                elif event.key == _pygame.K_RIGHTPAREN:
                    self.rightparenthesis_key.set_pressed(False)

                elif event.key == _pygame.K_ASTERISK:
                    self.asterisk_key.set_pressed(False)

                elif event.key == _pygame.K_PLUS:
                    self.plus_key.set_pressed(False)

                elif event.key == _pygame.K_COMMA:
                    self.comma_key.set_pressed(False)

                elif event.key == _pygame.K_MINUS:
                    self.minus_key.set_pressed(False)

                elif event.key == _pygame.K_PERIOD:
                    self.period_key.set_pressed(False)

                elif event.key == _pygame.K_SLASH:
                    self.forwardslash_key.set_pressed(False)

                elif event.key == _pygame.K_0:
                    self.primary0_key.set_pressed(False)

                elif event.key == _pygame.K_1:
                    self.primary1_key.set_pressed(False)

                elif event.key == _pygame.K_2:
                    self.primary2_key.set_pressed(False)

                elif event.key == _pygame.K_3:
                    self.primary3_key.set_pressed(False)

                elif event.key == _pygame.K_4:
                    self.primary4_key.set_pressed(False)

                elif event.key == _pygame.K_5:
                    self.primary5_key.set_pressed(False)

                elif event.key == _pygame.K_6:
                    self.primary6_key.set_pressed(False)

                elif event.key == _pygame.K_7:
                    self.primary7_key.set_pressed(False)

                elif event.key == _pygame.K_8:
                    self.primary8_key.set_pressed(False)

                elif event.key == _pygame.K_9:
                    self.primary9_key.set_pressed(False)

                elif event.key == _pygame.K_COLON:
                    self.colon_key.set_pressed(False)

                elif event.key == _pygame.K_SEMICOLON:
                    self.semicolon_key.set_pressed(False)

                elif event.key == _pygame.K_LESS:
                    self.lessthan_key.set_pressed(False)

                elif event.key == _pygame.K_EQUALS:
                    self.equals_key.set_pressed(False)

                elif event.key == _pygame.K_GREATER:
                    self.greaterthan_key.set_pressed(False)

                elif event.key == _pygame.K_QUESTION:
                    self.questionmark_key.set_pressed(False)

                elif event.key == _pygame.K_AT:
                    self.at_key.set_pressed(False)

                elif event.key == _pygame.K_LEFTBRACKET:
                    self.leftbracket_key.set_pressed(False)

                elif event.key == _pygame.K_BACKSLASH:
                    self.backslash_key.set_pressed(False)

                elif event.key == _pygame.K_RIGHTBRACKET:
                    self.rightbracket_key.set_pressed(False)

                elif event.key == _pygame.K_CARET:
                    self.caret_key.set_pressed(False)

                elif event.key == _pygame.K_UNDERSCORE:
                    self.underscore_key.set_pressed(False)

                elif event.key == _pygame.K_BACKQUOTE:
                    self.grave_key.set_pressed(False)

                elif event.key == _pygame.K_a:
                    self.primarya_key.set_pressed(False)

                elif event.key == _pygame.K_b:
                    self.primaryb_key.set_pressed(False)

                elif event.key == _pygame.K_c:
                    self.primaryc_key.set_pressed(False)

                elif event.key == _pygame.K_d:
                    self.primaryd_key.set_pressed(False)

                elif event.key == _pygame.K_e:
                    self.primarye_key.set_pressed(False)

                elif event.key == _pygame.K_f:
                    self.primaryf_key.set_pressed(False)

                elif event.key == _pygame.K_g:
                    self.primaryg_key.set_pressed(False)

                elif event.key == _pygame.K_h:
                    self.primaryh_key.set_pressed(False)

                elif event.key == _pygame.K_i:
                    self.primaryi_key.set_pressed(False)

                elif event.key == _pygame.K_j:
                    self.primaryj_key.set_pressed(False)

                elif event.key == _pygame.K_k:
                    self.primaryk_key.set_pressed(False)

                elif event.key == _pygame.K_l:
                    self.primaryl_key.set_pressed(False)

                elif event.key == _pygame.K_m:
                    self.primarym_key.set_pressed(False)

                elif event.key == _pygame.K_n:
                    self.primaryn_key.set_pressed(False)

                elif event.key == _pygame.K_o:
                    self.primaryo_key.set_pressed(False)

                elif event.key == _pygame.K_p:
                    self.primaryp_key.set_pressed(False)

                elif event.key == _pygame.K_q:
                    self.primaryq_key.set_pressed(False)

                elif event.key == _pygame.K_r:
                    self.primaryr_key.set_pressed(False)

                elif event.key == _pygame.K_s:
                    self.primarys_key.set_pressed(False)

                elif event.key == _pygame.K_t:
                    self.primaryt_key.set_pressed(False)

                elif event.key == _pygame.K_u:
                    self.primaryu_key.set_pressed(False)

                elif event.key == _pygame.K_v:
                    self.primaryv_key.set_pressed(False)

                elif event.key == _pygame.K_w:
                    self.primaryw_key.set_pressed(False)

                elif event.key == _pygame.K_x:
                    self.primaryx_key.set_pressed(False)

                elif event.key == _pygame.K_y:
                    self.primaryy_key.set_pressed(False)

                elif event.key == _pygame.K_z:
                    self.primaryz_key.set_pressed(False)

                elif event.key == _pygame.K_DELETE:
                    self.delete_key.set_pressed(False)

                elif event.key == _pygame.K_KP0:
                    self.numpad0_key.set_pressed(False)

                elif event.key == _pygame.K_KP1:
                    self.numpad1_key.set_pressed(False)

                elif event.key == _pygame.K_KP2:
                    self.numpad2_key.set_pressed(False)

                elif event.key == _pygame.K_KP3:
                    self.numpad3_key.set_pressed(False)

                elif event.key == _pygame.K_KP4:
                    self.numpad4_key.set_pressed(False)

                elif event.key == _pygame.K_KP5:
                    self.numpad5_key.set_pressed(False)

                elif event.key == _pygame.K_KP6:
                    self.numpad6_key.set_pressed(False)

                elif event.key == _pygame.K_KP7:
                    self.numpad7_key.set_pressed(False)

                elif event.key == _pygame.K_KP8:
                    self.numpad8_key.set_pressed(False)

                elif event.key == _pygame.K_KP9:
                    self.numpad9_key.set_pressed(False)

                elif event.key == _pygame.K_KP_PERIOD:
                    self.numpadperiod_key.set_pressed(False)

                elif event.key == _pygame.K_KP_DIVIDE:
                    self.numpaddivide_key.set_pressed(False)

                elif event.key == _pygame.K_KP_MULTIPLY:
                    self.numpadmultiply_key.set_pressed(False)

                elif event.key == _pygame.K_KP_MINUS:
                    self.numpadminus_key.set_pressed(False)

                elif event.key == _pygame.K_KP_PLUS:
                    self.numpadplus_key.set_pressed(False)

                elif event.key == _pygame.K_KP_ENTER:
                    self.numpadenter_key.set_pressed(False)

                elif event.key == _pygame.K_KP_EQUALS:
                    self.numpadequals_key.set_pressed(False)

                elif event.key == _pygame.K_UP:
                    self.up_key.set_pressed(False)

                elif event.key == _pygame.K_DOWN:
                    self.down_key.set_pressed(False)

                elif event.key == _pygame.K_RIGHT:
                    self.right_key.set_pressed(False)

                elif event.key == _pygame.K_LEFT:
                    self.left_key.set_pressed(False)

                elif event.key == _pygame.K_INSERT:
                    self.insert_key.set_pressed(False)

                elif event.key == _pygame.K_HOME:
                    self.home_key.set_pressed(False)

                elif event.key == _pygame.K_END:
                    self.end_key.set_pressed(False)

                elif event.key == _pygame.K_PAGEUP:
                    self.pageup_key.set_pressed(False)

                elif event.key == _pygame.K_PAGEDOWN:
                    self.pagedown_key.set_pressed(False)

                elif event.key == _pygame.K_F1:
                    self.function1_key.set_pressed(False)

                elif event.key == _pygame.K_F2:
                    self.function2_key.set_pressed(False)

                elif event.key == _pygame.K_F3:
                    self.function3_key.set_pressed(False)

                elif event.key == _pygame.K_F4:
                    self.function4_key.set_pressed(False)

                elif event.key == _pygame.K_F5:
                    self.function5_key.set_pressed(False)

                elif event.key == _pygame.K_F6:
                    self.function6_key.set_pressed(False)

                elif event.key == _pygame.K_F7:
                    self.function7_key.set_pressed(False)

                elif event.key == _pygame.K_F8:
                    self.function8_key.set_pressed(False)

                elif event.key == _pygame.K_F9:
                    self.function9_key.set_pressed(False)

                elif event.key == _pygame.K_F10:
                    self.function10_key.set_pressed(False)

                elif event.key == _pygame.K_F11:
                    self.function11_key.set_pressed(False)

                elif event.key == _pygame.K_F12:
                    self.function12_key.set_pressed(False)

                elif event.key == _pygame.K_F13:
                    self.function13_key.set_pressed(False)

                elif event.key == _pygame.K_F14:
                    self.function14_key.set_pressed(False)

                elif event.key == _pygame.K_F15:
                    self.function15_key.set_pressed(False)

                elif event.key == _pygame.K_NUMLOCK:
                    self.numlock_key.set_pressed(False)

                elif event.key == _pygame.K_CAPSLOCK:
                    self.capslock_key.set_pressed(False)

                elif event.key == _pygame.K_SCROLLOCK:
                    self.scrolllock_key.set_pressed(False)

                elif event.key == _pygame.K_RSHIFT:
                    self.rightshift_key.set_pressed(False)

                elif event.key == _pygame.K_LSHIFT:
                    self.leftshift_key.set_pressed(False)

                elif event.key == _pygame.K_RCTRL:
                    self.rightcontrol_key.set_pressed(False)

                elif event.key == _pygame.K_LCTRL:
                    self.leftcontrol_key.set_pressed(False)

                elif event.key == _pygame.K_RALT:
                    self.rightalt_key.set_pressed(False)

                elif event.key == _pygame.K_LALT:
                    self.leftalt_key.set_pressed(False)

                elif event.key == _pygame.K_RMETA:
                    self.rightmeta_key.set_pressed(False)

                elif event.key == _pygame.K_LMETA:
                    self.leftmeta_key.set_pressed(False)

                elif event.key == _pygame.K_LSUPER:
                    self.leftsuper_key.set_pressed(False)

                elif event.key == _pygame.K_RSUPER:
                    self.rightsuper_key.set_pressed(False)

                elif event.key == _pygame.K_MODE:
                    self.mode_key.set_pressed(False)

                elif event.key == _pygame.K_HELP:
                    self.help_key.set_pressed(False)

                elif event.key == _pygame.K_PRINT:
                    self.print_key.set_pressed(False)

                elif event.key == _pygame.K_SYSREQ:
                    self.systemrequest_key.set_pressed(False)

                elif event.key == _pygame.K_BREAK:
                    self.break_key.set_pressed(False)

                elif event.key == _pygame.K_MENU:
                    self.menu_key.set_pressed(False)

                elif event.key == _pygame.K_POWER:
                    self.power_key.set_pressed(False)

                elif event.key == _pygame.K_EURO:
                    self.euro_key.set_pressed(False)

                elif event.key == _pygame.K_AC_BACK:
                    self.androidback_key.set_pressed(False)

            elif event.type == _pygame.MULTIGESTURE:
                self.multigesture_event.set_gesture_center_x(event.x)
                self.multigesture_event.set_gesture_center_y(event.y)
                self.multigesture_event.set_number_of_fingers(event.num_fingers)
                self.multigesture_event.set_rotated_value(event.rotated)
                self.multigesture_event.set_pinched_value(event.pinched)

            elif event.type == _pygame.QUIT:
                self.quit_event.set_value(True)
                if handle_exit_events:
                    _Registry.running = False
                    _Backpack.running = False

            elif event.type == _pygame.RENDER_TARGETS_RESET:
                self.rendertargetsreset_event.set_value(True)

            elif event.type == _pygame.RENDER_DEVICE_RESET:
                self.renderdevicereset_event.set_value(True)

            elif event.type == _pygame.SYSWMEVENT:
                self.syswmevent_event.set_value(True)

            elif event.type == _pygame.WINDOWSHOWN:
                self.windowshown_event.set_value(True)

            elif event.type == _pygame.WINDOWHIDDEN:
                self.windowhidden_event.set_value(True)

            elif event.type == _pygame.WINDOWEXPOSED:
                self.windowexposed_event.set_value(True)

            elif event.type == _pygame.WINDOWMOVED:
                self.windowmoved_event.set_value(True)

            elif event.type == _pygame.WINDOWRESIZED or event.type == _pygame.WINDOWSIZECHANGED:
                self.windowresized_event.set_value(True)

            elif event.type == _pygame.WINDOWMINIMIZED:
                self.windowminimized_event.set_value(True)

            elif event.type == _pygame.WINDOWMAXIMIZED:
                self.windowmaximized_event.set_value(True)

            elif event.type == _pygame.WINDOWRESTORED:
                self.windowrestored_event.set_value(True)

            elif event.type == _pygame.WINDOWENTER:
                self.windowenter_event.set_value(True)

            elif event.type == _pygame.WINDOWLEAVE:
                self.windowleave_event.set_value(True)

            elif event.type == _pygame.WINDOWFOCUSGAINED:
                self.windowfocusgained_event.set_value(True)

            elif event.type == _pygame.WINDOWFOCUSLOST:
                self.windowfocuslost_event.set_value(True)

            elif event.type == _pygame.WINDOWCLOSE:
                self.windowclose_event.set_value(True)

            elif event.type == _pygame.WINDOWTAKEFOCUS:
                self.windowtakefocus_event.set_value(True)

            elif event.type == _pygame.WINDOWHITTEST:
                self.windowhittest_event.set_value(True)

            elif event.type == _pygame.WINDOWICCPROFCHANGED:
                self.windowiccprofchanged_event.set_value(True)

            elif event.type == _pygame.WINDOWDISPLAYCHANGED:
                self.windowdisplaychanged_event.set_value(True)

class Backspace_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)

        if not _Constants.BACKSPACE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.BACKSPACE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Backspace_KEY as _Backspace_KEY
            _Backspace_KEY()

        self._backspace_key_object_intermediary = _Registry.pmma_module_spine[_Constants.BACKSPACE_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._backspace_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._backspace_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._backspace_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._backspace_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return _Registry.pmma_module_spine[_Constants.BACKSPACE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        self._backspace_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._backspace_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._backspace_key_object_intermediary.set_double_tap_timing(value)

class Tab_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.TAB_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.TAB_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Tab_KEY as _Tab_KEY
            _Tab_KEY()

        self._tab_key_object_intermediary = _Registry.pmma_module_spine[_Constants.TAB_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._tab_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._tab_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._tab_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._tab_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._tab_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._tab_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._tab_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._tab_key_object_intermediary.set_double_tap_timing(value)

class Clear_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.CLEAR_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.CLEAR_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Clear_KEY as _Clear_KEY
            _Clear_KEY()

        self._clear_key_object_intermediary = _Registry.pmma_module_spine[_Constants.CLEAR_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._clear_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._clear_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._clear_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._clear_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._clear_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._clear_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._clear_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._clear_key_object_intermediary.set_double_tap_timing(value)

class Return_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.RETURN_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.RETURN_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Return_KEY as _Return_KEY
            _Return_KEY()

        self._return_key_object_intermediary = _Registry.pmma_module_spine[_Constants.RETURN_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._return_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._return_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._return_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._return_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._return_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._return_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._return_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._return_key_object_intermediary.set_double_tap_timing(value)

class Pause_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PAUSE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PAUSE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Pause_KEY as _Pause_KEY
            _Pause_KEY()

        self._pause_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PAUSE_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._pause_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._pause_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._pause_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._pause_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._pause_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._pause_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._pause_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._pause_key_object_intermediary.set_double_tap_timing(value)

class Escape_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.ESCAPE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.ESCAPE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Escape_KEY as _Escape_KEY
            _Escape_KEY()

        self._escape_key_object_intermediary = _Registry.pmma_module_spine[_Constants.ESCAPE_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._escape_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._escape_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._escape_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._escape_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._escape_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._escape_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._escape_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._escape_key_object_intermediary.set_double_tap_timing(value)

class Space_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.SPACE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.SPACE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Space_KEY as _Space_KEY
            _Space_KEY()

        self._space_key_object_intermediary = _Registry.pmma_module_spine[_Constants.SPACE_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._space_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._space_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._space_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._space_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._space_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._space_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._space_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._space_key_object_intermediary.set_double_tap_timing(value)

class ExclamationMark_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.EXCLAMATIONMARK_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.EXCLAMATIONMARK_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import ExclamationMark_KEY as _ExclamationMark_KEY
            _ExclamationMark_KEY()

        self._exclamationmark_key_object_intermediary = _Registry.pmma_module_spine[_Constants.EXCLAMATIONMARK_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._exclamationmark_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._exclamationmark_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._exclamationmark_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._exclamationmark_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._exclamationmark_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._exclamationmark_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._exclamationmark_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._exclamationmark_key_object_intermediary.set_double_tap_timing(value)

class DoubleQuote_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.DOUBLEQUOTE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.DOUBLEQUOTE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import DoubleQuote_KEY as _DoubleQuote_KEY
            _DoubleQuote_KEY()

        self._doublequote_key_object_intermediary = _Registry.pmma_module_spine[_Constants.DOUBLEQUOTE_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._doublequote_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._doublequote_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._doublequote_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._doublequote_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._doublequote_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._doublequote_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._doublequote_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._doublequote_key_object_intermediary.set_double_tap_timing(value)

class Hashtag_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.HASHTAG_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.HASHTAG_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Hashtag_KEY as _Hashtag_KEY
            _Hashtag_KEY()

        self._hashtag_key_object_intermediary = _Registry.pmma_module_spine[_Constants.HASHTAG_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._hashtag_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._hashtag_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._hashtag_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._hashtag_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._hashtag_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._hashtag_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._hashtag_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._hashtag_key_object_intermediary.set_double_tap_timing(value)

class Dollar_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.DOLLAR_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.DOLLAR_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Dollar_KEY as _Dollar_KEY
            _Dollar_KEY()

        self._dollar_key_object_intermediary = _Registry.pmma_module_spine[_Constants.DOLLAR_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._dollar_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._dollar_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._dollar_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._dollar_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._dollar_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._dollar_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._dollar_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._dollar_key_object_intermediary.set_double_tap_timing(value)

class Ampersand_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.AMPERSAND_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.AMPERSAND_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Ampersand_KEY as _Ampersand_KEY
            _Ampersand_KEY()

        self._ampersand_key_object_intermediary = _Registry.pmma_module_spine[_Constants.AMPERSAND_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._ampersand_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._ampersand_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._ampersand_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._ampersand_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._ampersand_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._ampersand_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._ampersand_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._ampersand_key_object_intermediary.set_double_tap_timing(value)

class SingleQuote_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.SINGLEQUOTE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.SINGLEQUOTE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import SingleQuote_KEY as _SingleQuote_KEY
            _SingleQuote_KEY()

        self._singlequote_key_object_intermediary = _Registry.pmma_module_spine[_Constants.SINGLEQUOTE_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._singlequote_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._singlequote_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._singlequote_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._singlequote_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._singlequote_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._singlequote_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._singlequote_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._singlequote_key_object_intermediary.set_double_tap_timing(value)

class LeftParenthesis_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.LEFTPARENTHESIS_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.LEFTPARENTHESIS_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import LeftParenthesis_KEY as _LeftParenthesis_KEY
            _LeftParenthesis_KEY()

        self._leftparenthesis_key_object_intermediary = _Registry.pmma_module_spine[_Constants.LEFTPARENTHESIS_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._leftparenthesis_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._leftparenthesis_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._leftparenthesis_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._leftparenthesis_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._leftparenthesis_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._leftparenthesis_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._leftparenthesis_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._leftparenthesis_key_object_intermediary.set_double_tap_timing(value)

class RightParenthesis_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.RIGHTPARENTHESIS_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.RIGHTPARENTHESIS_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import RightParenthesis_KEY as _RightParenthesis_KEY
            _RightParenthesis_KEY()

        self._rightparenthesis_key_object_intermediary = _Registry.pmma_module_spine[_Constants.RIGHTPARENTHESIS_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._rightparenthesis_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._rightparenthesis_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._rightparenthesis_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._rightparenthesis_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._rightparenthesis_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._rightparenthesis_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._rightparenthesis_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._rightparenthesis_key_object_intermediary.set_double_tap_timing(value)

class Asterisk_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.ASTERISK_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.ASTERISK_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Asterisk_KEY as _Asterisk_KEY
            _Asterisk_KEY()

        self._asterisk_key_object_intermediary = _Registry.pmma_module_spine[_Constants.ASTERISK_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._asterisk_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._asterisk_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._asterisk_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._asterisk_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._asterisk_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._asterisk_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._asterisk_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._asterisk_key_object_intermediary.set_double_tap_timing(value)

class Plus_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PLUS_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PLUS_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Plus_KEY as _Plus_KEY
            _Plus_KEY()

        self._plus_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PLUS_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._plus_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._plus_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._plus_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._plus_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._plus_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._plus_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._plus_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._plus_key_object_intermediary.set_double_tap_timing(value)

class Comma_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.COMMA_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.COMMA_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Comma_KEY as _Comma_KEY
            _Comma_KEY()

        self._comma_key_object_intermediary = _Registry.pmma_module_spine[_Constants.COMMA_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._comma_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._comma_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._comma_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._comma_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._comma_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._comma_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._comma_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._comma_key_object_intermediary.set_double_tap_timing(value)

class Minus_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.MINUS_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.MINUS_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Minus_KEY as _Minus_KEY
            _Minus_KEY()

        self._minus_key_object_intermediary = _Registry.pmma_module_spine[_Constants.MINUS_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._minus_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._minus_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._minus_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._minus_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._minus_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._minus_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._minus_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._minus_key_object_intermediary.set_double_tap_timing(value)

class Period_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PERIOD_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PERIOD_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Period_KEY as _Period_KEY
            _Period_KEY()

        self._period_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PERIOD_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._period_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._period_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._period_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._period_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._period_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._period_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._period_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._period_key_object_intermediary.set_double_tap_timing(value)

class ForwardSlash_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.FORWARDSLASH_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.FORWARDSLASH_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import ForwardSlash_KEY as _ForwardSlash_KEY
            _ForwardSlash_KEY()

        self._forwardslash_key_object_intermediary = _Registry.pmma_module_spine[_Constants.FORWARDSLASH_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._forwardslash_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._forwardslash_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._forwardslash_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._forwardslash_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._forwardslash_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._forwardslash_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._forwardslash_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._forwardslash_key_object_intermediary.set_double_tap_timing(value)

class Primary0_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARY0_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARY0_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary0_KEY as _Primary0_KEY
            _Primary0_KEY()

        self._primary0_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARY0_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primary0_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primary0_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primary0_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primary0_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primary0_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primary0_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primary0_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primary0_key_object_intermediary.set_double_tap_timing(value)

class Primary1_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARY1_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARY1_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary1_KEY as _Primary1_KEY
            _Primary1_KEY()

        self._primary1_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARY1_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primary1_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primary1_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primary1_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primary1_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primary1_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primary1_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primary1_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primary1_key_object_intermediary.set_double_tap_timing(value)

class Primary2_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARY2_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARY2_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary2_KEY as _Primary2_KEY
            _Primary2_KEY()

        self._primary2_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARY2_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primary2_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primary2_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primary2_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primary2_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primary2_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primary2_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primary2_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primary2_key_object_intermediary.set_double_tap_timing(value)

class Primary3_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARY3_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARY3_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary3_KEY as _Primary3_KEY
            _Primary3_KEY()

        self._primary3_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARY3_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primary3_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primary3_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primary3_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primary3_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primary3_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primary3_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primary3_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primary3_key_object_intermediary.set_double_tap_timing(value)

class Primary4_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARY4_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARY4_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary4_KEY as _Primary4_KEY
            _Primary4_KEY()

        self._primary4_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARY4_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primary4_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primary4_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primary4_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primary4_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primary4_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primary4_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primary4_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primary4_key_object_intermediary.set_double_tap_timing(value)

class Primary5_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARY5_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARY5_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary5_KEY as _Primary5_KEY
            _Primary5_KEY()

        self._primary5_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARY5_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primary5_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primary5_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primary5_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primary5_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primary5_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primary5_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primary5_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primary5_key_object_intermediary.set_double_tap_timing(value)

class Primary6_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARY6_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARY6_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary6_KEY as _Primary6_KEY
            _Primary6_KEY()

        self._primary6_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARY6_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primary6_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primary6_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primary6_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primary6_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primary6_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primary6_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primary6_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primary6_key_object_intermediary.set_double_tap_timing(value)

class Primary7_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARY7_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARY7_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary7_KEY as _Primary7_KEY
            _Primary7_KEY()

        self._primary7_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARY7_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primary7_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primary7_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primary7_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primary7_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primary7_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primary7_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primary7_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primary7_key_object_intermediary.set_double_tap_timing(value)

class Primary8_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARY8_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARY8_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary8_KEY as _Primary8_KEY
            _Primary8_KEY()

        self._primary8_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARY8_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primary8_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primary8_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primary8_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primary8_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primary8_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primary8_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primary8_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primary8_key_object_intermediary.set_double_tap_timing(value)

class Primary9_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARY9_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARY9_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Primary9_KEY as _Primary9_KEY
            _Primary9_KEY()

        self._primary9_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARY9_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primary9_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primary9_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primary9_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primary9_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primary9_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primary9_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primary9_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primary9_key_object_intermediary.set_double_tap_timing(value)

class Colon_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.COLON_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.COLON_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Colon_KEY as _Colon_KEY
            _Colon_KEY()

        self._colon_key_object_intermediary = _Registry.pmma_module_spine[_Constants.COLON_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._colon_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._colon_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._colon_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._colon_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._colon_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._colon_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._colon_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._colon_key_object_intermediary.set_double_tap_timing(value)

class SemiColon_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.SEMICOLON_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.SEMICOLON_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import SemiColon_KEY as _SemiColon_KEY
            _SemiColon_KEY()

        self._semicolon_key_object_intermediary = _Registry.pmma_module_spine[_Constants.SEMICOLON_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._semicolon_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._semicolon_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._semicolon_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._semicolon_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._semicolon_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._semicolon_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._semicolon_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._semicolon_key_object_intermediary.set_double_tap_timing(value)

class LessThan_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.LESSTHAN_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.LESSTHAN_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import LessThan_KEY as _LessThan_KEY
            _LessThan_KEY()

        self._lessthan_key_object_intermediary = _Registry.pmma_module_spine[_Constants.LESSTHAN_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._lessthan_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._lessthan_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._lessthan_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._lessthan_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._lessthan_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._lessthan_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._lessthan_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._lessthan_key_object_intermediary.set_double_tap_timing(value)

class Equals_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.EQUALS_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.EQUALS_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Equals_KEY as _Equals_KEY
            _Equals_KEY()

        self._equals_key_object_intermediary = _Registry.pmma_module_spine[_Constants.EQUALS_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._equals_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._equals_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._equals_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._equals_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._equals_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._equals_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._equals_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._equals_key_object_intermediary.set_double_tap_timing(value)

class GreaterThan_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.GREATERTHAN_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.GREATERTHAN_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import GreaterThan_KEY as _GreaterThan_KEY
            _GreaterThan_KEY()

        self._greaterthan_key_object_intermediary = _Registry.pmma_module_spine[_Constants.GREATERTHAN_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._greaterthan_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._greaterthan_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._greaterthan_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._greaterthan_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._greaterthan_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._greaterthan_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._greaterthan_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._greaterthan_key_object_intermediary.set_double_tap_timing(value)

class QuestionMark_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.QUESTIONMARK_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.QUESTIONMARK_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import QuestionMark_KEY as _QuestionMark_KEY
            _QuestionMark_KEY()

        self._questionmark_key_object_intermediary = _Registry.pmma_module_spine[_Constants.QUESTIONMARK_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._questionmark_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._questionmark_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._questionmark_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._questionmark_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._questionmark_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._questionmark_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._questionmark_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._questionmark_key_object_intermediary.set_double_tap_timing(value)

class At_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.AT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.AT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import At_KEY as _At_KEY
            _At_KEY()

        self._at_key_object_intermediary = _Registry.pmma_module_spine[_Constants.AT_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._at_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._at_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._at_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._at_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._at_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._at_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._at_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._at_key_object_intermediary.set_double_tap_timing(value)

class LeftBracket_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.LEFTBRACKET_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.LEFTBRACKET_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import LeftBracket_KEY as _LeftBracket_KEY
            _LeftBracket_KEY()

        self._leftbracket_key_object_intermediary = _Registry.pmma_module_spine[_Constants.LEFTBRACKET_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._leftbracket_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._leftbracket_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._leftbracket_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._leftbracket_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._leftbracket_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._leftbracket_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._leftbracket_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._leftbracket_key_object_intermediary.set_double_tap_timing(value)

class BackSlash_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.BACKSLASH_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.BACKSLASH_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import BackSlash_KEY as _BackSlash_KEY
            _BackSlash_KEY()

        self._backslash_key_object_intermediary = _Registry.pmma_module_spine[_Constants.BACKSLASH_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._backslash_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._backslash_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._backslash_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._backslash_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._backslash_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._backslash_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._backslash_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._backslash_key_object_intermediary.set_double_tap_timing(value)

class RightBracket_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.RIGHTBRACKET_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.RIGHTBRACKET_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import RightBracket_KEY as _RightBracket_KEY
            _RightBracket_KEY()

        self._rightbracket_key_object_intermediary = _Registry.pmma_module_spine[_Constants.RIGHTBRACKET_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._rightbracket_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._rightbracket_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._rightbracket_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._rightbracket_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._rightbracket_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._rightbracket_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._rightbracket_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._rightbracket_key_object_intermediary.set_double_tap_timing(value)

class Caret_KEY: # ^
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.CARET_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.CARET_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Caret_KEY as _Caret_KEY
            _Caret_KEY()

        self._caret_key_object_intermediary = _Registry.pmma_module_spine[_Constants.CARET_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._caret_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._caret_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._caret_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._caret_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._caret_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._caret_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._caret_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._caret_key_object_intermediary.set_double_tap_timing(value)

class Underscore_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.UNDERSCORE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.UNDERSCORE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Underscore_KEY as _Underscore_KEY
            _Underscore_KEY()

        self._underscore_key_object_intermediary = _Registry.pmma_module_spine[_Constants.UNDERSCORE_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._underscore_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._underscore_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._underscore_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._underscore_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._underscore_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._underscore_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._underscore_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._underscore_key_object_intermediary.set_double_tap_timing(value)

class Grave_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.GRAVE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.GRAVE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Grave_KEY as _Grave_KEY
            _Grave_KEY()

        self._grave_key_object_intermediary = _Registry.pmma_module_spine[_Constants.GRAVE_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._grave_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._grave_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._grave_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._grave_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._grave_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._grave_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._grave_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._grave_key_object_intermediary.set_double_tap_timing(value)

class PrimaryA_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYA_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYA_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryA_KEY as _PrimaryA_KEY
            _PrimaryA_KEY()

        self._primarya_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYA_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primarya_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primarya_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primarya_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primarya_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primarya_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primarya_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primarya_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primarya_key_object_intermediary.set_double_tap_timing(value)

class PrimaryB_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYB_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYB_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryB_KEY as _PrimaryB_KEY
            _PrimaryB_KEY()

        self._primaryb_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYB_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryb_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryb_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryb_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryb_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryb_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryb_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryb_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryb_key_object_intermediary.set_double_tap_timing(value)

class PrimaryC_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYC_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYC_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryC_KEY as _PrimaryC_KEY
            _PrimaryC_KEY()

        self._primaryc_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYC_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryc_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryc_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryc_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryc_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryc_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryc_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryc_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryc_key_object_intermediary.set_double_tap_timing(value)

class PrimaryD_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYD_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYD_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryD_KEY as _PrimaryD_KEY
            _PrimaryD_KEY()

        self._primaryd_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYD_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryd_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryd_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryd_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryd_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryd_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryd_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryd_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryd_key_object_intermediary.set_double_tap_timing(value)

class PrimaryE_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryE_KEY as _PrimaryE_KEY
            _PrimaryE_KEY()

        self._primarye_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYE_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primarye_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primarye_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primarye_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primarye_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primarye_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primarye_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primarye_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primarye_key_object_intermediary.set_double_tap_timing(value)

class PrimaryF_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYF_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYF_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryF_KEY as _PrimaryF_KEY
            _PrimaryF_KEY()

        self._primaryf_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYF_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryf_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryf_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryf_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryf_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryf_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryf_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryf_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryf_key_object_intermediary.set_double_tap_timing(value)

class PrimaryG_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYG_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYG_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryG_KEY as _PrimaryG_KEY
            _PrimaryG_KEY()

        self._primaryg_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYG_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryg_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryg_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryg_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryg_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryg_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryg_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryg_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryg_key_object_intermediary.set_double_tap_timing(value)

class PrimaryH_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYH_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYH_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryH_KEY as _PrimaryH_KEY
            _PrimaryH_KEY()

        self._primaryh_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYH_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryh_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryh_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryh_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryh_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryh_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryh_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryh_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryh_key_object_intermediary.set_double_tap_timing(value)

class PrimaryI_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYI_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYI_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryI_KEY as _PrimaryI_KEY
            _PrimaryI_KEY()

        self._primaryi_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYI_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryi_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryi_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryi_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryi_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryi_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryi_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryi_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryi_key_object_intermediary.set_double_tap_timing(value)

class PrimaryJ_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYJ_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYJ_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryJ_KEY as _PrimaryJ_KEY
            _PrimaryJ_KEY()

        self._primaryj_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYJ_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryj_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryj_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryj_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryj_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryj_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryj_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryj_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryj_key_object_intermediary.set_double_tap_timing(value)

class PrimaryK_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYK_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYK_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryK_KEY as _PrimaryK_KEY
            _PrimaryK_KEY()

        self._primaryk_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYK_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryk_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryk_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryk_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryk_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryk_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryk_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryk_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryk_key_object_intermediary.set_double_tap_timing(value)

class PrimaryL_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYL_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYL_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryL_KEY as _PrimaryL_KEY
            _PrimaryL_KEY()

        self._primaryl_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYL_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryl_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryl_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryl_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryl_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryl_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryl_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryl_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryl_key_object_intermediary.set_double_tap_timing(value)

class PrimaryM_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYM_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYM_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryM_KEY as _PrimaryM_KEY
            _PrimaryM_KEY()

        self._primarym_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYM_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primarym_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primarym_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primarym_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primarym_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primarym_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primarym_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primarym_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primarym_key_object_intermediary.set_double_tap_timing(value)

class PrimaryN_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYN_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYN_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryN_KEY as _PrimaryN_KEY
            _PrimaryN_KEY()

        self._primaryn_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYN_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryn_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryn_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryn_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryn_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryn_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryn_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryn_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryn_key_object_intermediary.set_double_tap_timing(value)

class PrimaryO_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYO_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYO_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryO_KEY as _PrimaryO_KEY
            _PrimaryO_KEY()

        self._primaryo_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYO_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryo_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryo_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryo_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryo_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryo_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryo_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryo_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryo_key_object_intermediary.set_double_tap_timing(value)

class PrimaryP_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYP_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYP_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryP_KEY as _PrimaryP_KEY
            _PrimaryP_KEY()

        self._primaryp_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYP_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryp_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryp_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryp_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryp_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryp_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryp_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryp_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryp_key_object_intermediary.set_double_tap_timing(value)

class PrimaryQ_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYQ_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYQ_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryQ_KEY as _PrimaryQ_KEY
            _PrimaryQ_KEY()

        self._primaryq_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYQ_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryq_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryq_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryq_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryq_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryq_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryq_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryq_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryq_key_object_intermediary.set_double_tap_timing(value)

class PrimaryR_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYR_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYR_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryR_KEY as _PrimaryR_KEY
            _PrimaryR_KEY()

        self._primaryr_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYR_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryr_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryr_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryr_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryr_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryr_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryr_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryr_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryr_key_object_intermediary.set_double_tap_timing(value)

class PrimaryS_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYS_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYS_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryS_KEY as _PrimaryS_KEY
            _PrimaryS_KEY()

        self._primarys_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYS_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primarys_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primarys_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primarys_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primarys_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primarys_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primarys_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primarys_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primarys_key_object_intermediary.set_double_tap_timing(value)

class PrimaryT_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryT_KEY as _PrimaryT_KEY
            _PrimaryT_KEY()

        self._primaryt_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYT_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryt_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryt_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryt_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryt_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryt_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryt_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryt_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryt_key_object_intermediary.set_double_tap_timing(value)

class PrimaryU_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYU_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYU_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryU_KEY as _PrimaryU_KEY
            _PrimaryU_KEY()

        self._primaryu_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYU_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryu_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryu_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryu_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryu_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryu_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryu_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryu_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryu_key_object_intermediary.set_double_tap_timing(value)

class PrimaryV_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYV_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYV_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryV_KEY as _PrimaryV_KEY
            _PrimaryV_KEY()

        self._primaryv_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYV_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryv_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryv_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryv_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryv_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryv_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryv_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryv_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryv_key_object_intermediary.set_double_tap_timing(value)

class PrimaryW_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYW_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYW_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryW_KEY as _PrimaryW_KEY
            _PrimaryW_KEY()

        self._primaryw_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYW_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryw_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryw_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryw_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryw_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryw_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryw_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryw_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryw_key_object_intermediary.set_double_tap_timing(value)

class PrimaryX_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYX_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYX_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryX_KEY as _PrimaryX_KEY
            _PrimaryX_KEY()

        self._primaryx_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYX_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryx_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryx_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryx_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryx_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryx_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryx_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryx_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryx_key_object_intermediary.set_double_tap_timing(value)

class PrimaryY_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYY_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYY_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryY_KEY as _PrimaryY_KEY
            _PrimaryY_KEY()

        self._primaryy_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYY_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryy_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryy_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryy_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryy_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryy_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryy_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryy_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryy_key_object_intermediary.set_double_tap_timing(value)

class PrimaryZ_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRIMARYZ_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRIMARYZ_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PrimaryZ_KEY as _PrimaryZ_KEY
            _PrimaryZ_KEY()

        self._primaryz_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRIMARYZ_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._primaryz_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._primaryz_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._primaryz_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._primaryz_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._primaryz_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._primaryz_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._primaryz_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._primaryz_key_object_intermediary.set_double_tap_timing(value)

class Delete_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.DELETE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.DELETE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Delete_KEY as _Delete_KEY
            _Delete_KEY()

        self._delete_key_object_intermediary = _Registry.pmma_module_spine[_Constants.DELETE_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._delete_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._delete_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._delete_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._delete_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._delete_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._delete_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._delete_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._delete_key_object_intermediary.set_double_tap_timing(value)

class Numpad0_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.NUMPAD0_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.NUMPAD0_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad0_KEY as _Numpad0_KEY
            _Numpad0_KEY()

        self._numpad0_key_object_intermediary = _Registry.pmma_module_spine[_Constants.NUMPAD0_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._numpad0_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._numpad0_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._numpad0_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._numpad0_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._numpad0_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._numpad0_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._numpad0_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._numpad0_key_object_intermediary.set_double_tap_timing(value)

class Numpad1_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.NUMPAD1_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.NUMPAD1_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad1_KEY as _Numpad1_KEY
            _Numpad1_KEY()

        self._numpad1_key_object_intermediary = _Registry.pmma_module_spine[_Constants.NUMPAD1_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._numpad1_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._numpad1_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._numpad1_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._numpad1_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._numpad1_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._numpad1_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._numpad1_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._numpad1_key_object_intermediary.set_double_tap_timing(value)

class Numpad2_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.NUMPAD2_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.NUMPAD2_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad2_KEY as _Numpad2_KEY
            _Numpad2_KEY()

        self._numpad2_key_object_intermediary = _Registry.pmma_module_spine[_Constants.NUMPAD2_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._numpad2_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._numpad2_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._numpad2_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._numpad2_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._numpad2_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._numpad2_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._numpad2_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._numpad2_key_object_intermediary.set_double_tap_timing(value)

class Numpad3_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.NUMPAD3_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.NUMPAD3_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad3_KEY as _Numpad3_KEY
            _Numpad3_KEY()

        self._numpad3_key_object_intermediary = _Registry.pmma_module_spine[_Constants.NUMPAD3_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._numpad3_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._numpad3_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._numpad3_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._numpad3_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._numpad3_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._numpad3_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._numpad3_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._numpad3_key_object_intermediary.set_double_tap_timing(value)

class Numpad4_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.NUMPAD4_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.NUMPAD4_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad4_KEY as _Numpad4_KEY
            _Numpad4_KEY()

        self._numpad4_key_object_intermediary = _Registry.pmma_module_spine[_Constants.NUMPAD4_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._numpad4_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._numpad4_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._numpad4_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._numpad4_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._numpad4_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._numpad4_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._numpad4_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._numpad4_key_object_intermediary.set_double_tap_timing(value)

class Numpad5_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.NUMPAD5_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.NUMPAD5_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad5_KEY as _Numpad5_KEY
            _Numpad5_KEY()

        self._numpad5_key_object_intermediary = _Registry.pmma_module_spine[_Constants.NUMPAD5_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._numpad5_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._numpad5_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._numpad5_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._numpad5_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._numpad5_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._numpad5_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._numpad5_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._numpad5_key_object_intermediary.set_double_tap_timing(value)

class Numpad6_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.NUMPAD6_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.NUMPAD6_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad6_KEY as _Numpad6_KEY
            _Numpad6_KEY()

        self._numpad6_key_object_intermediary = _Registry.pmma_module_spine[_Constants.NUMPAD6_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._numpad6_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._numpad6_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._numpad6_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._numpad6_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._numpad6_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._numpad6_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._numpad6_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._numpad6_key_object_intermediary.set_double_tap_timing(value)

class Numpad7_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.NUMPAD7_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.NUMPAD7_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad7_KEY as _Numpad7_KEY
            _Numpad7_KEY()

        self._numpad7_key_object_intermediary = _Registry.pmma_module_spine[_Constants.NUMPAD7_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._numpad7_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._numpad7_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._numpad7_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._numpad7_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._numpad7_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._numpad7_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._numpad7_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._numpad7_key_object_intermediary.set_double_tap_timing(value)

class Numpad8_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.NUMPAD8_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.NUMPAD8_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad8_KEY as _Numpad8_KEY
            _Numpad8_KEY()

        self._numpad8_key_object_intermediary = _Registry.pmma_module_spine[_Constants.NUMPAD8_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._numpad8_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._numpad8_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._numpad8_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._numpad8_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._numpad8_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._numpad8_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._numpad8_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._numpad8_key_object_intermediary.set_double_tap_timing(value)

class Numpad9_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.NUMPAD9_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.NUMPAD9_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Numpad9_KEY as _Numpad9_KEY
            _Numpad9_KEY()

        self._numpad9_key_object_intermediary = _Registry.pmma_module_spine[_Constants.NUMPAD9_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._numpad9_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._numpad9_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._numpad9_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._numpad9_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._numpad9_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._numpad9_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._numpad9_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._numpad9_key_object_intermediary.set_double_tap_timing(value)

class NumpadPeriod_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.NUMPADPERIOD_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.NUMPADPERIOD_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import NumpadPeriod_KEY as _NumpadPeriod_KEY
            _NumpadPeriod_KEY()

        self._numpadperiod_key_object_intermediary = _Registry.pmma_module_spine[_Constants.NUMPADPERIOD_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._numpadperiod_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._numpadperiod_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._numpadperiod_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._numpadperiod_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._numpadperiod_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._numpadperiod_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._numpadperiod_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._numpadperiod_key_object_intermediary.set_double_tap_timing(value)

class NumpadDivide_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.NUMPADDIVIDE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.NUMPADDIVIDE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import NumpadDivide_KEY as _NumpadDivide_KEY
            _NumpadDivide_KEY()

        self._numpaddivide_key_object_intermediary = _Registry.pmma_module_spine[_Constants.NUMPADDIVIDE_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._numpaddivide_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._numpaddivide_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._numpaddivide_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._numpaddivide_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._numpaddivide_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._numpaddivide_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._numpaddivide_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._numpaddivide_key_object_intermediary.set_double_tap_timing(value)

class NumpadMultiply_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.NUMPADMULTIPLY_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.NUMPADMULTIPLY_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import NumpadMultiply_KEY as _NumpadMultiply_KEY
            _NumpadMultiply_KEY()

        self._numpadmultiply_key_object_intermediary = _Registry.pmma_module_spine[_Constants.NUMPADMULTIPLY_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._numpadmultiply_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._numpadmultiply_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._numpadmultiply_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._numpadmultiply_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._numpadmultiply_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._numpadmultiply_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._numpadmultiply_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._numpadmultiply_key_object_intermediary.set_double_tap_timing(value)

class NumpadMinus_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.NUMPADMINUS_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.NUMPADMINUS_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import NumpadMinus_KEY as _NumpadMinus_KEY
            _NumpadMinus_KEY()

        self._numpadminus_key_object_intermediary = _Registry.pmma_module_spine[_Constants.NUMPADMINUS_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._numpadminus_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._numpadminus_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._numpadminus_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._numpadminus_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._numpadminus_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._numpadminus_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._numpadminus_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._numpadminus_key_object_intermediary.set_double_tap_timing(value)

class NumpadPlus_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.NUMPADPLUS_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.NUMPADPLUS_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import NumpadPlus_KEY as _NumpadPlus_KEY
            _NumpadPlus_KEY()

        self._numpadplus_key_object_intermediary = _Registry.pmma_module_spine[_Constants.NUMPADPLUS_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._numpadplus_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._numpadplus_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._numpadplus_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._numpadplus_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._numpadplus_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._numpadplus_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._numpadplus_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._numpadplus_key_object_intermediary.set_double_tap_timing(value)

class NumpadEnter_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.NUMPADENTER_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.NUMPADENTER_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import NumpadEnter_KEY as _NumpadEnter_KEY
            _NumpadEnter_KEY()

        self._numpadenter_key_object_intermediary = _Registry.pmma_module_spine[_Constants.NUMPADENTER_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._numpadenter_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._numpadenter_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._numpadenter_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._numpadenter_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._numpadenter_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._numpadenter_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._numpadenter_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._numpadenter_key_object_intermediary.set_double_tap_timing(value)

class NumpadEquals_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.NUMPADEQUALS_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.NUMPADEQUALS_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import NumpadEquals_KEY as _NumpadEquals_KEY
            _NumpadEquals_KEY()

        self._numpadequals_key_object_intermediary = _Registry.pmma_module_spine[_Constants.NUMPADEQUALS_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._numpadequals_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._numpadequals_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._numpadequals_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._numpadequals_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._numpadequals_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._numpadequals_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._numpadequals_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._numpadequals_key_object_intermediary.set_double_tap_timing(value)

class Up_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.UP_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.UP_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Up_KEY as _Up_KEY
            _Up_KEY()

        self._up_key_object_intermediary = _Registry.pmma_module_spine[_Constants.UP_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._up_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._up_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._up_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._up_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._up_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._up_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._up_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._up_key_object_intermediary.set_double_tap_timing(value)

class Down_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.DOWN_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.DOWN_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Down_KEY as _Down_KEY
            _Down_KEY()

        self._down_key_object_intermediary = _Registry.pmma_module_spine[_Constants.DOWN_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._down_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._down_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._down_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._down_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._down_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._down_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._down_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._down_key_object_intermediary.set_double_tap_timing(value)

class Right_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.RIGHT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.RIGHT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Right_KEY as _Right_KEY
            _Right_KEY()

        self._right_key_object_intermediary = _Registry.pmma_module_spine[_Constants.RIGHT_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._right_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._right_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._right_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._right_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._right_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._right_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._right_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._right_key_object_intermediary.set_double_tap_timing(value)

class Left_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.LEFT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.LEFT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Left_KEY as _Left_KEY
            _Left_KEY()

        self._left_key_object_intermediary = _Registry.pmma_module_spine[_Constants.LEFT_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._left_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._left_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._left_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._left_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._left_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._left_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._left_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._left_key_object_intermediary.set_double_tap_timing(value)

class Insert_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.INSERT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.INSERT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Insert_KEY as _Insert_KEY
            _Insert_KEY()

        self._insert_key_object_intermediary = _Registry.pmma_module_spine[_Constants.INSERT_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._insert_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._insert_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._insert_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._insert_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._insert_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._insert_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._insert_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._insert_key_object_intermediary.set_double_tap_timing(value)

class Home_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.HOME_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.HOME_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Home_KEY as _Home_KEY
            _Home_KEY()

        self._home_key_object_intermediary = _Registry.pmma_module_spine[_Constants.HOME_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._home_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._home_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._home_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._home_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._home_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._home_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._home_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._home_key_object_intermediary.set_double_tap_timing(value)

class End_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.END_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.END_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import End_KEY as _End_KEY
            _End_KEY()

        self._end_key_object_intermediary = _Registry.pmma_module_spine[_Constants.END_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._end_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._end_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._end_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._end_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._end_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._end_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._end_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._end_key_object_intermediary.set_double_tap_timing(value)

class PageUp_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PAGEUP_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PAGEUP_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PageUp_KEY as _PageUp_KEY
            _PageUp_KEY()

        self._pageup_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PAGEUP_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._pageup_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._pageup_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._pageup_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._pageup_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._pageup_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._pageup_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._pageup_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._pageup_key_object_intermediary.set_double_tap_timing(value)

class PageDown_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PAGEDOWN_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PAGEDOWN_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import PageDown_KEY as _PageDown_KEY
            _PageDown_KEY()

        self._pagedown_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PAGEDOWN_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._pagedown_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._pagedown_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._pagedown_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._pagedown_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._pagedown_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._pagedown_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._pagedown_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._pagedown_key_object_intermediary.set_double_tap_timing(value)

class Function1_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.FUNCTION1_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.FUNCTION1_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function1_KEY as _Function1_KEY
            _Function1_KEY()

        self._function1_key_object_intermediary = _Registry.pmma_module_spine[_Constants.FUNCTION1_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._function1_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._function1_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._function1_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._function1_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._function1_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._function1_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._function1_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._function1_key_object_intermediary.set_double_tap_timing(value)

class Function2_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.FUNCTION2_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.FUNCTION2_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function2_KEY as _Function2_KEY
            _Function2_KEY()

        self._function2_key_object_intermediary = _Registry.pmma_module_spine[_Constants.FUNCTION2_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._function2_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._function2_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._function2_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._function2_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._function2_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._function2_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._function2_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._function2_key_object_intermediary.set_double_tap_timing(value)

class Function3_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.FUNCTION3_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.FUNCTION3_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function3_KEY as _Function3_KEY
            _Function3_KEY()

        self._function3_key_object_intermediary = _Registry.pmma_module_spine[_Constants.FUNCTION3_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._function3_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._function3_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._function3_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._function3_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._function3_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._function3_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._function3_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._function3_key_object_intermediary.set_double_tap_timing(value)

class Function4_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.FUNCTION4_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.FUNCTION4_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function4_KEY as _Function4_KEY
            _Function4_KEY()

        self._function4_key_object_intermediary = _Registry.pmma_module_spine[_Constants.FUNCTION4_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._function4_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._function4_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._function4_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._function4_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._function4_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._function4_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._function4_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._function4_key_object_intermediary.set_double_tap_timing(value)

class Function5_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.FUNCTION5_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.FUNCTION5_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function5_KEY as _Function5_KEY
            _Function5_KEY()

        self._function5_key_object_intermediary = _Registry.pmma_module_spine[_Constants.FUNCTION5_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._function5_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._function5_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._function5_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._function5_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._function5_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._function5_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._function5_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._function5_key_object_intermediary.set_double_tap_timing(value)

class Function6_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.FUNCTION6_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.FUNCTION6_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function6_KEY as _Function6_KEY
            _Function6_KEY()

        self._function6_key_object_intermediary = _Registry.pmma_module_spine[_Constants.FUNCTION6_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._function6_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._function6_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._function6_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._function6_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._function6_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._function6_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._function6_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._function6_key_object_intermediary.set_double_tap_timing(value)

class Function7_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.FUNCTION7_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.FUNCTION7_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function7_KEY as _Function7_KEY
            _Function7_KEY()

        self._function7_key_object_intermediary = _Registry.pmma_module_spine[_Constants.FUNCTION7_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._function7_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._function7_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._function7_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._function7_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._function7_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._function7_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._function7_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._function7_key_object_intermediary.set_double_tap_timing(value)

class Function8_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.FUNCTION8_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.FUNCTION8_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function8_KEY as _Function8_KEY
            _Function8_KEY()

        self._function8_key_object_intermediary = _Registry.pmma_module_spine[_Constants.FUNCTION8_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._function8_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._function8_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._function8_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._function8_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._function8_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._function8_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._function8_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._function8_key_object_intermediary.set_double_tap_timing(value)

class Function9_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.FUNCTION9_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.FUNCTION9_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function9_KEY as _Function9_KEY
            _Function9_KEY()

        self._function9_key_object_intermediary = _Registry.pmma_module_spine[_Constants.FUNCTION9_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._function9_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._function9_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._function9_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._function9_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._function9_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._function9_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._function9_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._function9_key_object_intermediary.set_double_tap_timing(value)

class Function10_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.FUNCTION10_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.FUNCTION10_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function10_KEY as _Function10_KEY
            _Function10_KEY()

        self._function10_key_object_intermediary = _Registry.pmma_module_spine[_Constants.FUNCTION10_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._function10_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._function10_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._function10_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._function10_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._function10_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._function10_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._function10_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._function10_key_object_intermediary.set_double_tap_timing(value)

class Function11_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.FUNCTION11_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.FUNCTION11_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function11_KEY as _Function11_KEY
            _Function11_KEY()

        self._function11_key_object_intermediary = _Registry.pmma_module_spine[_Constants.FUNCTION11_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._function11_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._function11_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._function11_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._function11_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._function11_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._function11_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._function11_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._function11_key_object_intermediary.set_double_tap_timing(value)

class Function12_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.FUNCTION12_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.FUNCTION12_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function12_KEY as _Function12_KEY
            _Function12_KEY()

        self._function12_key_object_intermediary = _Registry.pmma_module_spine[_Constants.FUNCTION12_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._function12_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._function12_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._function12_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._function12_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._function12_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._function12_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._function12_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._function12_key_object_intermediary.set_double_tap_timing(value)

class Function13_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.FUNCTION13_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.FUNCTION13_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function13_KEY as _Function13_KEY
            _Function13_KEY()

        self._function13_key_object_intermediary = _Registry.pmma_module_spine[_Constants.FUNCTION13_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._function13_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._function13_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._function13_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._function13_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._function13_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._function13_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._function13_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._function13_key_object_intermediary.set_double_tap_timing(value)

class Function14_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.FUNCTION14_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.FUNCTION14_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function14_KEY as _Function14_KEY
            _Function14_KEY()

        self._function14_key_object_intermediary = _Registry.pmma_module_spine[_Constants.FUNCTION14_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._function14_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._function14_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._function14_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._function14_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._function14_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._function14_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._function14_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._function14_key_object_intermediary.set_double_tap_timing(value)

class Function15_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.FUNCTION15_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.FUNCTION15_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Function15_KEY as _Function15_KEY
            _Function15_KEY()

        self._function15_key_object_intermediary = _Registry.pmma_module_spine[_Constants.FUNCTION15_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._function15_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._function15_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._function15_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._function15_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._function15_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._function15_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._function15_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._function15_key_object_intermediary.set_double_tap_timing(value)

class NumLock_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.NUMLOCK_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.NUMLOCK_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import NumLock_KEY as _NumLock_KEY
            _NumLock_KEY()

        self._numlock_key_object_intermediary = _Registry.pmma_module_spine[_Constants.NUMLOCK_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._numlock_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._numlock_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._numlock_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._numlock_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._numlock_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._numlock_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._numlock_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._numlock_key_object_intermediary.set_double_tap_timing(value)

class CapsLock_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.CAPSLOCK_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.CAPSLOCK_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import CapsLock_KEY as _CapsLock_KEY
            _CapsLock_KEY()

        self._capslock_key_object_intermediary = _Registry.pmma_module_spine[_Constants.CAPSLOCK_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._capslock_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._capslock_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._capslock_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._capslock_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._capslock_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._capslock_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._capslock_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._capslock_key_object_intermediary.set_double_tap_timing(value)

class ScrollLock_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.SCROLLLOCK_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.SCROLLLOCK_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import ScrollLock_KEY as _ScrollLock_KEY
            _ScrollLock_KEY()

        self._scrolllock_key_object_intermediary = _Registry.pmma_module_spine[_Constants.SCROLLLOCK_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._scrolllock_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._scrolllock_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._scrolllock_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._scrolllock_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._scrolllock_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._scrolllock_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._scrolllock_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._scrolllock_key_object_intermediary.set_double_tap_timing(value)

class RightShift_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.RIGHTSHIFT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.RIGHTSHIFT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import RightShift_KEY as _RightShift_KEY
            _RightShift_KEY()

        self._rightshift_key_object_intermediary = _Registry.pmma_module_spine[_Constants.RIGHTSHIFT_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._rightshift_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._rightshift_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._rightshift_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._rightshift_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._rightshift_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._rightshift_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._rightshift_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._rightshift_key_object_intermediary.set_double_tap_timing(value)

class LeftShift_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.LEFTSHIFT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.LEFTSHIFT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import LeftShift_KEY as _LeftShift_KEY
            _LeftShift_KEY()

        self._leftshift_key_object_intermediary = _Registry.pmma_module_spine[_Constants.LEFTSHIFT_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._leftshift_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._leftshift_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._leftshift_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._leftshift_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._leftshift_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._leftshift_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._leftshift_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._leftshift_key_object_intermediary.set_double_tap_timing(value)

class Shift_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.SHIFT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.SHIFT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Shift_KEY as _Shift_KEY
            _Shift_KEY()

        self._shift_key_object_intermediary = _Registry.pmma_module_spine[_Constants.SHIFT_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._shift_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._shift_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._shift_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._shift_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._shift_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._shift_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._shift_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._shift_key_object_intermediary.set_double_tap_timing(value)

class RightControl_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.RIGHTCONTROL_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.RIGHTCONTROL_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import RightControl_KEY as _RightControl_KEY
            _RightControl_KEY()

        self._rightcontrol_key_object_intermediary = _Registry.pmma_module_spine[_Constants.RIGHTCONTROL_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._rightcontrol_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._rightcontrol_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._rightcontrol_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._rightcontrol_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._rightcontrol_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._rightcontrol_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._rightcontrol_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._rightcontrol_key_object_intermediary.set_double_tap_timing(value)

class LeftControl_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.LEFTCONTROL_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.LEFTCONTROL_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import LeftControl_KEY as _LeftControl_KEY
            _LeftControl_KEY()

        self._leftcontrol_key_object_intermediary = _Registry.pmma_module_spine[_Constants.LEFTCONTROL_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._leftcontrol_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._leftcontrol_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._leftcontrol_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._leftcontrol_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._leftcontrol_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._leftcontrol_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._leftcontrol_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._leftcontrol_key_object_intermediary.set_double_tap_timing(value)

class Control_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.CONTROL_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.CONTROL_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Control_KEY as _Control_KEY
            _Control_KEY()

        self._control_key_object_intermediary = _Registry.pmma_module_spine[_Constants.CONTROL_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._control_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._control_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._control_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._control_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._control_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._control_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._control_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._control_key_object_intermediary.set_double_tap_timing(value)

class RightAlt_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.RIGHTALT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.RIGHTALT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import RightAlt_KEY as _RightAlt_KEY
            _RightAlt_KEY()

        self._rightalt_key_object_intermediary = _Registry.pmma_module_spine[_Constants.RIGHTALT_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._rightalt_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._rightalt_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._rightalt_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._rightalt_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._rightalt_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._rightalt_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._rightalt_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._rightalt_key_object_intermediary.set_double_tap_timing(value)

class LeftAlt_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.LEFTALT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.LEFTALT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import LeftAlt_KEY as _LeftAlt_KEY
            _LeftAlt_KEY()

        self._leftalt_key_object_intermediary = _Registry.pmma_module_spine[_Constants.LEFTALT_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._leftalt_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._leftalt_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._leftalt_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._leftalt_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._leftalt_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._leftalt_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._leftalt_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._leftalt_key_object_intermediary.set_double_tap_timing(value)

class Alt_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.ALT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.ALT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Alt_KEY as _Alt_KEY
            _Alt_KEY()

        self._alt_key_object_intermediary = _Registry.pmma_module_spine[_Constants.ALT_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._alt_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._alt_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._alt_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._alt_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._alt_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._alt_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._alt_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._alt_key_object_intermediary.set_double_tap_timing(value)

class RightMeta_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.RIGHTMETA_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.RIGHTMETA_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import RightMeta_KEY as _RightMeta_KEY
            _RightMeta_KEY()

        self._rightmeta_key_object_intermediary = _Registry.pmma_module_spine[_Constants.RIGHTMETA_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._rightmeta_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._rightmeta_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._rightmeta_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._rightmeta_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._rightmeta_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._rightmeta_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._rightmeta_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._rightmeta_key_object_intermediary.set_double_tap_timing(value)

class LeftMeta_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.LEFTMETA_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.LEFTMETA_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import LeftMeta_KEY as _LeftMeta_KEY
            _LeftMeta_KEY()

        self._leftmeta_key_object_intermediary = _Registry.pmma_module_spine[_Constants.LEFTMETA_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._leftmeta_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._leftmeta_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._leftmeta_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._leftmeta_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._leftmeta_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._leftmeta_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._leftmeta_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._leftmeta_key_object_intermediary.set_double_tap_timing(value)

class Meta_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.META_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.META_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Meta_KEY as _Meta_KEY
            _Meta_KEY()

        self._meta_key_object_intermediary = _Registry.pmma_module_spine[_Constants.META_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._meta_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._meta_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._meta_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._meta_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._meta_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._meta_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._meta_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._meta_key_object_intermediary.set_double_tap_timing(value)

class LeftSuper_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.LEFTSUPER_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.LEFTSUPER_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import LeftSuper_KEY as _LeftSuper_KEY
            _LeftSuper_KEY()

        self._leftsuper_key_object_intermediary = _Registry.pmma_module_spine[_Constants.LEFTSUPER_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._leftsuper_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._leftsuper_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._leftsuper_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._leftsuper_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._leftsuper_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._leftsuper_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._leftsuper_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._leftsuper_key_object_intermediary.set_double_tap_timing(value)

class RightSuper_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.RIGHTSUPER_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.RIGHTSUPER_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import RightSuper_KEY as _RightSuper_KEY
            _RightSuper_KEY()

        self._rightsuper_key_object_intermediary = _Registry.pmma_module_spine[_Constants.RIGHTSUPER_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._rightsuper_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._rightsuper_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._rightsuper_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._rightsuper_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._rightsuper_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._rightsuper_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._rightsuper_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._rightsuper_key_object_intermediary.set_double_tap_timing(value)

class Super_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.SUPER_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.SUPER_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Super_KEY as _Super_KEY
            _Super_KEY()

        self._super_key_object_intermediary = _Registry.pmma_module_spine[_Constants.SUPER_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._super_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._super_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._super_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._super_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._super_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._super_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._super_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._super_key_object_intermediary.set_double_tap_timing(value)

class Mode_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.MODE_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.MODE_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Mode_KEY as _Mode_KEY
            _Mode_KEY()

        self._mode_key_object_intermediary = _Registry.pmma_module_spine[_Constants.MODE_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._mode_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._mode_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._mode_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._mode_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._mode_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._mode_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._mode_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._mode_key_object_intermediary.set_double_tap_timing(value)

class Help_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.HELP_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.HELP_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Help_KEY as _Help_KEY
            _Help_KEY()

        self._help_key_object_intermediary = _Registry.pmma_module_spine[_Constants.HELP_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._help_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._help_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._help_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._help_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._help_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._help_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._help_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._help_key_object_intermediary.set_double_tap_timing(value)

class Print_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.PRINT_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.PRINT_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Print_KEY as _Print_KEY
            _Print_KEY()

        self._print_key_object_intermediary = _Registry.pmma_module_spine[_Constants.PRINT_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._print_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._print_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._print_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._print_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._print_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._print_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._print_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._print_key_object_intermediary.set_double_tap_timing(value)

class SystemRequest_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.SYSTEMREQUEST_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.SYSTEMREQUEST_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import SystemRequest_KEY as _SystemRequest_KEY
            _SystemRequest_KEY()

        self._systemrequest_key_object_intermediary = _Registry.pmma_module_spine[_Constants.SYSTEMREQUEST_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._systemrequest_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._systemrequest_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._systemrequest_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._systemrequest_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._systemrequest_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._systemrequest_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._systemrequest_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._systemrequest_key_object_intermediary.set_double_tap_timing(value)

class Break_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.BREAK_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.BREAK_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Break_KEY as _Break_KEY
            _Break_KEY()

        self._break_key_object_intermediary = _Registry.pmma_module_spine[_Constants.BREAK_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._break_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._break_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._break_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._break_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._break_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._break_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._break_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._break_key_object_intermediary.set_double_tap_timing(value)

class Menu_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.MENU_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.MENU_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Menu_KEY as _Menu_KEY
            _Menu_KEY()

        self._menu_key_object_intermediary = _Registry.pmma_module_spine[_Constants.MENU_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._menu_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._menu_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._menu_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._menu_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._menu_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._menu_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._menu_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._menu_key_object_intermediary.set_double_tap_timing(value)

class Power_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.POWER_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.POWER_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Power_KEY as _Power_KEY
            _Power_KEY()

        self._power_key_object_intermediary = _Registry.pmma_module_spine[_Constants.POWER_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._power_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._power_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._power_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._power_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._power_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._power_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._power_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._power_key_object_intermediary.set_double_tap_timing(value)

class Euro_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.EURO_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.EURO_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import Euro_KEY as _Euro_KEY
            _Euro_KEY()

        self._euro_key_object_intermediary = _Registry.pmma_module_spine[_Constants.EURO_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._euro_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._euro_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._euro_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._euro_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._euro_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._euro_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._euro_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._euro_key_object_intermediary.set_double_tap_timing(value)

class AndroidBack_KEY:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.ANDROIDBACK_KEY_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.ANDROIDBACK_KEY_OBJECT)
            from pmma.python_src.utility.event_utils import AndroidBack_KEY as _AndroidBack_KEY
            _AndroidBack_KEY()

        self._androidback_key_object_intermediary = _Registry.pmma_module_spine[_Constants.ANDROIDBACK_KEY_OBJECT]

    def set_double_tapped(self, value):
        self._androidback_key_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._androidback_key_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._androidback_key_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._androidback_key_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._androidback_key_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._androidback_key_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._androidback_key_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._androidback_key_object_intermediary.set_double_tap_timing(value)

class LeftButton_MOUSE:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.LEFTBUTTON_MOUSE_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.LEFTBUTTON_MOUSE_OBJECT)
            from pmma.python_src.utility.event_utils import LeftButton_MOUSE as _LeftButton_MOUSE
            _LeftButton_MOUSE()

        self._leftbutton_mouse_object_intermediary = _Registry.pmma_module_spine[_Constants.LEFTBUTTON_MOUSE_OBJECT]

    def set_double_tapped(self, value):
        self._leftbutton_mouse_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._leftbutton_mouse_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._leftbutton_mouse_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._leftbutton_mouse_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._leftbutton_mouse_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._leftbutton_mouse_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._leftbutton_mouse_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._leftbutton_mouse_object_intermediary.set_double_tap_timing(value)

class MiddleButton_MOUSE:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.MIDDLEBUTTON_MOUSE_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.MIDDLEBUTTON_MOUSE_OBJECT)
            from pmma.python_src.utility.event_utils import MiddleButton_MOUSE as _MiddleButton_MOUSE
            _MiddleButton_MOUSE()

        self._middlebutton_mouse_object_intermediary = _Registry.pmma_module_spine[_Constants.MIDDLEBUTTON_MOUSE_OBJECT]

    def set_double_tapped(self, value):
        self._middlebutton_mouse_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._middlebutton_mouse_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._middlebutton_mouse_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._middlebutton_mouse_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._middlebutton_mouse_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._middlebutton_mouse_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._middlebutton_mouse_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._middlebutton_mouse_object_intermediary.set_double_tap_timing(value)

class RightButton_MOUSE:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.RIGHTBUTTON_MOUSE_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.RIGHTBUTTON_MOUSE_OBJECT)
            from pmma.python_src.utility.event_utils import RightButton_MOUSE as _RightButton_MOUSE
            _RightButton_MOUSE()

        self._rightbutton_mouse_object_intermediary = _Registry.pmma_module_spine[_Constants.RIGHTBUTTON_MOUSE_OBJECT]

    def set_double_tapped(self, value):
        self._rightbutton_mouse_object_intermediary.set_double_tapped(value)

    def get_double_tapped(self):
        return self._rightbutton_mouse_object_intermediary.get_double_tapped()

    def get_last_tap_time(self):
        return self._rightbutton_mouse_object_intermediary.get_last_tap_time()

    def set_last_tap_time(self, value):
        self._rightbutton_mouse_object_intermediary.set_last_tap_time(value)

    def get_pressed(self):
        return self._rightbutton_mouse_object_intermediary.get_pressed()

    def set_pressed(self, value):
        self._rightbutton_mouse_object_intermediary.set_pressed(value)

    def get_double_tap_timing(self):
        return self._rightbutton_mouse_object_intermediary.get_double_tap_timing()

    def set_double_tap_timing(self, value):
        self._rightbutton_mouse_object_intermediary.set_double_tap_timing(value)

class Mouse_SCROLL:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.MOUSE_SCROLL_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.MOUSE_SCROLL_OBJECT)
            from pmma.python_src.utility.event_utils import Mouse_SCROLL as _Mouse_SCROLL
            _Mouse_SCROLL()

        self._mouse_scroll_object_intermediary = _Registry.pmma_module_spine[_Constants.MOUSE_SCROLL_OBJECT]

    def get_x_displacement(self):
        return self._mouse_scroll_object_intermediary.get_x_displacement()

    def set_x_displacement(self, value):
        self._mouse_scroll_object_intermediary.set_x_displacement(value)

    def get_x_value(self):
        return self._mouse_scroll_object_intermediary.get_x_value()

    def set_x_value(self, value):
        self._mouse_scroll_object_intermediary.set_x_value(value)

    def get_y_displacement(self):
        return self._mouse_scroll_object_intermediary.get_y_displacement()

    def set_y_displacement(self, value):
        self._mouse_scroll_object_intermediary.set_y_displacement(value)

    def get_y_value(self):
        return self._mouse_scroll_object_intermediary.get_y_value()

    def set_y_value(self, value):
        self._mouse_scroll_object_intermediary.set_y_value(value)

class Mouse_POSITION:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.MOUSE_POSITION_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.MOUSE_POSITION_OBJECT)
            from pmma.python_src.utility.event_utils import Mouse_POSITION as _Mouse_POSITION
            _Mouse_POSITION()

        self._mouse_position_object_intermediary = _Registry.pmma_module_spine[_Constants.MOUSE_POSITION_OBJECT]

    def get_axis_displacement(self):
        return self._mouse_position_object_intermediary.get_axis_displacement()

    def get_x_axis_displacement(self):
        return self._mouse_position_object_intermediary.get_x_axis_displacement()

    def get_y_axis_displacement(self):
        return self._mouse_position_object_intermediary.get_y_axis_displacement()

    def get_x_axis(self):
        return self._mouse_position_object_intermediary.get_x_axis()

    def get_y_axis(self):
        return self._mouse_position_object_intermediary.get_y_axis()

    def set_x_axis(self, value):
        self._mouse_position_object_intermediary.set_x_axis(value)

    def set_y_axis(self, value):
        self._mouse_position_object_intermediary.set_y_axis(value)

    def set_x_axis_displacement(self, value):
        self._mouse_position_object_intermediary.set_x_axis_displacement(value)

    def set_y_axis_displacement(self, value):
        self._mouse_position_object_intermediary.set_y_axis_displacement(value)

class Active_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.ACTIVE_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.ACTIVE_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import Active_EVENT as _Active_EVENT
            _Active_EVENT()

        self._active_event_object_intermediary = _Registry.pmma_module_spine[_Constants.ACTIVE_EVENT_OBJECT]

    def set_value(self, value):
        self._active_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._active_event_object_intermediary.get_value()

class AppTerminating_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.APPTERMINATING_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.APPTERMINATING_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import AppTerminating_EVENT as _AppTerminating_EVENT
            _AppTerminating_EVENT()

        self._appterminatingevent_intermediary = _Registry.pmma_module_spine[_Constants.APPTERMINATING_EVENT_OBJECT]

        self._logger = _InternalLogger()

    def set_value(self, value):
        self._appterminatingevent_intermediary.set_value(value)

    def get_value(self):
        if _get_operating_system() != _Constants.ANDROID:
            self._logger.log_development("This event is exclusive to the Android operating system. Instead please use: 'Quit_EVENT' as this works across all platforms.")
        return self._appterminatingevent_intermediary.get_value()

class AppLowMemory_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.APPLOWMEMORY_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.APPLOWMEMORY_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import AppLowMemory_EVENT as _AppLowMemory_EVENT
            _AppLowMemory_EVENT()

        self._applowmemory_intermediary = _Registry.pmma_module_spine[_Constants.APPLOWMEMORY_EVENT_OBJECT]

        self._logger = _InternalLogger()

    def set_value(self, value):
        self._applowmemory_intermediary.set_value(value)

    def get_value(self):
        if _get_operating_system() != _Constants.ANDROID:
            self._logger.log_development("This event is exclusive to the Android operating system. There is no alternative to this on other operating systems due to how memory is allocated. If you are interested in getting information about memory, I'd recommend checking out PSUtil: https://pypi.org/project/psutil/")
        return self._applowmemory_intermediary.get_value()

class AppWillEnterBackground_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.APPWILLENTERBACKGROUND_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.APPWILLENTERBACKGROUND_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import AppWillEnterBackground_EVENT as _AppWillEnterBackground_EVENT
            _AppWillEnterBackground_EVENT()

        self._appwillenterbackground_intermediary = _Registry.pmma_module_spine[_Constants.APPWILLENTERBACKGROUND_EVENT_OBJECT]

        self._logger = _InternalLogger()

    def set_value(self, value):
        self._appwillenterbackground_intermediary.set_value(value)

    def get_value(self):
        self._logger.log_development("This event is exclusive to the Android operating system. There is no alternative to this on other operating systems.")
        return self._appwillenterbackground_intermediary.get_value()

class AppDidEnterBackground_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.APPDIDENTERBACKGROUND_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.APPDIDENTERBACKGROUND_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import AppDidEnterBackground_EVENT as _AppDidEnterBackground_EVENT
            _AppDidEnterBackground_EVENT()

        self._appdidenterbackground_intermediary = _Registry.pmma_module_spine[_Constants.APPDIDENTERBACKGROUND_EVENT_OBJECT]

        self._logger = _InternalLogger()

    def set_value(self, value):
        self._appdidenterbackground_intermediary.set_value(value)

    def get_value(self):
        self._logger.log_development("This event is exclusive to the Android operating system. Instead please use: 'WindowFocusLost' as this works across all platforms.")
        return self._appdidenterbackground_intermediary.get_value()

class AppWillEnterForeground_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.APPWILLENTERFOREGROUND_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.APPWILLENTERFOREGROUND_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import AppWillEnterForeground_EVENT as _AppWillEnterForeground_EVENT
            _AppWillEnterForeground_EVENT()

        self._appwillenterforeground_intermediary = _Registry.pmma_module_spine[_Constants.APPWILLENTERFOREGROUND_EVENT_OBJECT]

        self._logger = _InternalLogger()

    def set_value(self, value):
        self._appwillenterforeground_intermediary.set_value(value)

    def get_value(self):
        self._logger.log_development("This event is exclusive to the Android operating system. There is no alternative to this on other operating systems.")
        return self._appwillenterforeground_intermediary.get_value()

class AppDidEnterForeground_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.APPDIDENTERFOREGROUND_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.APPDIDENTERFOREGROUND_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import AppDidEnterForeground_EVENT as _AppDidEnterForeground_EVENT
            _AppDidEnterForeground_EVENT()

        self._appdidenterforeground_intermediary = _Registry.pmma_module_spine[_Constants.APPDIDENTERFOREGROUND_EVENT_OBJECT]

        self._logger = _InternalLogger()

    def set_value(self, value):
        self._appdidenterforeground_intermediary.set_value(value)

    def get_value(self):
        self._logger.log_development("This event is exclusive to the Android operating system. Instead please use: 'WindowFocusGained' as this works across all platforms.")
        return self._appdidenterforeground_intermediary.get_value()

class AudioDeviceAdded_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.AUDIODEVICEADDED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.AUDIODEVICEADDED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import AudioDeviceAdded_EVENT as _AudioDeviceAdded_EVENT
            _AudioDeviceAdded_EVENT()

        self._audiodeviceadded_event_object_intermediary = _Registry.pmma_module_spine[_Constants.AUDIODEVICEADDED_EVENT_OBJECT]

    def set_value(self, value):
        self._audiodeviceadded_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._audiodeviceadded_event_object_intermediary.get_value()

class AudioDeviceRemoved_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.AUDIODEVICEREMOVED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.AUDIODEVICEREMOVED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import AudioDeviceRemoved_EVENT as _AudioDeviceRemoved_EVENT
            _AudioDeviceRemoved_EVENT()

        self._audiodeviceremoved_event_object_intermediary = _Registry.pmma_module_spine[_Constants.AUDIODEVICEREMOVED_EVENT_OBJECT]

    def set_value(self, value):
        self._audiodeviceremoved_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._audiodeviceremoved_event_object_intermediary.get_value()

class ClipBoardUpdate_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.CLIPBOARDUPDATE_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.CLIPBOARDUPDATE_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import ClipBoardUpdate_EVENT as _ClipBoardUpdate_EVENT
            _ClipBoardUpdate_EVENT()

        self._clipboardupdate_event_object_intermediary = _Registry.pmma_module_spine[_Constants.CLIPBOARDUPDATE_EVENT_OBJECT]

    def set_value(self, value):
        self._clipboardupdate_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._clipboardupdate_event_object_intermediary.get_value()

class DropFile_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.DROPFILE_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.DROPFILE_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import DropFile_EVENT as _DropFile_EVENT
            _DropFile_EVENT()

        self._dropfile_event_object_intermediary = _Registry.pmma_module_spine[_Constants.DROPFILE_EVENT_OBJECT]

    def set_file(self, file):
        self._dropfile_event_object_intermediary.set_file(file)

    def get_file(self):
        return self._dropfile_event_object_intermediary.get_file()

class DropText_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.DROPTEXT_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.DROPTEXT_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import DropText_EVENT as _DropText_EVENT
            _DropText_EVENT()

        self._deoptext_intermediary = _Registry.pmma_module_spine[_Constants.DROPTEXT_EVENT_OBJECT]

        self._logger = _InternalLogger()

    def set_text(self, text):
        self._deoptext_intermediary.set_text(text)

    def get_text(self):
        self._logger.log_development("Please note that this event is not yet reliably supported across all operating systems. Windows compatability is generally mixed, MacOS compatability is generally good, Linux compatability varies based on what desktop envioment is being used and Android support being unofficial and limited. Effectively this means that your milage may vary when using this event if it is triggered reliably. Generally speaking however, if your developing your application to run on specific hardware - like a games console - you can try and use this event, if the event works and the software/hardware is the same, it should work more reliably. ALTERNATIVELY, use the 'DropFile_EVENT' event with the user dropping a text file, then open and read that for text inputs instead. In short - this event is not known to work reliably, using other events instead is recommended!")

        return self._deoptext_intermediary.get_text()

class DropBegin_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.DROPBEGIN_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.DROPBEGIN_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import DropBegin_EVENT as _DropBegin_EVENT
            _DropBegin_EVENT()

        self._dropbegin_event_object_intermediary = _Registry.pmma_module_spine[_Constants.DROPBEGIN_EVENT_OBJECT]

    def set_value(self, value):
        self._dropbegin_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._dropbegin_event_object_intermediary.get_value()

class DropComplete_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.DROPCOMPLETE_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.DROPCOMPLETE_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import DropComplete_EVENT as _DropComplete_EVENT
            _DropComplete_EVENT()

        self._dropcomplete_event_object_intermediary = _Registry.pmma_module_spine[_Constants.DROPCOMPLETE_EVENT_OBJECT]

    def set_value(self, value):
        self._dropcomplete_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._dropcomplete_event_object_intermediary.get_value()

class FingerMotion_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.FINGERMOTION_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.FINGERMOTION_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import FingerMotion_EVENT as _FingerMotion_EVENT
            _FingerMotion_EVENT()

        self._fingermotion_event_object_intermediary = _Registry.pmma_module_spine[_Constants.FINGERMOTION_EVENT_OBJECT]

    def set_value(self, value):
        self._fingermotion_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._fingermotion_event_object_intermediary.get_value()

class FingerDown_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.FINGERDOWN_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.FINGERDOWN_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import FingerDown_EVENT as _FingerDown_EVENT
            _FingerDown_EVENT()

        self._fingerdown_event_object_intermediary = _Registry.pmma_module_spine[_Constants.FINGERDOWN_EVENT_OBJECT]

    def set_value(self, value):
        self._fingerdown_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._fingerdown_event_object_intermediary.get_value()

class FingerUp_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.FINGERUP_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.FINGERUP_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import FingerUp_EVENT as _FingerUp_EVENT
            _FingerUp_EVENT()

        self._fingerup_event_object_intermediary = _Registry.pmma_module_spine[_Constants.FINGERUP_EVENT_OBJECT]

    def set_value(self, value):
        self._fingerup_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._fingerup_event_object_intermediary.get_value()

class KeyMapChanged_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.KEYMAPCHANGED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.KEYMAPCHANGED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import KeyMapChanged_EVENT as _KeyMapChanged_EVENT
            _KeyMapChanged_EVENT()

        self._keymapchanged_event_object_intermediary = _Registry.pmma_module_spine[_Constants.KEYMAPCHANGED_EVENT_OBJECT]

    def set_value(self, value):
        self._keymapchanged_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._keymapchanged_event_object_intermediary.get_value()

class LocaleChanged_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.LOCALECHANGED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.LOCALECHANGED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import LocaleChanged_EVENT as _LocaleChanged_EVENT
            _LocaleChanged_EVENT()

        self._localechanged_event_object_intermediary = _Registry.pmma_module_spine[_Constants.LOCALECHANGED_EVENT_OBJECT]

    def set_value(self, value):
        self._localechanged_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._localechanged_event_object_intermediary.get_value()

class MultiGesture_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.MULTIGESTURE_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.MULTIGESTURE_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import MultiGesture_EVENT as _MultiGesture_EVENT
            _MultiGesture_EVENT()

        self._multigesture_event_object_intermediary = _Registry.pmma_module_spine[_Constants.MULTIGESTURE_EVENT_OBJECT]

    def get_gesture_center_x(self):
        return self._multigesture_event_object_intermediary.get_gesture_center_x()

    def get_gesture_center_y(self):
        return self._multigesture_event_object_intermediary.get_gesture_center_y()

    def get_pinched_value(self):
        return self._multigesture_event_object_intermediary.get_pinched_value()

    def get_rotated_value(self):
        return self._multigesture_event_object_intermediary.get_rotated_value()

    def get_number_of_fingers(self):
        return self._multigesture_event_object_intermediary.get_number_of_fingers()

    def set_gesture_center_x(self, value):
        self._multigesture_event_object_intermediary.set_gesture_center_x(value)

    def set_gesture_center_y(self, value):
        self._multigesture_event_object_intermediary.set_gesture_center_y(value)

    def set_pinched_value(self, value):
        self._multigesture_event_object_intermediary.set_pinched_value(value)

    def set_rotated_value(self, value):
        self._multigesture_event_object_intermediary.set_rotated_value(value)

    def set_number_of_fingers(self, value):
        self._multigesture_event_object_intermediary.set_number_of_fingers(value)

class Quit_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.QUIT_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.QUIT_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import Quit_EVENT as _Quit_EVENT
            _Quit_EVENT()

        self._quit_event_object_intermediary = _Registry.pmma_module_spine[_Constants.QUIT_EVENT_OBJECT]

    def set_value(self, value):
        self._quit_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._quit_event_object_intermediary.get_value()

class RenderTargetsReset_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.RENDERTARGETSRESET_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.RENDERTARGETSRESET_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import RenderTargetsReset_EVENT as _RenderTargetsReset_EVENT
            _RenderTargetsReset_EVENT()

        self._rendertargetsreset_event_object_intermediary = _Registry.pmma_module_spine[_Constants.RENDERTARGETSRESET_EVENT_OBJECT]

    def set_value(self, value):
        self._rendertargetsreset_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._rendertargetsreset_event_object_intermediary.get_value()

class RenderDeviceReset_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.RENDERDEVICERESET_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.RENDERDEVICERESET_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import RenderDeviceReset_EVENT as _RenderDeviceReset_EVENT
            _RenderDeviceReset_EVENT()

        self._renderdevicereset_event_object_intermediary = _Registry.pmma_module_spine[_Constants.RENDERDEVICERESET_EVENT_OBJECT]

    def set_value(self, value):
        self._renderdevicereset_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._renderdevicereset_event_object_intermediary.get_value()

class SysWMEvent_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.SYSWMEVENT_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.SYSWMEVENT_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import SysWMEvent_EVENT as _SysWMEvent_EVENT
            _SysWMEvent_EVENT()

        self._syswmevent_event_object_intermediary = _Registry.pmma_module_spine[_Constants.SYSWMEVENT_EVENT_OBJECT]

    def set_value(self, value):
        self._syswmevent_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._syswmevent_event_object_intermediary.get_value()

class VideoResize_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.VIDEORESIZE_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.VIDEORESIZE_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import VideoResize_EVENT as _VideoResize_EVENT
            _VideoResize_EVENT()

        self._videoresize_event_object_intermediary = _Registry.pmma_module_spine[_Constants.VIDEORESIZE_EVENT_OBJECT]

    def set_value(self, value):
        self._videoresize_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._videoresize_event_object_intermediary.get_value()

class VideoExpose_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.VIDEOEXPOSE_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.VIDEOEXPOSE_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import VideoExpose_EVENT as _VideoExpose_EVENT
            _VideoExpose_EVENT()

        self._videoexpose_event_object_intermediary = _Registry.pmma_module_spine[_Constants.VIDEOEXPOSE_EVENT_OBJECT]

    def set_value(self, value):
        self._videoexpose_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._videoexpose_event_object_intermediary.get_value()

class WindowShown_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.WINDOWSHOWN_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.WINDOWSHOWN_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowShown_EVENT as _WindowShown_EVENT
            _WindowShown_EVENT()

        self._windowshown_event_object_intermediary = _Registry.pmma_module_spine[_Constants.WINDOWSHOWN_EVENT_OBJECT]

    def set_value(self, value):
        self._windowshown_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._windowshown_event_object_intermediary.get_value()

class WindowHidden_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.WINDOWHIDDEN_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.WINDOWHIDDEN_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowHidden_EVENT as _WindowHidden_EVENT
            _WindowHidden_EVENT()

        self._windowhidden_event_object_intermediary = _Registry.pmma_module_spine[_Constants.WINDOWHIDDEN_EVENT_OBJECT]

    def set_value(self, value):
        self._windowhidden_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._windowhidden_event_object_intermediary.get_value()

class WindowExposed_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.WINDOWEXPOSED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.WINDOWEXPOSED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowExposed_EVENT as _WindowExposed_EVENT
            _WindowExposed_EVENT()

        self._windowexposed_event_object_intermediary = _Registry.pmma_module_spine[_Constants.WINDOWEXPOSED_EVENT_OBJECT]

    def set_value(self, value):
        self._windowexposed_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._windowexposed_event_object_intermediary.get_value()

class WindowMoved_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.WINDOWMOVED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.WINDOWMOVED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowMoved_EVENT as _WindowMoved_EVENT
            _WindowMoved_EVENT()

        self._windowmoved_event_object_intermediary = _Registry.pmma_module_spine[_Constants.WINDOWMOVED_EVENT_OBJECT]

    def set_value(self, value):
        self._windowmoved_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._windowmoved_event_object_intermediary.get_value()

class WindowResized_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.WINDOWRESIZED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.WINDOWRESIZED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowResized_EVENT as _WindowResized_EVENT
            _WindowResized_EVENT()

        self._windowresized_event_object_intermediary = _Registry.pmma_module_spine[_Constants.WINDOWRESIZED_EVENT_OBJECT]

    def set_value(self, value):
        self._windowresized_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._windowresized_event_object_intermediary.get_value()

class WindowMinimized_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.WINDOWMINIMIZED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.WINDOWMINIMIZED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowMinimized_EVENT as _WindowMinimized_EVENT
            _WindowMinimized_EVENT()

        self._windowminimized_event_object_intermediary = _Registry.pmma_module_spine[_Constants.WINDOWMINIMIZED_EVENT_OBJECT]

    def set_value(self, value):
        self._windowminimized_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._windowminimized_event_object_intermediary.get_value()

class WindowMaximized_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.WINDOWMAXIMIZED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.WINDOWMAXIMIZED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowMaximized_EVENT as _WindowMaximized_EVENT
            _WindowMaximized_EVENT()

        self._windowmaximized_event_object_intermediary = _Registry.pmma_module_spine[_Constants.WINDOWMAXIMIZED_EVENT_OBJECT]

    def set_value(self, value):
        self._windowmaximized_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._windowmaximized_event_object_intermediary.get_value()

class WindowRestored_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.WINDOWRESTORED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.WINDOWRESTORED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowRestored_EVENT as _WindowRestored_EVENT
            _WindowRestored_EVENT()

        self._windowrestored_event_object_intermediary = _Registry.pmma_module_spine[_Constants.WINDOWRESTORED_EVENT_OBJECT]

    def set_value(self, value):
        self._windowrestored_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._windowrestored_event_object_intermediary.get_value()

class WindowEnter_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.WINDOWENTER_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.WINDOWENTER_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowEnter_EVENT as _WindowEnter_EVENT
            _WindowEnter_EVENT()

        self._windowenter_event_object_intermediary = _Registry.pmma_module_spine[_Constants.WINDOWENTER_EVENT_OBJECT]

    def set_value(self, value):
        self._windowenter_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._windowenter_event_object_intermediary.get_value()

class WindowLeave_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.WINDOWLEAVE_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.WINDOWLEAVE_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowLeave_EVENT as _WindowLeave_EVENT
            _WindowLeave_EVENT()

        self._windowleave_event_object_intermediary = _Registry.pmma_module_spine[_Constants.WINDOWLEAVE_EVENT_OBJECT]

    def set_value(self, value):
        self._windowleave_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._windowleave_event_object_intermediary.get_value()

class WindowFocusGained_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.WINDOWFOCUSGAINED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.WINDOWFOCUSGAINED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowFocusGained_EVENT as _WindowFocusGained_EVENT
            _WindowFocusGained_EVENT()

        self._windowfocusgained_event_object_intermediary = _Registry.pmma_module_spine[_Constants.WINDOWFOCUSGAINED_EVENT_OBJECT]

    def set_value(self, value):
        self._windowfocusgained_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._windowfocusgained_event_object_intermediary.get_value()

class WindowFocusLost_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.WINDOWFOCUSLOST_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.WINDOWFOCUSLOST_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowFocusLost_EVENT as _WindowFocusLost_EVENT
            _WindowFocusLost_EVENT()

        self._windowfocuslost_event_object_intermediary = _Registry.pmma_module_spine[_Constants.WINDOWFOCUSLOST_EVENT_OBJECT]

    def set_value(self, value):
        self._windowfocuslost_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._windowfocuslost_event_object_intermediary.get_value()

class WindowClose_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.WINDOWCLOSE_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.WINDOWCLOSE_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowClose_EVENT as _WindowClose_EVENT
            _WindowClose_EVENT()

        self._windowclose_event_object_intermediary = _Registry.pmma_module_spine[_Constants.WINDOWCLOSE_EVENT_OBJECT]

    def set_value(self, value):
        self._windowclose_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._windowclose_event_object_intermediary.get_value()

class WindowTakeFocus_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.WINDOWTAKEFOCUS_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.WINDOWTAKEFOCUS_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowTakeFocus_EVENT as _WindowTakeFocus_EVENT
            _WindowTakeFocus_EVENT()

        self._windowtakefocus_event_object_intermediary = _Registry.pmma_module_spine[_Constants.WINDOWTAKEFOCUS_EVENT_OBJECT]

    def set_value(self, value):
        self._windowtakefocus_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._windowtakefocus_event_object_intermediary.get_value()

class WindowHitTest_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.WINDOWHITTEST_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.WINDOWHITTEST_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowHitTest_EVENT as _WindowHitTest_EVENT
            _WindowHitTest_EVENT()

        self._windowhittest_event_object_intermediary = _Registry.pmma_module_spine[_Constants.WINDOWHITTEST_EVENT_OBJECT]

    def set_value(self, value):
        self._windowhittest_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._windowhittest_event_object_intermediary.get_value()

class WindowICCPROFChanged_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.WINDOWICCPROFCHANGED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.WINDOWICCPROFCHANGED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowICCPROFChanged_EVENT as _WindowICCPROFChanged_EVENT
            _WindowICCPROFChanged_EVENT()

        self._windowiccprofchanged_event_object_intermediary = _Registry.pmma_module_spine[_Constants.WINDOWICCPROFCHANGED_EVENT_OBJECT]

    def set_value(self, value):
        self._windowiccprofchanged_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._windowiccprofchanged_event_object_intermediary.get_value()

class WindowDisplayChanged_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.WINDOWDISPLAYCHANGED_EVENT_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.WINDOWDISPLAYCHANGED_EVENT_OBJECT)
            from pmma.python_src.utility.event_utils import WindowDisplayChanged_EVENT as _WindowDisplayChanged_EVENT
            _WindowDisplayChanged_EVENT()

        self._windowdisplaychanged_event_object_intermediary = _Registry.pmma_module_spine[_Constants.WINDOWDISPLAYCHANGED_EVENT_OBJECT]

    def set_value(self, value):
        self._windowdisplaychanged_event_object_intermediary.set_value(value)

    def get_value(self):
        return self._windowdisplaychanged_event_object_intermediary.get_value()

class JoyDeviceAdded_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.JOYDEVICEADDED_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.JOYDEVICEADDED_OBJECT)
            from pmma.python_src.utility.event_utils import JoyDeviceAdded_EVENT as _JoyDeviceAdded_EVENT
            _JoyDeviceAdded_EVENT()

        self._joydeviceadded_object_intermediary = _Registry.pmma_module_spine[_Constants.JOYDEVICEADDED_OBJECT]

    def set_value(self, value):
        self._joydeviceadded_object_intermediary.set_value(value)

    def get_value(self):
        return self._joydeviceadded_object_intermediary.get_value()

class JoyDeviceRemoved_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.JOYDEVICEREMOVED_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.JOYDEVICEREMOVED_OBJECT)
            from pmma.python_src.utility.event_utils import JoyDeviceRemoved_EVENT as _JoyDeviceRemoved_EVENT
            _JoyDeviceRemoved_EVENT()

        self._joydeviceremoved_object_intermediary = _Registry.pmma_module_spine[_Constants.JOYDEVICEREMOVED_OBJECT]

    def set_value(self, value):
        self._joydeviceremoved_object_intermediary.set_value(value)

    def get_value(self):
        return self._joydeviceremoved_object_intermediary.get_value()

class WindowFullScreenStatusChanged_EVENT:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc__collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        _initialize(self)
        if not _Constants.WINDOWFULLSCREENSTATECHANGED_OBJECT in _Registry.pmma_module_spine.keys():
            _PassportIntermediary.components_used.append(_Constants.WINDOWFULLSCREENSTATECHANGED_OBJECT)
            from pmma.python_src.utility.event_utils import WindowFullScreenStatusChanged_EVENT as _WindowFullScreenStatusChanged_EVENT
            _WindowFullScreenStatusChanged_EVENT()

        self._windowfullscreenstatechanged_object_intermediary = _Registry.pmma_module_spine[_Constants.WINDOWFULLSCREENSTATECHANGED_OBJECT]

    def set_value(self, value):
        self._windowfullscreenstatechanged_object_intermediary.set_value(value)

    def get_value(self):
        return self._windowfullscreenstatechanged_object_intermediary.get_value()