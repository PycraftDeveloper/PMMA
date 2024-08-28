import gc as _gc

import pygame as _pygame

from pmma.python_src.general import *
from pmma.python_src.registry import Registry
from pmma.python_src.constants import Constants
from pmma.python_src.utility.error_utils import *

from pmma.python_src.backpack import Backpack as _Backpack
from pmma.python_src.controller import Controllers as _Controllers

class Events:
    def __del__(self, do_garbage_collection=False):
        if self._shut_down is False:
            del self
            if do_garbage_collection:
                _gc.collect()

    def quit(self, do_garbage_collection=True):
        self.__del__(do_garbage_collection=do_garbage_collection)
        self._shut_down = True

    def __init__(self):
        initialize(self, unique_instance=Constants.EVENTS_OBJECT, add_to_pmma_module_spine=True, requires_display_mode_set=True)

        self.iteration_id = 0

        self.controllers = _Controllers()

        self.backspace_key = Backspace_KEY()
        self.tab_key = Tab_KEY()
        self.clear_key = Clear_KEY()
        self.return_key = Return_KEY()
        self.pause_key = Pause_KEY()
        self.escape_key = Escape_KEY()
        self.space_key = Space_KEY()
        self.exclamationmark_key = ExclamationMark_KEY()
        self.doublequote_key = DoubleQuote_KEY()
        self.hashtag_key = Hashtag_KEY()
        self.dollar_key = Dollar_KEY()
        self.ampersand_key = Ampersand_KEY()
        self.singlequote_key = SingleQuote_KEY()
        self.leftparenthesis_key = LeftParenthesis_KEY()
        self.rightparenthesis_key = RightParenthesis_KEY()
        self.asterisk_key = Asterisk_KEY()
        self.plus_key = Plus_KEY()
        self.comma_key = Comma_KEY()
        self.minus_key = Minus_KEY()
        self.period_key = Period_KEY()
        self.forwardslash_key = ForwardSlash_KEY()
        self.primary0_key = Primary0_KEY()
        self.primary1_key = Primary1_KEY()
        self.primary2_key = Primary2_KEY()
        self.primary3_key = Primary3_KEY()
        self.primary4_key = Primary4_KEY()
        self.primary5_key = Primary5_KEY()
        self.primary6_key = Primary6_KEY()
        self.primary7_key = Primary7_KEY()
        self.primary8_key = Primary8_KEY()
        self.primary9_key = Primary9_KEY()
        self.colon_key = Colon_KEY()
        self.semicolon_key = SemiColon_KEY()
        self.lessthan_key = LessThan_KEY()
        self.equals_key = Equals_KEY()
        self.greaterthan_key = GreaterThan_KEY()
        self.questionmark_key = QuestionMark_KEY()
        self.at_key = At_KEY()
        self.leftbracket_key = LeftBracket_KEY()
        self.backslash_key = BackSlash_KEY()
        self.rightbracket_key = RightBracket_KEY()
        self.caret_key = Caret_KEY()
        self.underscore_key = Underscore_KEY()
        self.grave_key = Grave_KEY()
        self.primarya_key = PrimaryA_KEY()
        self.primaryb_key = PrimaryB_KEY()
        self.primaryc_key = PrimaryC_KEY()
        self.primaryd_key = PrimaryD_KEY()
        self.primarye_key = PrimaryE_KEY()
        self.primaryf_key = PrimaryF_KEY()
        self.primaryg_key = PrimaryG_KEY()
        self.primaryh_key = PrimaryH_KEY()
        self.primaryi_key = PrimaryI_KEY()
        self.primaryj_key = PrimaryJ_KEY()
        self.primaryk_key = PrimaryK_KEY()
        self.primaryl_key = PrimaryL_KEY()
        self.primarym_key = PrimaryM_KEY()
        self.primaryn_key = PrimaryN_KEY()
        self.primaryo_key = PrimaryO_KEY()
        self.primaryp_key = PrimaryP_KEY()
        self.primaryq_key = PrimaryQ_KEY()
        self.primaryr_key = PrimaryR_KEY()
        self.primarys_key = PrimaryS_KEY()
        self.primaryt_key = PrimaryT_KEY()
        self.primaryu_key = PrimaryU_KEY()
        self.primaryv_key = PrimaryV_KEY()
        self.primaryw_key = PrimaryW_KEY()
        self.primaryx_key = PrimaryX_KEY()
        self.primaryy_key = PrimaryY_KEY()
        self.primaryz_key = PrimaryZ_KEY()
        self.delete_key = Delete_KEY()
        self.numpad0_key = Numpad0_KEY()
        self.numpad1_key = Numpad1_KEY()
        self.numpad2_key = Numpad2_KEY()
        self.numpad3_key = Numpad3_KEY()
        self.numpad4_key = Numpad4_KEY()
        self.numpad5_key = Numpad5_KEY()
        self.numpad6_key = Numpad6_KEY()
        self.numpad7_key = Numpad7_KEY()
        self.numpad8_key = Numpad8_KEY()
        self.numpad9_key = Numpad9_KEY()
        self.numpadperiod_key = NumpadPeriod_KEY()
        self.numpaddivide_key = NumpadDivide_KEY()
        self.numpadmultiply_key = NumpadMultiply_KEY()
        self.numpadminus_key = NumpadMinus_KEY()
        self.numpadplus_key = NumpadPlus_KEY()
        self.numpadenter_key = NumpadEnter_KEY()
        self.numpadequals_key = NumpadEquals_KEY()
        self.up_key = Up_KEY()
        self.down_key = Down_KEY()
        self.right_key = Right_KEY()
        self.left_key = Left_KEY()
        self.insert_key = Insert_KEY()
        self.home_key = Home_KEY()
        self.end_key = End_KEY()
        self.pageup_key = PageUp_KEY()
        self.pagedown_key = PageDown_KEY()
        self.function1_key = Function1_KEY()
        self.function2_key = Function2_KEY()
        self.function3_key = Function3_KEY()
        self.function4_key = Function4_KEY()
        self.function5_key = Function5_KEY()
        self.function6_key = Function6_KEY()
        self.function7_key = Function7_KEY()
        self.function8_key = Function8_KEY()
        self.function9_key = Function9_KEY()
        self.function10_key = Function10_KEY()
        self.function11_key = Function11_KEY()
        self.function12_key = Function12_KEY()
        self.function13_key = Function13_KEY()
        self.function14_key = Function14_KEY()
        self.function15_key = Function15_KEY()
        self.numlock_key = NumLock_KEY()
        self.capslock_key = CapsLock_KEY()
        self.scrolllock_key = ScrollLock_KEY()
        self.rightshift_key = RightShift_KEY()
        self.leftshift_key = LeftShift_KEY()
        self.shift_key = Shift_KEY()
        self.rightcontrol_key = RightControl_KEY()
        self.leftcontrol_key = LeftControl_KEY()
        self.control_key = Control_KEY()
        self.rightalt_key = RightAlt_KEY()
        self.leftalt_key = LeftAlt_KEY()
        self.alt_key = Alt_KEY()
        self.rightmeta_key = RightMeta_KEY()
        self.leftmeta_key = LeftMeta_KEY()
        self.meta_key = Meta_KEY()
        self.leftsuper_key = LeftSuper_KEY()
        self.rightsuper_key = RightSuper_KEY()
        self.super_key = Super_KEY()
        self.mode_key = Mode_KEY()
        self.help_key = Help_KEY()
        self.print_key = Print_KEY()
        self.systemrequest_key = SystemRequest_KEY()
        self.break_key = Break_KEY()
        self.menu_key = Menu_KEY()
        self.power_key = Power_KEY()
        self.euro_key = Euro_KEY()
        self.androidback_key = AndroidBack_KEY()
        self.leftbutton_mouse = LeftButton_MOUSE()
        self.middlebutton_mouse = MiddleButton_MOUSE()
        self.rightbutton_mouse = RightButton_MOUSE()
        self.mouse_scroll = Mouse_SCROLL()
        self.mouse_position = Mouse_POSITION()
        self.active_event = Active_EVENT()
        self.appterminating_event = AppTerminating_EVENT()
        self.applowmemory_event = AppLowMemory_EVENT()
        self.appwillenterbackground_event = AppWillEnterBackground_EVENT()
        self.appdidenterbackground_event = AppDidEnterBackground_EVENT()
        self.appwillenterforeground_event = AppWillEnterForeground_EVENT()
        self.appdidenterforeground_event = AppDidEnterForeground_EVENT()
        self.audiodeviceadded_event = AudioDeviceAdded_EVENT()
        self.audiodeviceremoved_event = AudioDeviceRemoved_EVENT()
        self.clipboardupdate_event = ClipBoardUpdate_EVENT()
        self.dropfile_event = DropFile_EVENT()
        self.droptext_event = DropText_EVENT()
        self.dropbegin_event = DropBegin_EVENT()
        self.dropcomplete_event = DropComplete_EVENT()
        self.fingermotion_event = FingerMotion_EVENT()
        self.fingerdown_event = FingerDown_EVENT()
        self.fingerup_event = FingerUp_EVENT()
        self.keymapchanged_event = KeyMapChanged_EVENT()
        self.localechanged_event = LocaleChanged_EVENT()
        self.multigesture_event = MultiGesture_EVENT()
        self.noevent_event = NoEvent_EVENT()
        self.quit_event = Quit_EVENT()
        self.rendertargetsreset_event = RenderTargetsReset_EVENT()
        self.renderdevicereset_event = RenderDeviceReset_EVENT()
        self.syswmevent_event = SysWMEvent_EVENT()
        self.textinput_event = TextInput_EVENT()
        self.textediting_event = TextEditing_EVENT()
        self.videoresize_event = VideoResize_EVENT()
        self.videoexpose_event = VideoExpose_EVENT()
        self.midiin_event = MidiIn_EVENT()
        self.midiout_event = MidiOut_EVENT()
        self.windowshown_event = WindowShown_EVENT()
        self.windowhidden_event = WindowHidden_EVENT()
        self.windowexposed_event = WindowExposed_EVENT()
        self.windowmoved_event = WindowMoved_EVENT()
        self.windowresized_event = WindowResized_EVENT()
        self.windowsizechanged_event = WindowSizeChanged_EVENT()
        self.windowminimized_event = WindowMinimized_EVENT()
        self.windowmaximized_event = WindowMaximized_EVENT()
        self.windowrestored_event = WindowRestored_EVENT()
        self.windowenter_event = WindowEnter_EVENT()
        self.windowleave_event = WindowLeave_EVENT()
        self.windowfocusgained_event = WindowFocusGained_EVENT()
        self.windowfocuslost_event = WindowFocusLost_EVENT()
        self.windowclose_event = WindowClose_EVENT()
        self.windowtakefocus_event = WindowTakeFocus_EVENT()
        self.windowhittest_event = WindowHitTest_EVENT()
        self.windowiccprofchanged_event = WindowICCPROFChanged_EVENT()
        self.windowdisplaychanged_event = WindowDisplayChanged_EVENT()
        self.joydeviceadded_event = JoyDeviceAdded_EVENT()
        self.joydeviceremoved_event = JoyDeviceRemoved_EVENT()

    def handle(self, enable_toggle_full_screen=True):
        if self.iteration_id == Registry.iteration_id:
            log_development("You have called the 'handle()' method from events \
multiple times within a single game loop. Whilst this isn't always a bad thing, \
it can lead to unexpected behavior a some events might not be captured reliably \
at each method call. For instance, one event might appear randomly between two \
different event loops, instead of consistently at one you might be expecting to \
find it at. If this isn't something you where intending to do, changing this will \
potentially save a lot of headaches later down the line.")
        self.iteration_id = Registry.iteration_id

        self.active_event.set_value(False)
        self.appterminating_event.set_value(False)
        self.applowmemory_event.set_value(False)
        self.appwillenterbackground_event.set_value(False)
        self.appdidenterbackground_event.set_value(False)
        self.appwillenterforeground_event.set_value(False)
        self.appdidenterforeground_event.set_value(False)
        self.audiodeviceadded_event.set_value(False)
        self.audiodeviceremoved_event.set_value(False)
        self.clipboardupdate_event.set_value(False)
        self.dropfile_event.set_value(False)
        self.droptext_event.set_value(False)
        self.dropbegin_event.set_value(False)
        self.dropcomplete_event.set_value(False)
        self.fingermotion_event.set_value(False)
        self.fingerdown_event.set_value(False)
        self.fingerup_event.set_value(False)
        self.keymapchanged_event.set_value(False)
        self.localechanged_event.set_value(False)
        self.multigesture_event.set_value(False)
        self.noevent_event.set_value(False)
        self.quit_event.set_value(False)
        self.rendertargetsreset_event.set_value(False)
        self.renderdevicereset_event.set_value(False)
        self.syswmevent_event.set_value(False)
        self.textinput_event.set_value(False)
        self.textediting_event.set_value(False)
        self.videoresize_event.set_value(False)
        self.videoexpose_event.set_value(False)
        self.midiin_event.set_value(False)
        self.midiout_event.set_value(False)
        self.windowshown_event.set_value(False)
        self.windowhidden_event.set_value(False)
        self.windowexposed_event.set_value(False)
        self.windowmoved_event.set_value(False)
        self.windowresized_event.set_value(False)
        self.windowsizechanged_event.set_value(False)
        self.windowminimized_event.set_value(False)
        self.windowmaximized_event.set_value(False)
        self.windowrestored_event.set_value(False)
        self.windowenter_event.set_value(False)
        self.windowleave_event.set_value(False)
        self.windowfocusgained_event.set_value(False)
        self.windowfocuslost_event.set_value(False)
        self.windowclose_event.set_value(False)
        self.windowtakefocus_event.set_value(False)
        self.windowhittest_event.set_value(False)
        self.windowiccprofchanged_event.set_value(False)
        self.windowdisplaychanged_event.set_value(False)
        self.joydeviceadded_event.set_value(False)
        self.joydeviceremoved_event.set_value(False)

        if Registry.display_mode == Constants.PYGAME:
            raw_events = _pygame.event.get()
            for event in raw_events:
                if event.type == _pygame.ACTIVEEVENT:
                    self.active_event.set_value(True)

                if event.type == _pygame.APP_TERMINATING:
                    self.appterminating_event.set_value(True)

                if event.type == _pygame.APP_LOWMEMORY:
                    self.applowmemory_event.set_value(True)

                if event.type == _pygame.APP_WILLENTERBACKGROUND:
                    self.appwillenterbackground_event.set_value(True)

                if event.type == _pygame.APP_DIDENTERBACKGROUND:
                    self.appdidenterbackground_event.set_value(True)

                if event.type == _pygame.APP_WILLENTERFOREGROUND:
                    self.appwillenterbackground_event.set_value(True)

                if event.type == _pygame.APP_DIDENTERFOREGROUND:
                    self.appdidenterforeground_event.set_value(True)

                if event.type == _pygame.AUDIODEVICEADDED:
                    self.audiodeviceadded_event.set_value(True)

                if event.type == _pygame.AUDIODEVICEREMOVED:
                    self.audiodeviceremoved_event.set_value(True)

                if event.type == _pygame.CLIPBOARDUPDATE:
                    self.clipboardupdate_event.set_value(True)

                if event.type == _pygame.DROPFILE:
                    self.dropfile_event.set_value(True)

                if event.type == _pygame.DROPTEXT:
                    self.droptext_event.set_value(True)

                if event.type == _pygame.DROPBEGIN:
                    self.dropbegin_event.set_value(True)

                if event.type == _pygame.DROPCOMPLETE:
                    self.dropcomplete_event.set_value(True)

                if event.type == _pygame.FINGERMOTION:
                    self.fingermotion_event.set_value(True)

                if event.type == _pygame.FINGERDOWN:
                    self.fingerdown_event.set_value(True)

                if event.type == _pygame.FINGERUP:
                    self.fingerup_event.set_value(True)

                if event.type == _pygame.KEYMAPCHANGED:
                    self.keymapchanged_event.set_value(True)

                if event.type == _pygame.JOYAXISMOTION:
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

                if event.type == _pygame.JOYBALLMOTION:
                    controller = self.controllers.get_controller(event.joy)
                    trackball = controller.get_track_ball_from_id(event.ball)
                    x_motion, y_motion = event.rel
                    trackball.set_x_motion(x_motion)
                    trackball.set_y_motion(y_motion)

                if event.type == _pygame.JOYBUTTONDOWN:
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

                if event.type == _pygame.JOYBUTTONUP:
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

                if event.type == _pygame.JOYDEVICEADDED:
                    self.joydeviceadded_event.set_value(True)

                if event.type == _pygame.JOYDEVICEREMOVED:
                    self.joydeviceremoved_event.set_value(True)

                if event.type == _pygame.LOCALECHANGED:
                    self.localechanged_event.set_value(True)

                if event.type == _pygame.MOUSEMOTION:
                    mouse_x_position, mouse_y_position = event.pos
                    mouse_x_displacement, mouse_y_displacement = event.rel
                    self.mouse_position.set_x_axis(mouse_x_position)
                    self.mouse_position.set_y_axis(mouse_y_position)
                    self.mouse_position.set_x_axis_displacement(mouse_x_displacement)
                    self.mouse_position.set_y_axis_displacement(mouse_y_displacement)

                if event.type == _pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.leftbutton_mouse.set_pressed(True)

                    elif event.button == 2:
                        self.middlebutton_mouse.set_pressed(True)

                    elif event.button == 3:
                        self.rightbutton_mouse.set_pressed(True)

                if event.type == _pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.leftbutton_mouse.set_pressed(False)

                    elif event.button == 2:
                        self.middlebutton_mouse.set_pressed(False)

                    elif event.button == 3:
                        self.rightbutton_mouse.set_pressed(False)

                if event.type == _pygame.MOUSEWHEEL:
                    self.mouse_scroll.set_scroll_displacement(event.precise_y)
                    total_scroll = self.mouse_scroll.get_scroll_value()
                    self.mouse_scroll.set_scroll_value(total_scroll + event.precise_y)

                if event.type == _pygame.KEYDOWN:
                    pass

                if event.type == _pygame.KEYUP:
                    pass

                if event.type == _pygame.MULTIGESTURE:
                    self.multigesture_event.set_value(True)

                if event.type == _pygame.NOEVENT:
                    self.noevent_event.set_value(True)

                if event.type == _pygame.QUIT:
                    self.quit_event.set_value(True)

                if event.type == _pygame.RENDER_TARGETS_RESET:
                    self.rendertargetsreset_event.set_value(True)

                if event.type == _pygame.RENDER_DEVICE_RESET:
                    self.renderdevicereset_event.set_value(True)

                if event.type == _pygame.SYSWMEVENT:
                    self.syswmevent_event.set_value(True)

                if event.type == _pygame.TEXTEDITING:
                    self.textediting_event.set_value(True)

                if event.type == _pygame.TEXTINPUT:
                    self.textinput_event.set_value(True)

                if event.type == _pygame.VIDEORESIZE:
                    self.videoresize_event.set_value(True)

                if event.type == _pygame.VIDEOEXPOSE:
                    self.videoexpose_event.set_value(True)

                if event.type == _pygame.MIDIIN:
                    self.midiin_event.set_value(True)

                if event.type == _pygame.MIDIOUT:
                    self.midiout_event.set_value(True)

                if event.type == _pygame.WINDOWSHOWN:
                    self.windowshown_event.set_value(True)

                if event.type == _pygame.WINDOWHIDDEN:
                    self.windowhidden_event.set_value(True)

                if event.type == _pygame.WINDOWEXPOSED:
                    self.windowexposed_event.set_value(True)

                if event.type == _pygame.WINDOWMOVED:
                    self.windowmoved_event.set_value(True)

                if event.type == _pygame.WINDOWRESIZED:
                    self.windowresized_event.set_value(True)

                if event.type == _pygame.WINDOWSIZECHANGED:
                    self.windowsizechanged_event.set_value(True)

                if event.type == _pygame.WINDOWMINIMIZED:
                    self.windowminimized_event.set_value(True)

                if event.type == _pygame.WINDOWMAXIMIZED:
                    self.windowmaximized_event.set_value(True)

                if event.type == _pygame.WINDOWRESTORED:
                    self.windowfocusgained_event.set_value(True)

                if event.type == _pygame.WINDOWENTER:
                    self.windowenter_event.set_value(True)

                if event.type == _pygame.WINDOWLEAVE:
                    self.windowleave_event.set_value(True)

                if event.type == _pygame.WINDOWFOCUSGAINED:
                    self.windowfocusgained_event.set_value(True)

                if event.type == _pygame.WINDOWFOCUSLOST:
                    self.windowfocuslost_event.set_value(True)

                if event.type == _pygame.WINDOWCLOSE:
                    self.windowclose_event.set_value(True)

                if event.type == _pygame.WINDOWTAKEFOCUS:
                    self.windowtakefocus_event.set_value(True)

                if event.type == _pygame.WINDOWHITTEST:
                    self.windowhittest_event.set_value(True)

                if event.type == _pygame.WINDOWICCPROFCHANGED:
                    self.windowiccprofchanged_event.set_value(True)

                if event.type == _pygame.WINDOWDISPLAYCHANGED:
                    self.windowdisplaychanged_event.set_value(True)

class Backspace_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.BACKSPACE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.BACKSPACE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.BACKSPACE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.BACKSPACE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.BACKSPACE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.BACKSPACE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.BACKSPACE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.BACKSPACE_KEY_OBJECT].set_double_tap_timing(value)

class Tab_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.TAB_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.TAB_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.TAB_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.TAB_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.TAB_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.TAB_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.TAB_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.TAB_KEY_OBJECT].set_double_tap_timing(value)

class Clear_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.CLEAR_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.CLEAR_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.CLEAR_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.CLEAR_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.CLEAR_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.CLEAR_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.CLEAR_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.CLEAR_KEY_OBJECT].set_double_tap_timing(value)

class Return_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RETURN_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RETURN_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RETURN_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RETURN_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RETURN_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RETURN_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RETURN_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RETURN_KEY_OBJECT].set_double_tap_timing(value)

class Pause_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PAUSE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PAUSE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PAUSE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PAUSE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PAUSE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PAUSE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PAUSE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PAUSE_KEY_OBJECT].set_double_tap_timing(value)

class Escape_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.ESCAPE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.ESCAPE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.ESCAPE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.ESCAPE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.ESCAPE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.ESCAPE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.ESCAPE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.ESCAPE_KEY_OBJECT].set_double_tap_timing(value)

class Space_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.SPACE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.SPACE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.SPACE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.SPACE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.SPACE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.SPACE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.SPACE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.SPACE_KEY_OBJECT].set_double_tap_timing(value)

class ExclamationMark_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.EXCLAMATIONMARK_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.EXCLAMATIONMARK_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.EXCLAMATIONMARK_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.EXCLAMATIONMARK_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.EXCLAMATIONMARK_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.EXCLAMATIONMARK_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.EXCLAMATIONMARK_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.EXCLAMATIONMARK_KEY_OBJECT].set_double_tap_timing(value)

class DoubleQuote_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.DOUBLEQUOTE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.DOUBLEQUOTE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.DOUBLEQUOTE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.DOUBLEQUOTE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.DOUBLEQUOTE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.DOUBLEQUOTE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.DOUBLEQUOTE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.DOUBLEQUOTE_KEY_OBJECT].set_double_tap_timing(value)

class Hashtag_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.HASHTAG_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.HASHTAG_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.HASHTAG_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.HASHTAG_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.HASHTAG_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.HASHTAG_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.HASHTAG_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.HASHTAG_KEY_OBJECT].set_double_tap_timing(value)

class Dollar_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.DOLLAR_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.DOLLAR_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.DOLLAR_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.DOLLAR_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.DOLLAR_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.DOLLAR_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.DOLLAR_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.DOLLAR_KEY_OBJECT].set_double_tap_timing(value)

class Ampersand_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.AMPERSAND_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.AMPERSAND_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.AMPERSAND_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.AMPERSAND_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.AMPERSAND_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.AMPERSAND_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.AMPERSAND_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.AMPERSAND_KEY_OBJECT].set_double_tap_timing(value)

class SingleQuote_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.SINGLEQUOTE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.SINGLEQUOTE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.SINGLEQUOTE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.SINGLEQUOTE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.SINGLEQUOTE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.SINGLEQUOTE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.SINGLEQUOTE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.SINGLEQUOTE_KEY_OBJECT].set_double_tap_timing(value)

class LeftParenthesis_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFTPARENTHESIS_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFTPARENTHESIS_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFTPARENTHESIS_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFTPARENTHESIS_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFTPARENTHESIS_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFTPARENTHESIS_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFTPARENTHESIS_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFTPARENTHESIS_KEY_OBJECT].set_double_tap_timing(value)

class RightParenthesis_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHTPARENTHESIS_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHTPARENTHESIS_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHTPARENTHESIS_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHTPARENTHESIS_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHTPARENTHESIS_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHTPARENTHESIS_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHTPARENTHESIS_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHTPARENTHESIS_KEY_OBJECT].set_double_tap_timing(value)

class Asterisk_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.ASTERISK_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.ASTERISK_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.ASTERISK_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.ASTERISK_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.ASTERISK_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.ASTERISK_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.ASTERISK_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.ASTERISK_KEY_OBJECT].set_double_tap_timing(value)

class Plus_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PLUS_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PLUS_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PLUS_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PLUS_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PLUS_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PLUS_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PLUS_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PLUS_KEY_OBJECT].set_double_tap_timing(value)

class Comma_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.COMMA_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.COMMA_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.COMMA_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.COMMA_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.COMMA_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.COMMA_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.COMMA_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.COMMA_KEY_OBJECT].set_double_tap_timing(value)

class Minus_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.MINUS_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.MINUS_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.MINUS_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.MINUS_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.MINUS_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.MINUS_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.MINUS_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.MINUS_KEY_OBJECT].set_double_tap_timing(value)

class Period_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PERIOD_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PERIOD_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PERIOD_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PERIOD_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PERIOD_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PERIOD_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PERIOD_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PERIOD_KEY_OBJECT].set_double_tap_timing(value)

class ForwardSlash_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FORWARDSLASH_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FORWARDSLASH_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FORWARDSLASH_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FORWARDSLASH_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FORWARDSLASH_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FORWARDSLASH_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FORWARDSLASH_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FORWARDSLASH_KEY_OBJECT].set_double_tap_timing(value)

class Primary0_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY0_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY0_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY0_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY0_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY0_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY0_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY0_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY0_KEY_OBJECT].set_double_tap_timing(value)

class Primary1_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY1_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY1_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY1_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY1_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY1_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY1_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY1_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY1_KEY_OBJECT].set_double_tap_timing(value)

class Primary2_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY2_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY2_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY2_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY2_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY2_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY2_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY2_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY2_KEY_OBJECT].set_double_tap_timing(value)

class Primary3_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY3_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY3_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY3_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY3_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY3_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY3_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY3_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY3_KEY_OBJECT].set_double_tap_timing(value)

class Primary4_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY4_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY4_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY4_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY4_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY4_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY4_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY4_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY4_KEY_OBJECT].set_double_tap_timing(value)

class Primary5_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY5_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY5_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY5_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY5_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY5_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY5_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY5_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY5_KEY_OBJECT].set_double_tap_timing(value)

class Primary6_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY6_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY6_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY6_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY6_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY6_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY6_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY6_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY6_KEY_OBJECT].set_double_tap_timing(value)

class Primary7_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY7_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY7_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY7_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY7_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY7_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY7_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY7_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY7_KEY_OBJECT].set_double_tap_timing(value)

class Primary8_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY8_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY8_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY8_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY8_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY8_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY8_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY8_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY8_KEY_OBJECT].set_double_tap_timing(value)

class Primary9_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY9_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARY9_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARY9_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY9_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARY9_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY9_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARY9_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARY9_KEY_OBJECT].set_double_tap_timing(value)

class Colon_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.COLON_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.COLON_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.COLON_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.COLON_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.COLON_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.COLON_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.COLON_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.COLON_KEY_OBJECT].set_double_tap_timing(value)

class SemiColon_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.SEMICOLON_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.SEMICOLON_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.SEMICOLON_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.SEMICOLON_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.SEMICOLON_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.SEMICOLON_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.SEMICOLON_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.SEMICOLON_KEY_OBJECT].set_double_tap_timing(value)

class LessThan_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LESSTHAN_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LESSTHAN_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LESSTHAN_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LESSTHAN_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LESSTHAN_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LESSTHAN_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LESSTHAN_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LESSTHAN_KEY_OBJECT].set_double_tap_timing(value)

class Equals_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.EQUALS_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.EQUALS_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.EQUALS_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.EQUALS_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.EQUALS_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.EQUALS_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.EQUALS_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.EQUALS_KEY_OBJECT].set_double_tap_timing(value)

class GreaterThan_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.GREATERTHAN_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.GREATERTHAN_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.GREATERTHAN_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.GREATERTHAN_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.GREATERTHAN_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.GREATERTHAN_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.GREATERTHAN_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.GREATERTHAN_KEY_OBJECT].set_double_tap_timing(value)

class QuestionMark_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.QUESTIONMARK_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.QUESTIONMARK_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.QUESTIONMARK_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.QUESTIONMARK_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.QUESTIONMARK_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.QUESTIONMARK_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.QUESTIONMARK_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.QUESTIONMARK_KEY_OBJECT].set_double_tap_timing(value)

class At_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.AT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.AT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.AT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.AT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.AT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.AT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.AT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.AT_KEY_OBJECT].set_double_tap_timing(value)

class LeftBracket_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFTBRACKET_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFTBRACKET_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFTBRACKET_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFTBRACKET_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFTBRACKET_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFTBRACKET_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFTBRACKET_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFTBRACKET_KEY_OBJECT].set_double_tap_timing(value)

class BackSlash_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.BACKSLASH_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.BACKSLASH_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.BACKSLASH_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.BACKSLASH_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.BACKSLASH_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.BACKSLASH_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.BACKSLASH_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.BACKSLASH_KEY_OBJECT].set_double_tap_timing(value)

class RightBracket_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHTBRACKET_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHTBRACKET_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHTBRACKET_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHTBRACKET_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHTBRACKET_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHTBRACKET_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHTBRACKET_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHTBRACKET_KEY_OBJECT].set_double_tap_timing(value)

class Caret_KEY: # ^
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.CARET_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.CARET_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.CARET_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.CARET_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.CARET_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.CARET_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.CARET_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.CARET_KEY_OBJECT].set_double_tap_timing(value)

class Underscore_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.UNDERSCORE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.UNDERSCORE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.UNDERSCORE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.UNDERSCORE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.UNDERSCORE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.UNDERSCORE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.UNDERSCORE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.UNDERSCORE_KEY_OBJECT].set_double_tap_timing(value)

class Grave_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.GRAVE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.GRAVE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.GRAVE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.GRAVE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.GRAVE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.GRAVE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.GRAVE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.GRAVE_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryA_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYA_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYA_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYA_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYA_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYA_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYA_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYA_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYA_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryB_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYB_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYB_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYB_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYB_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYB_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYB_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYB_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYB_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryC_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYC_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYC_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYC_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYC_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYC_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYC_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYC_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYC_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryD_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYD_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYD_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYD_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYD_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYD_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYD_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYD_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYD_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryE_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYE_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryF_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYF_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYF_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYF_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYF_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYF_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYF_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYF_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYF_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryG_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYG_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYG_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYG_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYG_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYG_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYG_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYG_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYG_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryH_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYH_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYH_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYH_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYH_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYH_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYH_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYH_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYH_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryI_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYI_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYI_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYI_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYI_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYI_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYI_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYI_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYI_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryJ_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYJ_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYJ_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYJ_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYJ_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYJ_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYJ_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYJ_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYJ_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryK_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYK_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYK_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYK_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYK_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYK_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYK_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYK_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYK_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryL_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYL_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYL_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYL_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYL_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYL_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYL_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYL_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYL_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryM_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYM_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYM_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYM_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYM_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYM_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYM_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYM_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYM_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryN_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYN_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYN_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYN_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYN_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYN_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYN_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYN_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYN_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryO_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYO_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYO_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYO_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYO_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYO_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYO_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYO_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYO_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryP_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYP_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYP_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYP_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYP_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYP_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYP_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYP_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYP_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryQ_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYQ_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYQ_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYQ_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYQ_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYQ_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYQ_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYQ_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYQ_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryR_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYR_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYR_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYR_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYR_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYR_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYR_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYR_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYR_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryS_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYS_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYS_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYS_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYS_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYS_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYS_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYS_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYS_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryT_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYT_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryU_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYU_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYU_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYU_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYU_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYU_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYU_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYU_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYU_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryV_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYV_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYV_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYV_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYV_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYV_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYV_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYV_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYV_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryW_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYW_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYW_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYW_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYW_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYW_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYW_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYW_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYW_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryX_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYX_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYX_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYX_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYX_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYX_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYX_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYX_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYX_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryY_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYY_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYY_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYY_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYY_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYY_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYY_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYY_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYY_KEY_OBJECT].set_double_tap_timing(value)

class PrimaryZ_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYZ_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRIMARYZ_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRIMARYZ_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYZ_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRIMARYZ_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYZ_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRIMARYZ_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRIMARYZ_KEY_OBJECT].set_double_tap_timing(value)

class Delete_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.DELETE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.DELETE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.DELETE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.DELETE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.DELETE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.DELETE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.DELETE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.DELETE_KEY_OBJECT].set_double_tap_timing(value)

class Numpad0_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD0_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD0_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD0_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD0_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD0_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD0_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD0_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD0_KEY_OBJECT].set_double_tap_timing(value)

class Numpad1_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD1_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD1_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD1_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD1_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD1_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD1_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD1_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD1_KEY_OBJECT].set_double_tap_timing(value)

class Numpad2_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD2_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD2_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD2_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD2_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD2_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD2_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD2_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD2_KEY_OBJECT].set_double_tap_timing(value)

class Numpad3_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD3_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD3_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD3_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD3_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD3_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD3_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD3_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD3_KEY_OBJECT].set_double_tap_timing(value)

class Numpad4_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD4_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD4_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD4_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD4_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD4_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD4_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD4_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD4_KEY_OBJECT].set_double_tap_timing(value)

class Numpad5_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD5_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD5_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD5_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD5_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD5_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD5_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD5_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD5_KEY_OBJECT].set_double_tap_timing(value)

class Numpad6_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD6_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD6_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD6_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD6_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD6_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD6_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD6_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD6_KEY_OBJECT].set_double_tap_timing(value)

class Numpad7_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD7_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD7_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD7_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD7_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD7_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD7_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD7_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD7_KEY_OBJECT].set_double_tap_timing(value)

class Numpad8_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD8_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD8_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD8_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD8_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD8_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD8_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD8_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD8_KEY_OBJECT].set_double_tap_timing(value)

class Numpad9_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD9_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPAD9_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPAD9_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD9_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPAD9_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD9_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPAD9_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPAD9_KEY_OBJECT].set_double_tap_timing(value)

class NumpadPeriod_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPADPERIOD_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPADPERIOD_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPADPERIOD_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPADPERIOD_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPADPERIOD_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPADPERIOD_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPADPERIOD_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPADPERIOD_KEY_OBJECT].set_double_tap_timing(value)

class NumpadDivide_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPADDIVIDE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPADDIVIDE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPADDIVIDE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPADDIVIDE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPADDIVIDE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPADDIVIDE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPADDIVIDE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPADDIVIDE_KEY_OBJECT].set_double_tap_timing(value)

class NumpadMultiply_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPADMULTIPLY_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPADMULTIPLY_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPADMULTIPLY_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPADMULTIPLY_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPADMULTIPLY_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPADMULTIPLY_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPADMULTIPLY_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPADMULTIPLY_KEY_OBJECT].set_double_tap_timing(value)

class NumpadMinus_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPADMINUS_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPADMINUS_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPADMINUS_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPADMINUS_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPADMINUS_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPADMINUS_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPADMINUS_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPADMINUS_KEY_OBJECT].set_double_tap_timing(value)

class NumpadPlus_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPADPLUS_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPADPLUS_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPADPLUS_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPADPLUS_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPADPLUS_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPADPLUS_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPADPLUS_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPADPLUS_KEY_OBJECT].set_double_tap_timing(value)

class NumpadEnter_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPADENTER_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPADENTER_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPADENTER_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPADENTER_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPADENTER_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPADENTER_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPADENTER_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPADENTER_KEY_OBJECT].set_double_tap_timing(value)

class NumpadEquals_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMPADEQUALS_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMPADEQUALS_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMPADEQUALS_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMPADEQUALS_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMPADEQUALS_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMPADEQUALS_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMPADEQUALS_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMPADEQUALS_KEY_OBJECT].set_double_tap_timing(value)

class Up_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.UP_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.UP_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.UP_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.UP_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.UP_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.UP_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.UP_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.UP_KEY_OBJECT].set_double_tap_timing(value)

class Down_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.DOWN_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.DOWN_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.DOWN_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.DOWN_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.DOWN_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.DOWN_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.DOWN_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.DOWN_KEY_OBJECT].set_double_tap_timing(value)

class Right_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHT_KEY_OBJECT].set_double_tap_timing(value)

class Left_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFT_KEY_OBJECT].set_double_tap_timing(value)

class Insert_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.INSERT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.INSERT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.INSERT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.INSERT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.INSERT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.INSERT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.INSERT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.INSERT_KEY_OBJECT].set_double_tap_timing(value)

class Home_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.HOME_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.HOME_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.HOME_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.HOME_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.HOME_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.HOME_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.HOME_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.HOME_KEY_OBJECT].set_double_tap_timing(value)

class End_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.END_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.END_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.END_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.END_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.END_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.END_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.END_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.END_KEY_OBJECT].set_double_tap_timing(value)

class PageUp_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PAGEUP_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PAGEUP_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PAGEUP_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PAGEUP_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PAGEUP_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PAGEUP_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PAGEUP_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PAGEUP_KEY_OBJECT].set_double_tap_timing(value)

class PageDown_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PAGEDOWN_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PAGEDOWN_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PAGEDOWN_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PAGEDOWN_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PAGEDOWN_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PAGEDOWN_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PAGEDOWN_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PAGEDOWN_KEY_OBJECT].set_double_tap_timing(value)

class Function1_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION1_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION1_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION1_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION1_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION1_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION1_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION1_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION1_KEY_OBJECT].set_double_tap_timing(value)

class Function2_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION2_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION2_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION2_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION2_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION2_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION2_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION2_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION2_KEY_OBJECT].set_double_tap_timing(value)

class Function3_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION3_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION3_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION3_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION3_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION3_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION3_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION3_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION3_KEY_OBJECT].set_double_tap_timing(value)

class Function4_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION4_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION4_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION4_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION4_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION4_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION4_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION4_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION4_KEY_OBJECT].set_double_tap_timing(value)

class Function5_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION5_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION5_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION5_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION5_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION5_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION5_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION5_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION5_KEY_OBJECT].set_double_tap_timing(value)

class Function6_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION6_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION6_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION6_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION6_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION6_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION6_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION6_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION6_KEY_OBJECT].set_double_tap_timing(value)

class Function7_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION7_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION7_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION7_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION7_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION7_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION7_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION7_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION7_KEY_OBJECT].set_double_tap_timing(value)

class Function8_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION8_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION8_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION8_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION8_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION8_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION8_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION8_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION8_KEY_OBJECT].set_double_tap_timing(value)

class Function9_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION9_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION9_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION9_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION9_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION9_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION9_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION9_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION9_KEY_OBJECT].set_double_tap_timing(value)

class Function10_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION10_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION10_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION10_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION10_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION10_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION10_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION10_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION10_KEY_OBJECT].set_double_tap_timing(value)

class Function11_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION11_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION11_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION11_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION11_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION11_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION11_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION11_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION11_KEY_OBJECT].set_double_tap_timing(value)

class Function12_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION12_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION12_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION12_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION12_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION12_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION12_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION12_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION12_KEY_OBJECT].set_double_tap_timing(value)

class Function13_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION13_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION13_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION13_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION13_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION13_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION13_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION13_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION13_KEY_OBJECT].set_double_tap_timing(value)

class Function14_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION14_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION14_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION14_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION14_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION14_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION14_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION14_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION14_KEY_OBJECT].set_double_tap_timing(value)

class Function15_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION15_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.FUNCTION15_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.FUNCTION15_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION15_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.FUNCTION15_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION15_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.FUNCTION15_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.FUNCTION15_KEY_OBJECT].set_double_tap_timing(value)

class NumLock_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.NUMLOCK_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.NUMLOCK_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.NUMLOCK_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.NUMLOCK_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.NUMLOCK_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.NUMLOCK_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.NUMLOCK_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.NUMLOCK_KEY_OBJECT].set_double_tap_timing(value)

class CapsLock_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.CAPSLOCK_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.CAPSLOCK_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.CAPSLOCK_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.CAPSLOCK_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.CAPSLOCK_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.CAPSLOCK_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.CAPSLOCK_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.CAPSLOCK_KEY_OBJECT].set_double_tap_timing(value)

class ScrollLock_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.SCROLLLOCK_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.SCROLLLOCK_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.SCROLLLOCK_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.SCROLLLOCK_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.SCROLLLOCK_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.SCROLLLOCK_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.SCROLLLOCK_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.SCROLLLOCK_KEY_OBJECT].set_double_tap_timing(value)

class RightShift_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHTSHIFT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHTSHIFT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHTSHIFT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHTSHIFT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHTSHIFT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHTSHIFT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHTSHIFT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHTSHIFT_KEY_OBJECT].set_double_tap_timing(value)

class LeftShift_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFTSHIFT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFTSHIFT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFTSHIFT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFTSHIFT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFTSHIFT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFTSHIFT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFTSHIFT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFTSHIFT_KEY_OBJECT].set_double_tap_timing(value)

class Shift_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.SHIFT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.SHIFT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.SHIFT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.SHIFT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.SHIFT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.SHIFT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.SHIFT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.SHIFT_KEY_OBJECT].set_double_tap_timing(value)

class RightControl_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHTCONTROL_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHTCONTROL_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHTCONTROL_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHTCONTROL_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHTCONTROL_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHTCONTROL_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHTCONTROL_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHTCONTROL_KEY_OBJECT].set_double_tap_timing(value)

class LeftControl_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFTCONTROL_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFTCONTROL_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFTCONTROL_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFTCONTROL_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFTCONTROL_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFTCONTROL_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFTCONTROL_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFTCONTROL_KEY_OBJECT].set_double_tap_timing(value)

class Control_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.CONTROL_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.CONTROL_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.CONTROL_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.CONTROL_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.CONTROL_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.CONTROL_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.CONTROL_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.CONTROL_KEY_OBJECT].set_double_tap_timing(value)

class RightAlt_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHTALT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHTALT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHTALT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHTALT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHTALT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHTALT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHTALT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHTALT_KEY_OBJECT].set_double_tap_timing(value)

class LeftAlt_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFTALT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFTALT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFTALT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFTALT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFTALT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFTALT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFTALT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFTALT_KEY_OBJECT].set_double_tap_timing(value)

class Alt_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.ALT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.ALT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.ALT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.ALT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.ALT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.ALT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.ALT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.ALT_KEY_OBJECT].set_double_tap_timing(value)

class RightMeta_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHTMETA_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHTMETA_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHTMETA_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHTMETA_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHTMETA_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHTMETA_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHTMETA_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHTMETA_KEY_OBJECT].set_double_tap_timing(value)

class LeftMeta_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFTMETA_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFTMETA_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFTMETA_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFTMETA_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFTMETA_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFTMETA_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFTMETA_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFTMETA_KEY_OBJECT].set_double_tap_timing(value)

class Meta_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.META_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.META_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.META_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.META_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.META_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.META_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.META_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.META_KEY_OBJECT].set_double_tap_timing(value)

class LeftSuper_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFTSUPER_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFTSUPER_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFTSUPER_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFTSUPER_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFTSUPER_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFTSUPER_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFTSUPER_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFTSUPER_KEY_OBJECT].set_double_tap_timing(value)

class RightSuper_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHTSUPER_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHTSUPER_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHTSUPER_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHTSUPER_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHTSUPER_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHTSUPER_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHTSUPER_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHTSUPER_KEY_OBJECT].set_double_tap_timing(value)

class Super_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.SUPER_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.SUPER_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.SUPER_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.SUPER_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.SUPER_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.SUPER_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.SUPER_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.SUPER_KEY_OBJECT].set_double_tap_timing(value)

class Mode_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.MODE_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.MODE_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.MODE_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.MODE_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.MODE_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.MODE_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.MODE_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.MODE_KEY_OBJECT].set_double_tap_timing(value)

class Help_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.HELP_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.HELP_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.HELP_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.HELP_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.HELP_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.HELP_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.HELP_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.HELP_KEY_OBJECT].set_double_tap_timing(value)

class Print_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.PRINT_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.PRINT_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.PRINT_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.PRINT_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.PRINT_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.PRINT_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.PRINT_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.PRINT_KEY_OBJECT].set_double_tap_timing(value)

class SystemRequest_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.SYSTEMREQUEST_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.SYSTEMREQUEST_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.SYSTEMREQUEST_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.SYSTEMREQUEST_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.SYSTEMREQUEST_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.SYSTEMREQUEST_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.SYSTEMREQUEST_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.SYSTEMREQUEST_KEY_OBJECT].set_double_tap_timing(value)

class Break_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.BREAK_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.BREAK_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.BREAK_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.BREAK_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.BREAK_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.BREAK_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.BREAK_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.BREAK_KEY_OBJECT].set_double_tap_timing(value)

class Menu_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.MENU_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.MENU_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.MENU_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.MENU_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.MENU_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.MENU_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.MENU_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.MENU_KEY_OBJECT].set_double_tap_timing(value)

class Power_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.POWER_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.POWER_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.POWER_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.POWER_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.POWER_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.POWER_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.POWER_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.POWER_KEY_OBJECT].set_double_tap_timing(value)

class Euro_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.EURO_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.EURO_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.EURO_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.EURO_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.EURO_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.EURO_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.EURO_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.EURO_KEY_OBJECT].set_double_tap_timing(value)

class AndroidBack_KEY:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.ANDROIDBACK_KEY_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.ANDROIDBACK_KEY_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.ANDROIDBACK_KEY_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.ANDROIDBACK_KEY_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.ANDROIDBACK_KEY_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.ANDROIDBACK_KEY_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.ANDROIDBACK_KEY_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.ANDROIDBACK_KEY_OBJECT].set_double_tap_timing(value)

class LeftButton_MOUSE:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.LEFTBUTTON_MOUSE_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.LEFTBUTTON_MOUSE_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.LEFTBUTTON_MOUSE_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.LEFTBUTTON_MOUSE_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.LEFTBUTTON_MOUSE_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.LEFTBUTTON_MOUSE_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.LEFTBUTTON_MOUSE_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.LEFTBUTTON_MOUSE_OBJECT].set_double_tap_timing(value)

class MiddleButton_MOUSE:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.MIDDLEBUTTON_MOUSE_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.MIDDLEBUTTON_MOUSE_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.MIDDLEBUTTON_MOUSE_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.MIDDLEBUTTON_MOUSE_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.MIDDLEBUTTON_MOUSE_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.MIDDLEBUTTON_MOUSE_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.MIDDLEBUTTON_MOUSE_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.MIDDLEBUTTON_MOUSE_OBJECT].set_double_tap_timing(value)

class RightButton_MOUSE:
    def __init__(self):
        initialize(self)

    def set_double_tapped(self, value):
        Registry.pmma_module_spine[Constants.RIGHTBUTTON_MOUSE_OBJECT].set_double_tapped(value)

    def get_double_tapped(self):
        return Registry.pmma_module_spine[Constants.RIGHTBUTTON_MOUSE_OBJECT].get_double_tapped()

    def get_last_tap_time(self):
        return Registry.pmma_module_spine[Constants.RIGHTBUTTON_MOUSE_OBJECT].get_last_tap_time()

    def set_last_tap_time(self, value):
        Registry.pmma_module_spine[Constants.RIGHTBUTTON_MOUSE_OBJECT].set_last_tap_time(value)

    def get_pressed(self):
        return Registry.pmma_module_spine[Constants.RIGHTBUTTON_MOUSE_OBJECT].get_pressed()

    def set_pressed(self, value):
        Registry.pmma_module_spine[Constants.RIGHTBUTTON_MOUSE_OBJECT].set_pressed(value)

    def get_double_tap_timing(self):
        return Registry.pmma_module_spine[Constants.RIGHTBUTTON_MOUSE_OBJECT].get_double_tap_timing()

    def set_double_tap_timing(self, value):
        Registry.pmma_module_spine[Constants.RIGHTBUTTON_MOUSE_OBJECT].set_double_tap_timing(value)

class Mouse_SCROLL:
    def __init__(self):
        initialize(self)

        self._scroll_value = 0
        self._scroll_displacement = 0

    def get_scroll_displacement(self):
        return Registry.pmma_module_spine[Constants.MOUSE_SCROLL_OBJECT].get_scroll_displacement()

    def set_scroll_displacement(self, value):
        Registry.pmma_module_spine[Constants.MOUSE_SCROLL_OBJECT].set_scroll_displacement(value)

    def get_scroll_value(self):
        return Registry.pmma_module_spine[Constants.MOUSE_SCROLL_OBJECT].get_scroll_value()

    def set_scroll_value(self, value):
        Registry.pmma_module_spine[Constants.MOUSE_SCROLL_OBJECT].set_scroll_value(value)

class Mouse_POSITION:
    def __init__(self):
        initialize(self)

    def get_axis_displacement(self):
        return Registry.pmma_module_spine[Constants.MOUSE_POSITION_OBJECT].get_axis_displacement()

    def get_x_axis_displacement(self):
        return Registry.pmma_module_spine[Constants.MOUSE_POSITION_OBJECT].get_x_axis_displacement()

    def get_y_axis_displacement(self):
        return Registry.pmma_module_spine[Constants.MOUSE_POSITION_OBJECT].get_y_axis_displacement()

    def get_x_axis(self):
        return Registry.pmma_module_spine[Constants.MOUSE_POSITION_OBJECT].get_x_axis()

    def get_y_axis(self):
        return Registry.pmma_module_spine[Constants.MOUSE_POSITION_OBJECT].get_y_axis()

    def set_x_axis(self, value):
        Registry.pmma_module_spine[Constants.MOUSE_POSITION_OBJECT].set_x_axis(value)

    def set_y_axis(self, value):
        Registry.pmma_module_spine[Constants.MOUSE_POSITION_OBJECT].set_y_axis(value)

    def set_x_axis_displacement(self, value):
        Registry.pmma_module_spine[Constants.MOUSE_POSITION_OBJECT].set_x_axis_displacement(value)

    def set_y_axis_displacement(self, value):
        Registry.pmma_module_spine[Constants.MOUSE_POSITION_OBJECT].set_y_axis_displacement(value)

class Active_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.ACTIVE_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.ACTIVE_EVENT_OBJECT].get_value()

class AppTerminating_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.APPTERMINATING_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.APPTERMINATING_EVENT_OBJECT].get_value()

class AppLowMemory_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.APPLOWMEMORY_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.APPLOWMEMORY_EVENT_OBJECT].get_value()

class AppWillEnterBackground_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.APPWILLENTERBACKGROUND_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.APPWILLENTERBACKGROUND_EVENT_OBJECT].get_value()

class AppDidEnterBackground_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.APPDIDENTERBACKGROUND_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.APPDIDENTERBACKGROUND_EVENT_OBJECT].get_value()

class AppWillEnterForeground_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.APPWILLENTERFOREGROUND_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.APPWILLENTERFOREGROUND_EVENT_OBJECT].get_value()

class AppDidEnterForeground_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.APPDIDENTERFOREGROUND_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.APPDIDENTERFOREGROUND_EVENT_OBJECT].get_value()

class AudioDeviceAdded_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.AUDIODEVICEADDED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.AUDIODEVICEADDED_EVENT_OBJECT].get_value()

class AudioDeviceRemoved_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.AUDIODEVICEREMOVED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.AUDIODEVICEREMOVED_EVENT_OBJECT].get_value()

class ClipBoardUpdate_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.CLIPBOARDUPDATE_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.CLIPBOARDUPDATE_EVENT_OBJECT].get_value()

class DropFile_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.DROPFILE_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.DROPFILE_EVENT_OBJECT].get_value()

class DropText_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.DROPTEXT_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.DROPTEXT_EVENT_OBJECT].get_value()

class DropBegin_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.DROPBEGIN_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.DROPBEGIN_EVENT_OBJECT].get_value()

class DropComplete_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.DROPCOMPLETE_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.DROPCOMPLETE_EVENT_OBJECT].get_value()

class FingerMotion_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.FINGERMOTION_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.FINGERMOTION_EVENT_OBJECT].get_value()

class FingerDown_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.FINGERDOWN_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.FINGERDOWN_EVENT_OBJECT].get_value()

class FingerUp_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.FINGERUP_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.FINGERUP_EVENT_OBJECT].get_value()

class KeyMapChanged_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.KEYMAPCHANGED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.KEYMAPCHANGED_EVENT_OBJECT].get_value()

class LocaleChanged_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.LOCALECHANGED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.LOCALECHANGED_EVENT_OBJECT].get_value()

class MultiGesture_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.MULTIGESTURE_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.MULTIGESTURE_EVENT_OBJECT].get_value()

class NoEvent_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.NOEVENT_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.NOEVENT_EVENT_OBJECT].get_value()

class Quit_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.QUIT_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.QUIT_EVENT_OBJECT].get_value()

class RenderTargetsReset_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.RENDERTARGETSRESET_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.RENDERTARGETSRESET_EVENT_OBJECT].get_value()

class RenderDeviceReset_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.RENDERDEVICERESET_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.RENDERDEVICERESET_EVENT_OBJECT].get_value()

class SysWMEvent_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.SYSWMEVENT_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.SYSWMEVENT_EVENT_OBJECT].get_value()

class TextInput_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.TEXTINPUT_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.TEXTINPUT_EVENT_OBJECT].get_value()

class TextEditing_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.TEXTEDITING_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.TEXTEDITING_EVENT_OBJECT].get_value()

class VideoResize_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.VIDEORESIZE_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.VIDEORESIZE_EVENT_OBJECT].get_value()

class VideoExpose_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.VIDEOEXPOSE_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.VIDEOEXPOSE_EVENT_OBJECT].get_value()

class MidiIn_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.MIDIIN_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.MIDIIN_EVENT_OBJECT].get_value()

class MidiOut_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.MIDIOUT_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.MIDIOUT_EVENT_OBJECT].get_value()

class WindowShown_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWSHOWN_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWSHOWN_EVENT_OBJECT].get_value()

class WindowHidden_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWHIDDEN_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWHIDDEN_EVENT_OBJECT].get_value()

class WindowExposed_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWEXPOSED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWEXPOSED_EVENT_OBJECT].get_value()

class WindowMoved_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWMOVED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWMOVED_EVENT_OBJECT].get_value()

class WindowResized_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWRESIZED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWRESIZED_EVENT_OBJECT].get_value()

class WindowSizeChanged_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWSIZECHANGED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWSIZECHANGED_EVENT_OBJECT].get_value()

class WindowMinimized_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWMINIMIZED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWMINIMIZED_EVENT_OBJECT].get_value()

class WindowMaximized_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWMAXIMIZED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWMAXIMIZED_EVENT_OBJECT].get_value()

class WindowRestored_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWRESTORED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWRESTORED_EVENT_OBJECT].get_value()

class WindowEnter_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWENTER_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWENTER_EVENT_OBJECT].get_value()

class WindowLeave_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWLEAVE_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWLEAVE_EVENT_OBJECT].get_value()

class WindowFocusGained_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWFOCUSGAINED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWFOCUSGAINED_EVENT_OBJECT].get_value()

class WindowFocusLost_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWFOCUSLOST_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWFOCUSLOST_EVENT_OBJECT].get_value()

class WindowClose_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWCLOSE_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWCLOSE_EVENT_OBJECT].get_value()

class WindowTakeFocus_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWTAKEFOCUS_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWTAKEFOCUS_EVENT_OBJECT].get_value()

class WindowHitTest_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWHITTEST_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWHITTEST_EVENT_OBJECT].get_value()

class WindowICCPROFChanged_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWICCPROFCHANGED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWICCPROFCHANGED_EVENT_OBJECT].get_value()

class WindowDisplayChanged_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.WINDOWDISPLAYCHANGED_EVENT_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.WINDOWDISPLAYCHANGED_EVENT_OBJECT].get_value()

class JoyDeviceAdded_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.JOYDEVICEADDED_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.JOYDEVICEADDED_OBJECT].get_value()

class JoyDeviceRemoved_EVENT:
    def __init__(self):
        initialize(self)

    def set_value(self, value):
        Registry.pmma_module_spine[Constants.JOYDEVICEREMOVED_OBJECT].set_value(value)

    def get_value(self):
        return Registry.pmma_module_spine[Constants.JOYDEVICEREMOVED_OBJECT].get_value()