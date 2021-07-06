#include <torch/extension.h>
#include <vector>
#include <iostream>
#include <cstdint>
#include <cstring>
#include "filr2.hpp"


using namespace std;








void printSharedString(const std::string s){
  std::shared_ptr<const std::string > pass = make_shared<const std::string>(s); 
  calling(pass);
}
PYBIND11_MODULE(TORCH_EXTENSION_NAME, m){
        m.def("printSharedString",torch::wrap_pybind_function(printSharedString),
        "Test to pass string pointer to a function of external library");
}