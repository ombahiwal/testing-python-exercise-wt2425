# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

#### Step 3, initial test
```
============================= test session starts ==============================
collecting ... collected 4 items

test_diffusion2d_functions.py::test_initialize_domain PASSED             [ 25%]
test_diffusion2d_functions.py::test_initialize_domain_test_2 PASSED      [ 50%]
test_diffusion2d_functions.py::test_initialize_physical_parameters PASSED [ 75%]dt = 0.0011428571428571432

test_diffusion2d_functions.py::test_set_initial_condition PASSED         [100%]

============================== 4 passed in 0.22s ===============================
```
#### Step 3, fail on purpose
```
============================= test session starts ==============================
collecting ... collected 4 items
#
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
#### Step 4: purposely break all unit tests
```
Launching pytest with arguments /Users/ombahiwal/Desktop/WS24/Courses_WS24/Simulation Software Engineering/Exercises/05_testing_ci/testing-python-exercise-wt2425/tests/unit/test_diffusion2d_functions.py --no-header --no-summary -q in /Users/ombahiwal/Desktop/WS24/Courses_WS24/Simulation Software Engineering/Exercises/05_testing_ci/testing-python-exercise-wt2425/tests/unit

============================= test session starts ==============================
collecting ... collected 4 items

test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain 
test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_domain_test_2 
test_diffusion2d_functions.py::TestDiffusion2D::test_initialize_physical_parameters 
test_diffusion2d_functions.py::TestDiffusion2D::test_set_initial_condition 

============================== 4 failed in 0.28s ===============================
FAILED [ 25%]
test_diffusion2d_functions.py:13 (TestDiffusion2D.test_initialize_domain)
5 != 10

Expected :10
Actual   :5
<Click to see difference>

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_domain>

    def test_initialize_domain(self):
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
E        +  where 5 = <diffusion2d.SolveDiffusion2D object at 0x10fe43e80>.nx

test_diffusion2d_functions.py:35: AssertionError
FAILED [ 50%]
test_diffusion2d_functions.py:37 (TestDiffusion2D.test_initialize_domain_test_2)
6 != 5

Expected :5
Actual   :6
<Click to see difference>

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_domain_test_2>

    def test_initialize_domain_test_2(self):
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
E        +  where 6 = <diffusion2d.SolveDiffusion2D object at 0x10fe7cd90>.nx

test_diffusion2d_functions.py:60: AssertionError
FAILED [ 75%]
test_diffusion2d_functions.py:62 (TestDiffusion2D.test_initialize_physical_parameters)
self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_initialize_physical_parameters>

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        # Arrange
        d = 3.5
        T_cold = 342.4
        T_hot = 723.15
        solver.dx = 0.1
        solver.dy = 0.2
    
        # Act
>       solver.initialize_physical_parameters(d, T_cold, T_hot)

test_diffusion2d_functions.py:76: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <diffusion2d.SolveDiffusion2D object at 0x10febfb50>, d = 3.5
T_cold = 342.4, T_hot = 723.15

    def initialize_physical_parameters(self, d=4., T_cold=300, T_hot=700):
        assert type(d) == float, "d must be a float"
        assert type(T_cold) == float, "T_cold must be a float"
        assert type(T_hot) == float, "T_cold must be a float"
        # Purposely break
        # self.D = d
        self.T_cold = T_cold
        self.T_hot = T_hot
    
        # Computing a stable time step
        dx2, dy2 = self.dx * self.dx, self.dy * self.dy
>       self.dt = dx2 * dy2 / (2 * self.D * (dx2 + dy2))
E       TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

../../diffusion2d.py:61: TypeError
FAILED [100%]
test_diffusion2d_functions.py:84 (TestDiffusion2D.test_set_initial_condition)
np.float64(100.0) != 600.0

Expected :600.0
Actual   :np.float64(100.0)
<Click to see difference>

self = <test_diffusion2d_functions.TestDiffusion2D testMethod=test_set_initial_condition>

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        # arranve values
        solver.nx = 100
        solver.ny = 50
        solver.dx = 0.1
        solver.dy = 0.2
        solver.T_cold = 100.
        solver.T_hot = 600.
    
        # call
        u: np.ndarray = solver.set_initial_condition()
    
        # assersion
    
        # Domain has expected dimensions
        assert u.shape[0] == solver.nx
        assert u.shape[1] == solver.ny
    
        # center is hot and border is cold
        assert u[0][0] == 100.
        assert u[99][0] == 100.
        assert u[0][49] == 100.
        assert u[99][49] == 100.
    
>       assert u[49][24] == 600.
E       assert np.float64(100.0) == 600.0

test_diffusion2d_functions.py:113: AssertionError

Process finished with exit code 1

```

### Step 5: Integration pytest
```
============================= test session starts ==============================
collecting ... collected 2 items

test_diffusion2d.py::test_initialize_physical_parameters PASSED          [ 50%]dt = 0.0016666666666666672

test_diffusion2d.py::test_set_initial_condition PASSED                   [100%]dt = 0.09259259259259259


============================== 2 passed in 0.24s ===============================


============================= test session starts ==============================
collecting ... collected 2 items

test_diffusion2d.py::test_initialize_physical_parameters FAILED          [ 50%]
test_diffusion2d.py:7 (test_initialize_physical_parameters)
def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(10., 20., 0.2, 0.1)
>       solver.initialize_physical_parameters(2.4, 0., 1.)

test_diffusion2d.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <diffusion2d.SolveDiffusion2D object at 0x110b00940>, d = 2.4
T_cold = 0.0, T_hot = 1.0

    def initialize_physical_parameters(self, d=4., T_cold=300, T_hot=700):
        assert type(d) == float, "d must be a float"
        assert type(T_cold) == float, "T_cold must be a float"
        assert type(T_hot) == float, "T_cold must be a float"
        # Purposely break
        # self.D = d
        self.T_cold = T_cold
        self.T_hot = T_hot
    
        # Computing a stable time step
        dx2, dy2 = self.dx * self.dx, self.dy * self.dy
>       self.dt = dx2 * dy2 / (2 * self.D * (dx2 + dy2))
E       TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

../../diffusion2d.py:61: TypeError

test_diffusion2d.py::test_set_initial_condition FAILED                   [100%]
test_diffusion2d.py:19 (test_set_initial_condition)
def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(10., 10., 1., 1.)
>       solver.initialize_physical_parameters(2.7, 0., 1.)

test_diffusion2d.py:26: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <diffusion2d.SolveDiffusion2D object at 0x111434bb0>, d = 2.7
T_cold = 0.0, T_hot = 1.0

    def initialize_physical_parameters(self, d=4., T_cold=300, T_hot=700):
        assert type(d) == float, "d must be a float"
        assert type(T_cold) == float, "T_cold must be a float"
        assert type(T_hot) == float, "T_cold must be a float"
        # Purposely break
        # self.D = d
        self.T_cold = T_cold
        self.T_hot = T_hot
    
        # Computing a stable time step
        dx2, dy2 = self.dx * self.dx, self.dy * self.dy
>       self.dt = dx2 * dy2 / (2 * self.D * (dx2 + dy2))
E       TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

../../diffusion2d.py:61: TypeError


============================== 2 failed in 0.27s ===============================

Process finished with exit code 1

```

#### Step 6 : Coverage

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
