#pragma once
#include "PMMA_Exports.hpp"

#include <stdexcept>

#include "PMMA_Core.hpp"

class EXPORT CPP_Space_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Space_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Space_Instance is null");
            }
            return PMMA::KeyEvent_Space_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Space_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Space_Instance is null");
            }
            PMMA::KeyEvent_Space_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Space_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Space_Instance is null");
            }
            return PMMA::KeyEvent_Space_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Space_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Space_Instance is null");
            }
            return PMMA::KeyEvent_Space_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Space_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Space_Instance is null");
            }
            PMMA::KeyEvent_Space_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Space_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Space_Instance is null");
            }
            return PMMA::KeyEvent_Space_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Space_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Space_Instance is null");
            }
            return PMMA::KeyEvent_Space_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Apostrophe_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Apostrophe_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Apostrophe_Instance is null");
            }
            return PMMA::KeyEvent_Apostrophe_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Apostrophe_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Apostrophe_Instance is null");
            }
            PMMA::KeyEvent_Apostrophe_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Apostrophe_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Apostrophe_Instance is null");
            }
            return PMMA::KeyEvent_Apostrophe_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Apostrophe_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Apostrophe_Instance is null");
            }
            return PMMA::KeyEvent_Apostrophe_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Apostrophe_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Apostrophe_Instance is null");
            }
            PMMA::KeyEvent_Apostrophe_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Apostrophe_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Apostrophe_Instance is null");
            }
            return PMMA::KeyEvent_Apostrophe_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Apostrophe_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Apostrophe_Instance is null");
            }
            return PMMA::KeyEvent_Apostrophe_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Comma_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Comma_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Comma_Instance is null");
            }
            return PMMA::KeyEvent_Comma_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Comma_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Comma_Instance is null");
            }
            PMMA::KeyEvent_Comma_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Comma_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Comma_Instance is null");
            }
            return PMMA::KeyEvent_Comma_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Comma_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Comma_Instance is null");
            }
            return PMMA::KeyEvent_Comma_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Comma_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Comma_Instance is null");
            }
            PMMA::KeyEvent_Comma_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Comma_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Comma_Instance is null");
            }
            return PMMA::KeyEvent_Comma_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Comma_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Comma_Instance is null");
            }
            return PMMA::KeyEvent_Comma_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Minus_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Minus_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Minus_Instance is null");
            }
            return PMMA::KeyEvent_Minus_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Minus_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Minus_Instance is null");
            }
            PMMA::KeyEvent_Minus_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Minus_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Minus_Instance is null");
            }
            return PMMA::KeyEvent_Minus_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Minus_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Minus_Instance is null");
            }
            return PMMA::KeyEvent_Minus_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Minus_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Minus_Instance is null");
            }
            PMMA::KeyEvent_Minus_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Minus_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Minus_Instance is null");
            }
            return PMMA::KeyEvent_Minus_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Minus_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Minus_Instance is null");
            }
            return PMMA::KeyEvent_Minus_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Period_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Period_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Period_Instance is null");
            }
            return PMMA::KeyEvent_Period_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Period_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Period_Instance is null");
            }
            PMMA::KeyEvent_Period_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Period_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Period_Instance is null");
            }
            return PMMA::KeyEvent_Period_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Period_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Period_Instance is null");
            }
            return PMMA::KeyEvent_Period_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Period_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Period_Instance is null");
            }
            PMMA::KeyEvent_Period_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Period_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Period_Instance is null");
            }
            return PMMA::KeyEvent_Period_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Period_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Period_Instance is null");
            }
            return PMMA::KeyEvent_Period_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Slash_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Slash_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Slash_Instance is null");
            }
            return PMMA::KeyEvent_Slash_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Slash_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Slash_Instance is null");
            }
            PMMA::KeyEvent_Slash_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Slash_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Slash_Instance is null");
            }
            return PMMA::KeyEvent_Slash_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Slash_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Slash_Instance is null");
            }
            return PMMA::KeyEvent_Slash_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Slash_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Slash_Instance is null");
            }
            PMMA::KeyEvent_Slash_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Slash_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Slash_Instance is null");
            }
            return PMMA::KeyEvent_Slash_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Slash_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Slash_Instance is null");
            }
            return PMMA::KeyEvent_Slash_Instance->PollLongPressed();
        };
};

class EXPORT CPP_0_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_0_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_0_Instance is null");
            }
            return PMMA::KeyEvent_0_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_0_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_0_Instance is null");
            }
            PMMA::KeyEvent_0_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_0_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_0_Instance is null");
            }
            return PMMA::KeyEvent_0_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_0_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_0_Instance is null");
            }
            return PMMA::KeyEvent_0_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_0_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_0_Instance is null");
            }
            PMMA::KeyEvent_0_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_0_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_0_Instance is null");
            }
            return PMMA::KeyEvent_0_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_0_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_0_Instance is null");
            }
            return PMMA::KeyEvent_0_Instance->PollLongPressed();
        };
};

class EXPORT CPP_1_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_1_Instance is null");
            }
            return PMMA::KeyEvent_1_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_1_Instance is null");
            }
            PMMA::KeyEvent_1_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_1_Instance is null");
            }
            return PMMA::KeyEvent_1_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_1_Instance is null");
            }
            return PMMA::KeyEvent_1_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_1_Instance is null");
            }
            PMMA::KeyEvent_1_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_1_Instance is null");
            }
            return PMMA::KeyEvent_1_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_1_Instance is null");
            }
            return PMMA::KeyEvent_1_Instance->PollLongPressed();
        };
};

class EXPORT CPP_2_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_2_Instance is null");
            }
            return PMMA::KeyEvent_2_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_2_Instance is null");
            }
            PMMA::KeyEvent_2_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_2_Instance is null");
            }
            return PMMA::KeyEvent_2_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_2_Instance is null");
            }
            return PMMA::KeyEvent_2_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_2_Instance is null");
            }
            PMMA::KeyEvent_2_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_2_Instance is null");
            }
            return PMMA::KeyEvent_2_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_2_Instance is null");
            }
            return PMMA::KeyEvent_2_Instance->PollLongPressed();
        };
};

class EXPORT CPP_3_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_3_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_3_Instance is null");
            }
            return PMMA::KeyEvent_3_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_3_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_3_Instance is null");
            }
            PMMA::KeyEvent_3_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_3_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_3_Instance is null");
            }
            return PMMA::KeyEvent_3_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_3_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_3_Instance is null");
            }
            return PMMA::KeyEvent_3_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_3_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_3_Instance is null");
            }
            PMMA::KeyEvent_3_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_3_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_3_Instance is null");
            }
            return PMMA::KeyEvent_3_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_3_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_3_Instance is null");
            }
            return PMMA::KeyEvent_3_Instance->PollLongPressed();
        };
};

class EXPORT CPP_4_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_4_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_4_Instance is null");
            }
            return PMMA::KeyEvent_4_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_4_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_4_Instance is null");
            }
            PMMA::KeyEvent_4_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_4_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_4_Instance is null");
            }
            return PMMA::KeyEvent_4_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_4_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_4_Instance is null");
            }
            return PMMA::KeyEvent_4_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_4_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_4_Instance is null");
            }
            PMMA::KeyEvent_4_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_4_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_4_Instance is null");
            }
            return PMMA::KeyEvent_4_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_4_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_4_Instance is null");
            }
            return PMMA::KeyEvent_4_Instance->PollLongPressed();
        };
};

class EXPORT CPP_5_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_5_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_5_Instance is null");
            }
            return PMMA::KeyEvent_5_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_5_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_5_Instance is null");
            }
            PMMA::KeyEvent_5_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_5_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_5_Instance is null");
            }
            return PMMA::KeyEvent_5_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_5_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_5_Instance is null");
            }
            return PMMA::KeyEvent_5_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_5_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_5_Instance is null");
            }
            PMMA::KeyEvent_5_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_5_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_5_Instance is null");
            }
            return PMMA::KeyEvent_5_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_5_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_5_Instance is null");
            }
            return PMMA::KeyEvent_5_Instance->PollLongPressed();
        };
};

class EXPORT CPP_6_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_6_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_6_Instance is null");
            }
            return PMMA::KeyEvent_6_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_6_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_6_Instance is null");
            }
            PMMA::KeyEvent_6_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_6_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_6_Instance is null");
            }
            return PMMA::KeyEvent_6_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_6_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_6_Instance is null");
            }
            return PMMA::KeyEvent_6_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_6_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_6_Instance is null");
            }
            PMMA::KeyEvent_6_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_6_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_6_Instance is null");
            }
            return PMMA::KeyEvent_6_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_6_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_6_Instance is null");
            }
            return PMMA::KeyEvent_6_Instance->PollLongPressed();
        };
};

class EXPORT CPP_7_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_7_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_7_Instance is null");
            }
            return PMMA::KeyEvent_7_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_7_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_7_Instance is null");
            }
            PMMA::KeyEvent_7_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_7_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_7_Instance is null");
            }
            return PMMA::KeyEvent_7_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_7_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_7_Instance is null");
            }
            return PMMA::KeyEvent_7_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_7_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_7_Instance is null");
            }
            PMMA::KeyEvent_7_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_7_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_7_Instance is null");
            }
            return PMMA::KeyEvent_7_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_7_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_7_Instance is null");
            }
            return PMMA::KeyEvent_7_Instance->PollLongPressed();
        };
};

class EXPORT CPP_8_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_8_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_8_Instance is null");
            }
            return PMMA::KeyEvent_8_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_8_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_8_Instance is null");
            }
            PMMA::KeyEvent_8_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_8_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_8_Instance is null");
            }
            return PMMA::KeyEvent_8_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_8_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_8_Instance is null");
            }
            return PMMA::KeyEvent_8_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_8_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_8_Instance is null");
            }
            PMMA::KeyEvent_8_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_8_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_8_Instance is null");
            }
            return PMMA::KeyEvent_8_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_8_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_8_Instance is null");
            }
            return PMMA::KeyEvent_8_Instance->PollLongPressed();
        };
};

class EXPORT CPP_9_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_9_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_9_Instance is null");
            }
            return PMMA::KeyEvent_9_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_9_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_9_Instance is null");
            }
            PMMA::KeyEvent_9_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_9_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_9_Instance is null");
            }
            return PMMA::KeyEvent_9_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_9_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_9_Instance is null");
            }
            return PMMA::KeyEvent_9_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_9_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_9_Instance is null");
            }
            PMMA::KeyEvent_9_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_9_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_9_Instance is null");
            }
            return PMMA::KeyEvent_9_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_9_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_9_Instance is null");
            }
            return PMMA::KeyEvent_9_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Semicolon_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Semicolon_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Semicolon_Instance is null");
            }
            return PMMA::KeyEvent_Semicolon_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Semicolon_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Semicolon_Instance is null");
            }
            PMMA::KeyEvent_Semicolon_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Semicolon_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Semicolon_Instance is null");
            }
            return PMMA::KeyEvent_Semicolon_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Semicolon_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Semicolon_Instance is null");
            }
            return PMMA::KeyEvent_Semicolon_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Semicolon_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Semicolon_Instance is null");
            }
            PMMA::KeyEvent_Semicolon_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Semicolon_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Semicolon_Instance is null");
            }
            return PMMA::KeyEvent_Semicolon_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Semicolon_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Semicolon_Instance is null");
            }
            return PMMA::KeyEvent_Semicolon_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Equal_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Equal_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Equal_Instance is null");
            }
            return PMMA::KeyEvent_Equal_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Equal_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Equal_Instance is null");
            }
            PMMA::KeyEvent_Equal_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Equal_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Equal_Instance is null");
            }
            return PMMA::KeyEvent_Equal_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Equal_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Equal_Instance is null");
            }
            return PMMA::KeyEvent_Equal_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Equal_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Equal_Instance is null");
            }
            PMMA::KeyEvent_Equal_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Equal_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Equal_Instance is null");
            }
            return PMMA::KeyEvent_Equal_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Equal_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Equal_Instance is null");
            }
            return PMMA::KeyEvent_Equal_Instance->PollLongPressed();
        };
};

class EXPORT CPP_A_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_A_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_A_Instance is null");
            }
            return PMMA::KeyEvent_A_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_A_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_A_Instance is null");
            }
            PMMA::KeyEvent_A_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_A_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_A_Instance is null");
            }
            return PMMA::KeyEvent_A_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_A_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_A_Instance is null");
            }
            return PMMA::KeyEvent_A_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_A_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_A_Instance is null");
            }
            PMMA::KeyEvent_A_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_A_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_A_Instance is null");
            }
            return PMMA::KeyEvent_A_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_A_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_A_Instance is null");
            }
            return PMMA::KeyEvent_A_Instance->PollLongPressed();
        };
};

class EXPORT CPP_B_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_B_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_B_Instance is null");
            }
            return PMMA::KeyEvent_B_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_B_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_B_Instance is null");
            }
            PMMA::KeyEvent_B_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_B_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_B_Instance is null");
            }
            return PMMA::KeyEvent_B_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_B_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_B_Instance is null");
            }
            return PMMA::KeyEvent_B_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_B_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_B_Instance is null");
            }
            PMMA::KeyEvent_B_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_B_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_B_Instance is null");
            }
            return PMMA::KeyEvent_B_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_B_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_B_Instance is null");
            }
            return PMMA::KeyEvent_B_Instance->PollLongPressed();
        };
};

class EXPORT CPP_C_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_C_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_C_Instance is null");
            }
            return PMMA::KeyEvent_C_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_C_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_C_Instance is null");
            }
            PMMA::KeyEvent_C_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_C_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_C_Instance is null");
            }
            return PMMA::KeyEvent_C_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_C_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_C_Instance is null");
            }
            return PMMA::KeyEvent_C_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_C_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_C_Instance is null");
            }
            PMMA::KeyEvent_C_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_C_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_C_Instance is null");
            }
            return PMMA::KeyEvent_C_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_C_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_C_Instance is null");
            }
            return PMMA::KeyEvent_C_Instance->PollLongPressed();
        };
};

class EXPORT CPP_D_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_D_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_D_Instance is null");
            }
            return PMMA::KeyEvent_D_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_D_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_D_Instance is null");
            }
            PMMA::KeyEvent_D_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_D_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_D_Instance is null");
            }
            return PMMA::KeyEvent_D_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_D_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_D_Instance is null");
            }
            return PMMA::KeyEvent_D_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_D_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_D_Instance is null");
            }
            PMMA::KeyEvent_D_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_D_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_D_Instance is null");
            }
            return PMMA::KeyEvent_D_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_D_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_D_Instance is null");
            }
            return PMMA::KeyEvent_D_Instance->PollLongPressed();
        };
};

class EXPORT CPP_E_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_E_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_E_Instance is null");
            }
            return PMMA::KeyEvent_E_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_E_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_E_Instance is null");
            }
            PMMA::KeyEvent_E_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_E_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_E_Instance is null");
            }
            return PMMA::KeyEvent_E_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_E_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_E_Instance is null");
            }
            return PMMA::KeyEvent_E_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_E_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_E_Instance is null");
            }
            PMMA::KeyEvent_E_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_E_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_E_Instance is null");
            }
            return PMMA::KeyEvent_E_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_E_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_E_Instance is null");
            }
            return PMMA::KeyEvent_E_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F_Instance is null");
            }
            return PMMA::KeyEvent_F_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F_Instance is null");
            }
            PMMA::KeyEvent_F_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F_Instance is null");
            }
            return PMMA::KeyEvent_F_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F_Instance is null");
            }
            return PMMA::KeyEvent_F_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F_Instance is null");
            }
            PMMA::KeyEvent_F_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F_Instance is null");
            }
            return PMMA::KeyEvent_F_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F_Instance is null");
            }
            return PMMA::KeyEvent_F_Instance->PollLongPressed();
        };
};

class EXPORT CPP_G_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_G_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_G_Instance is null");
            }
            return PMMA::KeyEvent_G_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_G_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_G_Instance is null");
            }
            PMMA::KeyEvent_G_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_G_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_G_Instance is null");
            }
            return PMMA::KeyEvent_G_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_G_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_G_Instance is null");
            }
            return PMMA::KeyEvent_G_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_G_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_G_Instance is null");
            }
            PMMA::KeyEvent_G_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_G_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_G_Instance is null");
            }
            return PMMA::KeyEvent_G_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_G_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_G_Instance is null");
            }
            return PMMA::KeyEvent_G_Instance->PollLongPressed();
        };
};

class EXPORT CPP_H_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_H_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_H_Instance is null");
            }
            return PMMA::KeyEvent_H_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_H_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_H_Instance is null");
            }
            PMMA::KeyEvent_H_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_H_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_H_Instance is null");
            }
            return PMMA::KeyEvent_H_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_H_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_H_Instance is null");
            }
            return PMMA::KeyEvent_H_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_H_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_H_Instance is null");
            }
            PMMA::KeyEvent_H_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_H_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_H_Instance is null");
            }
            return PMMA::KeyEvent_H_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_H_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_H_Instance is null");
            }
            return PMMA::KeyEvent_H_Instance->PollLongPressed();
        };
};

class EXPORT CPP_I_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_I_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_I_Instance is null");
            }
            return PMMA::KeyEvent_I_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_I_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_I_Instance is null");
            }
            PMMA::KeyEvent_I_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_I_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_I_Instance is null");
            }
            return PMMA::KeyEvent_I_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_I_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_I_Instance is null");
            }
            return PMMA::KeyEvent_I_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_I_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_I_Instance is null");
            }
            PMMA::KeyEvent_I_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_I_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_I_Instance is null");
            }
            return PMMA::KeyEvent_I_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_I_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_I_Instance is null");
            }
            return PMMA::KeyEvent_I_Instance->PollLongPressed();
        };
};

class EXPORT CPP_J_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_J_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_J_Instance is null");
            }
            return PMMA::KeyEvent_J_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_J_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_J_Instance is null");
            }
            PMMA::KeyEvent_J_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_J_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_J_Instance is null");
            }
            return PMMA::KeyEvent_J_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_J_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_J_Instance is null");
            }
            return PMMA::KeyEvent_J_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_J_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_J_Instance is null");
            }
            PMMA::KeyEvent_J_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_J_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_J_Instance is null");
            }
            return PMMA::KeyEvent_J_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_J_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_J_Instance is null");
            }
            return PMMA::KeyEvent_J_Instance->PollLongPressed();
        };
};

class EXPORT CPP_K_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_K_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_K_Instance is null");
            }
            return PMMA::KeyEvent_K_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_K_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_K_Instance is null");
            }
            PMMA::KeyEvent_K_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_K_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_K_Instance is null");
            }
            return PMMA::KeyEvent_K_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_K_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_K_Instance is null");
            }
            return PMMA::KeyEvent_K_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_K_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_K_Instance is null");
            }
            PMMA::KeyEvent_K_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_K_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_K_Instance is null");
            }
            return PMMA::KeyEvent_K_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_K_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_K_Instance is null");
            }
            return PMMA::KeyEvent_K_Instance->PollLongPressed();
        };
};

class EXPORT CPP_L_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_L_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_L_Instance is null");
            }
            return PMMA::KeyEvent_L_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_L_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_L_Instance is null");
            }
            PMMA::KeyEvent_L_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_L_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_L_Instance is null");
            }
            return PMMA::KeyEvent_L_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_L_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_L_Instance is null");
            }
            return PMMA::KeyEvent_L_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_L_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_L_Instance is null");
            }
            PMMA::KeyEvent_L_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_L_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_L_Instance is null");
            }
            return PMMA::KeyEvent_L_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_L_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_L_Instance is null");
            }
            return PMMA::KeyEvent_L_Instance->PollLongPressed();
        };
};

class EXPORT CPP_M_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_M_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_M_Instance is null");
            }
            return PMMA::KeyEvent_M_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_M_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_M_Instance is null");
            }
            PMMA::KeyEvent_M_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_M_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_M_Instance is null");
            }
            return PMMA::KeyEvent_M_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_M_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_M_Instance is null");
            }
            return PMMA::KeyEvent_M_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_M_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_M_Instance is null");
            }
            PMMA::KeyEvent_M_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_M_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_M_Instance is null");
            }
            return PMMA::KeyEvent_M_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_M_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_M_Instance is null");
            }
            return PMMA::KeyEvent_M_Instance->PollLongPressed();
        };
};

class EXPORT CPP_N_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_N_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_N_Instance is null");
            }
            return PMMA::KeyEvent_N_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_N_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_N_Instance is null");
            }
            PMMA::KeyEvent_N_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_N_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_N_Instance is null");
            }
            return PMMA::KeyEvent_N_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_N_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_N_Instance is null");
            }
            return PMMA::KeyEvent_N_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_N_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_N_Instance is null");
            }
            PMMA::KeyEvent_N_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_N_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_N_Instance is null");
            }
            return PMMA::KeyEvent_N_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_N_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_N_Instance is null");
            }
            return PMMA::KeyEvent_N_Instance->PollLongPressed();
        };
};

class EXPORT CPP_O_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_O_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_O_Instance is null");
            }
            return PMMA::KeyEvent_O_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_O_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_O_Instance is null");
            }
            PMMA::KeyEvent_O_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_O_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_O_Instance is null");
            }
            return PMMA::KeyEvent_O_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_O_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_O_Instance is null");
            }
            return PMMA::KeyEvent_O_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_O_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_O_Instance is null");
            }
            PMMA::KeyEvent_O_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_O_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_O_Instance is null");
            }
            return PMMA::KeyEvent_O_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_O_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_O_Instance is null");
            }
            return PMMA::KeyEvent_O_Instance->PollLongPressed();
        };
};

class EXPORT CPP_P_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_P_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_P_Instance is null");
            }
            return PMMA::KeyEvent_P_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_P_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_P_Instance is null");
            }
            PMMA::KeyEvent_P_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_P_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_P_Instance is null");
            }
            return PMMA::KeyEvent_P_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_P_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_P_Instance is null");
            }
            return PMMA::KeyEvent_P_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_P_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_P_Instance is null");
            }
            PMMA::KeyEvent_P_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_P_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_P_Instance is null");
            }
            return PMMA::KeyEvent_P_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_P_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_P_Instance is null");
            }
            return PMMA::KeyEvent_P_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Q_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Q_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Q_Instance is null");
            }
            return PMMA::KeyEvent_Q_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Q_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Q_Instance is null");
            }
            PMMA::KeyEvent_Q_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Q_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Q_Instance is null");
            }
            return PMMA::KeyEvent_Q_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Q_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Q_Instance is null");
            }
            return PMMA::KeyEvent_Q_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Q_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Q_Instance is null");
            }
            PMMA::KeyEvent_Q_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Q_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Q_Instance is null");
            }
            return PMMA::KeyEvent_Q_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Q_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Q_Instance is null");
            }
            return PMMA::KeyEvent_Q_Instance->PollLongPressed();
        };
};

class EXPORT CPP_R_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_R_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_R_Instance is null");
            }
            return PMMA::KeyEvent_R_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_R_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_R_Instance is null");
            }
            PMMA::KeyEvent_R_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_R_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_R_Instance is null");
            }
            return PMMA::KeyEvent_R_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_R_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_R_Instance is null");
            }
            return PMMA::KeyEvent_R_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_R_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_R_Instance is null");
            }
            PMMA::KeyEvent_R_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_R_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_R_Instance is null");
            }
            return PMMA::KeyEvent_R_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_R_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_R_Instance is null");
            }
            return PMMA::KeyEvent_R_Instance->PollLongPressed();
        };
};

class EXPORT CPP_S_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_S_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_S_Instance is null");
            }
            return PMMA::KeyEvent_S_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_S_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_S_Instance is null");
            }
            PMMA::KeyEvent_S_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_S_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_S_Instance is null");
            }
            return PMMA::KeyEvent_S_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_S_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_S_Instance is null");
            }
            return PMMA::KeyEvent_S_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_S_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_S_Instance is null");
            }
            PMMA::KeyEvent_S_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_S_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_S_Instance is null");
            }
            return PMMA::KeyEvent_S_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_S_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_S_Instance is null");
            }
            return PMMA::KeyEvent_S_Instance->PollLongPressed();
        };
};

class EXPORT CPP_T_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_T_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_T_Instance is null");
            }
            return PMMA::KeyEvent_T_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_T_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_T_Instance is null");
            }
            PMMA::KeyEvent_T_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_T_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_T_Instance is null");
            }
            return PMMA::KeyEvent_T_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_T_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_T_Instance is null");
            }
            return PMMA::KeyEvent_T_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_T_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_T_Instance is null");
            }
            PMMA::KeyEvent_T_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_T_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_T_Instance is null");
            }
            return PMMA::KeyEvent_T_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_T_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_T_Instance is null");
            }
            return PMMA::KeyEvent_T_Instance->PollLongPressed();
        };
};

class EXPORT CPP_U_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_U_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_U_Instance is null");
            }
            return PMMA::KeyEvent_U_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_U_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_U_Instance is null");
            }
            PMMA::KeyEvent_U_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_U_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_U_Instance is null");
            }
            return PMMA::KeyEvent_U_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_U_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_U_Instance is null");
            }
            return PMMA::KeyEvent_U_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_U_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_U_Instance is null");
            }
            PMMA::KeyEvent_U_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_U_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_U_Instance is null");
            }
            return PMMA::KeyEvent_U_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_U_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_U_Instance is null");
            }
            return PMMA::KeyEvent_U_Instance->PollLongPressed();
        };
};

class EXPORT CPP_V_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_V_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_V_Instance is null");
            }
            return PMMA::KeyEvent_V_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_V_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_V_Instance is null");
            }
            PMMA::KeyEvent_V_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_V_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_V_Instance is null");
            }
            return PMMA::KeyEvent_V_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_V_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_V_Instance is null");
            }
            return PMMA::KeyEvent_V_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_V_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_V_Instance is null");
            }
            PMMA::KeyEvent_V_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_V_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_V_Instance is null");
            }
            return PMMA::KeyEvent_V_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_V_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_V_Instance is null");
            }
            return PMMA::KeyEvent_V_Instance->PollLongPressed();
        };
};

class EXPORT CPP_W_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_W_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_W_Instance is null");
            }
            return PMMA::KeyEvent_W_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_W_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_W_Instance is null");
            }
            PMMA::KeyEvent_W_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_W_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_W_Instance is null");
            }
            return PMMA::KeyEvent_W_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_W_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_W_Instance is null");
            }
            return PMMA::KeyEvent_W_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_W_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_W_Instance is null");
            }
            PMMA::KeyEvent_W_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_W_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_W_Instance is null");
            }
            return PMMA::KeyEvent_W_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_W_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_W_Instance is null");
            }
            return PMMA::KeyEvent_W_Instance->PollLongPressed();
        };
};

class EXPORT CPP_X_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_X_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_X_Instance is null");
            }
            return PMMA::KeyEvent_X_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_X_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_X_Instance is null");
            }
            PMMA::KeyEvent_X_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_X_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_X_Instance is null");
            }
            return PMMA::KeyEvent_X_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_X_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_X_Instance is null");
            }
            return PMMA::KeyEvent_X_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_X_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_X_Instance is null");
            }
            PMMA::KeyEvent_X_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_X_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_X_Instance is null");
            }
            return PMMA::KeyEvent_X_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_X_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_X_Instance is null");
            }
            return PMMA::KeyEvent_X_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Y_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Y_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Y_Instance is null");
            }
            return PMMA::KeyEvent_Y_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Y_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Y_Instance is null");
            }
            PMMA::KeyEvent_Y_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Y_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Y_Instance is null");
            }
            return PMMA::KeyEvent_Y_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Y_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Y_Instance is null");
            }
            return PMMA::KeyEvent_Y_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Y_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Y_Instance is null");
            }
            PMMA::KeyEvent_Y_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Y_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Y_Instance is null");
            }
            return PMMA::KeyEvent_Y_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Y_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Y_Instance is null");
            }
            return PMMA::KeyEvent_Y_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Z_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Z_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Z_Instance is null");
            }
            return PMMA::KeyEvent_Z_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Z_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Z_Instance is null");
            }
            PMMA::KeyEvent_Z_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Z_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Z_Instance is null");
            }
            return PMMA::KeyEvent_Z_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Z_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Z_Instance is null");
            }
            return PMMA::KeyEvent_Z_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Z_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Z_Instance is null");
            }
            PMMA::KeyEvent_Z_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Z_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Z_Instance is null");
            }
            return PMMA::KeyEvent_Z_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Z_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Z_Instance is null");
            }
            return PMMA::KeyEvent_Z_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Left_Bracket_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Left_Bracket_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Bracket_Instance is null");
            }
            return PMMA::KeyEvent_Left_Bracket_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Left_Bracket_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Bracket_Instance is null");
            }
            PMMA::KeyEvent_Left_Bracket_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Left_Bracket_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Bracket_Instance is null");
            }
            return PMMA::KeyEvent_Left_Bracket_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Left_Bracket_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Bracket_Instance is null");
            }
            return PMMA::KeyEvent_Left_Bracket_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Left_Bracket_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Bracket_Instance is null");
            }
            PMMA::KeyEvent_Left_Bracket_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Left_Bracket_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Bracket_Instance is null");
            }
            return PMMA::KeyEvent_Left_Bracket_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Left_Bracket_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Bracket_Instance is null");
            }
            return PMMA::KeyEvent_Left_Bracket_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Backslash_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Backslash_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Backslash_Instance is null");
            }
            return PMMA::KeyEvent_Backslash_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Backslash_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Backslash_Instance is null");
            }
            PMMA::KeyEvent_Backslash_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Backslash_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Backslash_Instance is null");
            }
            return PMMA::KeyEvent_Backslash_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Backslash_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Backslash_Instance is null");
            }
            return PMMA::KeyEvent_Backslash_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Backslash_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Backslash_Instance is null");
            }
            PMMA::KeyEvent_Backslash_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Backslash_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Backslash_Instance is null");
            }
            return PMMA::KeyEvent_Backslash_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Backslash_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Backslash_Instance is null");
            }
            return PMMA::KeyEvent_Backslash_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Right_Bracket_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Right_Bracket_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Bracket_Instance is null");
            }
            return PMMA::KeyEvent_Right_Bracket_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Right_Bracket_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Bracket_Instance is null");
            }
            PMMA::KeyEvent_Right_Bracket_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Right_Bracket_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Bracket_Instance is null");
            }
            return PMMA::KeyEvent_Right_Bracket_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Right_Bracket_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Bracket_Instance is null");
            }
            return PMMA::KeyEvent_Right_Bracket_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Right_Bracket_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Bracket_Instance is null");
            }
            PMMA::KeyEvent_Right_Bracket_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Right_Bracket_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Bracket_Instance is null");
            }
            return PMMA::KeyEvent_Right_Bracket_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Right_Bracket_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Bracket_Instance is null");
            }
            return PMMA::KeyEvent_Right_Bracket_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Grave_Accent_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Grave_Accent_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Grave_Accent_Instance is null");
            }
            return PMMA::KeyEvent_Grave_Accent_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Grave_Accent_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Grave_Accent_Instance is null");
            }
            PMMA::KeyEvent_Grave_Accent_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Grave_Accent_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Grave_Accent_Instance is null");
            }
            return PMMA::KeyEvent_Grave_Accent_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Grave_Accent_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Grave_Accent_Instance is null");
            }
            return PMMA::KeyEvent_Grave_Accent_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Grave_Accent_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Grave_Accent_Instance is null");
            }
            PMMA::KeyEvent_Grave_Accent_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Grave_Accent_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Grave_Accent_Instance is null");
            }
            return PMMA::KeyEvent_Grave_Accent_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Grave_Accent_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Grave_Accent_Instance is null");
            }
            return PMMA::KeyEvent_Grave_Accent_Instance->PollLongPressed();
        };
};

class EXPORT CPP_World_1_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_World_1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_World_1_Instance is null");
            }
            return PMMA::KeyEvent_World_1_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_World_1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_World_1_Instance is null");
            }
            PMMA::KeyEvent_World_1_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_World_1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_World_1_Instance is null");
            }
            return PMMA::KeyEvent_World_1_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_World_1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_World_1_Instance is null");
            }
            return PMMA::KeyEvent_World_1_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_World_1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_World_1_Instance is null");
            }
            PMMA::KeyEvent_World_1_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_World_1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_World_1_Instance is null");
            }
            return PMMA::KeyEvent_World_1_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_World_1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_World_1_Instance is null");
            }
            return PMMA::KeyEvent_World_1_Instance->PollLongPressed();
        };
};

class EXPORT CPP_World_2_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_World_2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_World_2_Instance is null");
            }
            return PMMA::KeyEvent_World_2_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_World_2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_World_2_Instance is null");
            }
            PMMA::KeyEvent_World_2_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_World_2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_World_2_Instance is null");
            }
            return PMMA::KeyEvent_World_2_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_World_2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_World_2_Instance is null");
            }
            return PMMA::KeyEvent_World_2_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_World_2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_World_2_Instance is null");
            }
            PMMA::KeyEvent_World_2_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_World_2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_World_2_Instance is null");
            }
            return PMMA::KeyEvent_World_2_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_World_2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_World_2_Instance is null");
            }
            return PMMA::KeyEvent_World_2_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Escape_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Escape_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Escape_Instance is null");
            }
            return PMMA::KeyEvent_Escape_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Escape_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Escape_Instance is null");
            }
            PMMA::KeyEvent_Escape_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Escape_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Escape_Instance is null");
            }
            return PMMA::KeyEvent_Escape_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Escape_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Escape_Instance is null");
            }
            return PMMA::KeyEvent_Escape_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Escape_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Escape_Instance is null");
            }
            PMMA::KeyEvent_Escape_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Escape_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Escape_Instance is null");
            }
            return PMMA::KeyEvent_Escape_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Escape_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Escape_Instance is null");
            }
            return PMMA::KeyEvent_Escape_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Enter_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Enter_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Enter_Instance is null");
            }
            return PMMA::KeyEvent_Enter_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Enter_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Enter_Instance is null");
            }
            PMMA::KeyEvent_Enter_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Enter_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Enter_Instance is null");
            }
            return PMMA::KeyEvent_Enter_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Enter_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Enter_Instance is null");
            }
            return PMMA::KeyEvent_Enter_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Enter_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Enter_Instance is null");
            }
            PMMA::KeyEvent_Enter_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Enter_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Enter_Instance is null");
            }
            return PMMA::KeyEvent_Enter_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Enter_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Enter_Instance is null");
            }
            return PMMA::KeyEvent_Enter_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Tab_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Tab_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Tab_Instance is null");
            }
            return PMMA::KeyEvent_Tab_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Tab_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Tab_Instance is null");
            }
            PMMA::KeyEvent_Tab_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Tab_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Tab_Instance is null");
            }
            return PMMA::KeyEvent_Tab_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Tab_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Tab_Instance is null");
            }
            return PMMA::KeyEvent_Tab_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Tab_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Tab_Instance is null");
            }
            PMMA::KeyEvent_Tab_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Tab_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Tab_Instance is null");
            }
            return PMMA::KeyEvent_Tab_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Tab_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Tab_Instance is null");
            }
            return PMMA::KeyEvent_Tab_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Backspace_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Backspace_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Backspace_Instance is null");
            }
            return PMMA::KeyEvent_Backspace_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Backspace_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Backspace_Instance is null");
            }
            PMMA::KeyEvent_Backspace_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Backspace_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Backspace_Instance is null");
            }
            return PMMA::KeyEvent_Backspace_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Backspace_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Backspace_Instance is null");
            }
            return PMMA::KeyEvent_Backspace_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Backspace_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Backspace_Instance is null");
            }
            PMMA::KeyEvent_Backspace_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Backspace_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Backspace_Instance is null");
            }
            return PMMA::KeyEvent_Backspace_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Backspace_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Backspace_Instance is null");
            }
            return PMMA::KeyEvent_Backspace_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Insert_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Insert_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Insert_Instance is null");
            }
            return PMMA::KeyEvent_Insert_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Insert_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Insert_Instance is null");
            }
            PMMA::KeyEvent_Insert_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Insert_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Insert_Instance is null");
            }
            return PMMA::KeyEvent_Insert_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Insert_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Insert_Instance is null");
            }
            return PMMA::KeyEvent_Insert_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Insert_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Insert_Instance is null");
            }
            PMMA::KeyEvent_Insert_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Insert_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Insert_Instance is null");
            }
            return PMMA::KeyEvent_Insert_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Insert_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Insert_Instance is null");
            }
            return PMMA::KeyEvent_Insert_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Delete_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Delete_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Delete_Instance is null");
            }
            return PMMA::KeyEvent_Delete_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Delete_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Delete_Instance is null");
            }
            PMMA::KeyEvent_Delete_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Delete_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Delete_Instance is null");
            }
            return PMMA::KeyEvent_Delete_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Delete_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Delete_Instance is null");
            }
            return PMMA::KeyEvent_Delete_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Delete_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Delete_Instance is null");
            }
            PMMA::KeyEvent_Delete_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Delete_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Delete_Instance is null");
            }
            return PMMA::KeyEvent_Delete_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Delete_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Delete_Instance is null");
            }
            return PMMA::KeyEvent_Delete_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Right_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Right_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Instance is null");
            }
            return PMMA::KeyEvent_Right_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Right_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Instance is null");
            }
            PMMA::KeyEvent_Right_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Right_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Instance is null");
            }
            return PMMA::KeyEvent_Right_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Right_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Instance is null");
            }
            return PMMA::KeyEvent_Right_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Right_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Instance is null");
            }
            PMMA::KeyEvent_Right_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Right_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Instance is null");
            }
            return PMMA::KeyEvent_Right_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Right_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Instance is null");
            }
            return PMMA::KeyEvent_Right_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Left_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Left_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Instance is null");
            }
            return PMMA::KeyEvent_Left_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Left_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Instance is null");
            }
            PMMA::KeyEvent_Left_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Left_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Instance is null");
            }
            return PMMA::KeyEvent_Left_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Left_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Instance is null");
            }
            return PMMA::KeyEvent_Left_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Left_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Instance is null");
            }
            PMMA::KeyEvent_Left_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Left_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Instance is null");
            }
            return PMMA::KeyEvent_Left_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Left_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Instance is null");
            }
            return PMMA::KeyEvent_Left_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Down_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Down_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Down_Instance is null");
            }
            return PMMA::KeyEvent_Down_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Down_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Down_Instance is null");
            }
            PMMA::KeyEvent_Down_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Down_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Down_Instance is null");
            }
            return PMMA::KeyEvent_Down_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Down_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Down_Instance is null");
            }
            return PMMA::KeyEvent_Down_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Down_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Down_Instance is null");
            }
            PMMA::KeyEvent_Down_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Down_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Down_Instance is null");
            }
            return PMMA::KeyEvent_Down_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Down_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Down_Instance is null");
            }
            return PMMA::KeyEvent_Down_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Up_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Up_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Up_Instance is null");
            }
            return PMMA::KeyEvent_Up_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Up_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Up_Instance is null");
            }
            PMMA::KeyEvent_Up_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Up_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Up_Instance is null");
            }
            return PMMA::KeyEvent_Up_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Up_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Up_Instance is null");
            }
            return PMMA::KeyEvent_Up_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Up_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Up_Instance is null");
            }
            PMMA::KeyEvent_Up_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Up_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Up_Instance is null");
            }
            return PMMA::KeyEvent_Up_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Up_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Up_Instance is null");
            }
            return PMMA::KeyEvent_Up_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Page_Up_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Page_Up_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Page_Up_Instance is null");
            }
            return PMMA::KeyEvent_Page_Up_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Page_Up_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Page_Up_Instance is null");
            }
            PMMA::KeyEvent_Page_Up_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Page_Up_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Page_Up_Instance is null");
            }
            return PMMA::KeyEvent_Page_Up_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Page_Up_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Page_Up_Instance is null");
            }
            return PMMA::KeyEvent_Page_Up_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Page_Up_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Page_Up_Instance is null");
            }
            PMMA::KeyEvent_Page_Up_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Page_Up_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Page_Up_Instance is null");
            }
            return PMMA::KeyEvent_Page_Up_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Page_Up_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Page_Up_Instance is null");
            }
            return PMMA::KeyEvent_Page_Up_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Page_Down_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Page_Down_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Page_Down_Instance is null");
            }
            return PMMA::KeyEvent_Page_Down_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Page_Down_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Page_Down_Instance is null");
            }
            PMMA::KeyEvent_Page_Down_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Page_Down_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Page_Down_Instance is null");
            }
            return PMMA::KeyEvent_Page_Down_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Page_Down_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Page_Down_Instance is null");
            }
            return PMMA::KeyEvent_Page_Down_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Page_Down_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Page_Down_Instance is null");
            }
            PMMA::KeyEvent_Page_Down_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Page_Down_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Page_Down_Instance is null");
            }
            return PMMA::KeyEvent_Page_Down_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Page_Down_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Page_Down_Instance is null");
            }
            return PMMA::KeyEvent_Page_Down_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Home_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Home_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Home_Instance is null");
            }
            return PMMA::KeyEvent_Home_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Home_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Home_Instance is null");
            }
            PMMA::KeyEvent_Home_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Home_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Home_Instance is null");
            }
            return PMMA::KeyEvent_Home_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Home_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Home_Instance is null");
            }
            return PMMA::KeyEvent_Home_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Home_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Home_Instance is null");
            }
            PMMA::KeyEvent_Home_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Home_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Home_Instance is null");
            }
            return PMMA::KeyEvent_Home_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Home_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Home_Instance is null");
            }
            return PMMA::KeyEvent_Home_Instance->PollLongPressed();
        };
};

class EXPORT CPP_End_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_End_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_End_Instance is null");
            }
            return PMMA::KeyEvent_End_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_End_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_End_Instance is null");
            }
            PMMA::KeyEvent_End_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_End_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_End_Instance is null");
            }
            return PMMA::KeyEvent_End_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_End_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_End_Instance is null");
            }
            return PMMA::KeyEvent_End_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_End_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_End_Instance is null");
            }
            PMMA::KeyEvent_End_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_End_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_End_Instance is null");
            }
            return PMMA::KeyEvent_End_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_End_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_End_Instance is null");
            }
            return PMMA::KeyEvent_End_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Caps_Lock_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Caps_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Caps_Lock_Instance is null");
            }
            return PMMA::KeyEvent_Caps_Lock_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Caps_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Caps_Lock_Instance is null");
            }
            PMMA::KeyEvent_Caps_Lock_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Caps_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Caps_Lock_Instance is null");
            }
            return PMMA::KeyEvent_Caps_Lock_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Caps_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Caps_Lock_Instance is null");
            }
            return PMMA::KeyEvent_Caps_Lock_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Caps_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Caps_Lock_Instance is null");
            }
            PMMA::KeyEvent_Caps_Lock_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Caps_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Caps_Lock_Instance is null");
            }
            return PMMA::KeyEvent_Caps_Lock_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Caps_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Caps_Lock_Instance is null");
            }
            return PMMA::KeyEvent_Caps_Lock_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Scroll_Lock_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Scroll_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Scroll_Lock_Instance is null");
            }
            return PMMA::KeyEvent_Scroll_Lock_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Scroll_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Scroll_Lock_Instance is null");
            }
            PMMA::KeyEvent_Scroll_Lock_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Scroll_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Scroll_Lock_Instance is null");
            }
            return PMMA::KeyEvent_Scroll_Lock_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Scroll_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Scroll_Lock_Instance is null");
            }
            return PMMA::KeyEvent_Scroll_Lock_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Scroll_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Scroll_Lock_Instance is null");
            }
            PMMA::KeyEvent_Scroll_Lock_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Scroll_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Scroll_Lock_Instance is null");
            }
            return PMMA::KeyEvent_Scroll_Lock_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Scroll_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Scroll_Lock_Instance is null");
            }
            return PMMA::KeyEvent_Scroll_Lock_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Num_Lock_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Num_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Num_Lock_Instance is null");
            }
            return PMMA::KeyEvent_Num_Lock_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Num_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Num_Lock_Instance is null");
            }
            PMMA::KeyEvent_Num_Lock_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Num_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Num_Lock_Instance is null");
            }
            return PMMA::KeyEvent_Num_Lock_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Num_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Num_Lock_Instance is null");
            }
            return PMMA::KeyEvent_Num_Lock_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Num_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Num_Lock_Instance is null");
            }
            PMMA::KeyEvent_Num_Lock_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Num_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Num_Lock_Instance is null");
            }
            return PMMA::KeyEvent_Num_Lock_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Num_Lock_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Num_Lock_Instance is null");
            }
            return PMMA::KeyEvent_Num_Lock_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Print_Screen_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Print_Screen_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Print_Screen_Instance is null");
            }
            return PMMA::KeyEvent_Print_Screen_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Print_Screen_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Print_Screen_Instance is null");
            }
            PMMA::KeyEvent_Print_Screen_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Print_Screen_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Print_Screen_Instance is null");
            }
            return PMMA::KeyEvent_Print_Screen_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Print_Screen_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Print_Screen_Instance is null");
            }
            return PMMA::KeyEvent_Print_Screen_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Print_Screen_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Print_Screen_Instance is null");
            }
            PMMA::KeyEvent_Print_Screen_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Print_Screen_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Print_Screen_Instance is null");
            }
            return PMMA::KeyEvent_Print_Screen_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Print_Screen_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Print_Screen_Instance is null");
            }
            return PMMA::KeyEvent_Print_Screen_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Pause_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Pause_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Pause_Instance is null");
            }
            return PMMA::KeyEvent_Pause_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Pause_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Pause_Instance is null");
            }
            PMMA::KeyEvent_Pause_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Pause_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Pause_Instance is null");
            }
            return PMMA::KeyEvent_Pause_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Pause_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Pause_Instance is null");
            }
            return PMMA::KeyEvent_Pause_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Pause_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Pause_Instance is null");
            }
            PMMA::KeyEvent_Pause_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Pause_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Pause_Instance is null");
            }
            return PMMA::KeyEvent_Pause_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Pause_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Pause_Instance is null");
            }
            return PMMA::KeyEvent_Pause_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F1_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F1_Instance is null");
            }
            return PMMA::KeyEvent_F1_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F1_Instance is null");
            }
            PMMA::KeyEvent_F1_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F1_Instance is null");
            }
            return PMMA::KeyEvent_F1_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F1_Instance is null");
            }
            return PMMA::KeyEvent_F1_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F1_Instance is null");
            }
            PMMA::KeyEvent_F1_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F1_Instance is null");
            }
            return PMMA::KeyEvent_F1_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F1_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F1_Instance is null");
            }
            return PMMA::KeyEvent_F1_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F2_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F2_Instance is null");
            }
            return PMMA::KeyEvent_F2_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F2_Instance is null");
            }
            PMMA::KeyEvent_F2_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F2_Instance is null");
            }
            return PMMA::KeyEvent_F2_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F2_Instance is null");
            }
            return PMMA::KeyEvent_F2_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F2_Instance is null");
            }
            PMMA::KeyEvent_F2_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F2_Instance is null");
            }
            return PMMA::KeyEvent_F2_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F2_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F2_Instance is null");
            }
            return PMMA::KeyEvent_F2_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F3_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F3_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F3_Instance is null");
            }
            return PMMA::KeyEvent_F3_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F3_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F3_Instance is null");
            }
            PMMA::KeyEvent_F3_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F3_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F3_Instance is null");
            }
            return PMMA::KeyEvent_F3_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F3_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F3_Instance is null");
            }
            return PMMA::KeyEvent_F3_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F3_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F3_Instance is null");
            }
            PMMA::KeyEvent_F3_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F3_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F3_Instance is null");
            }
            return PMMA::KeyEvent_F3_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F3_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F3_Instance is null");
            }
            return PMMA::KeyEvent_F3_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F4_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F4_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F4_Instance is null");
            }
            return PMMA::KeyEvent_F4_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F4_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F4_Instance is null");
            }
            PMMA::KeyEvent_F4_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F4_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F4_Instance is null");
            }
            return PMMA::KeyEvent_F4_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F4_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F4_Instance is null");
            }
            return PMMA::KeyEvent_F4_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F4_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F4_Instance is null");
            }
            PMMA::KeyEvent_F4_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F4_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F4_Instance is null");
            }
            return PMMA::KeyEvent_F4_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F4_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F4_Instance is null");
            }
            return PMMA::KeyEvent_F4_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F5_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F5_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F5_Instance is null");
            }
            return PMMA::KeyEvent_F5_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F5_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F5_Instance is null");
            }
            PMMA::KeyEvent_F5_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F5_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F5_Instance is null");
            }
            return PMMA::KeyEvent_F5_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F5_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F5_Instance is null");
            }
            return PMMA::KeyEvent_F5_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F5_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F5_Instance is null");
            }
            PMMA::KeyEvent_F5_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F5_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F5_Instance is null");
            }
            return PMMA::KeyEvent_F5_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F5_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F5_Instance is null");
            }
            return PMMA::KeyEvent_F5_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F6_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F6_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F6_Instance is null");
            }
            return PMMA::KeyEvent_F6_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F6_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F6_Instance is null");
            }
            PMMA::KeyEvent_F6_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F6_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F6_Instance is null");
            }
            return PMMA::KeyEvent_F6_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F6_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F6_Instance is null");
            }
            return PMMA::KeyEvent_F6_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F6_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F6_Instance is null");
            }
            PMMA::KeyEvent_F6_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F6_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F6_Instance is null");
            }
            return PMMA::KeyEvent_F6_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F6_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F6_Instance is null");
            }
            return PMMA::KeyEvent_F6_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F7_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F7_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F7_Instance is null");
            }
            return PMMA::KeyEvent_F7_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F7_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F7_Instance is null");
            }
            PMMA::KeyEvent_F7_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F7_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F7_Instance is null");
            }
            return PMMA::KeyEvent_F7_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F7_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F7_Instance is null");
            }
            return PMMA::KeyEvent_F7_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F7_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F7_Instance is null");
            }
            PMMA::KeyEvent_F7_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F7_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F7_Instance is null");
            }
            return PMMA::KeyEvent_F7_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F7_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F7_Instance is null");
            }
            return PMMA::KeyEvent_F7_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F8_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F8_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F8_Instance is null");
            }
            return PMMA::KeyEvent_F8_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F8_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F8_Instance is null");
            }
            PMMA::KeyEvent_F8_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F8_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F8_Instance is null");
            }
            return PMMA::KeyEvent_F8_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F8_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F8_Instance is null");
            }
            return PMMA::KeyEvent_F8_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F8_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F8_Instance is null");
            }
            PMMA::KeyEvent_F8_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F8_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F8_Instance is null");
            }
            return PMMA::KeyEvent_F8_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F8_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F8_Instance is null");
            }
            return PMMA::KeyEvent_F8_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F9_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F9_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F9_Instance is null");
            }
            return PMMA::KeyEvent_F9_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F9_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F9_Instance is null");
            }
            PMMA::KeyEvent_F9_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F9_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F9_Instance is null");
            }
            return PMMA::KeyEvent_F9_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F9_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F9_Instance is null");
            }
            return PMMA::KeyEvent_F9_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F9_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F9_Instance is null");
            }
            PMMA::KeyEvent_F9_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F9_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F9_Instance is null");
            }
            return PMMA::KeyEvent_F9_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F9_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F9_Instance is null");
            }
            return PMMA::KeyEvent_F9_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F10_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F10_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F10_Instance is null");
            }
            return PMMA::KeyEvent_F10_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F10_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F10_Instance is null");
            }
            PMMA::KeyEvent_F10_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F10_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F10_Instance is null");
            }
            return PMMA::KeyEvent_F10_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F10_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F10_Instance is null");
            }
            return PMMA::KeyEvent_F10_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F10_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F10_Instance is null");
            }
            PMMA::KeyEvent_F10_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F10_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F10_Instance is null");
            }
            return PMMA::KeyEvent_F10_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F10_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F10_Instance is null");
            }
            return PMMA::KeyEvent_F10_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F11_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F11_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F11_Instance is null");
            }
            return PMMA::KeyEvent_F11_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F11_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F11_Instance is null");
            }
            PMMA::KeyEvent_F11_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F11_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F11_Instance is null");
            }
            return PMMA::KeyEvent_F11_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F11_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F11_Instance is null");
            }
            return PMMA::KeyEvent_F11_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F11_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F11_Instance is null");
            }
            PMMA::KeyEvent_F11_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F11_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F11_Instance is null");
            }
            return PMMA::KeyEvent_F11_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F11_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F11_Instance is null");
            }
            return PMMA::KeyEvent_F11_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F12_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F12_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F12_Instance is null");
            }
            return PMMA::KeyEvent_F12_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F12_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F12_Instance is null");
            }
            PMMA::KeyEvent_F12_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F12_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F12_Instance is null");
            }
            return PMMA::KeyEvent_F12_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F12_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F12_Instance is null");
            }
            return PMMA::KeyEvent_F12_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F12_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F12_Instance is null");
            }
            PMMA::KeyEvent_F12_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F12_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F12_Instance is null");
            }
            return PMMA::KeyEvent_F12_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F12_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F12_Instance is null");
            }
            return PMMA::KeyEvent_F12_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F13_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F13_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F13_Instance is null");
            }
            return PMMA::KeyEvent_F13_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F13_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F13_Instance is null");
            }
            PMMA::KeyEvent_F13_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F13_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F13_Instance is null");
            }
            return PMMA::KeyEvent_F13_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F13_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F13_Instance is null");
            }
            return PMMA::KeyEvent_F13_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F13_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F13_Instance is null");
            }
            PMMA::KeyEvent_F13_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F13_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F13_Instance is null");
            }
            return PMMA::KeyEvent_F13_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F13_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F13_Instance is null");
            }
            return PMMA::KeyEvent_F13_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F14_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F14_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F14_Instance is null");
            }
            return PMMA::KeyEvent_F14_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F14_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F14_Instance is null");
            }
            PMMA::KeyEvent_F14_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F14_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F14_Instance is null");
            }
            return PMMA::KeyEvent_F14_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F14_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F14_Instance is null");
            }
            return PMMA::KeyEvent_F14_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F14_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F14_Instance is null");
            }
            PMMA::KeyEvent_F14_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F14_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F14_Instance is null");
            }
            return PMMA::KeyEvent_F14_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F14_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F14_Instance is null");
            }
            return PMMA::KeyEvent_F14_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F15_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F15_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F15_Instance is null");
            }
            return PMMA::KeyEvent_F15_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F15_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F15_Instance is null");
            }
            PMMA::KeyEvent_F15_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F15_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F15_Instance is null");
            }
            return PMMA::KeyEvent_F15_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F15_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F15_Instance is null");
            }
            return PMMA::KeyEvent_F15_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F15_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F15_Instance is null");
            }
            PMMA::KeyEvent_F15_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F15_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F15_Instance is null");
            }
            return PMMA::KeyEvent_F15_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F15_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F15_Instance is null");
            }
            return PMMA::KeyEvent_F15_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F16_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F16_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F16_Instance is null");
            }
            return PMMA::KeyEvent_F16_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F16_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F16_Instance is null");
            }
            PMMA::KeyEvent_F16_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F16_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F16_Instance is null");
            }
            return PMMA::KeyEvent_F16_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F16_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F16_Instance is null");
            }
            return PMMA::KeyEvent_F16_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F16_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F16_Instance is null");
            }
            PMMA::KeyEvent_F16_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F16_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F16_Instance is null");
            }
            return PMMA::KeyEvent_F16_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F16_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F16_Instance is null");
            }
            return PMMA::KeyEvent_F16_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F17_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F17_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F17_Instance is null");
            }
            return PMMA::KeyEvent_F17_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F17_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F17_Instance is null");
            }
            PMMA::KeyEvent_F17_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F17_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F17_Instance is null");
            }
            return PMMA::KeyEvent_F17_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F17_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F17_Instance is null");
            }
            return PMMA::KeyEvent_F17_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F17_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F17_Instance is null");
            }
            PMMA::KeyEvent_F17_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F17_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F17_Instance is null");
            }
            return PMMA::KeyEvent_F17_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F17_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F17_Instance is null");
            }
            return PMMA::KeyEvent_F17_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F18_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F18_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F18_Instance is null");
            }
            return PMMA::KeyEvent_F18_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F18_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F18_Instance is null");
            }
            PMMA::KeyEvent_F18_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F18_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F18_Instance is null");
            }
            return PMMA::KeyEvent_F18_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F18_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F18_Instance is null");
            }
            return PMMA::KeyEvent_F18_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F18_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F18_Instance is null");
            }
            PMMA::KeyEvent_F18_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F18_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F18_Instance is null");
            }
            return PMMA::KeyEvent_F18_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F18_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F18_Instance is null");
            }
            return PMMA::KeyEvent_F18_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F19_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F19_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F19_Instance is null");
            }
            return PMMA::KeyEvent_F19_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F19_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F19_Instance is null");
            }
            PMMA::KeyEvent_F19_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F19_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F19_Instance is null");
            }
            return PMMA::KeyEvent_F19_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F19_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F19_Instance is null");
            }
            return PMMA::KeyEvent_F19_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F19_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F19_Instance is null");
            }
            PMMA::KeyEvent_F19_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F19_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F19_Instance is null");
            }
            return PMMA::KeyEvent_F19_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F19_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F19_Instance is null");
            }
            return PMMA::KeyEvent_F19_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F20_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F20_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F20_Instance is null");
            }
            return PMMA::KeyEvent_F20_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F20_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F20_Instance is null");
            }
            PMMA::KeyEvent_F20_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F20_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F20_Instance is null");
            }
            return PMMA::KeyEvent_F20_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F20_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F20_Instance is null");
            }
            return PMMA::KeyEvent_F20_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F20_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F20_Instance is null");
            }
            PMMA::KeyEvent_F20_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F20_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F20_Instance is null");
            }
            return PMMA::KeyEvent_F20_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F20_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F20_Instance is null");
            }
            return PMMA::KeyEvent_F20_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F21_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F21_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F21_Instance is null");
            }
            return PMMA::KeyEvent_F21_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F21_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F21_Instance is null");
            }
            PMMA::KeyEvent_F21_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F21_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F21_Instance is null");
            }
            return PMMA::KeyEvent_F21_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F21_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F21_Instance is null");
            }
            return PMMA::KeyEvent_F21_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F21_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F21_Instance is null");
            }
            PMMA::KeyEvent_F21_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F21_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F21_Instance is null");
            }
            return PMMA::KeyEvent_F21_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F21_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F21_Instance is null");
            }
            return PMMA::KeyEvent_F21_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F22_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F22_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F22_Instance is null");
            }
            return PMMA::KeyEvent_F22_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F22_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F22_Instance is null");
            }
            PMMA::KeyEvent_F22_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F22_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F22_Instance is null");
            }
            return PMMA::KeyEvent_F22_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F22_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F22_Instance is null");
            }
            return PMMA::KeyEvent_F22_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F22_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F22_Instance is null");
            }
            PMMA::KeyEvent_F22_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F22_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F22_Instance is null");
            }
            return PMMA::KeyEvent_F22_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F22_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F22_Instance is null");
            }
            return PMMA::KeyEvent_F22_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F23_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F23_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F23_Instance is null");
            }
            return PMMA::KeyEvent_F23_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F23_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F23_Instance is null");
            }
            PMMA::KeyEvent_F23_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F23_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F23_Instance is null");
            }
            return PMMA::KeyEvent_F23_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F23_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F23_Instance is null");
            }
            return PMMA::KeyEvent_F23_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F23_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F23_Instance is null");
            }
            PMMA::KeyEvent_F23_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F23_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F23_Instance is null");
            }
            return PMMA::KeyEvent_F23_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F23_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F23_Instance is null");
            }
            return PMMA::KeyEvent_F23_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F24_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F24_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F24_Instance is null");
            }
            return PMMA::KeyEvent_F24_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F24_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F24_Instance is null");
            }
            PMMA::KeyEvent_F24_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F24_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F24_Instance is null");
            }
            return PMMA::KeyEvent_F24_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F24_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F24_Instance is null");
            }
            return PMMA::KeyEvent_F24_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F24_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F24_Instance is null");
            }
            PMMA::KeyEvent_F24_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F24_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F24_Instance is null");
            }
            return PMMA::KeyEvent_F24_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F24_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F24_Instance is null");
            }
            return PMMA::KeyEvent_F24_Instance->PollLongPressed();
        };
};

class EXPORT CPP_F25_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_F25_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F25_Instance is null");
            }
            return PMMA::KeyEvent_F25_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_F25_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F25_Instance is null");
            }
            PMMA::KeyEvent_F25_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_F25_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F25_Instance is null");
            }
            return PMMA::KeyEvent_F25_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_F25_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F25_Instance is null");
            }
            return PMMA::KeyEvent_F25_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_F25_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F25_Instance is null");
            }
            PMMA::KeyEvent_F25_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_F25_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F25_Instance is null");
            }
            return PMMA::KeyEvent_F25_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_F25_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_F25_Instance is null");
            }
            return PMMA::KeyEvent_F25_Instance->PollLongPressed();
        };
};

class EXPORT CPP_0_KeyPadEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyPadEvent_0_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_0_Instance is null");
            }
            return PMMA::KeyPadEvent_0_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyPadEvent_0_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_0_Instance is null");
            }
            PMMA::KeyPadEvent_0_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyPadEvent_0_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_0_Instance is null");
            }
            return PMMA::KeyPadEvent_0_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyPadEvent_0_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_0_Instance is null");
            }
            return PMMA::KeyPadEvent_0_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyPadEvent_0_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_0_Instance is null");
            }
            PMMA::KeyPadEvent_0_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyPadEvent_0_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_0_Instance is null");
            }
            return PMMA::KeyPadEvent_0_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyPadEvent_0_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_0_Instance is null");
            }
            return PMMA::KeyPadEvent_0_Instance->PollLongPressed();
        };
};

class EXPORT CPP_1_KeyPadEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyPadEvent_1_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_1_Instance is null");
            }
            return PMMA::KeyPadEvent_1_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyPadEvent_1_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_1_Instance is null");
            }
            PMMA::KeyPadEvent_1_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyPadEvent_1_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_1_Instance is null");
            }
            return PMMA::KeyPadEvent_1_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyPadEvent_1_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_1_Instance is null");
            }
            return PMMA::KeyPadEvent_1_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyPadEvent_1_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_1_Instance is null");
            }
            PMMA::KeyPadEvent_1_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyPadEvent_1_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_1_Instance is null");
            }
            return PMMA::KeyPadEvent_1_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyPadEvent_1_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_1_Instance is null");
            }
            return PMMA::KeyPadEvent_1_Instance->PollLongPressed();
        };
};

class EXPORT CPP_2_KeyPadEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyPadEvent_2_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_2_Instance is null");
            }
            return PMMA::KeyPadEvent_2_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyPadEvent_2_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_2_Instance is null");
            }
            PMMA::KeyPadEvent_2_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyPadEvent_2_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_2_Instance is null");
            }
            return PMMA::KeyPadEvent_2_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyPadEvent_2_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_2_Instance is null");
            }
            return PMMA::KeyPadEvent_2_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyPadEvent_2_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_2_Instance is null");
            }
            PMMA::KeyPadEvent_2_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyPadEvent_2_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_2_Instance is null");
            }
            return PMMA::KeyPadEvent_2_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyPadEvent_2_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_2_Instance is null");
            }
            return PMMA::KeyPadEvent_2_Instance->PollLongPressed();
        };
};

class EXPORT CPP_3_KeyPadEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyPadEvent_3_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_3_Instance is null");
            }
            return PMMA::KeyPadEvent_3_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyPadEvent_3_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_3_Instance is null");
            }
            PMMA::KeyPadEvent_3_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyPadEvent_3_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_3_Instance is null");
            }
            return PMMA::KeyPadEvent_3_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyPadEvent_3_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_3_Instance is null");
            }
            return PMMA::KeyPadEvent_3_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyPadEvent_3_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_3_Instance is null");
            }
            PMMA::KeyPadEvent_3_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyPadEvent_3_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_3_Instance is null");
            }
            return PMMA::KeyPadEvent_3_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyPadEvent_3_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_3_Instance is null");
            }
            return PMMA::KeyPadEvent_3_Instance->PollLongPressed();
        };
};

class EXPORT CPP_4_KeyPadEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyPadEvent_4_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_4_Instance is null");
            }
            return PMMA::KeyPadEvent_4_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyPadEvent_4_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_4_Instance is null");
            }
            PMMA::KeyPadEvent_4_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyPadEvent_4_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_4_Instance is null");
            }
            return PMMA::KeyPadEvent_4_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyPadEvent_4_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_4_Instance is null");
            }
            return PMMA::KeyPadEvent_4_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyPadEvent_4_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_4_Instance is null");
            }
            PMMA::KeyPadEvent_4_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyPadEvent_4_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_4_Instance is null");
            }
            return PMMA::KeyPadEvent_4_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyPadEvent_4_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_4_Instance is null");
            }
            return PMMA::KeyPadEvent_4_Instance->PollLongPressed();
        };
};

class EXPORT CPP_5_KeyPadEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyPadEvent_5_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_5_Instance is null");
            }
            return PMMA::KeyPadEvent_5_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyPadEvent_5_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_5_Instance is null");
            }
            PMMA::KeyPadEvent_5_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyPadEvent_5_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_5_Instance is null");
            }
            return PMMA::KeyPadEvent_5_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyPadEvent_5_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_5_Instance is null");
            }
            return PMMA::KeyPadEvent_5_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyPadEvent_5_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_5_Instance is null");
            }
            PMMA::KeyPadEvent_5_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyPadEvent_5_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_5_Instance is null");
            }
            return PMMA::KeyPadEvent_5_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyPadEvent_5_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_5_Instance is null");
            }
            return PMMA::KeyPadEvent_5_Instance->PollLongPressed();
        };
};

class EXPORT CPP_6_KeyPadEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyPadEvent_6_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_6_Instance is null");
            }
            return PMMA::KeyPadEvent_6_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyPadEvent_6_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_6_Instance is null");
            }
            PMMA::KeyPadEvent_6_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyPadEvent_6_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_6_Instance is null");
            }
            return PMMA::KeyPadEvent_6_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyPadEvent_6_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_6_Instance is null");
            }
            return PMMA::KeyPadEvent_6_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyPadEvent_6_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_6_Instance is null");
            }
            PMMA::KeyPadEvent_6_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyPadEvent_6_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_6_Instance is null");
            }
            return PMMA::KeyPadEvent_6_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyPadEvent_6_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_6_Instance is null");
            }
            return PMMA::KeyPadEvent_6_Instance->PollLongPressed();
        };
};

class EXPORT CPP_7_KeyPadEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyPadEvent_7_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_7_Instance is null");
            }
            return PMMA::KeyPadEvent_7_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyPadEvent_7_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_7_Instance is null");
            }
            PMMA::KeyPadEvent_7_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyPadEvent_7_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_7_Instance is null");
            }
            return PMMA::KeyPadEvent_7_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyPadEvent_7_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_7_Instance is null");
            }
            return PMMA::KeyPadEvent_7_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyPadEvent_7_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_7_Instance is null");
            }
            PMMA::KeyPadEvent_7_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyPadEvent_7_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_7_Instance is null");
            }
            return PMMA::KeyPadEvent_7_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyPadEvent_7_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_7_Instance is null");
            }
            return PMMA::KeyPadEvent_7_Instance->PollLongPressed();
        };
};

class EXPORT CPP_8_KeyPadEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyPadEvent_8_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_8_Instance is null");
            }
            return PMMA::KeyPadEvent_8_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyPadEvent_8_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_8_Instance is null");
            }
            PMMA::KeyPadEvent_8_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyPadEvent_8_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_8_Instance is null");
            }
            return PMMA::KeyPadEvent_8_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyPadEvent_8_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_8_Instance is null");
            }
            return PMMA::KeyPadEvent_8_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyPadEvent_8_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_8_Instance is null");
            }
            PMMA::KeyPadEvent_8_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyPadEvent_8_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_8_Instance is null");
            }
            return PMMA::KeyPadEvent_8_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyPadEvent_8_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_8_Instance is null");
            }
            return PMMA::KeyPadEvent_8_Instance->PollLongPressed();
        };
};

class EXPORT CPP_9_KeyPadEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyPadEvent_9_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_9_Instance is null");
            }
            return PMMA::KeyPadEvent_9_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyPadEvent_9_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_9_Instance is null");
            }
            PMMA::KeyPadEvent_9_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyPadEvent_9_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_9_Instance is null");
            }
            return PMMA::KeyPadEvent_9_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyPadEvent_9_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_9_Instance is null");
            }
            return PMMA::KeyPadEvent_9_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyPadEvent_9_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_9_Instance is null");
            }
            PMMA::KeyPadEvent_9_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyPadEvent_9_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_9_Instance is null");
            }
            return PMMA::KeyPadEvent_9_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyPadEvent_9_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_9_Instance is null");
            }
            return PMMA::KeyPadEvent_9_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Decimal_KeyPadEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyPadEvent_Decimal_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Decimal_Instance is null");
            }
            return PMMA::KeyPadEvent_Decimal_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyPadEvent_Decimal_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Decimal_Instance is null");
            }
            PMMA::KeyPadEvent_Decimal_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyPadEvent_Decimal_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Decimal_Instance is null");
            }
            return PMMA::KeyPadEvent_Decimal_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyPadEvent_Decimal_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Decimal_Instance is null");
            }
            return PMMA::KeyPadEvent_Decimal_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyPadEvent_Decimal_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Decimal_Instance is null");
            }
            PMMA::KeyPadEvent_Decimal_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyPadEvent_Decimal_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Decimal_Instance is null");
            }
            return PMMA::KeyPadEvent_Decimal_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyPadEvent_Decimal_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Decimal_Instance is null");
            }
            return PMMA::KeyPadEvent_Decimal_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Divide_KeyPadEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyPadEvent_Divide_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Divide_Instance is null");
            }
            return PMMA::KeyPadEvent_Divide_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyPadEvent_Divide_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Divide_Instance is null");
            }
            PMMA::KeyPadEvent_Divide_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyPadEvent_Divide_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Divide_Instance is null");
            }
            return PMMA::KeyPadEvent_Divide_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyPadEvent_Divide_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Divide_Instance is null");
            }
            return PMMA::KeyPadEvent_Divide_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyPadEvent_Divide_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Divide_Instance is null");
            }
            PMMA::KeyPadEvent_Divide_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyPadEvent_Divide_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Divide_Instance is null");
            }
            return PMMA::KeyPadEvent_Divide_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyPadEvent_Divide_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Divide_Instance is null");
            }
            return PMMA::KeyPadEvent_Divide_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Multiply_KeyPadEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyPadEvent_Multiply_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Multiply_Instance is null");
            }
            return PMMA::KeyPadEvent_Multiply_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyPadEvent_Multiply_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Multiply_Instance is null");
            }
            PMMA::KeyPadEvent_Multiply_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyPadEvent_Multiply_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Multiply_Instance is null");
            }
            return PMMA::KeyPadEvent_Multiply_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyPadEvent_Multiply_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Multiply_Instance is null");
            }
            return PMMA::KeyPadEvent_Multiply_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyPadEvent_Multiply_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Multiply_Instance is null");
            }
            PMMA::KeyPadEvent_Multiply_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyPadEvent_Multiply_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Multiply_Instance is null");
            }
            return PMMA::KeyPadEvent_Multiply_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyPadEvent_Multiply_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Multiply_Instance is null");
            }
            return PMMA::KeyPadEvent_Multiply_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Subtract_KeyPadEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyPadEvent_Subtract_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Subtract_Instance is null");
            }
            return PMMA::KeyPadEvent_Subtract_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyPadEvent_Subtract_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Subtract_Instance is null");
            }
            PMMA::KeyPadEvent_Subtract_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyPadEvent_Subtract_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Subtract_Instance is null");
            }
            return PMMA::KeyPadEvent_Subtract_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyPadEvent_Subtract_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Subtract_Instance is null");
            }
            return PMMA::KeyPadEvent_Subtract_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyPadEvent_Subtract_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Subtract_Instance is null");
            }
            PMMA::KeyPadEvent_Subtract_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyPadEvent_Subtract_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Subtract_Instance is null");
            }
            return PMMA::KeyPadEvent_Subtract_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyPadEvent_Subtract_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Subtract_Instance is null");
            }
            return PMMA::KeyPadEvent_Subtract_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Add_KeyPadEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyPadEvent_Add_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Add_Instance is null");
            }
            return PMMA::KeyPadEvent_Add_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyPadEvent_Add_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Add_Instance is null");
            }
            PMMA::KeyPadEvent_Add_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyPadEvent_Add_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Add_Instance is null");
            }
            return PMMA::KeyPadEvent_Add_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyPadEvent_Add_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Add_Instance is null");
            }
            return PMMA::KeyPadEvent_Add_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyPadEvent_Add_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Add_Instance is null");
            }
            PMMA::KeyPadEvent_Add_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyPadEvent_Add_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Add_Instance is null");
            }
            return PMMA::KeyPadEvent_Add_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyPadEvent_Add_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Add_Instance is null");
            }
            return PMMA::KeyPadEvent_Add_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Enter_KeyPadEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyPadEvent_Enter_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Enter_Instance is null");
            }
            return PMMA::KeyPadEvent_Enter_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyPadEvent_Enter_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Enter_Instance is null");
            }
            PMMA::KeyPadEvent_Enter_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyPadEvent_Enter_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Enter_Instance is null");
            }
            return PMMA::KeyPadEvent_Enter_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyPadEvent_Enter_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Enter_Instance is null");
            }
            return PMMA::KeyPadEvent_Enter_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyPadEvent_Enter_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Enter_Instance is null");
            }
            PMMA::KeyPadEvent_Enter_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyPadEvent_Enter_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Enter_Instance is null");
            }
            return PMMA::KeyPadEvent_Enter_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyPadEvent_Enter_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Enter_Instance is null");
            }
            return PMMA::KeyPadEvent_Enter_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Equal_KeyPadEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyPadEvent_Equal_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Equal_Instance is null");
            }
            return PMMA::KeyPadEvent_Equal_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyPadEvent_Equal_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Equal_Instance is null");
            }
            PMMA::KeyPadEvent_Equal_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyPadEvent_Equal_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Equal_Instance is null");
            }
            return PMMA::KeyPadEvent_Equal_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyPadEvent_Equal_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Equal_Instance is null");
            }
            return PMMA::KeyPadEvent_Equal_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyPadEvent_Equal_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Equal_Instance is null");
            }
            PMMA::KeyPadEvent_Equal_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyPadEvent_Equal_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Equal_Instance is null");
            }
            return PMMA::KeyPadEvent_Equal_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyPadEvent_Equal_Instance == nullptr) {
                throw std::runtime_error("KeyPadEvent_Equal_Instance is null");
            }
            return PMMA::KeyPadEvent_Equal_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Left_Shift_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Left_Shift_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Shift_Instance is null");
            }
            return PMMA::KeyEvent_Left_Shift_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Left_Shift_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Shift_Instance is null");
            }
            PMMA::KeyEvent_Left_Shift_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Left_Shift_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Shift_Instance is null");
            }
            return PMMA::KeyEvent_Left_Shift_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Left_Shift_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Shift_Instance is null");
            }
            return PMMA::KeyEvent_Left_Shift_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Left_Shift_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Shift_Instance is null");
            }
            PMMA::KeyEvent_Left_Shift_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Left_Shift_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Shift_Instance is null");
            }
            return PMMA::KeyEvent_Left_Shift_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Left_Shift_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Shift_Instance is null");
            }
            return PMMA::KeyEvent_Left_Shift_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Left_Control_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Left_Control_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Control_Instance is null");
            }
            return PMMA::KeyEvent_Left_Control_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Left_Control_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Control_Instance is null");
            }
            PMMA::KeyEvent_Left_Control_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Left_Control_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Control_Instance is null");
            }
            return PMMA::KeyEvent_Left_Control_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Left_Control_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Control_Instance is null");
            }
            return PMMA::KeyEvent_Left_Control_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Left_Control_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Control_Instance is null");
            }
            PMMA::KeyEvent_Left_Control_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Left_Control_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Control_Instance is null");
            }
            return PMMA::KeyEvent_Left_Control_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Left_Control_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Control_Instance is null");
            }
            return PMMA::KeyEvent_Left_Control_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Left_Alt_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Left_Alt_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Alt_Instance is null");
            }
            return PMMA::KeyEvent_Left_Alt_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Left_Alt_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Alt_Instance is null");
            }
            PMMA::KeyEvent_Left_Alt_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Left_Alt_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Alt_Instance is null");
            }
            return PMMA::KeyEvent_Left_Alt_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Left_Alt_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Alt_Instance is null");
            }
            return PMMA::KeyEvent_Left_Alt_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Left_Alt_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Alt_Instance is null");
            }
            PMMA::KeyEvent_Left_Alt_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Left_Alt_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Alt_Instance is null");
            }
            return PMMA::KeyEvent_Left_Alt_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Left_Alt_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Alt_Instance is null");
            }
            return PMMA::KeyEvent_Left_Alt_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Left_Super_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Left_Super_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Super_Instance is null");
            }
            return PMMA::KeyEvent_Left_Super_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Left_Super_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Super_Instance is null");
            }
            PMMA::KeyEvent_Left_Super_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Left_Super_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Super_Instance is null");
            }
            return PMMA::KeyEvent_Left_Super_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Left_Super_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Super_Instance is null");
            }
            return PMMA::KeyEvent_Left_Super_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Left_Super_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Super_Instance is null");
            }
            PMMA::KeyEvent_Left_Super_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Left_Super_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Super_Instance is null");
            }
            return PMMA::KeyEvent_Left_Super_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Left_Super_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Left_Super_Instance is null");
            }
            return PMMA::KeyEvent_Left_Super_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Right_Shift_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Right_Shift_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Shift_Instance is null");
            }
            return PMMA::KeyEvent_Right_Shift_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Right_Shift_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Shift_Instance is null");
            }
            PMMA::KeyEvent_Right_Shift_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Right_Shift_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Shift_Instance is null");
            }
            return PMMA::KeyEvent_Right_Shift_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Right_Shift_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Shift_Instance is null");
            }
            return PMMA::KeyEvent_Right_Shift_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Right_Shift_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Shift_Instance is null");
            }
            PMMA::KeyEvent_Right_Shift_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Right_Shift_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Shift_Instance is null");
            }
            return PMMA::KeyEvent_Right_Shift_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Right_Shift_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Shift_Instance is null");
            }
            return PMMA::KeyEvent_Right_Shift_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Right_Control_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Right_Control_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Control_Instance is null");
            }
            return PMMA::KeyEvent_Right_Control_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Right_Control_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Control_Instance is null");
            }
            PMMA::KeyEvent_Right_Control_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Right_Control_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Control_Instance is null");
            }
            return PMMA::KeyEvent_Right_Control_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Right_Control_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Control_Instance is null");
            }
            return PMMA::KeyEvent_Right_Control_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Right_Control_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Control_Instance is null");
            }
            PMMA::KeyEvent_Right_Control_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Right_Control_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Control_Instance is null");
            }
            return PMMA::KeyEvent_Right_Control_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Right_Control_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Control_Instance is null");
            }
            return PMMA::KeyEvent_Right_Control_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Right_Alt_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Right_Alt_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Alt_Instance is null");
            }
            return PMMA::KeyEvent_Right_Alt_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Right_Alt_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Alt_Instance is null");
            }
            PMMA::KeyEvent_Right_Alt_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Right_Alt_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Alt_Instance is null");
            }
            return PMMA::KeyEvent_Right_Alt_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Right_Alt_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Alt_Instance is null");
            }
            return PMMA::KeyEvent_Right_Alt_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Right_Alt_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Alt_Instance is null");
            }
            PMMA::KeyEvent_Right_Alt_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Right_Alt_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Alt_Instance is null");
            }
            return PMMA::KeyEvent_Right_Alt_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Right_Alt_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Alt_Instance is null");
            }
            return PMMA::KeyEvent_Right_Alt_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Right_Super_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Right_Super_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Super_Instance is null");
            }
            return PMMA::KeyEvent_Right_Super_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Right_Super_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Super_Instance is null");
            }
            PMMA::KeyEvent_Right_Super_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Right_Super_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Super_Instance is null");
            }
            return PMMA::KeyEvent_Right_Super_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Right_Super_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Super_Instance is null");
            }
            return PMMA::KeyEvent_Right_Super_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Right_Super_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Super_Instance is null");
            }
            PMMA::KeyEvent_Right_Super_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Right_Super_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Super_Instance is null");
            }
            return PMMA::KeyEvent_Right_Super_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Right_Super_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Right_Super_Instance is null");
            }
            return PMMA::KeyEvent_Right_Super_Instance->PollLongPressed();
        };
};

class EXPORT CPP_Menu_KeyEvent {
    public:
        inline bool GetPressed() {
            if (PMMA::KeyEvent_Menu_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Menu_Instance is null");
            }
            return PMMA::KeyEvent_Menu_Instance->GetPressed();
        };

        inline void SetDoublePressDuration(float duration) {
            if (PMMA::KeyEvent_Menu_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Menu_Instance is null");
            }
            PMMA::KeyEvent_Menu_Instance->SetDoublePressDuration(duration);
        };

        inline bool GetPressedToggle() {
            if (PMMA::KeyEvent_Menu_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Menu_Instance is null");
            }
            return PMMA::KeyEvent_Menu_Instance->GetPressedToggle();
        };

        inline bool GetDoublePressed() {
            if (PMMA::KeyEvent_Menu_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Menu_Instance is null");
            }
            return PMMA::KeyEvent_Menu_Instance->GetDoublePressed();
        };

        inline void SetLongPressDuration(float duration) {
            if (PMMA::KeyEvent_Menu_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Menu_Instance is null");
            }
            PMMA::KeyEvent_Menu_Instance->SetLongPressDuration(duration);
        };

        inline bool GetLongPressed() {
            if (PMMA::KeyEvent_Menu_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Menu_Instance is null");
            }
            return PMMA::KeyEvent_Menu_Instance->GetLongPressed();
        };

        inline bool PollLongPressed() {
            if (PMMA::KeyEvent_Menu_Instance == nullptr) {
                throw std::runtime_error("KeyEvent_Menu_Instance is null");
            }
            return PMMA::KeyEvent_Menu_Instance->PollLongPressed();
        };
};