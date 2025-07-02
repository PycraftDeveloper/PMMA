#include <string>

#include "Events/KeyEvents.hpp"

#include "PMMA_Core.hpp"

using namespace std;

CPP_KeyEvent_Space::CPP_KeyEvent_Space() {
    PMMA::KeyEvent_Space_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Space::~CPP_KeyEvent_Space() {
    auto it = find(PMMA::KeyEvent_Space_Instances.begin(), PMMA::KeyEvent_Space_Instances.end(), this);
    if (it != PMMA::KeyEvent_Space_Instances.end()) {
        PMMA::KeyEvent_Space_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Apostrophe::CPP_KeyEvent_Apostrophe() {
    PMMA::KeyEvent_Apostrophe_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Apostrophe::~CPP_KeyEvent_Apostrophe() {
    auto it = find(PMMA::KeyEvent_Apostrophe_Instances.begin(), PMMA::KeyEvent_Apostrophe_Instances.end(), this);
    if (it != PMMA::KeyEvent_Apostrophe_Instances.end()) {
        PMMA::KeyEvent_Apostrophe_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Comma::CPP_KeyEvent_Comma() {
    PMMA::KeyEvent_Comma_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Comma::~CPP_KeyEvent_Comma() {
    auto it = find(PMMA::KeyEvent_Comma_Instances.begin(), PMMA::KeyEvent_Comma_Instances.end(), this);
    if (it != PMMA::KeyEvent_Comma_Instances.end()) {
        PMMA::KeyEvent_Comma_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Minus::CPP_KeyEvent_Minus() {
    PMMA::KeyEvent_Minus_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Minus::~CPP_KeyEvent_Minus() {
    auto it = find(PMMA::KeyEvent_Minus_Instances.begin(), PMMA::KeyEvent_Minus_Instances.end(), this);
    if (it != PMMA::KeyEvent_Minus_Instances.end()) {
        PMMA::KeyEvent_Minus_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Period::CPP_KeyEvent_Period() {
    PMMA::KeyEvent_Period_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Period::~CPP_KeyEvent_Period() {
    auto it = find(PMMA::KeyEvent_Period_Instances.begin(), PMMA::KeyEvent_Period_Instances.end(), this);
    if (it != PMMA::KeyEvent_Period_Instances.end()) {
        PMMA::KeyEvent_Period_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Slash::CPP_KeyEvent_Slash() {
    PMMA::KeyEvent_Slash_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Slash::~CPP_KeyEvent_Slash() {
    auto it = find(PMMA::KeyEvent_Slash_Instances.begin(), PMMA::KeyEvent_Slash_Instances.end(), this);
    if (it != PMMA::KeyEvent_Slash_Instances.end()) {
        PMMA::KeyEvent_Slash_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_0::CPP_KeyEvent_0() {
    PMMA::KeyEvent_0_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_0::~CPP_KeyEvent_0() {
    auto it = find(PMMA::KeyEvent_0_Instances.begin(), PMMA::KeyEvent_0_Instances.end(), this);
    if (it != PMMA::KeyEvent_0_Instances.end()) {
        PMMA::KeyEvent_0_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_1::CPP_KeyEvent_1() {
    PMMA::KeyEvent_1_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_1::~CPP_KeyEvent_1() {
    auto it = find(PMMA::KeyEvent_1_Instances.begin(), PMMA::KeyEvent_1_Instances.end(), this);
    if (it != PMMA::KeyEvent_1_Instances.end()) {
        PMMA::KeyEvent_1_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_2::CPP_KeyEvent_2() {
    PMMA::KeyEvent_2_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_2::~CPP_KeyEvent_2() {
    auto it = find(PMMA::KeyEvent_2_Instances.begin(), PMMA::KeyEvent_2_Instances.end(), this);
    if (it != PMMA::KeyEvent_2_Instances.end()) {
        PMMA::KeyEvent_2_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_3::CPP_KeyEvent_3() {
    PMMA::KeyEvent_3_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_3::~CPP_KeyEvent_3() {
    auto it = find(PMMA::KeyEvent_3_Instances.begin(), PMMA::KeyEvent_3_Instances.end(), this);
    if (it != PMMA::KeyEvent_3_Instances.end()) {
        PMMA::KeyEvent_3_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_4::CPP_KeyEvent_4() {
    PMMA::KeyEvent_4_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_4::~CPP_KeyEvent_4() {
    auto it = find(PMMA::KeyEvent_4_Instances.begin(), PMMA::KeyEvent_4_Instances.end(), this);
    if (it != PMMA::KeyEvent_4_Instances.end()) {
        PMMA::KeyEvent_4_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_5::CPP_KeyEvent_5() {
    PMMA::KeyEvent_5_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_5::~CPP_KeyEvent_5() {
    auto it = find(PMMA::KeyEvent_5_Instances.begin(), PMMA::KeyEvent_5_Instances.end(), this);
    if (it != PMMA::KeyEvent_5_Instances.end()) {
        PMMA::KeyEvent_5_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_6::CPP_KeyEvent_6() {
    PMMA::KeyEvent_6_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_6::~CPP_KeyEvent_6() {
    auto it = find(PMMA::KeyEvent_6_Instances.begin(), PMMA::KeyEvent_6_Instances.end(), this);
    if (it != PMMA::KeyEvent_6_Instances.end()) {
        PMMA::KeyEvent_6_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_7::CPP_KeyEvent_7() {
    PMMA::KeyEvent_7_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_7::~CPP_KeyEvent_7() {
    auto it = find(PMMA::KeyEvent_7_Instances.begin(), PMMA::KeyEvent_7_Instances.end(), this);
    if (it != PMMA::KeyEvent_7_Instances.end()) {
        PMMA::KeyEvent_7_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_8::CPP_KeyEvent_8() {
    PMMA::KeyEvent_8_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_8::~CPP_KeyEvent_8() {
    auto it = find(PMMA::KeyEvent_8_Instances.begin(), PMMA::KeyEvent_8_Instances.end(), this);
    if (it != PMMA::KeyEvent_8_Instances.end()) {
        PMMA::KeyEvent_8_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_9::CPP_KeyEvent_9() {
    PMMA::KeyEvent_9_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_9::~CPP_KeyEvent_9() {
    auto it = find(PMMA::KeyEvent_9_Instances.begin(), PMMA::KeyEvent_9_Instances.end(), this);
    if (it != PMMA::KeyEvent_9_Instances.end()) {
        PMMA::KeyEvent_9_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Semicolon::CPP_KeyEvent_Semicolon() {
    PMMA::KeyEvent_Semicolon_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Semicolon::~CPP_KeyEvent_Semicolon() {
    auto it = find(PMMA::KeyEvent_Semicolon_Instances.begin(), PMMA::KeyEvent_Semicolon_Instances.end(), this);
    if (it != PMMA::KeyEvent_Semicolon_Instances.end()) {
        PMMA::KeyEvent_Semicolon_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Equal::CPP_KeyEvent_Equal() {
    PMMA::KeyEvent_Equal_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Equal::~CPP_KeyEvent_Equal() {
    auto it = find(PMMA::KeyEvent_Equal_Instances.begin(), PMMA::KeyEvent_Equal_Instances.end(), this);
    if (it != PMMA::KeyEvent_Equal_Instances.end()) {
        PMMA::KeyEvent_Equal_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_A::CPP_KeyEvent_A() {
    PMMA::KeyEvent_A_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_A::~CPP_KeyEvent_A() {
    auto it = find(PMMA::KeyEvent_A_Instances.begin(), PMMA::KeyEvent_A_Instances.end(), this);
    if (it != PMMA::KeyEvent_A_Instances.end()) {
        PMMA::KeyEvent_A_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_B::CPP_KeyEvent_B() {
    PMMA::KeyEvent_B_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_B::~CPP_KeyEvent_B() {
    auto it = find(PMMA::KeyEvent_B_Instances.begin(), PMMA::KeyEvent_B_Instances.end(), this);
    if (it != PMMA::KeyEvent_B_Instances.end()) {
        PMMA::KeyEvent_B_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_C::CPP_KeyEvent_C() {
    PMMA::KeyEvent_C_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_C::~CPP_KeyEvent_C() {
    auto it = find(PMMA::KeyEvent_C_Instances.begin(), PMMA::KeyEvent_C_Instances.end(), this);
    if (it != PMMA::KeyEvent_C_Instances.end()) {
        PMMA::KeyEvent_C_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_D::CPP_KeyEvent_D() {
    PMMA::KeyEvent_D_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_D::~CPP_KeyEvent_D() {
    auto it = find(PMMA::KeyEvent_D_Instances.begin(), PMMA::KeyEvent_D_Instances.end(), this);
    if (it != PMMA::KeyEvent_D_Instances.end()) {
        PMMA::KeyEvent_D_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_E::CPP_KeyEvent_E() {
    PMMA::KeyEvent_E_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_E::~CPP_KeyEvent_E() {
    auto it = find(PMMA::KeyEvent_E_Instances.begin(), PMMA::KeyEvent_E_Instances.end(), this);
    if (it != PMMA::KeyEvent_E_Instances.end()) {
        PMMA::KeyEvent_E_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F::CPP_KeyEvent_F() {
    PMMA::KeyEvent_F_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F::~CPP_KeyEvent_F() {
    auto it = find(PMMA::KeyEvent_F_Instances.begin(), PMMA::KeyEvent_F_Instances.end(), this);
    if (it != PMMA::KeyEvent_F_Instances.end()) {
        PMMA::KeyEvent_F_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_G::CPP_KeyEvent_G() {
    PMMA::KeyEvent_G_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_G::~CPP_KeyEvent_G() {
    auto it = find(PMMA::KeyEvent_G_Instances.begin(), PMMA::KeyEvent_G_Instances.end(), this);
    if (it != PMMA::KeyEvent_G_Instances.end()) {
        PMMA::KeyEvent_G_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_H::CPP_KeyEvent_H() {
    PMMA::KeyEvent_H_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_H::~CPP_KeyEvent_H() {
    auto it = find(PMMA::KeyEvent_H_Instances.begin(), PMMA::KeyEvent_H_Instances.end(), this);
    if (it != PMMA::KeyEvent_H_Instances.end()) {
        PMMA::KeyEvent_H_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_I::CPP_KeyEvent_I() {
    PMMA::KeyEvent_I_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_I::~CPP_KeyEvent_I() {
    auto it = find(PMMA::KeyEvent_I_Instances.begin(), PMMA::KeyEvent_I_Instances.end(), this);
    if (it != PMMA::KeyEvent_I_Instances.end()) {
        PMMA::KeyEvent_I_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_J::CPP_KeyEvent_J() {
    PMMA::KeyEvent_J_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_J::~CPP_KeyEvent_J() {
    auto it = find(PMMA::KeyEvent_J_Instances.begin(), PMMA::KeyEvent_J_Instances.end(), this);
    if (it != PMMA::KeyEvent_J_Instances.end()) {
        PMMA::KeyEvent_J_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_K::CPP_KeyEvent_K() {
    PMMA::KeyEvent_K_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_K::~CPP_KeyEvent_K() {
    auto it = find(PMMA::KeyEvent_K_Instances.begin(), PMMA::KeyEvent_K_Instances.end(), this);
    if (it != PMMA::KeyEvent_K_Instances.end()) {
        PMMA::KeyEvent_K_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_L::CPP_KeyEvent_L() {
    PMMA::KeyEvent_L_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_L::~CPP_KeyEvent_L() {
    auto it = find(PMMA::KeyEvent_L_Instances.begin(), PMMA::KeyEvent_L_Instances.end(), this);
    if (it != PMMA::KeyEvent_L_Instances.end()) {
        PMMA::KeyEvent_L_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_M::CPP_KeyEvent_M() {
    PMMA::KeyEvent_M_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_M::~CPP_KeyEvent_M() {
    auto it = find(PMMA::KeyEvent_M_Instances.begin(), PMMA::KeyEvent_M_Instances.end(), this);
    if (it != PMMA::KeyEvent_M_Instances.end()) {
        PMMA::KeyEvent_M_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_N::CPP_KeyEvent_N() {
    PMMA::KeyEvent_N_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_N::~CPP_KeyEvent_N() {
    auto it = find(PMMA::KeyEvent_N_Instances.begin(), PMMA::KeyEvent_N_Instances.end(), this);
    if (it != PMMA::KeyEvent_N_Instances.end()) {
        PMMA::KeyEvent_N_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_O::CPP_KeyEvent_O() {
    PMMA::KeyEvent_O_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_O::~CPP_KeyEvent_O() {
    auto it = find(PMMA::KeyEvent_O_Instances.begin(), PMMA::KeyEvent_O_Instances.end(), this);
    if (it != PMMA::KeyEvent_O_Instances.end()) {
        PMMA::KeyEvent_O_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_P::CPP_KeyEvent_P() {
    PMMA::KeyEvent_P_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_P::~CPP_KeyEvent_P() {
    auto it = find(PMMA::KeyEvent_P_Instances.begin(), PMMA::KeyEvent_P_Instances.end(), this);
    if (it != PMMA::KeyEvent_P_Instances.end()) {
        PMMA::KeyEvent_P_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Q::CPP_KeyEvent_Q() {
    PMMA::KeyEvent_Q_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Q::~CPP_KeyEvent_Q() {
    auto it = find(PMMA::KeyEvent_Q_Instances.begin(), PMMA::KeyEvent_Q_Instances.end(), this);
    if (it != PMMA::KeyEvent_Q_Instances.end()) {
        PMMA::KeyEvent_Q_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_R::CPP_KeyEvent_R() {
    PMMA::KeyEvent_R_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_R::~CPP_KeyEvent_R() {
    auto it = find(PMMA::KeyEvent_R_Instances.begin(), PMMA::KeyEvent_R_Instances.end(), this);
    if (it != PMMA::KeyEvent_R_Instances.end()) {
        PMMA::KeyEvent_R_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_S::CPP_KeyEvent_S() {
    PMMA::KeyEvent_S_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_S::~CPP_KeyEvent_S() {
    auto it = find(PMMA::KeyEvent_S_Instances.begin(), PMMA::KeyEvent_S_Instances.end(), this);
    if (it != PMMA::KeyEvent_S_Instances.end()) {
        PMMA::KeyEvent_S_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_T::CPP_KeyEvent_T() {
    PMMA::KeyEvent_T_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_T::~CPP_KeyEvent_T() {
    auto it = find(PMMA::KeyEvent_T_Instances.begin(), PMMA::KeyEvent_T_Instances.end(), this);
    if (it != PMMA::KeyEvent_T_Instances.end()) {
        PMMA::KeyEvent_T_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_U::CPP_KeyEvent_U() {
    PMMA::KeyEvent_U_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_U::~CPP_KeyEvent_U() {
    auto it = find(PMMA::KeyEvent_U_Instances.begin(), PMMA::KeyEvent_U_Instances.end(), this);
    if (it != PMMA::KeyEvent_U_Instances.end()) {
        PMMA::KeyEvent_U_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_V::CPP_KeyEvent_V() {
    PMMA::KeyEvent_V_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_V::~CPP_KeyEvent_V() {
    auto it = find(PMMA::KeyEvent_V_Instances.begin(), PMMA::KeyEvent_V_Instances.end(), this);
    if (it != PMMA::KeyEvent_V_Instances.end()) {
        PMMA::KeyEvent_V_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_W::CPP_KeyEvent_W() {
    PMMA::KeyEvent_W_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_W::~CPP_KeyEvent_W() {
    auto it = find(PMMA::KeyEvent_W_Instances.begin(), PMMA::KeyEvent_W_Instances.end(), this);
    if (it != PMMA::KeyEvent_W_Instances.end()) {
        PMMA::KeyEvent_W_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_X::CPP_KeyEvent_X() {
    PMMA::KeyEvent_X_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_X::~CPP_KeyEvent_X() {
    auto it = find(PMMA::KeyEvent_X_Instances.begin(), PMMA::KeyEvent_X_Instances.end(), this);
    if (it != PMMA::KeyEvent_X_Instances.end()) {
        PMMA::KeyEvent_X_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Y::CPP_KeyEvent_Y() {
    PMMA::KeyEvent_Y_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Y::~CPP_KeyEvent_Y() {
    auto it = find(PMMA::KeyEvent_Y_Instances.begin(), PMMA::KeyEvent_Y_Instances.end(), this);
    if (it != PMMA::KeyEvent_Y_Instances.end()) {
        PMMA::KeyEvent_Y_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Z::CPP_KeyEvent_Z() {
    PMMA::KeyEvent_Z_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Z::~CPP_KeyEvent_Z() {
    auto it = find(PMMA::KeyEvent_Z_Instances.begin(), PMMA::KeyEvent_Z_Instances.end(), this);
    if (it != PMMA::KeyEvent_Z_Instances.end()) {
        PMMA::KeyEvent_Z_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Left_Bracket::CPP_KeyEvent_Left_Bracket() {
    PMMA::KeyEvent_Left_Bracket_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Left_Bracket::~CPP_KeyEvent_Left_Bracket() {
    auto it = find(PMMA::KeyEvent_Left_Bracket_Instances.begin(), PMMA::KeyEvent_Left_Bracket_Instances.end(), this);
    if (it != PMMA::KeyEvent_Left_Bracket_Instances.end()) {
        PMMA::KeyEvent_Left_Bracket_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Backslash::CPP_KeyEvent_Backslash() {
    PMMA::KeyEvent_Backslash_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Backslash::~CPP_KeyEvent_Backslash() {
    auto it = find(PMMA::KeyEvent_Backslash_Instances.begin(), PMMA::KeyEvent_Backslash_Instances.end(), this);
    if (it != PMMA::KeyEvent_Backslash_Instances.end()) {
        PMMA::KeyEvent_Backslash_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Right_Bracket::CPP_KeyEvent_Right_Bracket() {
    PMMA::KeyEvent_Right_Bracket_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Right_Bracket::~CPP_KeyEvent_Right_Bracket() {
    auto it = find(PMMA::KeyEvent_Right_Bracket_Instances.begin(), PMMA::KeyEvent_Right_Bracket_Instances.end(), this);
    if (it != PMMA::KeyEvent_Right_Bracket_Instances.end()) {
        PMMA::KeyEvent_Right_Bracket_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Grave_Accent::CPP_KeyEvent_Grave_Accent() {
    PMMA::KeyEvent_Grave_Accent_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Grave_Accent::~CPP_KeyEvent_Grave_Accent() {
    auto it = find(PMMA::KeyEvent_Grave_Accent_Instances.begin(), PMMA::KeyEvent_Grave_Accent_Instances.end(), this);
    if (it != PMMA::KeyEvent_Grave_Accent_Instances.end()) {
        PMMA::KeyEvent_Grave_Accent_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_World_1::CPP_KeyEvent_World_1() {
    PMMA::KeyEvent_World_1_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_World_1::~CPP_KeyEvent_World_1() {
    auto it = find(PMMA::KeyEvent_World_1_Instances.begin(), PMMA::KeyEvent_World_1_Instances.end(), this);
    if (it != PMMA::KeyEvent_World_1_Instances.end()) {
        PMMA::KeyEvent_World_1_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_World_2::CPP_KeyEvent_World_2() {
    PMMA::KeyEvent_World_2_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_World_2::~CPP_KeyEvent_World_2() {
    auto it = find(PMMA::KeyEvent_World_2_Instances.begin(), PMMA::KeyEvent_World_2_Instances.end(), this);
    if (it != PMMA::KeyEvent_World_2_Instances.end()) {
        PMMA::KeyEvent_World_2_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Escape::CPP_KeyEvent_Escape() {
    PMMA::KeyEvent_Escape_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Escape::~CPP_KeyEvent_Escape() {
    auto it = find(PMMA::KeyEvent_Escape_Instances.begin(), PMMA::KeyEvent_Escape_Instances.end(), this);
    if (it != PMMA::KeyEvent_Escape_Instances.end()) {
        PMMA::KeyEvent_Escape_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Enter::CPP_KeyEvent_Enter() {
    PMMA::KeyEvent_Enter_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Enter::~CPP_KeyEvent_Enter() {
    auto it = find(PMMA::KeyEvent_Enter_Instances.begin(), PMMA::KeyEvent_Enter_Instances.end(), this);
    if (it != PMMA::KeyEvent_Enter_Instances.end()) {
        PMMA::KeyEvent_Enter_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Tab::CPP_KeyEvent_Tab() {
    PMMA::KeyEvent_Tab_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Tab::~CPP_KeyEvent_Tab() {
    auto it = find(PMMA::KeyEvent_Tab_Instances.begin(), PMMA::KeyEvent_Tab_Instances.end(), this);
    if (it != PMMA::KeyEvent_Tab_Instances.end()) {
        PMMA::KeyEvent_Tab_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Backspace::CPP_KeyEvent_Backspace() {
    PMMA::KeyEvent_Backspace_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Backspace::~CPP_KeyEvent_Backspace() {
    auto it = find(PMMA::KeyEvent_Backspace_Instances.begin(), PMMA::KeyEvent_Backspace_Instances.end(), this);
    if (it != PMMA::KeyEvent_Backspace_Instances.end()) {
        PMMA::KeyEvent_Backspace_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Insert::CPP_KeyEvent_Insert() {
    PMMA::KeyEvent_Insert_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Insert::~CPP_KeyEvent_Insert() {
    auto it = find(PMMA::KeyEvent_Insert_Instances.begin(), PMMA::KeyEvent_Insert_Instances.end(), this);
    if (it != PMMA::KeyEvent_Insert_Instances.end()) {
        PMMA::KeyEvent_Insert_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Delete::CPP_KeyEvent_Delete() {
    PMMA::KeyEvent_Delete_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Delete::~CPP_KeyEvent_Delete() {
    auto it = find(PMMA::KeyEvent_Delete_Instances.begin(), PMMA::KeyEvent_Delete_Instances.end(), this);
    if (it != PMMA::KeyEvent_Delete_Instances.end()) {
        PMMA::KeyEvent_Delete_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Right::CPP_KeyEvent_Right() {
    PMMA::KeyEvent_Right_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Right::~CPP_KeyEvent_Right() {
    auto it = find(PMMA::KeyEvent_Right_Instances.begin(), PMMA::KeyEvent_Right_Instances.end(), this);
    if (it != PMMA::KeyEvent_Right_Instances.end()) {
        PMMA::KeyEvent_Right_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Left::CPP_KeyEvent_Left() {
    PMMA::KeyEvent_Left_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Left::~CPP_KeyEvent_Left() {
    auto it = find(PMMA::KeyEvent_Left_Instances.begin(), PMMA::KeyEvent_Left_Instances.end(), this);
    if (it != PMMA::KeyEvent_Left_Instances.end()) {
        PMMA::KeyEvent_Left_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Down::CPP_KeyEvent_Down() {
    PMMA::KeyEvent_Down_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Down::~CPP_KeyEvent_Down() {
    auto it = find(PMMA::KeyEvent_Down_Instances.begin(), PMMA::KeyEvent_Down_Instances.end(), this);
    if (it != PMMA::KeyEvent_Down_Instances.end()) {
        PMMA::KeyEvent_Down_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Up::CPP_KeyEvent_Up() {
    PMMA::KeyEvent_Up_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Up::~CPP_KeyEvent_Up() {
    auto it = find(PMMA::KeyEvent_Up_Instances.begin(), PMMA::KeyEvent_Up_Instances.end(), this);
    if (it != PMMA::KeyEvent_Up_Instances.end()) {
        PMMA::KeyEvent_Up_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Page_Up::CPP_KeyEvent_Page_Up() {
    PMMA::KeyEvent_Page_Up_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Page_Up::~CPP_KeyEvent_Page_Up() {
    auto it = find(PMMA::KeyEvent_Page_Up_Instances.begin(), PMMA::KeyEvent_Page_Up_Instances.end(), this);
    if (it != PMMA::KeyEvent_Page_Up_Instances.end()) {
        PMMA::KeyEvent_Page_Up_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Page_Down::CPP_KeyEvent_Page_Down() {
    PMMA::KeyEvent_Page_Down_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Page_Down::~CPP_KeyEvent_Page_Down() {
    auto it = find(PMMA::KeyEvent_Page_Down_Instances.begin(), PMMA::KeyEvent_Page_Down_Instances.end(), this);
    if (it != PMMA::KeyEvent_Page_Down_Instances.end()) {
        PMMA::KeyEvent_Page_Down_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Home::CPP_KeyEvent_Home() {
    PMMA::KeyEvent_Home_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Home::~CPP_KeyEvent_Home() {
    auto it = find(PMMA::KeyEvent_Home_Instances.begin(), PMMA::KeyEvent_Home_Instances.end(), this);
    if (it != PMMA::KeyEvent_Home_Instances.end()) {
        PMMA::KeyEvent_Home_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_End::CPP_KeyEvent_End() {
    PMMA::KeyEvent_End_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_End::~CPP_KeyEvent_End() {
    auto it = find(PMMA::KeyEvent_End_Instances.begin(), PMMA::KeyEvent_End_Instances.end(), this);
    if (it != PMMA::KeyEvent_End_Instances.end()) {
        PMMA::KeyEvent_End_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Caps_Lock::CPP_KeyEvent_Caps_Lock() {
    PMMA::KeyEvent_Caps_Lock_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Caps_Lock::~CPP_KeyEvent_Caps_Lock() {
    auto it = find(PMMA::KeyEvent_Caps_Lock_Instances.begin(), PMMA::KeyEvent_Caps_Lock_Instances.end(), this);
    if (it != PMMA::KeyEvent_Caps_Lock_Instances.end()) {
        PMMA::KeyEvent_Caps_Lock_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Scroll_Lock::CPP_KeyEvent_Scroll_Lock() {
    PMMA::KeyEvent_Scroll_Lock_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Scroll_Lock::~CPP_KeyEvent_Scroll_Lock() {
    auto it = find(PMMA::KeyEvent_Scroll_Lock_Instances.begin(), PMMA::KeyEvent_Scroll_Lock_Instances.end(), this);
    if (it != PMMA::KeyEvent_Scroll_Lock_Instances.end()) {
        PMMA::KeyEvent_Scroll_Lock_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Num_Lock::CPP_KeyEvent_Num_Lock() {
    PMMA::KeyEvent_Num_Lock_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Num_Lock::~CPP_KeyEvent_Num_Lock() {
    auto it = find(PMMA::KeyEvent_Num_Lock_Instances.begin(), PMMA::KeyEvent_Num_Lock_Instances.end(), this);
    if (it != PMMA::KeyEvent_Num_Lock_Instances.end()) {
        PMMA::KeyEvent_Num_Lock_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Print_Screen::CPP_KeyEvent_Print_Screen() {
    PMMA::KeyEvent_Print_Screen_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Print_Screen::~CPP_KeyEvent_Print_Screen() {
    auto it = find(PMMA::KeyEvent_Print_Screen_Instances.begin(), PMMA::KeyEvent_Print_Screen_Instances.end(), this);
    if (it != PMMA::KeyEvent_Print_Screen_Instances.end()) {
        PMMA::KeyEvent_Print_Screen_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Pause::CPP_KeyEvent_Pause() {
    PMMA::KeyEvent_Pause_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Pause::~CPP_KeyEvent_Pause() {
    auto it = find(PMMA::KeyEvent_Pause_Instances.begin(), PMMA::KeyEvent_Pause_Instances.end(), this);
    if (it != PMMA::KeyEvent_Pause_Instances.end()) {
        PMMA::KeyEvent_Pause_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F1::CPP_KeyEvent_F1() {
    PMMA::KeyEvent_F1_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F1::~CPP_KeyEvent_F1() {
    auto it = find(PMMA::KeyEvent_F1_Instances.begin(), PMMA::KeyEvent_F1_Instances.end(), this);
    if (it != PMMA::KeyEvent_F1_Instances.end()) {
        PMMA::KeyEvent_F1_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F2::CPP_KeyEvent_F2() {
    PMMA::KeyEvent_F2_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F2::~CPP_KeyEvent_F2() {
    auto it = find(PMMA::KeyEvent_F2_Instances.begin(), PMMA::KeyEvent_F2_Instances.end(), this);
    if (it != PMMA::KeyEvent_F2_Instances.end()) {
        PMMA::KeyEvent_F2_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F3::CPP_KeyEvent_F3() {
    PMMA::KeyEvent_F3_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F3::~CPP_KeyEvent_F3() {
    auto it = find(PMMA::KeyEvent_F3_Instances.begin(), PMMA::KeyEvent_F3_Instances.end(), this);
    if (it != PMMA::KeyEvent_F3_Instances.end()) {
        PMMA::KeyEvent_F3_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F4::CPP_KeyEvent_F4() {
    PMMA::KeyEvent_F4_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F4::~CPP_KeyEvent_F4() {
    auto it = find(PMMA::KeyEvent_F4_Instances.begin(), PMMA::KeyEvent_F4_Instances.end(), this);
    if (it != PMMA::KeyEvent_F4_Instances.end()) {
        PMMA::KeyEvent_F4_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F5::CPP_KeyEvent_F5() {
    PMMA::KeyEvent_F5_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F5::~CPP_KeyEvent_F5() {
    auto it = find(PMMA::KeyEvent_F5_Instances.begin(), PMMA::KeyEvent_F5_Instances.end(), this);
    if (it != PMMA::KeyEvent_F5_Instances.end()) {
        PMMA::KeyEvent_F5_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F6::CPP_KeyEvent_F6() {
    PMMA::KeyEvent_F6_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F6::~CPP_KeyEvent_F6() {
    auto it = find(PMMA::KeyEvent_F6_Instances.begin(), PMMA::KeyEvent_F6_Instances.end(), this);
    if (it != PMMA::KeyEvent_F6_Instances.end()) {
        PMMA::KeyEvent_F6_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F7::CPP_KeyEvent_F7() {
    PMMA::KeyEvent_F7_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F7::~CPP_KeyEvent_F7() {
    auto it = find(PMMA::KeyEvent_F7_Instances.begin(), PMMA::KeyEvent_F7_Instances.end(), this);
    if (it != PMMA::KeyEvent_F7_Instances.end()) {
        PMMA::KeyEvent_F7_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F8::CPP_KeyEvent_F8() {
    PMMA::KeyEvent_F8_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F8::~CPP_KeyEvent_F8() {
    auto it = find(PMMA::KeyEvent_F8_Instances.begin(), PMMA::KeyEvent_F8_Instances.end(), this);
    if (it != PMMA::KeyEvent_F8_Instances.end()) {
        PMMA::KeyEvent_F8_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F9::CPP_KeyEvent_F9() {
    PMMA::KeyEvent_F9_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F9::~CPP_KeyEvent_F9() {
    auto it = find(PMMA::KeyEvent_F9_Instances.begin(), PMMA::KeyEvent_F9_Instances.end(), this);
    if (it != PMMA::KeyEvent_F9_Instances.end()) {
        PMMA::KeyEvent_F9_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F10::CPP_KeyEvent_F10() {
    PMMA::KeyEvent_F10_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F10::~CPP_KeyEvent_F10() {
    auto it = find(PMMA::KeyEvent_F10_Instances.begin(), PMMA::KeyEvent_F10_Instances.end(), this);
    if (it != PMMA::KeyEvent_F10_Instances.end()) {
        PMMA::KeyEvent_F10_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F11::CPP_KeyEvent_F11() {
    PMMA::KeyEvent_F11_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F11::~CPP_KeyEvent_F11() {
    auto it = find(PMMA::KeyEvent_F11_Instances.begin(), PMMA::KeyEvent_F11_Instances.end(), this);
    if (it != PMMA::KeyEvent_F11_Instances.end()) {
        PMMA::KeyEvent_F11_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F12::CPP_KeyEvent_F12() {
    PMMA::KeyEvent_F12_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F12::~CPP_KeyEvent_F12() {
    auto it = find(PMMA::KeyEvent_F12_Instances.begin(), PMMA::KeyEvent_F12_Instances.end(), this);
    if (it != PMMA::KeyEvent_F12_Instances.end()) {
        PMMA::KeyEvent_F12_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F13::CPP_KeyEvent_F13() {
    PMMA::KeyEvent_F13_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F13::~CPP_KeyEvent_F13() {
    auto it = find(PMMA::KeyEvent_F13_Instances.begin(), PMMA::KeyEvent_F13_Instances.end(), this);
    if (it != PMMA::KeyEvent_F13_Instances.end()) {
        PMMA::KeyEvent_F13_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F14::CPP_KeyEvent_F14() {
    PMMA::KeyEvent_F14_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F14::~CPP_KeyEvent_F14() {
    auto it = find(PMMA::KeyEvent_F14_Instances.begin(), PMMA::KeyEvent_F14_Instances.end(), this);
    if (it != PMMA::KeyEvent_F14_Instances.end()) {
        PMMA::KeyEvent_F14_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F15::CPP_KeyEvent_F15() {
    PMMA::KeyEvent_F15_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F15::~CPP_KeyEvent_F15() {
    auto it = find(PMMA::KeyEvent_F15_Instances.begin(), PMMA::KeyEvent_F15_Instances.end(), this);
    if (it != PMMA::KeyEvent_F15_Instances.end()) {
        PMMA::KeyEvent_F15_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F16::CPP_KeyEvent_F16() {
    PMMA::KeyEvent_F16_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F16::~CPP_KeyEvent_F16() {
    auto it = find(PMMA::KeyEvent_F16_Instances.begin(), PMMA::KeyEvent_F16_Instances.end(), this);
    if (it != PMMA::KeyEvent_F16_Instances.end()) {
        PMMA::KeyEvent_F16_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F17::CPP_KeyEvent_F17() {
    PMMA::KeyEvent_F17_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F17::~CPP_KeyEvent_F17() {
    auto it = find(PMMA::KeyEvent_F17_Instances.begin(), PMMA::KeyEvent_F17_Instances.end(), this);
    if (it != PMMA::KeyEvent_F17_Instances.end()) {
        PMMA::KeyEvent_F17_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F18::CPP_KeyEvent_F18() {
    PMMA::KeyEvent_F18_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F18::~CPP_KeyEvent_F18() {
    auto it = find(PMMA::KeyEvent_F18_Instances.begin(), PMMA::KeyEvent_F18_Instances.end(), this);
    if (it != PMMA::KeyEvent_F18_Instances.end()) {
        PMMA::KeyEvent_F18_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F19::CPP_KeyEvent_F19() {
    PMMA::KeyEvent_F19_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F19::~CPP_KeyEvent_F19() {
    auto it = find(PMMA::KeyEvent_F19_Instances.begin(), PMMA::KeyEvent_F19_Instances.end(), this);
    if (it != PMMA::KeyEvent_F19_Instances.end()) {
        PMMA::KeyEvent_F19_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F20::CPP_KeyEvent_F20() {
    PMMA::KeyEvent_F20_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F20::~CPP_KeyEvent_F20() {
    auto it = find(PMMA::KeyEvent_F20_Instances.begin(), PMMA::KeyEvent_F20_Instances.end(), this);
    if (it != PMMA::KeyEvent_F20_Instances.end()) {
        PMMA::KeyEvent_F20_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F21::CPP_KeyEvent_F21() {
    PMMA::KeyEvent_F21_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F21::~CPP_KeyEvent_F21() {
    auto it = find(PMMA::KeyEvent_F21_Instances.begin(), PMMA::KeyEvent_F21_Instances.end(), this);
    if (it != PMMA::KeyEvent_F21_Instances.end()) {
        PMMA::KeyEvent_F21_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F22::CPP_KeyEvent_F22() {
    PMMA::KeyEvent_F22_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F22::~CPP_KeyEvent_F22() {
    auto it = find(PMMA::KeyEvent_F22_Instances.begin(), PMMA::KeyEvent_F22_Instances.end(), this);
    if (it != PMMA::KeyEvent_F22_Instances.end()) {
        PMMA::KeyEvent_F22_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F23::CPP_KeyEvent_F23() {
    PMMA::KeyEvent_F23_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F23::~CPP_KeyEvent_F23() {
    auto it = find(PMMA::KeyEvent_F23_Instances.begin(), PMMA::KeyEvent_F23_Instances.end(), this);
    if (it != PMMA::KeyEvent_F23_Instances.end()) {
        PMMA::KeyEvent_F23_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F24::CPP_KeyEvent_F24() {
    PMMA::KeyEvent_F24_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F24::~CPP_KeyEvent_F24() {
    auto it = find(PMMA::KeyEvent_F24_Instances.begin(), PMMA::KeyEvent_F24_Instances.end(), this);
    if (it != PMMA::KeyEvent_F24_Instances.end()) {
        PMMA::KeyEvent_F24_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F25::CPP_KeyEvent_F25() {
    PMMA::KeyEvent_F25_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F25::~CPP_KeyEvent_F25() {
    auto it = find(PMMA::KeyEvent_F25_Instances.begin(), PMMA::KeyEvent_F25_Instances.end(), this);
    if (it != PMMA::KeyEvent_F25_Instances.end()) {
        PMMA::KeyEvent_F25_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Left_Shift::CPP_KeyEvent_Left_Shift() {
    PMMA::KeyEvent_Left_Shift_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Left_Shift::~CPP_KeyEvent_Left_Shift() {
    auto it = find(PMMA::KeyEvent_Left_Shift_Instances.begin(), PMMA::KeyEvent_Left_Shift_Instances.end(), this);
    if (it != PMMA::KeyEvent_Left_Shift_Instances.end()) {
        PMMA::KeyEvent_Left_Shift_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Left_Control::CPP_KeyEvent_Left_Control() {
    PMMA::KeyEvent_Left_Control_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Left_Control::~CPP_KeyEvent_Left_Control() {
    auto it = find(PMMA::KeyEvent_Left_Control_Instances.begin(), PMMA::KeyEvent_Left_Control_Instances.end(), this);
    if (it != PMMA::KeyEvent_Left_Control_Instances.end()) {
        PMMA::KeyEvent_Left_Control_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Left_Alt::CPP_KeyEvent_Left_Alt() {
    PMMA::KeyEvent_Left_Alt_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Left_Alt::~CPP_KeyEvent_Left_Alt() {
    auto it = find(PMMA::KeyEvent_Left_Alt_Instances.begin(), PMMA::KeyEvent_Left_Alt_Instances.end(), this);
    if (it != PMMA::KeyEvent_Left_Alt_Instances.end()) {
        PMMA::KeyEvent_Left_Alt_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Left_Super::CPP_KeyEvent_Left_Super() {
    PMMA::KeyEvent_Left_Super_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Left_Super::~CPP_KeyEvent_Left_Super() {
    auto it = find(PMMA::KeyEvent_Left_Super_Instances.begin(), PMMA::KeyEvent_Left_Super_Instances.end(), this);
    if (it != PMMA::KeyEvent_Left_Super_Instances.end()) {
        PMMA::KeyEvent_Left_Super_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Right_Shift::CPP_KeyEvent_Right_Shift() {
    PMMA::KeyEvent_Right_Shift_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Right_Shift::~CPP_KeyEvent_Right_Shift() {
    auto it = find(PMMA::KeyEvent_Right_Shift_Instances.begin(), PMMA::KeyEvent_Right_Shift_Instances.end(), this);
    if (it != PMMA::KeyEvent_Right_Shift_Instances.end()) {
        PMMA::KeyEvent_Right_Shift_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Right_Control::CPP_KeyEvent_Right_Control() {
    PMMA::KeyEvent_Right_Control_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Right_Control::~CPP_KeyEvent_Right_Control() {
    auto it = find(PMMA::KeyEvent_Right_Control_Instances.begin(), PMMA::KeyEvent_Right_Control_Instances.end(), this);
    if (it != PMMA::KeyEvent_Right_Control_Instances.end()) {
        PMMA::KeyEvent_Right_Control_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Right_Alt::CPP_KeyEvent_Right_Alt() {
    PMMA::KeyEvent_Right_Alt_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Right_Alt::~CPP_KeyEvent_Right_Alt() {
    auto it = find(PMMA::KeyEvent_Right_Alt_Instances.begin(), PMMA::KeyEvent_Right_Alt_Instances.end(), this);
    if (it != PMMA::KeyEvent_Right_Alt_Instances.end()) {
        PMMA::KeyEvent_Right_Alt_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Right_Super::CPP_KeyEvent_Right_Super() {
    PMMA::KeyEvent_Right_Super_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Right_Super::~CPP_KeyEvent_Right_Super() {
    auto it = find(PMMA::KeyEvent_Right_Super_Instances.begin(), PMMA::KeyEvent_Right_Super_Instances.end(), this);
    if (it != PMMA::KeyEvent_Right_Super_Instances.end()) {
        PMMA::KeyEvent_Right_Super_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Shift::CPP_KeyEvent_Shift() {
    PMMA::KeyEvent_Shift_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Shift::~CPP_KeyEvent_Shift() {
    auto it = find(PMMA::KeyEvent_Shift_Instances.begin(), PMMA::KeyEvent_Shift_Instances.end(), this);
    if (it != PMMA::KeyEvent_Shift_Instances.end()) {
        PMMA::KeyEvent_Shift_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Control::CPP_KeyEvent_Control() {
    PMMA::KeyEvent_Control_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Control::~CPP_KeyEvent_Control() {
    auto it = find(PMMA::KeyEvent_Control_Instances.begin(), PMMA::KeyEvent_Control_Instances.end(), this);
    if (it != PMMA::KeyEvent_Control_Instances.end()) {
        PMMA::KeyEvent_Control_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Alt::CPP_KeyEvent_Alt() {
    PMMA::KeyEvent_Alt_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Alt::~CPP_KeyEvent_Alt() {
    auto it = find(PMMA::KeyEvent_Alt_Instances.begin(), PMMA::KeyEvent_Alt_Instances.end(), this);
    if (it != PMMA::KeyEvent_Alt_Instances.end()) {
        PMMA::KeyEvent_Alt_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Super::CPP_KeyEvent_Super() {
    PMMA::KeyEvent_Super_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Super::~CPP_KeyEvent_Super() {
    auto it = find(PMMA::KeyEvent_Super_Instances.begin(), PMMA::KeyEvent_Super_Instances.end(), this);
    if (it != PMMA::KeyEvent_Super_Instances.end()) {
        PMMA::KeyEvent_Super_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Menu::CPP_KeyEvent_Menu() {
    PMMA::KeyEvent_Menu_Instances.push_back(this);

    PMMA::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Menu::~CPP_KeyEvent_Menu() {
    auto it = find(PMMA::KeyEvent_Menu_Instances.begin(), PMMA::KeyEvent_Menu_Instances.end(), this);
    if (it != PMMA::KeyEvent_Menu_Instances.end()) {
        PMMA::KeyEvent_Menu_Instances.erase(it);
    }

    PMMA::KeyboardEventInstanceCount--;
};