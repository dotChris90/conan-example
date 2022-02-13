#include "Greeter.hpp"
#include "boost/format.hpp"

namespace conan
{
    Greeter::Greeter(/* args */) {
        
    }
    
    Greeter::~Greeter() {
        
    }
    
    std::string Greeter::Greet(const std::string& name) {
        return  (boost::format("Hello %1%") % name).str();
    }
}