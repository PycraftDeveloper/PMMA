#include "PMMA_Core.hpp"

PMMA::Events::Key_Space::Key_Space() {
    PMMA::Core::KeyEvent_Space_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_Space::~Key_Space() {
    auto it = find(PMMA::Core::KeyEvent_Space_Instances.begin(), PMMA::Core::KeyEvent_Space_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Space_Instances.end()) {
        PMMA::Core::KeyEvent_Space_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_Apostrophe::Key_Apostrophe() {
    PMMA::Core::KeyEvent_Apostrophe_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_Apostrophe::~Key_Apostrophe() {
    auto it = find(PMMA::Core::KeyEvent_Apostrophe_Instances.begin(), PMMA::Core::KeyEvent_Apostrophe_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Apostrophe_Instances.end()) {
        PMMA::Core::KeyEvent_Apostrophe_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_Comma::Key_Comma() {
    PMMA::Core::KeyEvent_Comma_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_Comma::~Key_Comma() {
    auto it = find(PMMA::Core::KeyEvent_Comma_Instances.begin(), PMMA::Core::KeyEvent_Comma_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Comma_Instances.end()) {
        PMMA::Core::KeyEvent_Comma_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_Minus::Key_Minus() {
    PMMA::Core::KeyEvent_Minus_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_Minus::~Key_Minus() {
    auto it = find(PMMA::Core::KeyEvent_Minus_Instances.begin(), PMMA::Core::KeyEvent_Minus_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Minus_Instances.end()) {
        PMMA::Core::KeyEvent_Minus_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_Period::Key_Period() {
    PMMA::Core::KeyEvent_Period_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_Period::~Key_Period() {
    auto it = find(PMMA::Core::KeyEvent_Period_Instances.begin(), PMMA::Core::KeyEvent_Period_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Period_Instances.end()) {
        PMMA::Core::KeyEvent_Period_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_Slash::Key_Slash() {
    PMMA::Core::KeyEvent_Slash_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_Slash::~Key_Slash() {
    auto it = find(PMMA::Core::KeyEvent_Slash_Instances.begin(), PMMA::Core::KeyEvent_Slash_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Slash_Instances.end()) {
        PMMA::Core::KeyEvent_Slash_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_0::Key_0() {
    PMMA::Core::KeyEvent_0_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_0::~Key_0() {
    auto it = find(PMMA::Core::KeyEvent_0_Instances.begin(), PMMA::Core::KeyEvent_0_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_0_Instances.end()) {
        PMMA::Core::KeyEvent_0_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_1::Key_1() {
    PMMA::Core::KeyEvent_1_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_1::~Key_1() {
    auto it = find(PMMA::Core::KeyEvent_1_Instances.begin(), PMMA::Core::KeyEvent_1_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_1_Instances.end()) {
        PMMA::Core::KeyEvent_1_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_2::Key_2() {
    PMMA::Core::KeyEvent_2_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_2::~Key_2() {
    auto it = find(PMMA::Core::KeyEvent_2_Instances.begin(), PMMA::Core::KeyEvent_2_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_2_Instances.end()) {
        PMMA::Core::KeyEvent_2_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_3::Key_3() {
    PMMA::Core::KeyEvent_3_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_3::~Key_3() {
    auto it = find(PMMA::Core::KeyEvent_3_Instances.begin(), PMMA::Core::KeyEvent_3_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_3_Instances.end()) {
        PMMA::Core::KeyEvent_3_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_4::Key_4() {
    PMMA::Core::KeyEvent_4_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_4::~Key_4() {
    auto it = find(PMMA::Core::KeyEvent_4_Instances.begin(), PMMA::Core::KeyEvent_4_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_4_Instances.end()) {
        PMMA::Core::KeyEvent_4_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_5::Key_5() {
    PMMA::Core::KeyEvent_5_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_5::~Key_5() {
    auto it = find(PMMA::Core::KeyEvent_5_Instances.begin(), PMMA::Core::KeyEvent_5_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_5_Instances.end()) {
        PMMA::Core::KeyEvent_5_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_6::Key_6() {
    PMMA::Core::KeyEvent_6_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_6::~Key_6() {
    auto it = find(PMMA::Core::KeyEvent_6_Instances.begin(), PMMA::Core::KeyEvent_6_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_6_Instances.end()) {
        PMMA::Core::KeyEvent_6_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_7::Key_7() {
    PMMA::Core::KeyEvent_7_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_7::~Key_7() {
    auto it = find(PMMA::Core::KeyEvent_7_Instances.begin(), PMMA::Core::KeyEvent_7_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_7_Instances.end()) {
        PMMA::Core::KeyEvent_7_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_8::Key_8() {
    PMMA::Core::KeyEvent_8_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_8::~Key_8() {
    auto it = find(PMMA::Core::KeyEvent_8_Instances.begin(), PMMA::Core::KeyEvent_8_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_8_Instances.end()) {
        PMMA::Core::KeyEvent_8_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_9::Key_9() {
    PMMA::Core::KeyEvent_9_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_9::~Key_9() {
    auto it = find(PMMA::Core::KeyEvent_9_Instances.begin(), PMMA::Core::KeyEvent_9_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_9_Instances.end()) {
        PMMA::Core::KeyEvent_9_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_Semicolon::Key_Semicolon() {
    PMMA::Core::KeyEvent_Semicolon_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_Semicolon::~Key_Semicolon() {
    auto it = find(PMMA::Core::KeyEvent_Semicolon_Instances.begin(), PMMA::Core::KeyEvent_Semicolon_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Semicolon_Instances.end()) {
        PMMA::Core::KeyEvent_Semicolon_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_Equal::Key_Equal() {
    PMMA::Core::KeyEvent_Equal_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_Equal::~Key_Equal() {
    auto it = find(PMMA::Core::KeyEvent_Equal_Instances.begin(), PMMA::Core::KeyEvent_Equal_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Equal_Instances.end()) {
        PMMA::Core::KeyEvent_Equal_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_A::Key_A() {
    PMMA::Core::KeyEvent_A_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_A::~Key_A() {
    auto it = find(PMMA::Core::KeyEvent_A_Instances.begin(), PMMA::Core::KeyEvent_A_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_A_Instances.end()) {
        PMMA::Core::KeyEvent_A_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_B::Key_B() {
    PMMA::Core::KeyEvent_B_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_B::~Key_B() {
    auto it = find(PMMA::Core::KeyEvent_B_Instances.begin(), PMMA::Core::KeyEvent_B_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_B_Instances.end()) {
        PMMA::Core::KeyEvent_B_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_C::Key_C() {
    PMMA::Core::KeyEvent_C_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_C::~Key_C() {
    auto it = find(PMMA::Core::KeyEvent_C_Instances.begin(), PMMA::Core::KeyEvent_C_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_C_Instances.end()) {
        PMMA::Core::KeyEvent_C_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_D::Key_D() {
    PMMA::Core::KeyEvent_D_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_D::~Key_D() {
    auto it = find(PMMA::Core::KeyEvent_D_Instances.begin(), PMMA::Core::KeyEvent_D_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_D_Instances.end()) {
        PMMA::Core::KeyEvent_D_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_E::Key_E() {
    PMMA::Core::KeyEvent_E_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_E::~Key_E() {
    auto it = find(PMMA::Core::KeyEvent_E_Instances.begin(), PMMA::Core::KeyEvent_E_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_E_Instances.end()) {
        PMMA::Core::KeyEvent_E_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_F::Key_F() {
    PMMA::Core::KeyEvent_F_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_F::~Key_F() {
    auto it = find(PMMA::Core::KeyEvent_F_Instances.begin(), PMMA::Core::KeyEvent_F_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F_Instances.end()) {
        PMMA::Core::KeyEvent_F_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_G::Key_G() {
    PMMA::Core::KeyEvent_G_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_G::~Key_G() {
    auto it = find(PMMA::Core::KeyEvent_G_Instances.begin(), PMMA::Core::KeyEvent_G_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_G_Instances.end()) {
        PMMA::Core::KeyEvent_G_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_H::Key_H() {
    PMMA::Core::KeyEvent_H_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_H::~Key_H() {
    auto it = find(PMMA::Core::KeyEvent_H_Instances.begin(), PMMA::Core::KeyEvent_H_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_H_Instances.end()) {
        PMMA::Core::KeyEvent_H_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_I::Key_I() {
    PMMA::Core::KeyEvent_I_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_I::~Key_I() {
    auto it = find(PMMA::Core::KeyEvent_I_Instances.begin(), PMMA::Core::KeyEvent_I_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_I_Instances.end()) {
        PMMA::Core::KeyEvent_I_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_J::Key_J() {
    PMMA::Core::KeyEvent_J_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_J::~Key_J() {
    auto it = find(PMMA::Core::KeyEvent_J_Instances.begin(), PMMA::Core::KeyEvent_J_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_J_Instances.end()) {
        PMMA::Core::KeyEvent_J_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_K::Key_K() {
    PMMA::Core::KeyEvent_K_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_K::~Key_K() {
    auto it = find(PMMA::Core::KeyEvent_K_Instances.begin(), PMMA::Core::KeyEvent_K_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_K_Instances.end()) {
        PMMA::Core::KeyEvent_K_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_L::Key_L() {
    PMMA::Core::KeyEvent_L_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_L::~Key_L() {
    auto it = find(PMMA::Core::KeyEvent_L_Instances.begin(), PMMA::Core::KeyEvent_L_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_L_Instances.end()) {
        PMMA::Core::KeyEvent_L_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_M::Key_M() {
    PMMA::Core::KeyEvent_M_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_M::~Key_M() {
    auto it = find(PMMA::Core::KeyEvent_M_Instances.begin(), PMMA::Core::KeyEvent_M_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_M_Instances.end()) {
        PMMA::Core::KeyEvent_M_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_N::Key_N() {
    PMMA::Core::KeyEvent_N_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_N::~Key_N() {
    auto it = find(PMMA::Core::KeyEvent_N_Instances.begin(), PMMA::Core::KeyEvent_N_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_N_Instances.end()) {
        PMMA::Core::KeyEvent_N_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_O::Key_O() {
    PMMA::Core::KeyEvent_O_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_O::~Key_O() {
    auto it = find(PMMA::Core::KeyEvent_O_Instances.begin(), PMMA::Core::KeyEvent_O_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_O_Instances.end()) {
        PMMA::Core::KeyEvent_O_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_P::Key_P() {
    PMMA::Core::KeyEvent_P_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_P::~Key_P() {
    auto it = find(PMMA::Core::KeyEvent_P_Instances.begin(), PMMA::Core::KeyEvent_P_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_P_Instances.end()) {
        PMMA::Core::KeyEvent_P_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_Q::Key_Q() {
    PMMA::Core::KeyEvent_Q_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_Q::~Key_Q() {
    auto it = find(PMMA::Core::KeyEvent_Q_Instances.begin(), PMMA::Core::KeyEvent_Q_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Q_Instances.end()) {
        PMMA::Core::KeyEvent_Q_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_R::Key_R() {
    PMMA::Core::KeyEvent_R_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_R::~Key_R() {
    auto it = find(PMMA::Core::KeyEvent_R_Instances.begin(), PMMA::Core::KeyEvent_R_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_R_Instances.end()) {
        PMMA::Core::KeyEvent_R_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_S::Key_S() {
    PMMA::Core::KeyEvent_S_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_S::~Key_S() {
    auto it = find(PMMA::Core::KeyEvent_S_Instances.begin(), PMMA::Core::KeyEvent_S_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_S_Instances.end()) {
        PMMA::Core::KeyEvent_S_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_T::Key_T() {
    PMMA::Core::KeyEvent_T_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_T::~Key_T() {
    auto it = find(PMMA::Core::KeyEvent_T_Instances.begin(), PMMA::Core::KeyEvent_T_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_T_Instances.end()) {
        PMMA::Core::KeyEvent_T_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_U::Key_U() {
    PMMA::Core::KeyEvent_U_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_U::~Key_U() {
    auto it = find(PMMA::Core::KeyEvent_U_Instances.begin(), PMMA::Core::KeyEvent_U_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_U_Instances.end()) {
        PMMA::Core::KeyEvent_U_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_V::Key_V() {
    PMMA::Core::KeyEvent_V_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_V::~Key_V() {
    auto it = find(PMMA::Core::KeyEvent_V_Instances.begin(), PMMA::Core::KeyEvent_V_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_V_Instances.end()) {
        PMMA::Core::KeyEvent_V_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_W::Key_W() {
    PMMA::Core::KeyEvent_W_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_W::~Key_W() {
    auto it = find(PMMA::Core::KeyEvent_W_Instances.begin(), PMMA::Core::KeyEvent_W_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_W_Instances.end()) {
        PMMA::Core::KeyEvent_W_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_X::Key_X() {
    PMMA::Core::KeyEvent_X_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_X::~Key_X() {
    auto it = find(PMMA::Core::KeyEvent_X_Instances.begin(), PMMA::Core::KeyEvent_X_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_X_Instances.end()) {
        PMMA::Core::KeyEvent_X_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_Y::Key_Y() {
    PMMA::Core::KeyEvent_Y_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_Y::~Key_Y() {
    auto it = find(PMMA::Core::KeyEvent_Y_Instances.begin(), PMMA::Core::KeyEvent_Y_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Y_Instances.end()) {
        PMMA::Core::KeyEvent_Y_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_Z::Key_Z() {
    PMMA::Core::KeyEvent_Z_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_Z::~Key_Z() {
    auto it = find(PMMA::Core::KeyEvent_Z_Instances.begin(), PMMA::Core::KeyEvent_Z_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Z_Instances.end()) {
        PMMA::Core::KeyEvent_Z_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_Left_Bracket::Key_Left_Bracket() {
    PMMA::Core::KeyEvent_Left_Bracket_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_Left_Bracket::~Key_Left_Bracket() {
    auto it = find(PMMA::Core::KeyEvent_Left_Bracket_Instances.begin(), PMMA::Core::KeyEvent_Left_Bracket_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Left_Bracket_Instances.end()) {
        PMMA::Core::KeyEvent_Left_Bracket_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_Backslash::Key_Backslash() {
    PMMA::Core::KeyEvent_Backslash_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_Backslash::~Key_Backslash() {
    auto it = find(PMMA::Core::KeyEvent_Backslash_Instances.begin(), PMMA::Core::KeyEvent_Backslash_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Backslash_Instances.end()) {
        PMMA::Core::KeyEvent_Backslash_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_Right_Bracket::Key_Right_Bracket() {
    PMMA::Core::KeyEvent_Right_Bracket_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_Right_Bracket::~Key_Right_Bracket() {
    auto it = find(PMMA::Core::KeyEvent_Right_Bracket_Instances.begin(), PMMA::Core::KeyEvent_Right_Bracket_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Right_Bracket_Instances.end()) {
        PMMA::Core::KeyEvent_Right_Bracket_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_Grave_Accent::Key_Grave_Accent() {
    PMMA::Core::KeyEvent_Grave_Accent_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_Grave_Accent::~Key_Grave_Accent() {
    auto it = find(PMMA::Core::KeyEvent_Grave_Accent_Instances.begin(), PMMA::Core::KeyEvent_Grave_Accent_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Grave_Accent_Instances.end()) {
        PMMA::Core::KeyEvent_Grave_Accent_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_World_1::Key_World_1() {
    PMMA::Core::KeyEvent_World_1_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_World_1::~Key_World_1() {
    auto it = find(PMMA::Core::KeyEvent_World_1_Instances.begin(), PMMA::Core::KeyEvent_World_1_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_World_1_Instances.end()) {
        PMMA::Core::KeyEvent_World_1_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_World_2::Key_World_2() {
    PMMA::Core::KeyEvent_World_2_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

PMMA::Events::Key_World_2::~Key_World_2() {
    auto it = find(PMMA::Core::KeyEvent_World_2_Instances.begin(), PMMA::Core::KeyEvent_World_2_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_World_2_Instances.end()) {
        PMMA::Core::KeyEvent_World_2_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

PMMA::Events::Key_Escape::Key_Escape() {
    PMMA::Core::KeyEvent_Escape_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Escape::~Key_Escape() {
    auto it = find(PMMA::Core::KeyEvent_Escape_Instances.begin(), PMMA::Core::KeyEvent_Escape_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Escape_Instances.end()) {
        PMMA::Core::KeyEvent_Escape_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Enter::Key_Enter() {
    PMMA::Core::KeyEvent_Enter_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Enter::~Key_Enter() {
    auto it = find(PMMA::Core::KeyEvent_Enter_Instances.begin(), PMMA::Core::KeyEvent_Enter_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Enter_Instances.end()) {
        PMMA::Core::KeyEvent_Enter_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Tab::Key_Tab() {
    PMMA::Core::KeyEvent_Tab_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Tab::~Key_Tab() {
    auto it = find(PMMA::Core::KeyEvent_Tab_Instances.begin(), PMMA::Core::KeyEvent_Tab_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Tab_Instances.end()) {
        PMMA::Core::KeyEvent_Tab_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Backspace::Key_Backspace() {
    PMMA::Core::KeyEvent_Backspace_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Backspace::~Key_Backspace() {
    auto it = find(PMMA::Core::KeyEvent_Backspace_Instances.begin(), PMMA::Core::KeyEvent_Backspace_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Backspace_Instances.end()) {
        PMMA::Core::KeyEvent_Backspace_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Insert::Key_Insert() {
    PMMA::Core::KeyEvent_Insert_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Insert::~Key_Insert() {
    auto it = find(PMMA::Core::KeyEvent_Insert_Instances.begin(), PMMA::Core::KeyEvent_Insert_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Insert_Instances.end()) {
        PMMA::Core::KeyEvent_Insert_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Delete::Key_Delete() {
    PMMA::Core::KeyEvent_Delete_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Delete::~Key_Delete() {
    auto it = find(PMMA::Core::KeyEvent_Delete_Instances.begin(), PMMA::Core::KeyEvent_Delete_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Delete_Instances.end()) {
        PMMA::Core::KeyEvent_Delete_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Right::Key_Right() {
    PMMA::Core::KeyEvent_Right_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Right::~Key_Right() {
    auto it = find(PMMA::Core::KeyEvent_Right_Instances.begin(), PMMA::Core::KeyEvent_Right_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Right_Instances.end()) {
        PMMA::Core::KeyEvent_Right_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Left::Key_Left() {
    PMMA::Core::KeyEvent_Left_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Left::~Key_Left() {
    auto it = find(PMMA::Core::KeyEvent_Left_Instances.begin(), PMMA::Core::KeyEvent_Left_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Left_Instances.end()) {
        PMMA::Core::KeyEvent_Left_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Down::Key_Down() {
    PMMA::Core::KeyEvent_Down_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Down::~Key_Down() {
    auto it = find(PMMA::Core::KeyEvent_Down_Instances.begin(), PMMA::Core::KeyEvent_Down_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Down_Instances.end()) {
        PMMA::Core::KeyEvent_Down_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Up::Key_Up() {
    PMMA::Core::KeyEvent_Up_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Up::~Key_Up() {
    auto it = find(PMMA::Core::KeyEvent_Up_Instances.begin(), PMMA::Core::KeyEvent_Up_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Up_Instances.end()) {
        PMMA::Core::KeyEvent_Up_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Page_Up::Key_Page_Up() {
    PMMA::Core::KeyEvent_Page_Up_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Page_Up::~Key_Page_Up() {
    auto it = find(PMMA::Core::KeyEvent_Page_Up_Instances.begin(), PMMA::Core::KeyEvent_Page_Up_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Page_Up_Instances.end()) {
        PMMA::Core::KeyEvent_Page_Up_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Page_Down::Key_Page_Down() {
    PMMA::Core::KeyEvent_Page_Down_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Page_Down::~Key_Page_Down() {
    auto it = find(PMMA::Core::KeyEvent_Page_Down_Instances.begin(), PMMA::Core::KeyEvent_Page_Down_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Page_Down_Instances.end()) {
        PMMA::Core::KeyEvent_Page_Down_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Home::Key_Home() {
    PMMA::Core::KeyEvent_Home_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Home::~Key_Home() {
    auto it = find(PMMA::Core::KeyEvent_Home_Instances.begin(), PMMA::Core::KeyEvent_Home_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Home_Instances.end()) {
        PMMA::Core::KeyEvent_Home_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_End::Key_End() {
    PMMA::Core::KeyEvent_End_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_End::~Key_End() {
    auto it = find(PMMA::Core::KeyEvent_End_Instances.begin(), PMMA::Core::KeyEvent_End_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_End_Instances.end()) {
        PMMA::Core::KeyEvent_End_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Caps_Lock::Key_Caps_Lock() {
    PMMA::Core::KeyEvent_Caps_Lock_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Caps_Lock::~Key_Caps_Lock() {
    auto it = find(PMMA::Core::KeyEvent_Caps_Lock_Instances.begin(), PMMA::Core::KeyEvent_Caps_Lock_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Caps_Lock_Instances.end()) {
        PMMA::Core::KeyEvent_Caps_Lock_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Scroll_Lock::Key_Scroll_Lock() {
    PMMA::Core::KeyEvent_Scroll_Lock_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Scroll_Lock::~Key_Scroll_Lock() {
    auto it = find(PMMA::Core::KeyEvent_Scroll_Lock_Instances.begin(), PMMA::Core::KeyEvent_Scroll_Lock_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Scroll_Lock_Instances.end()) {
        PMMA::Core::KeyEvent_Scroll_Lock_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Num_Lock::Key_Num_Lock() {
    PMMA::Core::KeyEvent_Num_Lock_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Num_Lock::~Key_Num_Lock() {
    auto it = find(PMMA::Core::KeyEvent_Num_Lock_Instances.begin(), PMMA::Core::KeyEvent_Num_Lock_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Num_Lock_Instances.end()) {
        PMMA::Core::KeyEvent_Num_Lock_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Print_Screen::Key_Print_Screen() {
    PMMA::Core::KeyEvent_Print_Screen_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Print_Screen::~Key_Print_Screen() {
    auto it = find(PMMA::Core::KeyEvent_Print_Screen_Instances.begin(), PMMA::Core::KeyEvent_Print_Screen_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Print_Screen_Instances.end()) {
        PMMA::Core::KeyEvent_Print_Screen_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Pause::Key_Pause() {
    PMMA::Core::KeyEvent_Pause_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Pause::~Key_Pause() {
    auto it = find(PMMA::Core::KeyEvent_Pause_Instances.begin(), PMMA::Core::KeyEvent_Pause_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Pause_Instances.end()) {
        PMMA::Core::KeyEvent_Pause_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F1::Key_F1() {
    PMMA::Core::KeyEvent_F1_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F1::~Key_F1() {
    auto it = find(PMMA::Core::KeyEvent_F1_Instances.begin(), PMMA::Core::KeyEvent_F1_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F1_Instances.end()) {
        PMMA::Core::KeyEvent_F1_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F2::Key_F2() {
    PMMA::Core::KeyEvent_F2_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F2::~Key_F2() {
    auto it = find(PMMA::Core::KeyEvent_F2_Instances.begin(), PMMA::Core::KeyEvent_F2_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F2_Instances.end()) {
        PMMA::Core::KeyEvent_F2_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F3::Key_F3() {
    PMMA::Core::KeyEvent_F3_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F3::~Key_F3() {
    auto it = find(PMMA::Core::KeyEvent_F3_Instances.begin(), PMMA::Core::KeyEvent_F3_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F3_Instances.end()) {
        PMMA::Core::KeyEvent_F3_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F4::Key_F4() {
    PMMA::Core::KeyEvent_F4_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F4::~Key_F4() {
    auto it = find(PMMA::Core::KeyEvent_F4_Instances.begin(), PMMA::Core::KeyEvent_F4_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F4_Instances.end()) {
        PMMA::Core::KeyEvent_F4_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F5::Key_F5() {
    PMMA::Core::KeyEvent_F5_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F5::~Key_F5() {
    auto it = find(PMMA::Core::KeyEvent_F5_Instances.begin(), PMMA::Core::KeyEvent_F5_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F5_Instances.end()) {
        PMMA::Core::KeyEvent_F5_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F6::Key_F6() {
    PMMA::Core::KeyEvent_F6_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F6::~Key_F6() {
    auto it = find(PMMA::Core::KeyEvent_F6_Instances.begin(), PMMA::Core::KeyEvent_F6_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F6_Instances.end()) {
        PMMA::Core::KeyEvent_F6_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F7::Key_F7() {
    PMMA::Core::KeyEvent_F7_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F7::~Key_F7() {
    auto it = find(PMMA::Core::KeyEvent_F7_Instances.begin(), PMMA::Core::KeyEvent_F7_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F7_Instances.end()) {
        PMMA::Core::KeyEvent_F7_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F8::Key_F8() {
    PMMA::Core::KeyEvent_F8_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F8::~Key_F8() {
    auto it = find(PMMA::Core::KeyEvent_F8_Instances.begin(), PMMA::Core::KeyEvent_F8_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F8_Instances.end()) {
        PMMA::Core::KeyEvent_F8_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F9::Key_F9() {
    PMMA::Core::KeyEvent_F9_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F9::~Key_F9() {
    auto it = find(PMMA::Core::KeyEvent_F9_Instances.begin(), PMMA::Core::KeyEvent_F9_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F9_Instances.end()) {
        PMMA::Core::KeyEvent_F9_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F10::Key_F10() {
    PMMA::Core::KeyEvent_F10_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F10::~Key_F10() {
    auto it = find(PMMA::Core::KeyEvent_F10_Instances.begin(), PMMA::Core::KeyEvent_F10_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F10_Instances.end()) {
        PMMA::Core::KeyEvent_F10_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F11::Key_F11() {
    PMMA::Core::KeyEvent_F11_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F11::~Key_F11() {
    auto it = find(PMMA::Core::KeyEvent_F11_Instances.begin(), PMMA::Core::KeyEvent_F11_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F11_Instances.end()) {
        PMMA::Core::KeyEvent_F11_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F12::Key_F12() {
    PMMA::Core::KeyEvent_F12_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F12::~Key_F12() {
    auto it = find(PMMA::Core::KeyEvent_F12_Instances.begin(), PMMA::Core::KeyEvent_F12_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F12_Instances.end()) {
        PMMA::Core::KeyEvent_F12_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F13::Key_F13() {
    PMMA::Core::KeyEvent_F13_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F13::~Key_F13() {
    auto it = find(PMMA::Core::KeyEvent_F13_Instances.begin(), PMMA::Core::KeyEvent_F13_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F13_Instances.end()) {
        PMMA::Core::KeyEvent_F13_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F14::Key_F14() {
    PMMA::Core::KeyEvent_F14_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F14::~Key_F14() {
    auto it = find(PMMA::Core::KeyEvent_F14_Instances.begin(), PMMA::Core::KeyEvent_F14_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F14_Instances.end()) {
        PMMA::Core::KeyEvent_F14_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F15::Key_F15() {
    PMMA::Core::KeyEvent_F15_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F15::~Key_F15() {
    auto it = find(PMMA::Core::KeyEvent_F15_Instances.begin(), PMMA::Core::KeyEvent_F15_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F15_Instances.end()) {
        PMMA::Core::KeyEvent_F15_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F16::Key_F16() {
    PMMA::Core::KeyEvent_F16_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F16::~Key_F16() {
    auto it = find(PMMA::Core::KeyEvent_F16_Instances.begin(), PMMA::Core::KeyEvent_F16_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F16_Instances.end()) {
        PMMA::Core::KeyEvent_F16_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F17::Key_F17() {
    PMMA::Core::KeyEvent_F17_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F17::~Key_F17() {
    auto it = find(PMMA::Core::KeyEvent_F17_Instances.begin(), PMMA::Core::KeyEvent_F17_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F17_Instances.end()) {
        PMMA::Core::KeyEvent_F17_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F18::Key_F18() {
    PMMA::Core::KeyEvent_F18_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F18::~Key_F18() {
    auto it = find(PMMA::Core::KeyEvent_F18_Instances.begin(), PMMA::Core::KeyEvent_F18_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F18_Instances.end()) {
        PMMA::Core::KeyEvent_F18_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F19::Key_F19() {
    PMMA::Core::KeyEvent_F19_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F19::~Key_F19() {
    auto it = find(PMMA::Core::KeyEvent_F19_Instances.begin(), PMMA::Core::KeyEvent_F19_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F19_Instances.end()) {
        PMMA::Core::KeyEvent_F19_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F20::Key_F20() {
    PMMA::Core::KeyEvent_F20_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F20::~Key_F20() {
    auto it = find(PMMA::Core::KeyEvent_F20_Instances.begin(), PMMA::Core::KeyEvent_F20_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F20_Instances.end()) {
        PMMA::Core::KeyEvent_F20_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F21::Key_F21() {
    PMMA::Core::KeyEvent_F21_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F21::~Key_F21() {
    auto it = find(PMMA::Core::KeyEvent_F21_Instances.begin(), PMMA::Core::KeyEvent_F21_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F21_Instances.end()) {
        PMMA::Core::KeyEvent_F21_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F22::Key_F22() {
    PMMA::Core::KeyEvent_F22_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F22::~Key_F22() {
    auto it = find(PMMA::Core::KeyEvent_F22_Instances.begin(), PMMA::Core::KeyEvent_F22_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F22_Instances.end()) {
        PMMA::Core::KeyEvent_F22_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F23::Key_F23() {
    PMMA::Core::KeyEvent_F23_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F23::~Key_F23() {
    auto it = find(PMMA::Core::KeyEvent_F23_Instances.begin(), PMMA::Core::KeyEvent_F23_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F23_Instances.end()) {
        PMMA::Core::KeyEvent_F23_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F24::Key_F24() {
    PMMA::Core::KeyEvent_F24_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F24::~Key_F24() {
    auto it = find(PMMA::Core::KeyEvent_F24_Instances.begin(), PMMA::Core::KeyEvent_F24_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F24_Instances.end()) {
        PMMA::Core::KeyEvent_F24_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_F25::Key_F25() {
    PMMA::Core::KeyEvent_F25_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_F25::~Key_F25() {
    auto it = find(PMMA::Core::KeyEvent_F25_Instances.begin(), PMMA::Core::KeyEvent_F25_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_F25_Instances.end()) {
        PMMA::Core::KeyEvent_F25_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Left_Shift::Key_Left_Shift() {
    PMMA::Core::KeyEvent_Left_Shift_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Left_Shift::~Key_Left_Shift() {
    auto it = find(PMMA::Core::KeyEvent_Left_Shift_Instances.begin(), PMMA::Core::KeyEvent_Left_Shift_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Left_Shift_Instances.end()) {
        PMMA::Core::KeyEvent_Left_Shift_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Left_Control::Key_Left_Control() {
    PMMA::Core::KeyEvent_Left_Control_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Left_Control::~Key_Left_Control() {
    auto it = find(PMMA::Core::KeyEvent_Left_Control_Instances.begin(), PMMA::Core::KeyEvent_Left_Control_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Left_Control_Instances.end()) {
        PMMA::Core::KeyEvent_Left_Control_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Left_Alt::Key_Left_Alt() {
    PMMA::Core::KeyEvent_Left_Alt_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Left_Alt::~Key_Left_Alt() {
    auto it = find(PMMA::Core::KeyEvent_Left_Alt_Instances.begin(), PMMA::Core::KeyEvent_Left_Alt_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Left_Alt_Instances.end()) {
        PMMA::Core::KeyEvent_Left_Alt_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Left_Super::Key_Left_Super() {
    PMMA::Core::KeyEvent_Left_Super_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Left_Super::~Key_Left_Super() {
    auto it = find(PMMA::Core::KeyEvent_Left_Super_Instances.begin(), PMMA::Core::KeyEvent_Left_Super_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Left_Super_Instances.end()) {
        PMMA::Core::KeyEvent_Left_Super_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Right_Shift::Key_Right_Shift() {
    PMMA::Core::KeyEvent_Right_Shift_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Right_Shift::~Key_Right_Shift() {
    auto it = find(PMMA::Core::KeyEvent_Right_Shift_Instances.begin(), PMMA::Core::KeyEvent_Right_Shift_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Right_Shift_Instances.end()) {
        PMMA::Core::KeyEvent_Right_Shift_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Right_Control::Key_Right_Control() {
    PMMA::Core::KeyEvent_Right_Control_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Right_Control::~Key_Right_Control() {
    auto it = find(PMMA::Core::KeyEvent_Right_Control_Instances.begin(), PMMA::Core::KeyEvent_Right_Control_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Right_Control_Instances.end()) {
        PMMA::Core::KeyEvent_Right_Control_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Right_Alt::Key_Right_Alt() {
    PMMA::Core::KeyEvent_Right_Alt_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Right_Alt::~Key_Right_Alt() {
    auto it = find(PMMA::Core::KeyEvent_Right_Alt_Instances.begin(), PMMA::Core::KeyEvent_Right_Alt_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Right_Alt_Instances.end()) {
        PMMA::Core::KeyEvent_Right_Alt_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Right_Super::Key_Right_Super() {
    PMMA::Core::KeyEvent_Right_Super_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Right_Super::~Key_Right_Super() {
    auto it = find(PMMA::Core::KeyEvent_Right_Super_Instances.begin(), PMMA::Core::KeyEvent_Right_Super_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Right_Super_Instances.end()) {
        PMMA::Core::KeyEvent_Right_Super_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Shift::Key_Shift() {
    PMMA::Core::KeyEvent_Shift_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Shift::~Key_Shift() {
    auto it = find(PMMA::Core::KeyEvent_Shift_Instances.begin(), PMMA::Core::KeyEvent_Shift_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Shift_Instances.end()) {
        PMMA::Core::KeyEvent_Shift_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Control::Key_Control() {
    PMMA::Core::KeyEvent_Control_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Control::~Key_Control() {
    auto it = find(PMMA::Core::KeyEvent_Control_Instances.begin(), PMMA::Core::KeyEvent_Control_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Control_Instances.end()) {
        PMMA::Core::KeyEvent_Control_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Alt::Key_Alt() {
    PMMA::Core::KeyEvent_Alt_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Alt::~Key_Alt() {
    auto it = find(PMMA::Core::KeyEvent_Alt_Instances.begin(), PMMA::Core::KeyEvent_Alt_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Alt_Instances.end()) {
        PMMA::Core::KeyEvent_Alt_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Super::Key_Super() {
    PMMA::Core::KeyEvent_Super_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Super::~Key_Super() {
    auto it = find(PMMA::Core::KeyEvent_Super_Instances.begin(), PMMA::Core::KeyEvent_Super_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Super_Instances.end()) {
        PMMA::Core::KeyEvent_Super_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};

Key_Menu::Key_Menu() {
    PMMA::Core::KeyEvent_Menu_Instances.push_back(this);

    PMMA::Registry::KeyboardEventInstanceCount++;
};

Key_Menu::~Key_Menu() {
    auto it = find(PMMA::Core::KeyEvent_Menu_Instances.begin(), PMMA::Core::KeyEvent_Menu_Instances.end(), this);
    if (it != PMMA::Core::KeyEvent_Menu_Instances.end()) {
        PMMA::Core::KeyEvent_Menu_Instances.erase(it);
    }

    PMMA::Registry::KeyboardEventInstanceCount--;
};