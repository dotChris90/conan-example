#pragma once

#ifdef WIN32
  #define abc_EXPORT __declspec(dllexport)
#else
  #define abc_EXPORT
#endif

abc_EXPORT void fcn();
