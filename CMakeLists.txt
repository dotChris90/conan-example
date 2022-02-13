cmake_minimum_required(VERSION 3.15)
project(abc CXX)

find_package(Boost REQUIRED COMPONENTS headers
)

add_executable(main     src/fcn.cpp 
                        src/main.cpp
)

add_library(Hello       src/Greeter.cpp
)     

target_link_libraries(Hello Boost::headers
)

set_target_properties(Hello PROPERTIES PUBLIC_HEADER "src/Greeter.hpp"
)

install(TARGETS main DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
)

install(TARGETS Hello DESTINATION "."
        PUBLIC_HEADER DESTINATION include
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )

