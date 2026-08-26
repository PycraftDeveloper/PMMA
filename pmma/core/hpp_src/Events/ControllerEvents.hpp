#pragma once
#include "Internal/Core/PMMA_Exports.hpp"

#include <algorithm>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

#include <GLFW/glfw3.h>

namespace PMMA::Internal::Events {
	class ButtonPressed;
}

namespace PMMA::Events {
	class EXPORT Controller {
	public:
		PMMA::Internal::Events::ButtonPressed* A_Button = nullptr;
		PMMA::Internal::Events::ButtonPressed* B_Button = nullptr;
		PMMA::Internal::Events::ButtonPressed* X_Button = nullptr;
		PMMA::Internal::Events::ButtonPressed* Y_Button = nullptr;
		PMMA::Internal::Events::ButtonPressed* Left_Bumper_Button = nullptr;
		PMMA::Internal::Events::ButtonPressed* Right_Bumper_Button = nullptr;
		PMMA::Internal::Events::ButtonPressed* Back_Button = nullptr;
		PMMA::Internal::Events::ButtonPressed* Start_Button = nullptr;
		PMMA::Internal::Events::ButtonPressed* Guide_Button = nullptr;
		PMMA::Internal::Events::ButtonPressed* Left_Thumb_Button = nullptr;
		PMMA::Internal::Events::ButtonPressed* Right_Thumb_Button = nullptr;
		PMMA::Internal::Events::ButtonPressed* DPad_Up_Button = nullptr;
		PMMA::Internal::Events::ButtonPressed* DPad_Down_Button = nullptr;
		PMMA::Internal::Events::ButtonPressed* DPad_Left_Button = nullptr;
		PMMA::Internal::Events::ButtonPressed* DPad_Right_Button = nullptr;

	private:
		unsigned int ID;

	public:
		Controller(unsigned int new_ID);
		~Controller();

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
} // namespace PMMA::Events