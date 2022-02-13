#pragma once

#include <string>

namespace conan {
    class Greeter {
    private:
        /* data */
    public:
        Greeter(/* args */);
        ~Greeter();
        std::string Greet(const std::string& name);
    };
}