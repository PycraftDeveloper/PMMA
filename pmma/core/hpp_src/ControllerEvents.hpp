#pragma once
#include "PMMA_Exports.hpp"

#include <stdexcept>
#include <vector>

#include <GLFW/glfw3.h>

#include "NumberConverter.hpp"

class EXPORT CPP_ControllerEvent {
    private:
        unsigned int ID;
    public:
        CPP_ControllerEvent(unsigned int new_ID);

        ~CPP_ControllerEvent();

        bool GetConnected();

        float GetAxis_Decimal(int AxisID);

        float GetAxis_Percentage(int AxisID);

        bool GetActive();
};

class EXPORT CPP_InternalControllerEvent {
    private:
        std::string Name;
        std::string GUID;
        std::vector<CPP_BasicProportionConverter> AxesData;
        unsigned int ID;
        int AxisCount;
        bool Connected;

    public:
        CPP_InternalControllerEvent(unsigned int new_ID) {
            ID = new_ID;
            Connected = false;
            Name = "";
            GUID = "";
        };

        inline void UpdateConnection(bool new_Connected) {
            if (new_Connected) {
                Name = glfwGetJoystickName(ID);
                GUID = glfwGetJoystickGUID(ID);

                glfwGetJoystickAxes(ID, &AxisCount);
                for (int i = 0; i < AxisCount; i++) {
                    AxesData.emplace_back();
                }

                Update();
            } else {
                Name = "";
                GUID = "";
                AxesData.clear();
            }
            Connected = new_Connected;
        };

        inline void Update() {
            const float* axes = glfwGetJoystickAxes(ID, &AxisCount);
            for (int i = 0; i < AxisCount; i++) {
                AxesData[i].SetProportion_Decimal(axes[i]);
            }
        };

        inline bool GetConnected() {
            return Connected;
        };

        inline float GetAxis_Decimal(int AxisID) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return AxesData[AxisID].GetProportion_Decimal();
        };

        inline float GetAxis_Percentage(int AxisID) {
            if (!Connected) {
                throw std::runtime_error("Controller is not connected");
            }
            return AxesData[AxisID].GetProportion_Percentage();
        };
};