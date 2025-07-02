#pragma once
#include "PMMA_Exports.hpp"

#include <stdexcept>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

#include <GLFW/glfw3.h>

#include "NumberConverter.hpp"
#include "Constants.hpp"
#include "EventsCore.hpp"

class EXPORT CPP_ControllerEvent {
    private:
        unsigned int ID;
    public:
        CPP_ControllerEvent(unsigned int new_ID);
        ~CPP_ControllerEvent();

        void Update();

        bool GetConnected();
        std::string GetRawName();
        std::string GetGamePadName();
        std::string GetGUID();

        float GetRawAxis_Decimal(int AxisID);
        float GetRawAxis_Percentage(int AxisID);
        bool GetRawButtonPressed(int ButtonID);
        std::string GetRawHatState(int HatID);

        int GetRawAxisCount();
        int GetRawButtonCount();
        int GetRawHatCount();

        bool GetActive();

        CPP_ButtonPressedEvent* A_Button = nullptr;
        CPP_ButtonPressedEvent* B_Button = nullptr;
        CPP_ButtonPressedEvent* X_Button = nullptr;
        CPP_ButtonPressedEvent* Y_Button = nullptr;
        CPP_ButtonPressedEvent* Left_Bumper_Button = nullptr;
        CPP_ButtonPressedEvent* Right_Bumper_Button = nullptr;
        CPP_ButtonPressedEvent* Back_Button = nullptr;
        CPP_ButtonPressedEvent* Start_Button = nullptr;
        CPP_ButtonPressedEvent* Guide_Button = nullptr;
        CPP_ButtonPressedEvent* Left_Thumb_Button = nullptr;
        CPP_ButtonPressedEvent* Right_Thumb_Button = nullptr;
        CPP_ButtonPressedEvent* DPad_Up_Button = nullptr;
        CPP_ButtonPressedEvent* DPad_Down_Button = nullptr;
        CPP_ButtonPressedEvent* DPad_Left_Button = nullptr;
        CPP_ButtonPressedEvent* DPad_Right_Button = nullptr;

        float Get_Right_Stick_X_Axis_Percentage(float DeadZone);
        float Get_Right_Stick_Y_Axis_Percentage(float DeadZone);

        float Get_Right_Stick_X_Axis_Decimal(float DeadZone);
        float Get_Right_Stick_Y_Axis_Decimal(float DeadZone);

        float Get_Left_Stick_X_Axis_Percentage(float DeadZone);
        float Get_Left_Stick_Y_Axis_Percentage(float DeadZone);

        float Get_Left_Stick_X_Axis_Decimal(float DeadZone);
        float Get_Left_Stick_Y_Axis_Decimal(float DeadZone);

        float Get_Right_Trigger_Axis_Percentage(float DeadZone);
        float Get_Left_Trigger_Axis_Percentage(float DeadZone);

        float Get_Right_Trigger_Axis_Decimal(float DeadZone);
        float Get_Left_Trigger_Axis_Decimal(float DeadZone);

        void Get_Left_Stick_Position_Percentage(float DeadZone, float* out);
        void Get_Right_Stick_Position_Percentage(float DeadZone, float* out);

        void Get_Left_Stick_Position_Decimal(float DeadZone, float* out);
        void Get_Right_Stick_Position_Decimal(float DeadZone, float* out);
};

class EXPORT CPP_InternalControllerEvent {
    public:
        CPP_ButtonPressedEvent* GamePad_A_Button = nullptr;
        CPP_ButtonPressedEvent* GamePad_B_Button = nullptr;
        CPP_ButtonPressedEvent* GamePad_X_Button = nullptr;
        CPP_ButtonPressedEvent* GamePad_Y_Button = nullptr;
        CPP_ButtonPressedEvent* GamePad_Left_Bumper_Button = nullptr;
        CPP_ButtonPressedEvent* GamePad_Right_Bumper_Button = nullptr;
        CPP_ButtonPressedEvent* GamePad_Back_Button = nullptr;
        CPP_ButtonPressedEvent* GamePad_Start_Button = nullptr;
        CPP_ButtonPressedEvent* GamePad_Guide_Button = nullptr;
        CPP_ButtonPressedEvent* GamePad_Left_Thumb_Button = nullptr;
        CPP_ButtonPressedEvent* GamePad_Right_Thumb_Button = nullptr;
        CPP_ButtonPressedEvent* GamePad_DPad_Up_Button = nullptr;
        CPP_ButtonPressedEvent* GamePad_DPad_Right_Button = nullptr;
        CPP_ButtonPressedEvent* GamePad_DPad_Down_Button = nullptr;
        CPP_ButtonPressedEvent* GamePad_DPad_Left_Button = nullptr;

    private:
        CPP_BasicProportionConverter* GamePad_Left_Trigger = nullptr;
        CPP_BasicProportionConverter* GamePad_Right_Trigger = nullptr;
        CPP_BasicProportionConverter* GamePad_Left_Stick_X = nullptr;
        CPP_BasicProportionConverter* GamePad_Left_Stick_Y = nullptr;
        CPP_BasicProportionConverter* GamePad_Right_Stick_X = nullptr;
        CPP_BasicProportionConverter* GamePad_Right_Stick_Y = nullptr;

        std::vector<CPP_BasicProportionConverter> RawAxesData;
        std::vector<bool> RawButtonData;
        std::vector<std::string> RawHatStateData;
        std::string RawName;
        std::string GamePadName;
        std::string GUID;

        unsigned int ID;
        int RawAxisCount;
        int RawButtonCount;
        int RawHatCount;
        bool Connected;
        bool IsGamePad;
        bool UpdateRawData;

    public:
        CPP_InternalControllerEvent(unsigned int new_ID) {
            GamePad_A_Button = new CPP_ButtonPressedEvent();
            GamePad_B_Button = new CPP_ButtonPressedEvent();
            GamePad_X_Button = new CPP_ButtonPressedEvent();
            GamePad_Y_Button = new CPP_ButtonPressedEvent();
            GamePad_Left_Bumper_Button = new CPP_ButtonPressedEvent();
            GamePad_Right_Bumper_Button = new CPP_ButtonPressedEvent();
            GamePad_Back_Button = new CPP_ButtonPressedEvent();
            GamePad_Start_Button = new CPP_ButtonPressedEvent();
            GamePad_Guide_Button = new CPP_ButtonPressedEvent();
            GamePad_Left_Thumb_Button = new CPP_ButtonPressedEvent();
            GamePad_Right_Thumb_Button = new CPP_ButtonPressedEvent();
            GamePad_DPad_Up_Button = new CPP_ButtonPressedEvent();
            GamePad_DPad_Right_Button = new CPP_ButtonPressedEvent();
            GamePad_DPad_Down_Button = new CPP_ButtonPressedEvent();
            GamePad_DPad_Left_Button = new CPP_ButtonPressedEvent();

            GamePad_Left_Trigger = new CPP_BasicProportionConverter();
            GamePad_Right_Trigger = new CPP_BasicProportionConverter();
            GamePad_Left_Stick_X = new CPP_BasicProportionConverter();
            GamePad_Left_Stick_Y = new CPP_BasicProportionConverter();
            GamePad_Right_Stick_X = new CPP_BasicProportionConverter();
            GamePad_Right_Stick_Y = new CPP_BasicProportionConverter();

            ID = new_ID;
            Connected = false;
            IsGamePad = false;
            UpdateRawData = false;
            GamePadName = "";
            RawName = "";
            GUID = "";
        };

        ~CPP_InternalControllerEvent() {
            delete GamePad_A_Button;
            delete GamePad_B_Button;
            delete GamePad_X_Button;
            delete GamePad_Y_Button;
            delete GamePad_Left_Bumper_Button;
            delete GamePad_Right_Bumper_Button;
            delete GamePad_Back_Button;
            delete GamePad_Start_Button;
            delete GamePad_Guide_Button;
            delete GamePad_Left_Thumb_Button;
            delete GamePad_Right_Thumb_Button;
            delete GamePad_DPad_Up_Button;
            delete GamePad_DPad_Right_Button;
            delete GamePad_DPad_Down_Button;
            delete GamePad_DPad_Left_Button;

            delete GamePad_Left_Trigger;
            delete GamePad_Right_Trigger;
            delete GamePad_Left_Stick_X;
            delete GamePad_Left_Stick_Y;
            delete GamePad_Right_Stick_X;
            delete GamePad_Right_Stick_Y;

            GamePad_A_Button = nullptr;
            GamePad_B_Button = nullptr;
            GamePad_X_Button = nullptr;
            GamePad_Y_Button = nullptr;
            GamePad_Left_Bumper_Button = nullptr;
            GamePad_Right_Bumper_Button = nullptr;
            GamePad_Back_Button = nullptr;
            GamePad_Start_Button = nullptr;
            GamePad_Guide_Button = nullptr;
            GamePad_Left_Thumb_Button = nullptr;
            GamePad_Right_Thumb_Button = nullptr;
            GamePad_DPad_Up_Button = nullptr;
            GamePad_DPad_Right_Button = nullptr;
            GamePad_DPad_Down_Button = nullptr;
            GamePad_DPad_Left_Button = nullptr;

            GamePad_Left_Trigger = nullptr;
            GamePad_Right_Trigger = nullptr;
            GamePad_Left_Stick_X = nullptr;
            GamePad_Left_Stick_Y = nullptr;
            GamePad_Right_Stick_X = nullptr;
            GamePad_Right_Stick_Y = nullptr;

            RawAxesData.clear();
            RawButtonData.clear();
            RawHatStateData.clear();
        }

        inline void UpdateConnection(bool new_Connected) {
            if (new_Connected) {
                RawName = glfwGetJoystickName(ID);
                GUID = glfwGetJoystickGUID(ID);

                IsGamePad = glfwJoystickIsGamepad(ID);

                if (IsGamePad) {
                    GamePadName = glfwGetGamepadName(ID);
                }

                glfwGetJoystickAxes(ID, &RawAxisCount);
                for (int i = 0; i < RawAxisCount; i++) {
                    RawAxesData.emplace_back();
                }

                glfwGetJoystickButtons(ID, &RawButtonCount);
                for (int i = 0; i < RawButtonCount; i++) {
                    RawButtonData.push_back(false);
                }

                glfwGetJoystickHats(ID, &RawHatCount);
                for (int i = 0; i < RawHatCount; i++) {
                    RawHatStateData.push_back(CPP_Constants::HAT_NOT_PRESSED);
                }

                Update();

            } else {
                RawName = "";
                GUID = "";
                GamePadName = "";
                RawAxesData.clear();
                RawButtonData.clear();
                RawHatStateData.clear();
            }
            Connected = new_Connected;
        };

        inline void Update() {
            if (UpdateRawData) {
                const float* axes = glfwGetJoystickAxes(ID, &RawAxisCount);
                for (int i = 0; i < RawAxisCount; i++) {
                    RawAxesData[i].SetProportion_Decimal(axes[i]);
                }

                const unsigned char* buttons = glfwGetJoystickButtons(ID, &RawButtonCount);
                for (int i = 0; i < RawButtonCount; i++) {
                    RawButtonData[i] = (buttons[i] == GLFW_PRESS);
                }

                const unsigned char* hats = glfwGetJoystickHats(ID, &RawHatCount);
                for (int i = 0; i < RawHatCount; i++) {
                    switch (hats[i]) {
                        case GLFW_HAT_CENTERED:
                            RawHatStateData[i] = (CPP_Constants::HAT_NOT_PRESSED);
                            break;
                        case GLFW_HAT_UP:
                            RawHatStateData[i] = (CPP_Constants::HAT_PRESSED_UP);
                            break;
                        case GLFW_HAT_RIGHT:
                            RawHatStateData[i] = (CPP_Constants::HAT_PRESSED_RIGHT);
                            break;
                        case GLFW_HAT_DOWN:
                            RawHatStateData[i] = (CPP_Constants::HAT_PRESSED_DOWN);
                            break;
                        case GLFW_HAT_LEFT:
                            RawHatStateData[i] = (CPP_Constants::HAT_PRESSED_LEFT);
                            break;
                        case GLFW_HAT_RIGHT | GLFW_HAT_UP:
                            RawHatStateData[i] = (CPP_Constants::HAT_PRESSED_UP_RIGHT);
                            break;
                        case GLFW_HAT_RIGHT | GLFW_HAT_DOWN:
                            RawHatStateData[i] = (CPP_Constants::HAT_PRESSED_DOWN_RIGHT);
                            break;
                        case GLFW_HAT_LEFT | GLFW_HAT_DOWN:
                            RawHatStateData[i] = (CPP_Constants::HAT_PRESSED_DOWN_LEFT);
                            break;
                        case GLFW_HAT_LEFT | GLFW_HAT_UP:
                            RawHatStateData[i] = (CPP_Constants::HAT_PRESSED_UP_LEFT);
                            break;
                        default:
                            RawHatStateData[i] = (CPP_Constants::HAT_NOT_PRESSED);
                    };
                }
            }

            if (IsGamePad) {
                GLFWgamepadstate state;

                if (glfwGetGamepadState(ID, &state)) {
                    GamePad_A_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_A] == GLFW_PRESS);
                    GamePad_B_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_B] == GLFW_PRESS);
                    GamePad_X_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_X] == GLFW_PRESS);
                    GamePad_Y_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_Y] == GLFW_PRESS);
                    GamePad_Left_Bumper_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_LEFT_BUMPER] == GLFW_PRESS);
                    GamePad_Right_Bumper_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_RIGHT_BUMPER] == GLFW_PRESS);
                    GamePad_Back_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_BACK] == GLFW_PRESS);
                    GamePad_Start_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_START] == GLFW_PRESS);
                    GamePad_Guide_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_GUIDE] == GLFW_PRESS);
                    GamePad_Left_Thumb_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_LEFT_THUMB] == GLFW_PRESS);
                    GamePad_Right_Thumb_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_RIGHT_THUMB] == GLFW_PRESS);
                    GamePad_DPad_Up_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_DPAD_UP] == GLFW_PRESS);
                    GamePad_DPad_Right_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_DPAD_RIGHT] == GLFW_PRESS);
                    GamePad_DPad_Down_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_DPAD_DOWN] == GLFW_PRESS);
                    GamePad_DPad_Left_Button->Update(state.buttons[GLFW_GAMEPAD_BUTTON_DPAD_LEFT] == GLFW_PRESS);

                    GamePad_Left_Trigger->SetProportion_Decimal(state.axes[GLFW_GAMEPAD_AXIS_LEFT_TRIGGER]);
                    GamePad_Right_Trigger->SetProportion_Decimal(state.axes[GLFW_GAMEPAD_AXIS_RIGHT_TRIGGER]);
                    GamePad_Left_Stick_X->SetProportion_Decimal(state.axes[GLFW_GAMEPAD_AXIS_LEFT_X]);
                    GamePad_Left_Stick_Y->SetProportion_Decimal(state.axes[GLFW_GAMEPAD_AXIS_LEFT_Y]);
                    GamePad_Right_Stick_X->SetProportion_Decimal(state.axes[GLFW_GAMEPAD_AXIS_RIGHT_X]);
                    GamePad_Right_Stick_Y->SetProportion_Decimal(state.axes[GLFW_GAMEPAD_AXIS_RIGHT_Y]);
                }
            }
        };

        inline std::string GetRawName() {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return RawName;
        };

        inline std::string GetGamePadName() {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return GamePadName;
        };

        inline std::string GetGUID() {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return GUID;
        };

        inline bool GetConnected() {
            return Connected;
        };

        inline int GetRawAxisCount() {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return RawAxisCount;
        };

        inline int GetRawButtonCount() {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return RawButtonCount;
        };

        inline int GetRawHatCount() {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return RawHatCount;
        };

        inline float GetRawAxis_Decimal(int AxisID) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            //std::cout << "Using raw controller data - we always recommend using 'non-raw' data for better performance." << std::endl;
            UpdateRawData = true;
            return RawAxesData[AxisID].GetProportion_Decimal();
        };

        inline float GetRawAxis_Percentage(int AxisID) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            //std::cout << "Using raw controller data - we always recommend using 'non-raw' data for better performance." << std::endl;
            UpdateRawData = true;
            return RawAxesData[AxisID].GetProportion_Percentage();
        };

        inline bool GetRawButtonPressed(int ButtonID) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            //std::cout << "Using raw controller data - we always recommend using 'non-raw' data for better performance." << std::endl;
            UpdateRawData = true;
            return RawButtonData[ButtonID];
        };

        inline std::string GetRawHatState(int HatID) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            //std::cout << "Using raw controller data - we always recommend using 'non-raw' data for better performance." << std::endl;
            UpdateRawData = true;
            return RawHatStateData[HatID];
        };

        inline float AxisDeadZoneConverter_Percentage(float DeadZone, float value) { // DeadZone as percentage, value as percentage
            if (abs(value) <= DeadZone) {
                return 0.0f;
            }

            if (value >= 0) {
                return std::max(0.0f, ((value - DeadZone) / (100 - DeadZone)) * 100);
            }
            return std::min(0.0f, ((value - DeadZone) / (100 + DeadZone)) * 100);
        }

        inline float AxisDeadZoneConverter_Decimal(float DeadZone, float value) { // DeadZone as percentage
            return AxisDeadZoneConverter_Percentage(DeadZone, value * 100) / 100;
        }

        inline float Get_Left_Trigger_Axis_Percentage(float DeadZone) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Left_Trigger->GetProportion_Percentage());
        }

        inline float Get_Right_Trigger_Axis_Percentage(float DeadZone) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Right_Trigger->GetProportion_Percentage());
        }

        inline float Get_Left_Trigger_Axis_Decimal(float DeadZone) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Left_Trigger->GetProportion_Decimal());
        }

        inline float Get_Right_Trigger_Axis_Decimal(float DeadZone) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Right_Trigger->GetProportion_Decimal());
        }

        inline float Get_Right_Stick_X_Axis_Percentage(float DeadZone) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Right_Stick_X->GetProportion_Percentage());
        }

        inline float Get_Right_Stick_Y_Axis_Percentage(float DeadZone) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Right_Stick_Y->GetProportion_Percentage());
        }

        inline float Get_Right_Stick_X_Axis_Decimal(float DeadZone) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Right_Stick_X->GetProportion_Decimal());
        }

        inline float Get_Right_Stick_Y_Axis_Decimal(float DeadZone) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Right_Stick_Y->GetProportion_Decimal());
        }


        inline float Get_Left_Stick_X_Axis_Percentage(float DeadZone) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Left_Stick_X->GetProportion_Percentage());
        }

        inline float Get_Left_Stick_Y_Axis_Percentage(float DeadZone) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Left_Stick_Y->GetProportion_Percentage());
        }

        inline float Get_Left_Stick_X_Axis_Decimal(float DeadZone) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Left_Stick_X->GetProportion_Decimal());
        }

        inline float Get_Left_Stick_Y_Axis_Decimal(float DeadZone) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Left_Stick_Y->GetProportion_Decimal());
        }

        inline void Get_Left_Stick_Position_Decimal(float DeadZone, float* out) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            out[0] = AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Left_Stick_X->GetProportion_Decimal());
            out[1] = AxisDeadZoneConverter_Decimal(DeadZone, GamePad_Left_Stick_Y->GetProportion_Decimal());
        }

        inline void Get_Right_Stick_Position_Decimal(float DeadZone, float* out) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            out[0] = GamePad_Right_Stick_X->GetProportion_Decimal();
            out[1] = GamePad_Right_Stick_Y->GetProportion_Decimal();
        }

        inline void Get_Left_Stick_Position_Percentage(float DeadZone, float* out) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            out[0] = AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Left_Stick_X->GetProportion_Percentage());
            out[1] = AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Left_Stick_Y->GetProportion_Percentage());
        }

        inline void Get_Right_Stick_Position_Percentage(float DeadZone, float* out) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            out[0] = AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Right_Stick_X->GetProportion_Percentage());
            out[1] = AxisDeadZoneConverter_Percentage(DeadZone, GamePad_Right_Stick_Y->GetProportion_Percentage());
        }
};