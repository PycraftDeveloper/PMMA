#include "PMMA_Core.hpp"

PMMA::Events::KeyPad_0::KeyPad_0() {
    PMMA::Core::KeyPadEvent_0_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::KeyPad_0::~KeyPad_0() {
    auto it = find(PMMA::Core::KeyPadEvent_0_Instances.begin(), PMMA::Core::KeyPadEvent_0_Instances.end(), this);
    if (it != PMMA::Core::KeyPadEvent_0_Instances.end()) {
        PMMA::Core::KeyPadEvent_0_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::KeyPad_1::KeyPad_1() {
    PMMA::Core::KeyPadEvent_1_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::KeyPad_1::~KeyPad_1() {
    auto it = find(PMMA::Core::KeyPadEvent_1_Instances.begin(), PMMA::Core::KeyPadEvent_1_Instances.end(), this);
    if (it != PMMA::Core::KeyPadEvent_1_Instances.end()) {
        PMMA::Core::KeyPadEvent_1_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::KeyPad_2::KeyPad_2() {
    PMMA::Core::KeyPadEvent_2_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::KeyPad_2::~KeyPad_2() {
    auto it = find(PMMA::Core::KeyPadEvent_2_Instances.begin(), PMMA::Core::KeyPadEvent_2_Instances.end(), this);
    if (it != PMMA::Core::KeyPadEvent_2_Instances.end()) {
        PMMA::Core::KeyPadEvent_2_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::KeyPad_3::KeyPad_3() {
    PMMA::Core::KeyPadEvent_3_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::KeyPad_3::~KeyPad_3() {
    auto it = find(PMMA::Core::KeyPadEvent_3_Instances.begin(), PMMA::Core::KeyPadEvent_3_Instances.end(), this);
    if (it != PMMA::Core::KeyPadEvent_3_Instances.end()) {
        PMMA::Core::KeyPadEvent_3_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::KeyPad_4::KeyPad_4() {
    PMMA::Core::KeyPadEvent_4_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::KeyPad_4::~KeyPad_4() {
    auto it = find(PMMA::Core::KeyPadEvent_4_Instances.begin(), PMMA::Core::KeyPadEvent_4_Instances.end(), this);
    if (it != PMMA::Core::KeyPadEvent_4_Instances.end()) {
        PMMA::Core::KeyPadEvent_4_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::KeyPad_5::KeyPad_5() {
    PMMA::Core::KeyPadEvent_5_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::KeyPad_5::~KeyPad_5() {
    auto it = find(PMMA::Core::KeyPadEvent_5_Instances.begin(), PMMA::Core::KeyPadEvent_5_Instances.end(), this);
    if (it != PMMA::Core::KeyPadEvent_5_Instances.end()) {
        PMMA::Core::KeyPadEvent_5_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::KeyPad_6::KeyPad_6() {
    PMMA::Core::KeyPadEvent_6_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::KeyPad_6::~KeyPad_6() {
    auto it = find(PMMA::Core::KeyPadEvent_6_Instances.begin(), PMMA::Core::KeyPadEvent_6_Instances.end(), this);
    if (it != PMMA::Core::KeyPadEvent_6_Instances.end()) {
        PMMA::Core::KeyPadEvent_6_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::KeyPad_7::KeyPad_7() {
    PMMA::Core::KeyPadEvent_7_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::KeyPad_7::~KeyPad_7() {
    auto it = find(PMMA::Core::KeyPadEvent_7_Instances.begin(), PMMA::Core::KeyPadEvent_7_Instances.end(), this);
    if (it != PMMA::Core::KeyPadEvent_7_Instances.end()) {
        PMMA::Core::KeyPadEvent_7_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::KeyPad_8::KeyPad_8() {
    PMMA::Core::KeyPadEvent_8_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::KeyPad_8::~KeyPad_8() {
    auto it = find(PMMA::Core::KeyPadEvent_8_Instances.begin(), PMMA::Core::KeyPadEvent_8_Instances.end(), this);
    if (it != PMMA::Core::KeyPadEvent_8_Instances.end()) {
        PMMA::Core::KeyPadEvent_8_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::KeyPad_9::KeyPad_9() {
    PMMA::Core::KeyPadEvent_9_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::KeyPad_9::~KeyPad_9() {
    auto it = find(PMMA::Core::KeyPadEvent_9_Instances.begin(), PMMA::Core::KeyPadEvent_9_Instances.end(), this);
    if (it != PMMA::Core::KeyPadEvent_9_Instances.end()) {
        PMMA::Core::KeyPadEvent_9_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::KeyPad_Decimal::KeyPad_Decimal() {
    PMMA::Core::KeyPadEvent_Decimal_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::KeyPad_Decimal::~KeyPad_Decimal() {
    auto it = find(PMMA::Core::KeyPadEvent_Decimal_Instances.begin(), PMMA::Core::KeyPadEvent_Decimal_Instances.end(), this);
    if (it != PMMA::Core::KeyPadEvent_Decimal_Instances.end()) {
        PMMA::Core::KeyPadEvent_Decimal_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::KeyPad_Divide::KeyPad_Divide() {
    PMMA::Core::KeyPadEvent_Divide_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::KeyPad_Divide::~KeyPad_Divide() {
    auto it = find(PMMA::Core::KeyPadEvent_Divide_Instances.begin(), PMMA::Core::KeyPadEvent_Divide_Instances.end(), this);
    if (it != PMMA::Core::KeyPadEvent_Divide_Instances.end()) {
        PMMA::Core::KeyPadEvent_Divide_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::KeyPad_Multiply::KeyPad_Multiply() {
    PMMA::Core::KeyPadEvent_Multiply_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::KeyPad_Multiply::~KeyPad_Multiply() {
    auto it = find(PMMA::Core::KeyPadEvent_Multiply_Instances.begin(), PMMA::Core::KeyPadEvent_Multiply_Instances.end(), this);
    if (it != PMMA::Core::KeyPadEvent_Multiply_Instances.end()) {
        PMMA::Core::KeyPadEvent_Multiply_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::KeyPad_Subtract::KeyPad_Subtract() {
    PMMA::Core::KeyPadEvent_Subtract_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::KeyPad_Subtract::~KeyPad_Subtract() {
    auto it = find(PMMA::Core::KeyPadEvent_Subtract_Instances.begin(), PMMA::Core::KeyPadEvent_Subtract_Instances.end(), this);
    if (it != PMMA::Core::KeyPadEvent_Subtract_Instances.end()) {
        PMMA::Core::KeyPadEvent_Subtract_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::KeyPad_Add::KeyPad_Add() {
    PMMA::Core::KeyPadEvent_Add_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::KeyPad_Add::~KeyPad_Add() {
    auto it = find(PMMA::Core::KeyPadEvent_Add_Instances.begin(), PMMA::Core::KeyPadEvent_Add_Instances.end(), this);
    if (it != PMMA::Core::KeyPadEvent_Add_Instances.end()) {
        PMMA::Core::KeyPadEvent_Add_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::KeyPad_Enter::KeyPad_Enter() {
    PMMA::Core::KeyPadEvent_Enter_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::KeyPad_Enter::~KeyPad_Enter() {
    auto it = find(PMMA::Core::KeyPadEvent_Enter_Instances.begin(), PMMA::Core::KeyPadEvent_Enter_Instances.end(), this);
    if (it != PMMA::Core::KeyPadEvent_Enter_Instances.end()) {
        PMMA::Core::KeyPadEvent_Enter_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::KeyPad_Equal::KeyPad_Equal() {
    PMMA::Core::KeyPadEvent_Equal_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::KeyPad_Equal::~KeyPad_Equal() {
    auto it = find(PMMA::Core::KeyPadEvent_Equal_Instances.begin(), PMMA::Core::KeyPadEvent_Equal_Instances.end(), this);
    if (it != PMMA::Core::KeyPadEvent_Equal_Instances.end()) {
        PMMA::Core::KeyPadEvent_Equal_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};