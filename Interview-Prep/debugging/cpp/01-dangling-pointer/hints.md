# Hints — dangling reference

1. What is the lifetime of `message` inside `greeting`? When is it destroyed?
2. The function returns `const std::string&`. After the function returns, does
   the thing it refers to still exist?
3. `-Wall -Wextra` may warn: *"reference to local variable returned"*.
4. AddressSanitizer will report a **stack-use-after-return**.
5. Fix: return **by value** (`std::string`, not `const std::string&`). Return
   value optimization / move makes this cheap — there's no extra copy to fear.
