#include "Events/KeyPadEvents.hpp"

#include "PMMA_Core.hpp"

using namespace std;

CPP_KeyPadEvent_0::CPP_KeyPadEvent_0() {
    PMMA::KeyPadEvent_0_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyPadEvent_0::~CPP_KeyPadEvent_0() {
    auto it = find(PMMA::KeyPadEvent_0_Instances.begin(), PMMA::KeyPadEvent_0_Instances.end(), this);
    if (it != PMMA::KeyPadEvent_0_Instances.end()) {
        PMMA::KeyPadEvent_0_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyPadEvent_1::CPP_KeyPadEvent_1() {
    PMMA::KeyPadEvent_1_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyPadEvent_1::~CPP_KeyPadEvent_1() {
    auto it = find(PMMA::KeyPadEvent_1_Instances.begin(), PMMA::KeyPadEvent_1_Instances.end(), this);
    if (it != PMMA::KeyPadEvent_1_Instances.end()) {
        PMMA::KeyPadEvent_1_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyPadEvent_2::CPP_KeyPadEvent_2() {
    PMMA::KeyPadEvent_2_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyPadEvent_2::~CPP_KeyPadEvent_2() {
    auto it = find(PMMA::KeyPadEvent_2_Instances.begin(), PMMA::KeyPadEvent_2_Instances.end(), this);
    if (it != PMMA::KeyPadEvent_2_Instances.end()) {
        PMMA::KeyPadEvent_2_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyPadEvent_3::CPP_KeyPadEvent_3() {
    PMMA::KeyPadEvent_3_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyPadEvent_3::~CPP_KeyPadEvent_3() {
    auto it = find(PMMA::KeyPadEvent_3_Instances.begin(), PMMA::KeyPadEvent_3_Instances.end(), this);
    if (it != PMMA::KeyPadEvent_3_Instances.end()) {
        PMMA::KeyPadEvent_3_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyPadEvent_4::CPP_KeyPadEvent_4() {
    PMMA::KeyPadEvent_4_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyPadEvent_4::~CPP_KeyPadEvent_4() {
    auto it = find(PMMA::KeyPadEvent_4_Instances.begin(), PMMA::KeyPadEvent_4_Instances.end(), this);
    if (it != PMMA::KeyPadEvent_4_Instances.end()) {
        PMMA::KeyPadEvent_4_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyPadEvent_5::CPP_KeyPadEvent_5() {
    PMMA::KeyPadEvent_5_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyPadEvent_5::~CPP_KeyPadEvent_5() {
    auto it = find(PMMA::KeyPadEvent_5_Instances.begin(), PMMA::KeyPadEvent_5_Instances.end(), this);
    if (it != PMMA::KeyPadEvent_5_Instances.end()) {
        PMMA::KeyPadEvent_5_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyPadEvent_6::CPP_KeyPadEvent_6() {
    PMMA::KeyPadEvent_6_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyPadEvent_6::~CPP_KeyPadEvent_6() {
    auto it = find(PMMA::KeyPadEvent_6_Instances.begin(), PMMA::KeyPadEvent_6_Instances.end(), this);
    if (it != PMMA::KeyPadEvent_6_Instances.end()) {
        PMMA::KeyPadEvent_6_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyPadEvent_7::CPP_KeyPadEvent_7() {
    PMMA::KeyPadEvent_7_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyPadEvent_7::~CPP_KeyPadEvent_7() {
    auto it = find(PMMA::KeyPadEvent_7_Instances.begin(), PMMA::KeyPadEvent_7_Instances.end(), this);
    if (it != PMMA::KeyPadEvent_7_Instances.end()) {
        PMMA::KeyPadEvent_7_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyPadEvent_8::CPP_KeyPadEvent_8() {
    PMMA::KeyPadEvent_8_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyPadEvent_8::~CPP_KeyPadEvent_8() {
    auto it = find(PMMA::KeyPadEvent_8_Instances.begin(), PMMA::KeyPadEvent_8_Instances.end(), this);
    if (it != PMMA::KeyPadEvent_8_Instances.end()) {
        PMMA::KeyPadEvent_8_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyPadEvent_9::CPP_KeyPadEvent_9() {
    PMMA::KeyPadEvent_9_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyPadEvent_9::~CPP_KeyPadEvent_9() {
    auto it = find(PMMA::KeyPadEvent_9_Instances.begin(), PMMA::KeyPadEvent_9_Instances.end(), this);
    if (it != PMMA::KeyPadEvent_9_Instances.end()) {
        PMMA::KeyPadEvent_9_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyPadEvent_Decimal::CPP_KeyPadEvent_Decimal() {
    PMMA::KeyPadEvent_Decimal_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyPadEvent_Decimal::~CPP_KeyPadEvent_Decimal() {
    auto it = find(PMMA::KeyPadEvent_Decimal_Instances.begin(), PMMA::KeyPadEvent_Decimal_Instances.end(), this);
    if (it != PMMA::KeyPadEvent_Decimal_Instances.end()) {
        PMMA::KeyPadEvent_Decimal_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyPadEvent_Divide::CPP_KeyPadEvent_Divide() {
    PMMA::KeyPadEvent_Divide_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyPadEvent_Divide::~CPP_KeyPadEvent_Divide() {
    auto it = find(PMMA::KeyPadEvent_Divide_Instances.begin(), PMMA::KeyPadEvent_Divide_Instances.end(), this);
    if (it != PMMA::KeyPadEvent_Divide_Instances.end()) {
        PMMA::KeyPadEvent_Divide_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyPadEvent_Multiply::CPP_KeyPadEvent_Multiply() {
    PMMA::KeyPadEvent_Multiply_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyPadEvent_Multiply::~CPP_KeyPadEvent_Multiply() {
    auto it = find(PMMA::KeyPadEvent_Multiply_Instances.begin(), PMMA::KeyPadEvent_Multiply_Instances.end(), this);
    if (it != PMMA::KeyPadEvent_Multiply_Instances.end()) {
        PMMA::KeyPadEvent_Multiply_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyPadEvent_Subtract::CPP_KeyPadEvent_Subtract() {
    PMMA::KeyPadEvent_Subtract_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyPadEvent_Subtract::~CPP_KeyPadEvent_Subtract() {
    auto it = find(PMMA::KeyPadEvent_Subtract_Instances.begin(), PMMA::KeyPadEvent_Subtract_Instances.end(), this);
    if (it != PMMA::KeyPadEvent_Subtract_Instances.end()) {
        PMMA::KeyPadEvent_Subtract_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyPadEvent_Add::CPP_KeyPadEvent_Add() {
    PMMA::KeyPadEvent_Add_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyPadEvent_Add::~CPP_KeyPadEvent_Add() {
    auto it = find(PMMA::KeyPadEvent_Add_Instances.begin(), PMMA::KeyPadEvent_Add_Instances.end(), this);
    if (it != PMMA::KeyPadEvent_Add_Instances.end()) {
        PMMA::KeyPadEvent_Add_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyPadEvent_Enter::CPP_KeyPadEvent_Enter() {
    PMMA::KeyPadEvent_Enter_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyPadEvent_Enter::~CPP_KeyPadEvent_Enter() {
    auto it = find(PMMA::KeyPadEvent_Enter_Instances.begin(), PMMA::KeyPadEvent_Enter_Instances.end(), this);
    if (it != PMMA::KeyPadEvent_Enter_Instances.end()) {
        PMMA::KeyPadEvent_Enter_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyPadEvent_Equal::CPP_KeyPadEvent_Equal() {
    PMMA::KeyPadEvent_Equal_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyPadEvent_Equal::~CPP_KeyPadEvent_Equal() {
    auto it = find(PMMA::KeyPadEvent_Equal_Instances.begin(), PMMA::KeyPadEvent_Equal_Instances.end(), this);
    if (it != PMMA::KeyPadEvent_Equal_Instances.end()) {
        PMMA::KeyPadEvent_Equal_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};