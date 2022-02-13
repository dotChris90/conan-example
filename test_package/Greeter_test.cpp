#include "gtest/gtest.h"
#include "Greeter.hpp"

// Demonstrate some basic assertions.
TEST(GreeterTest, BasicAssertions) {
  
  conan::Greeter greeter;
  EXPECT_STREQ(greeter.Greet("ABC!").c_str(),"Hello ABC!");

}