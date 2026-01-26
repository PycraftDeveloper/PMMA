#include "PMMA_Core.hpp"

using namespace std;

CPP_KeyEvent_Space::CPP_KeyEvent_Space() {
    PMMA_Core::KeyEvent_Space_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Space::~CPP_KeyEvent_Space() {
    auto it = find(PMMA_Core::KeyEvent_Space_Instances.begin(), PMMA_Core::KeyEvent_Space_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Space_Instances.end()) {
        PMMA_Core::KeyEvent_Space_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Apostrophe::CPP_KeyEvent_Apostrophe() {
    PMMA_Core::KeyEvent_Apostrophe_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Apostrophe::~CPP_KeyEvent_Apostrophe() {
    auto it = find(PMMA_Core::KeyEvent_Apostrophe_Instances.begin(), PMMA_Core::KeyEvent_Apostrophe_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Apostrophe_Instances.end()) {
        PMMA_Core::KeyEvent_Apostrophe_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Comma::CPP_KeyEvent_Comma() {
    PMMA_Core::KeyEvent_Comma_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Comma::~CPP_KeyEvent_Comma() {
    auto it = find(PMMA_Core::KeyEvent_Comma_Instances.begin(), PMMA_Core::KeyEvent_Comma_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Comma_Instances.end()) {
        PMMA_Core::KeyEvent_Comma_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Minus::CPP_KeyEvent_Minus() {
    PMMA_Core::KeyEvent_Minus_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Minus::~CPP_KeyEvent_Minus() {
    auto it = find(PMMA_Core::KeyEvent_Minus_Instances.begin(), PMMA_Core::KeyEvent_Minus_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Minus_Instances.end()) {
        PMMA_Core::KeyEvent_Minus_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Period::CPP_KeyEvent_Period() {
    PMMA_Core::KeyEvent_Period_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Period::~CPP_KeyEvent_Period() {
    auto it = find(PMMA_Core::KeyEvent_Period_Instances.begin(), PMMA_Core::KeyEvent_Period_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Period_Instances.end()) {
        PMMA_Core::KeyEvent_Period_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Slash::CPP_KeyEvent_Slash() {
    PMMA_Core::KeyEvent_Slash_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Slash::~CPP_KeyEvent_Slash() {
    auto it = find(PMMA_Core::KeyEvent_Slash_Instances.begin(), PMMA_Core::KeyEvent_Slash_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Slash_Instances.end()) {
        PMMA_Core::KeyEvent_Slash_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_0::CPP_KeyEvent_0() {
    PMMA_Core::KeyEvent_0_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_0::~CPP_KeyEvent_0() {
    auto it = find(PMMA_Core::KeyEvent_0_Instances.begin(), PMMA_Core::KeyEvent_0_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_0_Instances.end()) {
        PMMA_Core::KeyEvent_0_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_1::CPP_KeyEvent_1() {
    PMMA_Core::KeyEvent_1_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_1::~CPP_KeyEvent_1() {
    auto it = find(PMMA_Core::KeyEvent_1_Instances.begin(), PMMA_Core::KeyEvent_1_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_1_Instances.end()) {
        PMMA_Core::KeyEvent_1_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_2::CPP_KeyEvent_2() {
    PMMA_Core::KeyEvent_2_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_2::~CPP_KeyEvent_2() {
    auto it = find(PMMA_Core::KeyEvent_2_Instances.begin(), PMMA_Core::KeyEvent_2_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_2_Instances.end()) {
        PMMA_Core::KeyEvent_2_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_3::CPP_KeyEvent_3() {
    PMMA_Core::KeyEvent_3_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_3::~CPP_KeyEvent_3() {
    auto it = find(PMMA_Core::KeyEvent_3_Instances.begin(), PMMA_Core::KeyEvent_3_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_3_Instances.end()) {
        PMMA_Core::KeyEvent_3_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_4::CPP_KeyEvent_4() {
    PMMA_Core::KeyEvent_4_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_4::~CPP_KeyEvent_4() {
    auto it = find(PMMA_Core::KeyEvent_4_Instances.begin(), PMMA_Core::KeyEvent_4_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_4_Instances.end()) {
        PMMA_Core::KeyEvent_4_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_5::CPP_KeyEvent_5() {
    PMMA_Core::KeyEvent_5_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_5::~CPP_KeyEvent_5() {
    auto it = find(PMMA_Core::KeyEvent_5_Instances.begin(), PMMA_Core::KeyEvent_5_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_5_Instances.end()) {
        PMMA_Core::KeyEvent_5_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_6::CPP_KeyEvent_6() {
    PMMA_Core::KeyEvent_6_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_6::~CPP_KeyEvent_6() {
    auto it = find(PMMA_Core::KeyEvent_6_Instances.begin(), PMMA_Core::KeyEvent_6_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_6_Instances.end()) {
        PMMA_Core::KeyEvent_6_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_7::CPP_KeyEvent_7() {
    PMMA_Core::KeyEvent_7_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_7::~CPP_KeyEvent_7() {
    auto it = find(PMMA_Core::KeyEvent_7_Instances.begin(), PMMA_Core::KeyEvent_7_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_7_Instances.end()) {
        PMMA_Core::KeyEvent_7_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_8::CPP_KeyEvent_8() {
    PMMA_Core::KeyEvent_8_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_8::~CPP_KeyEvent_8() {
    auto it = find(PMMA_Core::KeyEvent_8_Instances.begin(), PMMA_Core::KeyEvent_8_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_8_Instances.end()) {
        PMMA_Core::KeyEvent_8_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_9::CPP_KeyEvent_9() {
    PMMA_Core::KeyEvent_9_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_9::~CPP_KeyEvent_9() {
    auto it = find(PMMA_Core::KeyEvent_9_Instances.begin(), PMMA_Core::KeyEvent_9_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_9_Instances.end()) {
        PMMA_Core::KeyEvent_9_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Semicolon::CPP_KeyEvent_Semicolon() {
    PMMA_Core::KeyEvent_Semicolon_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Semicolon::~CPP_KeyEvent_Semicolon() {
    auto it = find(PMMA_Core::KeyEvent_Semicolon_Instances.begin(), PMMA_Core::KeyEvent_Semicolon_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Semicolon_Instances.end()) {
        PMMA_Core::KeyEvent_Semicolon_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Equal::CPP_KeyEvent_Equal() {
    PMMA_Core::KeyEvent_Equal_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Equal::~CPP_KeyEvent_Equal() {
    auto it = find(PMMA_Core::KeyEvent_Equal_Instances.begin(), PMMA_Core::KeyEvent_Equal_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Equal_Instances.end()) {
        PMMA_Core::KeyEvent_Equal_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_A::CPP_KeyEvent_A() {
    PMMA_Core::KeyEvent_A_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_A::~CPP_KeyEvent_A() {
    auto it = find(PMMA_Core::KeyEvent_A_Instances.begin(), PMMA_Core::KeyEvent_A_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_A_Instances.end()) {
        PMMA_Core::KeyEvent_A_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_B::CPP_KeyEvent_B() {
    PMMA_Core::KeyEvent_B_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_B::~CPP_KeyEvent_B() {
    auto it = find(PMMA_Core::KeyEvent_B_Instances.begin(), PMMA_Core::KeyEvent_B_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_B_Instances.end()) {
        PMMA_Core::KeyEvent_B_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_C::CPP_KeyEvent_C() {
    PMMA_Core::KeyEvent_C_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_C::~CPP_KeyEvent_C() {
    auto it = find(PMMA_Core::KeyEvent_C_Instances.begin(), PMMA_Core::KeyEvent_C_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_C_Instances.end()) {
        PMMA_Core::KeyEvent_C_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_D::CPP_KeyEvent_D() {
    PMMA_Core::KeyEvent_D_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_D::~CPP_KeyEvent_D() {
    auto it = find(PMMA_Core::KeyEvent_D_Instances.begin(), PMMA_Core::KeyEvent_D_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_D_Instances.end()) {
        PMMA_Core::KeyEvent_D_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_E::CPP_KeyEvent_E() {
    PMMA_Core::KeyEvent_E_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_E::~CPP_KeyEvent_E() {
    auto it = find(PMMA_Core::KeyEvent_E_Instances.begin(), PMMA_Core::KeyEvent_E_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_E_Instances.end()) {
        PMMA_Core::KeyEvent_E_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F::CPP_KeyEvent_F() {
    PMMA_Core::KeyEvent_F_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F::~CPP_KeyEvent_F() {
    auto it = find(PMMA_Core::KeyEvent_F_Instances.begin(), PMMA_Core::KeyEvent_F_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F_Instances.end()) {
        PMMA_Core::KeyEvent_F_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_G::CPP_KeyEvent_G() {
    PMMA_Core::KeyEvent_G_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_G::~CPP_KeyEvent_G() {
    auto it = find(PMMA_Core::KeyEvent_G_Instances.begin(), PMMA_Core::KeyEvent_G_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_G_Instances.end()) {
        PMMA_Core::KeyEvent_G_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_H::CPP_KeyEvent_H() {
    PMMA_Core::KeyEvent_H_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_H::~CPP_KeyEvent_H() {
    auto it = find(PMMA_Core::KeyEvent_H_Instances.begin(), PMMA_Core::KeyEvent_H_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_H_Instances.end()) {
        PMMA_Core::KeyEvent_H_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_I::CPP_KeyEvent_I() {
    PMMA_Core::KeyEvent_I_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_I::~CPP_KeyEvent_I() {
    auto it = find(PMMA_Core::KeyEvent_I_Instances.begin(), PMMA_Core::KeyEvent_I_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_I_Instances.end()) {
        PMMA_Core::KeyEvent_I_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_J::CPP_KeyEvent_J() {
    PMMA_Core::KeyEvent_J_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_J::~CPP_KeyEvent_J() {
    auto it = find(PMMA_Core::KeyEvent_J_Instances.begin(), PMMA_Core::KeyEvent_J_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_J_Instances.end()) {
        PMMA_Core::KeyEvent_J_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_K::CPP_KeyEvent_K() {
    PMMA_Core::KeyEvent_K_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_K::~CPP_KeyEvent_K() {
    auto it = find(PMMA_Core::KeyEvent_K_Instances.begin(), PMMA_Core::KeyEvent_K_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_K_Instances.end()) {
        PMMA_Core::KeyEvent_K_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_L::CPP_KeyEvent_L() {
    PMMA_Core::KeyEvent_L_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_L::~CPP_KeyEvent_L() {
    auto it = find(PMMA_Core::KeyEvent_L_Instances.begin(), PMMA_Core::KeyEvent_L_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_L_Instances.end()) {
        PMMA_Core::KeyEvent_L_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_M::CPP_KeyEvent_M() {
    PMMA_Core::KeyEvent_M_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_M::~CPP_KeyEvent_M() {
    auto it = find(PMMA_Core::KeyEvent_M_Instances.begin(), PMMA_Core::KeyEvent_M_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_M_Instances.end()) {
        PMMA_Core::KeyEvent_M_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_N::CPP_KeyEvent_N() {
    PMMA_Core::KeyEvent_N_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_N::~CPP_KeyEvent_N() {
    auto it = find(PMMA_Core::KeyEvent_N_Instances.begin(), PMMA_Core::KeyEvent_N_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_N_Instances.end()) {
        PMMA_Core::KeyEvent_N_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_O::CPP_KeyEvent_O() {
    PMMA_Core::KeyEvent_O_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_O::~CPP_KeyEvent_O() {
    auto it = find(PMMA_Core::KeyEvent_O_Instances.begin(), PMMA_Core::KeyEvent_O_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_O_Instances.end()) {
        PMMA_Core::KeyEvent_O_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_P::CPP_KeyEvent_P() {
    PMMA_Core::KeyEvent_P_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_P::~CPP_KeyEvent_P() {
    auto it = find(PMMA_Core::KeyEvent_P_Instances.begin(), PMMA_Core::KeyEvent_P_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_P_Instances.end()) {
        PMMA_Core::KeyEvent_P_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Q::CPP_KeyEvent_Q() {
    PMMA_Core::KeyEvent_Q_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Q::~CPP_KeyEvent_Q() {
    auto it = find(PMMA_Core::KeyEvent_Q_Instances.begin(), PMMA_Core::KeyEvent_Q_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Q_Instances.end()) {
        PMMA_Core::KeyEvent_Q_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_R::CPP_KeyEvent_R() {
    PMMA_Core::KeyEvent_R_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_R::~CPP_KeyEvent_R() {
    auto it = find(PMMA_Core::KeyEvent_R_Instances.begin(), PMMA_Core::KeyEvent_R_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_R_Instances.end()) {
        PMMA_Core::KeyEvent_R_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_S::CPP_KeyEvent_S() {
    PMMA_Core::KeyEvent_S_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_S::~CPP_KeyEvent_S() {
    auto it = find(PMMA_Core::KeyEvent_S_Instances.begin(), PMMA_Core::KeyEvent_S_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_S_Instances.end()) {
        PMMA_Core::KeyEvent_S_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_T::CPP_KeyEvent_T() {
    PMMA_Core::KeyEvent_T_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_T::~CPP_KeyEvent_T() {
    auto it = find(PMMA_Core::KeyEvent_T_Instances.begin(), PMMA_Core::KeyEvent_T_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_T_Instances.end()) {
        PMMA_Core::KeyEvent_T_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_U::CPP_KeyEvent_U() {
    PMMA_Core::KeyEvent_U_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_U::~CPP_KeyEvent_U() {
    auto it = find(PMMA_Core::KeyEvent_U_Instances.begin(), PMMA_Core::KeyEvent_U_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_U_Instances.end()) {
        PMMA_Core::KeyEvent_U_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_V::CPP_KeyEvent_V() {
    PMMA_Core::KeyEvent_V_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_V::~CPP_KeyEvent_V() {
    auto it = find(PMMA_Core::KeyEvent_V_Instances.begin(), PMMA_Core::KeyEvent_V_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_V_Instances.end()) {
        PMMA_Core::KeyEvent_V_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_W::CPP_KeyEvent_W() {
    PMMA_Core::KeyEvent_W_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_W::~CPP_KeyEvent_W() {
    auto it = find(PMMA_Core::KeyEvent_W_Instances.begin(), PMMA_Core::KeyEvent_W_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_W_Instances.end()) {
        PMMA_Core::KeyEvent_W_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_X::CPP_KeyEvent_X() {
    PMMA_Core::KeyEvent_X_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_X::~CPP_KeyEvent_X() {
    auto it = find(PMMA_Core::KeyEvent_X_Instances.begin(), PMMA_Core::KeyEvent_X_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_X_Instances.end()) {
        PMMA_Core::KeyEvent_X_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Y::CPP_KeyEvent_Y() {
    PMMA_Core::KeyEvent_Y_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Y::~CPP_KeyEvent_Y() {
    auto it = find(PMMA_Core::KeyEvent_Y_Instances.begin(), PMMA_Core::KeyEvent_Y_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Y_Instances.end()) {
        PMMA_Core::KeyEvent_Y_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Z::CPP_KeyEvent_Z() {
    PMMA_Core::KeyEvent_Z_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Z::~CPP_KeyEvent_Z() {
    auto it = find(PMMA_Core::KeyEvent_Z_Instances.begin(), PMMA_Core::KeyEvent_Z_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Z_Instances.end()) {
        PMMA_Core::KeyEvent_Z_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Left_Bracket::CPP_KeyEvent_Left_Bracket() {
    PMMA_Core::KeyEvent_Left_Bracket_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Left_Bracket::~CPP_KeyEvent_Left_Bracket() {
    auto it = find(PMMA_Core::KeyEvent_Left_Bracket_Instances.begin(), PMMA_Core::KeyEvent_Left_Bracket_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Left_Bracket_Instances.end()) {
        PMMA_Core::KeyEvent_Left_Bracket_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Backslash::CPP_KeyEvent_Backslash() {
    PMMA_Core::KeyEvent_Backslash_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Backslash::~CPP_KeyEvent_Backslash() {
    auto it = find(PMMA_Core::KeyEvent_Backslash_Instances.begin(), PMMA_Core::KeyEvent_Backslash_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Backslash_Instances.end()) {
        PMMA_Core::KeyEvent_Backslash_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Right_Bracket::CPP_KeyEvent_Right_Bracket() {
    PMMA_Core::KeyEvent_Right_Bracket_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Right_Bracket::~CPP_KeyEvent_Right_Bracket() {
    auto it = find(PMMA_Core::KeyEvent_Right_Bracket_Instances.begin(), PMMA_Core::KeyEvent_Right_Bracket_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Right_Bracket_Instances.end()) {
        PMMA_Core::KeyEvent_Right_Bracket_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Grave_Accent::CPP_KeyEvent_Grave_Accent() {
    PMMA_Core::KeyEvent_Grave_Accent_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Grave_Accent::~CPP_KeyEvent_Grave_Accent() {
    auto it = find(PMMA_Core::KeyEvent_Grave_Accent_Instances.begin(), PMMA_Core::KeyEvent_Grave_Accent_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Grave_Accent_Instances.end()) {
        PMMA_Core::KeyEvent_Grave_Accent_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_World_1::CPP_KeyEvent_World_1() {
    PMMA_Core::KeyEvent_World_1_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_World_1::~CPP_KeyEvent_World_1() {
    auto it = find(PMMA_Core::KeyEvent_World_1_Instances.begin(), PMMA_Core::KeyEvent_World_1_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_World_1_Instances.end()) {
        PMMA_Core::KeyEvent_World_1_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_World_2::CPP_KeyEvent_World_2() {
    PMMA_Core::KeyEvent_World_2_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_World_2::~CPP_KeyEvent_World_2() {
    auto it = find(PMMA_Core::KeyEvent_World_2_Instances.begin(), PMMA_Core::KeyEvent_World_2_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_World_2_Instances.end()) {
        PMMA_Core::KeyEvent_World_2_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Escape::CPP_KeyEvent_Escape() {
    PMMA_Core::KeyEvent_Escape_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Escape::~CPP_KeyEvent_Escape() {
    auto it = find(PMMA_Core::KeyEvent_Escape_Instances.begin(), PMMA_Core::KeyEvent_Escape_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Escape_Instances.end()) {
        PMMA_Core::KeyEvent_Escape_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Enter::CPP_KeyEvent_Enter() {
    PMMA_Core::KeyEvent_Enter_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Enter::~CPP_KeyEvent_Enter() {
    auto it = find(PMMA_Core::KeyEvent_Enter_Instances.begin(), PMMA_Core::KeyEvent_Enter_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Enter_Instances.end()) {
        PMMA_Core::KeyEvent_Enter_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Tab::CPP_KeyEvent_Tab() {
    PMMA_Core::KeyEvent_Tab_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Tab::~CPP_KeyEvent_Tab() {
    auto it = find(PMMA_Core::KeyEvent_Tab_Instances.begin(), PMMA_Core::KeyEvent_Tab_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Tab_Instances.end()) {
        PMMA_Core::KeyEvent_Tab_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Backspace::CPP_KeyEvent_Backspace() {
    PMMA_Core::KeyEvent_Backspace_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Backspace::~CPP_KeyEvent_Backspace() {
    auto it = find(PMMA_Core::KeyEvent_Backspace_Instances.begin(), PMMA_Core::KeyEvent_Backspace_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Backspace_Instances.end()) {
        PMMA_Core::KeyEvent_Backspace_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Insert::CPP_KeyEvent_Insert() {
    PMMA_Core::KeyEvent_Insert_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Insert::~CPP_KeyEvent_Insert() {
    auto it = find(PMMA_Core::KeyEvent_Insert_Instances.begin(), PMMA_Core::KeyEvent_Insert_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Insert_Instances.end()) {
        PMMA_Core::KeyEvent_Insert_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Delete::CPP_KeyEvent_Delete() {
    PMMA_Core::KeyEvent_Delete_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Delete::~CPP_KeyEvent_Delete() {
    auto it = find(PMMA_Core::KeyEvent_Delete_Instances.begin(), PMMA_Core::KeyEvent_Delete_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Delete_Instances.end()) {
        PMMA_Core::KeyEvent_Delete_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Right::CPP_KeyEvent_Right() {
    PMMA_Core::KeyEvent_Right_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Right::~CPP_KeyEvent_Right() {
    auto it = find(PMMA_Core::KeyEvent_Right_Instances.begin(), PMMA_Core::KeyEvent_Right_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Right_Instances.end()) {
        PMMA_Core::KeyEvent_Right_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Left::CPP_KeyEvent_Left() {
    PMMA_Core::KeyEvent_Left_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Left::~CPP_KeyEvent_Left() {
    auto it = find(PMMA_Core::KeyEvent_Left_Instances.begin(), PMMA_Core::KeyEvent_Left_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Left_Instances.end()) {
        PMMA_Core::KeyEvent_Left_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Down::CPP_KeyEvent_Down() {
    PMMA_Core::KeyEvent_Down_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Down::~CPP_KeyEvent_Down() {
    auto it = find(PMMA_Core::KeyEvent_Down_Instances.begin(), PMMA_Core::KeyEvent_Down_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Down_Instances.end()) {
        PMMA_Core::KeyEvent_Down_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Up::CPP_KeyEvent_Up() {
    PMMA_Core::KeyEvent_Up_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Up::~CPP_KeyEvent_Up() {
    auto it = find(PMMA_Core::KeyEvent_Up_Instances.begin(), PMMA_Core::KeyEvent_Up_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Up_Instances.end()) {
        PMMA_Core::KeyEvent_Up_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Page_Up::CPP_KeyEvent_Page_Up() {
    PMMA_Core::KeyEvent_Page_Up_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Page_Up::~CPP_KeyEvent_Page_Up() {
    auto it = find(PMMA_Core::KeyEvent_Page_Up_Instances.begin(), PMMA_Core::KeyEvent_Page_Up_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Page_Up_Instances.end()) {
        PMMA_Core::KeyEvent_Page_Up_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Page_Down::CPP_KeyEvent_Page_Down() {
    PMMA_Core::KeyEvent_Page_Down_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Page_Down::~CPP_KeyEvent_Page_Down() {
    auto it = find(PMMA_Core::KeyEvent_Page_Down_Instances.begin(), PMMA_Core::KeyEvent_Page_Down_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Page_Down_Instances.end()) {
        PMMA_Core::KeyEvent_Page_Down_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Home::CPP_KeyEvent_Home() {
    PMMA_Core::KeyEvent_Home_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Home::~CPP_KeyEvent_Home() {
    auto it = find(PMMA_Core::KeyEvent_Home_Instances.begin(), PMMA_Core::KeyEvent_Home_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Home_Instances.end()) {
        PMMA_Core::KeyEvent_Home_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_End::CPP_KeyEvent_End() {
    PMMA_Core::KeyEvent_End_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_End::~CPP_KeyEvent_End() {
    auto it = find(PMMA_Core::KeyEvent_End_Instances.begin(), PMMA_Core::KeyEvent_End_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_End_Instances.end()) {
        PMMA_Core::KeyEvent_End_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Caps_Lock::CPP_KeyEvent_Caps_Lock() {
    PMMA_Core::KeyEvent_Caps_Lock_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Caps_Lock::~CPP_KeyEvent_Caps_Lock() {
    auto it = find(PMMA_Core::KeyEvent_Caps_Lock_Instances.begin(), PMMA_Core::KeyEvent_Caps_Lock_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Caps_Lock_Instances.end()) {
        PMMA_Core::KeyEvent_Caps_Lock_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Scroll_Lock::CPP_KeyEvent_Scroll_Lock() {
    PMMA_Core::KeyEvent_Scroll_Lock_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Scroll_Lock::~CPP_KeyEvent_Scroll_Lock() {
    auto it = find(PMMA_Core::KeyEvent_Scroll_Lock_Instances.begin(), PMMA_Core::KeyEvent_Scroll_Lock_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Scroll_Lock_Instances.end()) {
        PMMA_Core::KeyEvent_Scroll_Lock_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Num_Lock::CPP_KeyEvent_Num_Lock() {
    PMMA_Core::KeyEvent_Num_Lock_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Num_Lock::~CPP_KeyEvent_Num_Lock() {
    auto it = find(PMMA_Core::KeyEvent_Num_Lock_Instances.begin(), PMMA_Core::KeyEvent_Num_Lock_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Num_Lock_Instances.end()) {
        PMMA_Core::KeyEvent_Num_Lock_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Print_Screen::CPP_KeyEvent_Print_Screen() {
    PMMA_Core::KeyEvent_Print_Screen_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Print_Screen::~CPP_KeyEvent_Print_Screen() {
    auto it = find(PMMA_Core::KeyEvent_Print_Screen_Instances.begin(), PMMA_Core::KeyEvent_Print_Screen_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Print_Screen_Instances.end()) {
        PMMA_Core::KeyEvent_Print_Screen_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Pause::CPP_KeyEvent_Pause() {
    PMMA_Core::KeyEvent_Pause_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Pause::~CPP_KeyEvent_Pause() {
    auto it = find(PMMA_Core::KeyEvent_Pause_Instances.begin(), PMMA_Core::KeyEvent_Pause_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Pause_Instances.end()) {
        PMMA_Core::KeyEvent_Pause_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F1::CPP_KeyEvent_F1() {
    PMMA_Core::KeyEvent_F1_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F1::~CPP_KeyEvent_F1() {
    auto it = find(PMMA_Core::KeyEvent_F1_Instances.begin(), PMMA_Core::KeyEvent_F1_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F1_Instances.end()) {
        PMMA_Core::KeyEvent_F1_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F2::CPP_KeyEvent_F2() {
    PMMA_Core::KeyEvent_F2_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F2::~CPP_KeyEvent_F2() {
    auto it = find(PMMA_Core::KeyEvent_F2_Instances.begin(), PMMA_Core::KeyEvent_F2_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F2_Instances.end()) {
        PMMA_Core::KeyEvent_F2_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F3::CPP_KeyEvent_F3() {
    PMMA_Core::KeyEvent_F3_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F3::~CPP_KeyEvent_F3() {
    auto it = find(PMMA_Core::KeyEvent_F3_Instances.begin(), PMMA_Core::KeyEvent_F3_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F3_Instances.end()) {
        PMMA_Core::KeyEvent_F3_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F4::CPP_KeyEvent_F4() {
    PMMA_Core::KeyEvent_F4_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F4::~CPP_KeyEvent_F4() {
    auto it = find(PMMA_Core::KeyEvent_F4_Instances.begin(), PMMA_Core::KeyEvent_F4_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F4_Instances.end()) {
        PMMA_Core::KeyEvent_F4_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F5::CPP_KeyEvent_F5() {
    PMMA_Core::KeyEvent_F5_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F5::~CPP_KeyEvent_F5() {
    auto it = find(PMMA_Core::KeyEvent_F5_Instances.begin(), PMMA_Core::KeyEvent_F5_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F5_Instances.end()) {
        PMMA_Core::KeyEvent_F5_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F6::CPP_KeyEvent_F6() {
    PMMA_Core::KeyEvent_F6_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F6::~CPP_KeyEvent_F6() {
    auto it = find(PMMA_Core::KeyEvent_F6_Instances.begin(), PMMA_Core::KeyEvent_F6_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F6_Instances.end()) {
        PMMA_Core::KeyEvent_F6_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F7::CPP_KeyEvent_F7() {
    PMMA_Core::KeyEvent_F7_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F7::~CPP_KeyEvent_F7() {
    auto it = find(PMMA_Core::KeyEvent_F7_Instances.begin(), PMMA_Core::KeyEvent_F7_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F7_Instances.end()) {
        PMMA_Core::KeyEvent_F7_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F8::CPP_KeyEvent_F8() {
    PMMA_Core::KeyEvent_F8_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F8::~CPP_KeyEvent_F8() {
    auto it = find(PMMA_Core::KeyEvent_F8_Instances.begin(), PMMA_Core::KeyEvent_F8_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F8_Instances.end()) {
        PMMA_Core::KeyEvent_F8_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F9::CPP_KeyEvent_F9() {
    PMMA_Core::KeyEvent_F9_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F9::~CPP_KeyEvent_F9() {
    auto it = find(PMMA_Core::KeyEvent_F9_Instances.begin(), PMMA_Core::KeyEvent_F9_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F9_Instances.end()) {
        PMMA_Core::KeyEvent_F9_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F10::CPP_KeyEvent_F10() {
    PMMA_Core::KeyEvent_F10_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F10::~CPP_KeyEvent_F10() {
    auto it = find(PMMA_Core::KeyEvent_F10_Instances.begin(), PMMA_Core::KeyEvent_F10_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F10_Instances.end()) {
        PMMA_Core::KeyEvent_F10_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F11::CPP_KeyEvent_F11() {
    PMMA_Core::KeyEvent_F11_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F11::~CPP_KeyEvent_F11() {
    auto it = find(PMMA_Core::KeyEvent_F11_Instances.begin(), PMMA_Core::KeyEvent_F11_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F11_Instances.end()) {
        PMMA_Core::KeyEvent_F11_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F12::CPP_KeyEvent_F12() {
    PMMA_Core::KeyEvent_F12_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F12::~CPP_KeyEvent_F12() {
    auto it = find(PMMA_Core::KeyEvent_F12_Instances.begin(), PMMA_Core::KeyEvent_F12_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F12_Instances.end()) {
        PMMA_Core::KeyEvent_F12_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F13::CPP_KeyEvent_F13() {
    PMMA_Core::KeyEvent_F13_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F13::~CPP_KeyEvent_F13() {
    auto it = find(PMMA_Core::KeyEvent_F13_Instances.begin(), PMMA_Core::KeyEvent_F13_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F13_Instances.end()) {
        PMMA_Core::KeyEvent_F13_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F14::CPP_KeyEvent_F14() {
    PMMA_Core::KeyEvent_F14_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F14::~CPP_KeyEvent_F14() {
    auto it = find(PMMA_Core::KeyEvent_F14_Instances.begin(), PMMA_Core::KeyEvent_F14_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F14_Instances.end()) {
        PMMA_Core::KeyEvent_F14_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F15::CPP_KeyEvent_F15() {
    PMMA_Core::KeyEvent_F15_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F15::~CPP_KeyEvent_F15() {
    auto it = find(PMMA_Core::KeyEvent_F15_Instances.begin(), PMMA_Core::KeyEvent_F15_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F15_Instances.end()) {
        PMMA_Core::KeyEvent_F15_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F16::CPP_KeyEvent_F16() {
    PMMA_Core::KeyEvent_F16_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F16::~CPP_KeyEvent_F16() {
    auto it = find(PMMA_Core::KeyEvent_F16_Instances.begin(), PMMA_Core::KeyEvent_F16_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F16_Instances.end()) {
        PMMA_Core::KeyEvent_F16_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F17::CPP_KeyEvent_F17() {
    PMMA_Core::KeyEvent_F17_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F17::~CPP_KeyEvent_F17() {
    auto it = find(PMMA_Core::KeyEvent_F17_Instances.begin(), PMMA_Core::KeyEvent_F17_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F17_Instances.end()) {
        PMMA_Core::KeyEvent_F17_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F18::CPP_KeyEvent_F18() {
    PMMA_Core::KeyEvent_F18_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F18::~CPP_KeyEvent_F18() {
    auto it = find(PMMA_Core::KeyEvent_F18_Instances.begin(), PMMA_Core::KeyEvent_F18_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F18_Instances.end()) {
        PMMA_Core::KeyEvent_F18_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F19::CPP_KeyEvent_F19() {
    PMMA_Core::KeyEvent_F19_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F19::~CPP_KeyEvent_F19() {
    auto it = find(PMMA_Core::KeyEvent_F19_Instances.begin(), PMMA_Core::KeyEvent_F19_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F19_Instances.end()) {
        PMMA_Core::KeyEvent_F19_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F20::CPP_KeyEvent_F20() {
    PMMA_Core::KeyEvent_F20_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F20::~CPP_KeyEvent_F20() {
    auto it = find(PMMA_Core::KeyEvent_F20_Instances.begin(), PMMA_Core::KeyEvent_F20_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F20_Instances.end()) {
        PMMA_Core::KeyEvent_F20_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F21::CPP_KeyEvent_F21() {
    PMMA_Core::KeyEvent_F21_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F21::~CPP_KeyEvent_F21() {
    auto it = find(PMMA_Core::KeyEvent_F21_Instances.begin(), PMMA_Core::KeyEvent_F21_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F21_Instances.end()) {
        PMMA_Core::KeyEvent_F21_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F22::CPP_KeyEvent_F22() {
    PMMA_Core::KeyEvent_F22_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F22::~CPP_KeyEvent_F22() {
    auto it = find(PMMA_Core::KeyEvent_F22_Instances.begin(), PMMA_Core::KeyEvent_F22_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F22_Instances.end()) {
        PMMA_Core::KeyEvent_F22_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F23::CPP_KeyEvent_F23() {
    PMMA_Core::KeyEvent_F23_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F23::~CPP_KeyEvent_F23() {
    auto it = find(PMMA_Core::KeyEvent_F23_Instances.begin(), PMMA_Core::KeyEvent_F23_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F23_Instances.end()) {
        PMMA_Core::KeyEvent_F23_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F24::CPP_KeyEvent_F24() {
    PMMA_Core::KeyEvent_F24_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F24::~CPP_KeyEvent_F24() {
    auto it = find(PMMA_Core::KeyEvent_F24_Instances.begin(), PMMA_Core::KeyEvent_F24_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F24_Instances.end()) {
        PMMA_Core::KeyEvent_F24_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_F25::CPP_KeyEvent_F25() {
    PMMA_Core::KeyEvent_F25_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_F25::~CPP_KeyEvent_F25() {
    auto it = find(PMMA_Core::KeyEvent_F25_Instances.begin(), PMMA_Core::KeyEvent_F25_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_F25_Instances.end()) {
        PMMA_Core::KeyEvent_F25_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Left_Shift::CPP_KeyEvent_Left_Shift() {
    PMMA_Core::KeyEvent_Left_Shift_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Left_Shift::~CPP_KeyEvent_Left_Shift() {
    auto it = find(PMMA_Core::KeyEvent_Left_Shift_Instances.begin(), PMMA_Core::KeyEvent_Left_Shift_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Left_Shift_Instances.end()) {
        PMMA_Core::KeyEvent_Left_Shift_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Left_Control::CPP_KeyEvent_Left_Control() {
    PMMA_Core::KeyEvent_Left_Control_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Left_Control::~CPP_KeyEvent_Left_Control() {
    auto it = find(PMMA_Core::KeyEvent_Left_Control_Instances.begin(), PMMA_Core::KeyEvent_Left_Control_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Left_Control_Instances.end()) {
        PMMA_Core::KeyEvent_Left_Control_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Left_Alt::CPP_KeyEvent_Left_Alt() {
    PMMA_Core::KeyEvent_Left_Alt_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Left_Alt::~CPP_KeyEvent_Left_Alt() {
    auto it = find(PMMA_Core::KeyEvent_Left_Alt_Instances.begin(), PMMA_Core::KeyEvent_Left_Alt_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Left_Alt_Instances.end()) {
        PMMA_Core::KeyEvent_Left_Alt_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Left_Super::CPP_KeyEvent_Left_Super() {
    PMMA_Core::KeyEvent_Left_Super_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Left_Super::~CPP_KeyEvent_Left_Super() {
    auto it = find(PMMA_Core::KeyEvent_Left_Super_Instances.begin(), PMMA_Core::KeyEvent_Left_Super_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Left_Super_Instances.end()) {
        PMMA_Core::KeyEvent_Left_Super_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Right_Shift::CPP_KeyEvent_Right_Shift() {
    PMMA_Core::KeyEvent_Right_Shift_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Right_Shift::~CPP_KeyEvent_Right_Shift() {
    auto it = find(PMMA_Core::KeyEvent_Right_Shift_Instances.begin(), PMMA_Core::KeyEvent_Right_Shift_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Right_Shift_Instances.end()) {
        PMMA_Core::KeyEvent_Right_Shift_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Right_Control::CPP_KeyEvent_Right_Control() {
    PMMA_Core::KeyEvent_Right_Control_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Right_Control::~CPP_KeyEvent_Right_Control() {
    auto it = find(PMMA_Core::KeyEvent_Right_Control_Instances.begin(), PMMA_Core::KeyEvent_Right_Control_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Right_Control_Instances.end()) {
        PMMA_Core::KeyEvent_Right_Control_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Right_Alt::CPP_KeyEvent_Right_Alt() {
    PMMA_Core::KeyEvent_Right_Alt_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Right_Alt::~CPP_KeyEvent_Right_Alt() {
    auto it = find(PMMA_Core::KeyEvent_Right_Alt_Instances.begin(), PMMA_Core::KeyEvent_Right_Alt_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Right_Alt_Instances.end()) {
        PMMA_Core::KeyEvent_Right_Alt_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Right_Super::CPP_KeyEvent_Right_Super() {
    PMMA_Core::KeyEvent_Right_Super_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Right_Super::~CPP_KeyEvent_Right_Super() {
    auto it = find(PMMA_Core::KeyEvent_Right_Super_Instances.begin(), PMMA_Core::KeyEvent_Right_Super_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Right_Super_Instances.end()) {
        PMMA_Core::KeyEvent_Right_Super_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Shift::CPP_KeyEvent_Shift() {
    PMMA_Core::KeyEvent_Shift_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Shift::~CPP_KeyEvent_Shift() {
    auto it = find(PMMA_Core::KeyEvent_Shift_Instances.begin(), PMMA_Core::KeyEvent_Shift_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Shift_Instances.end()) {
        PMMA_Core::KeyEvent_Shift_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Control::CPP_KeyEvent_Control() {
    PMMA_Core::KeyEvent_Control_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Control::~CPP_KeyEvent_Control() {
    auto it = find(PMMA_Core::KeyEvent_Control_Instances.begin(), PMMA_Core::KeyEvent_Control_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Control_Instances.end()) {
        PMMA_Core::KeyEvent_Control_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Alt::CPP_KeyEvent_Alt() {
    PMMA_Core::KeyEvent_Alt_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Alt::~CPP_KeyEvent_Alt() {
    auto it = find(PMMA_Core::KeyEvent_Alt_Instances.begin(), PMMA_Core::KeyEvent_Alt_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Alt_Instances.end()) {
        PMMA_Core::KeyEvent_Alt_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Super::CPP_KeyEvent_Super() {
    PMMA_Core::KeyEvent_Super_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Super::~CPP_KeyEvent_Super() {
    auto it = find(PMMA_Core::KeyEvent_Super_Instances.begin(), PMMA_Core::KeyEvent_Super_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Super_Instances.end()) {
        PMMA_Core::KeyEvent_Super_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};

CPP_KeyEvent_Menu::CPP_KeyEvent_Menu() {
    PMMA_Core::KeyEvent_Menu_Instances.push_back(this);

    PMMA_Registry::KeyboardEventInstanceCount++;
};

CPP_KeyEvent_Menu::~CPP_KeyEvent_Menu() {
    auto it = find(PMMA_Core::KeyEvent_Menu_Instances.begin(), PMMA_Core::KeyEvent_Menu_Instances.end(), this);
    if (it != PMMA_Core::KeyEvent_Menu_Instances.end()) {
        PMMA_Core::KeyEvent_Menu_Instances.erase(it);
    }

    PMMA_Registry::KeyboardEventInstanceCount--;
};