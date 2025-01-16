"""
Tests for functions in class SolveDiffusion2D
"""
import pytest
import numpy as np
from diffusion2d import SolveDiffusion2D
from unittest import TestCase
import unittest

class TestDiffusion2D(unittest.TestCase):

    def setUp(self):
        self.solver = SolveDiffusion2D()
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
        assert solver.nx == 10
        assert solver.ny == 50

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
        assert solver.nx == 5
        assert solver.ny == 58

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
        solver.initialize_physical_parameters(d, T_cold, T_hot)

        # Assert
        assert solver.D == d
        assert solver.T_cold == T_cold
        assert solver.T_hot == T_hot
        assert solver.dt == pytest.approx(0.001142, abs=1e-6)


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

        assert u[49][24] == 600.
        assert u[50][24] == 600.
        assert u[49][25] == 600.
        assert u[50][25] == 600.