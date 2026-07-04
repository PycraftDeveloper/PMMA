#pragma once
#include "PMMA_Exports.hpp"

#include "Internal/Events/EventsManager.hpp"
#include "Internal/Events/InternalEvents.hpp"

namespace PMMA::Events {
class EXPORT KeyPad_0 : public PMMA::Internal::Events::ButtonPressed {
public:
    KeyPad_0();
    ~KeyPad_0();
};

class EXPORT KeyPad_1 : public PMMA::Internal::Events::ButtonPressed {
public:
    KeyPad_1();
    ~KeyPad_1();
};

class EXPORT KeyPad_2 : public PMMA::Internal::Events::ButtonPressed {
public:
    KeyPad_2();
    ~KeyPad_2();
};

class EXPORT KeyPad_3 : public PMMA::Internal::Events::ButtonPressed {
public:
    KeyPad_3();
    ~KeyPad_3();
};

class EXPORT KeyPad_4 : public PMMA::Internal::Events::ButtonPressed {
public:
    KeyPad_4();
    ~KeyPad_4();
};

class EXPORT KeyPad_5 : public PMMA::Internal::Events::ButtonPressed {
public:
    KeyPad_5();
    ~KeyPad_5();
};

class EXPORT KeyPad_6 : public PMMA::Internal::Events::ButtonPressed {
public:
    KeyPad_6();
    ~KeyPad_6();
};

class EXPORT KeyPad_7 : public PMMA::Internal::Events::ButtonPressed {
public:
    KeyPad_7();
    ~KeyPad_7();
};

class EXPORT KeyPad_8 : public PMMA::Internal::Events::ButtonPressed {
public:
    KeyPad_8();
    ~KeyPad_8();
};

class EXPORT KeyPad_9 : public PMMA::Internal::Events::ButtonPressed {
public:
    KeyPad_9();
    ~KeyPad_9();
};

class EXPORT KeyPad_Decimal : public PMMA::Internal::Events::ButtonPressed {
public:
    KeyPad_Decimal();
    ~KeyPad_Decimal();
};

class EXPORT KeyPad_Divide : public PMMA::Internal::Events::ButtonPressed {
public:
    KeyPad_Divide();
    ~KeyPad_Divide();
};

class EXPORT KeyPad_Multiply : public PMMA::Internal::Events::ButtonPressed {
public:
    KeyPad_Multiply();
    ~KeyPad_Multiply();
};

class EXPORT KeyPad_Subtract : public PMMA::Internal::Events::ButtonPressed {
public:
    KeyPad_Subtract();
    ~KeyPad_Subtract();
};

class EXPORT KeyPad_Add : public PMMA::Internal::Events::ButtonPressed {
public:
    KeyPad_Add();
    ~KeyPad_Add();
};

class EXPORT KeyPad_Enter : public PMMA::Internal::Events::ButtonPressed {
public:
    KeyPad_Enter();
    ~KeyPad_Enter();
};

class EXPORT KeyPad_Equal : public PMMA::Internal::Events::ButtonPressed {
public:
    KeyPad_Equal();
    ~KeyPad_Equal();
};
}