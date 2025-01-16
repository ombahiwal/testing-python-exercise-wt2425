# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

#### Step 2, initial test
```
============================= test session starts ==============================
collecting ... collected 4 items

test_diffusion2d_functions.py::test_initialize_domain PASSED             [ 25%]
test_diffusion2d_functions.py::test_initialize_domain_test_2 PASSED      [ 50%]
test_diffusion2d_functions.py::test_initialize_physical_parameters PASSED [ 75%]dt = 0.0011428571428571432

test_diffusion2d_functions.py::test_set_initial_condition PASSED         [100%]

============================== 4 passed in 0.22s ===============================
```
#### Step 2, fail on purpose
```
============================= test session starts ==============================
collecting ... collected 4 items

test_diffusion2d_functions.py::test_initialize_domain FAILED             [ 25%]
test_diffusion2d_functions.py:7 (test_initialize_domain)
5 != 10

Expected :10
Actual   :5
<Click to see difference>

def test_initialize_domain():
"""
Check function SolveDiffusion2D.initialize_domain
"""
solver = SolveDiffusion2D()
# test values
w = 20.
h = 10.
dx = 2.
dy = 0.2

        # call function
        solver.initialize_domain(w, h, dx, dy)
    
        # assertions
        assert solver.w == w
        assert solver.h == h
        assert solver.dx == dx
        assert solver.dy == dy
    
        # expected op
>       assert solver.nx == 10
E       assert 5 == 10
E        +  where 5 = <diffusion2d.SolveDiffusion2D object at 0x110efd9a0>.nx

test_diffusion2d_functions.py:29: AssertionError

test_diffusion2d_functions.py::test_initialize_domain_test_2 FAILED      [ 50%]
test_diffusion2d_functions.py:31 (test_initialize_domain_test_2)
6 != 5

Expected :5
Actual   :6
<Click to see difference>

def test_initialize_domain_test_2():
"""
Second testcase for function SolveDiffusion2D.initialize_domain
"""
solver = SolveDiffusion2D()
# Arrange test values
# bad values
    
    w = 15.2
    h = 17.1
    dx = 2.7
    dy = 0.29

        # Act (= Perform test action)
        solver.initialize_domain(w, h, dx, dy)
    
        # assersions
        assert solver.w == w
        assert solver.h == h
        assert solver.dx == dx
        assert solver.dy == dy
    
        # expected op
>       assert solver.nx == 5
E       assert 6 == 5
E        +  where 6 = <diffusion2d.SolveDiffusion2D object at 0x111843460>.nx

test_diffusion2d_functions.py:54: AssertionError

test_diffusion2d_functions.py::test_initialize_physical_parameters PASSED [ 75%]dt = 0.0011428571428571432

test_diffusion2d_functions.py::test_set_initial_condition PASSED         [100%]

========================= 2 failed, 2 passed in 0.30s ==========================

Process finished with exit code 1
```

### unittest log

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
