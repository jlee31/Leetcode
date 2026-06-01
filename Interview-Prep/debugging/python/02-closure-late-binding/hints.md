# Hints — closures capture variables, not values (late binding)

1. The lambda closes over the *variable* `i`, not the value `i` had when the
   lambda was created.
2. By the time you *call* any lambda, the loop has finished and `i == 2`. So all
   three print `20`.
3. Fix A — bind the current value as a default argument (evaluated at def time):
   ```python
   funcs.append(lambda x, i=i: x * i)
   ```
4. Fix B — use a factory function so each `i` lives in its own scope:
   ```python
   def multiplier(i):
       return lambda x: x * i
   funcs.append(multiplier(i))
   ```
5. This is "late binding". Same gotcha bites generator expressions and any
   deferred callable created in a loop.
