# -*- coding: utf-8 -*-
import numpy as np
import pytest

from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.Interpolation import Interpolation
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.RefSegmentP1 import RefSegmentP1
from pyleecan.Classes.RefTriangle3 import RefTriangle3


@pytest.mark.MeshSol
def test_line():
    DELTA = 1e-10

    mesh = MeshMat()
    mesh.element["line"] = ElementMat(nb_node_per_element=2)
    mesh.node = NodeMat()
    mesh.node.add_node(np.array([0, 0]))
    mesh.node.add_node(np.array([1, 0]))
    mesh.node.add_node(np.array([0, 1]))

    mesh.add_element(np.array([0, 1]), "line")
    mesh.add_element(np.array([0, 2]), "line")
    mesh.add_element(np.array([1, 2]), "line")

    c_line = mesh.element["line"]

    c_line.interpolation = Interpolation()
    c_line.interpolation.ref_element = RefSegmentP1()

    # This node is inside
    test_pt = np.array([[0.7, 0]])
    sol = 0
    elements = mesh.find_element(test_pt)[0][1]
    testA = np.sum(abs(elements - sol))
    msg = "Wrong result: returned " + str(elements) + ", expected: " + str(sol)
    assert testA == pytest.approx(0, abs=DELTA), msg

    # This node is outside but in the error margin, so it is considered "inside"
    test_pt = np.array([[0.0001, 0.4]])
    sol = 1
    elements = mesh.find_element(test_pt)[0][1]
    testA = np.sum(abs(elements - sol))
    msg = "Wrong result: returned " + str(elements) + ", expected: " + str(sol)
    assert testA == pytest.approx(0, abs=DELTA), msg

    # This node is outside any element, so it must return None
    test_pt = np.array([[0.1, 0.4]])
    elements = mesh.find_element(test_pt)
    testA = elements == [None]
    msg = "Wrong result: returned " + str(elements) + ", expected: " + str([None])
    assert testA is True


@pytest.mark.MeshSol
def test_triangle3():
    DELTA = 1e-10

    mesh = MeshMat(dimension=2)
    mesh.node = NodeMat()
    mesh.node.add_node(np.array([0, 0]))
    mesh.node.add_node(np.array([2, 0]))
    mesh.node.add_node(np.array([2, 2]))
    mesh.node.add_node(np.array([0, 2]))

    mesh.element["triangle"] = ElementMat(nb_node_per_element=3)
    mesh.add_element(np.array([0, 1, 2]), "triangle")
    mesh.add_element(np.array([0, 3, 2]), "triangle")

    c_tgl = mesh.element["triangle"]
    c_tgl.interpolation = Interpolation()
    c_tgl.interpolation.ref_element = RefTriangle3()

    # This node is inside element 0
    test_pt = np.array([[1, 0.5]])
    sol = 0
    elements = mesh.find_element(test_pt)[0][1]
    testA = np.sum(abs(elements - sol))
    msg = "Wrong result: returned " + str(elements) + ", expected: " + str(sol)
    assert testA == pytest.approx(0, abs=DELTA), msg

    # This node is inside element 1
    test_pt = np.array([[0.5, 1]])
    sol = 1
    elements = mesh.find_element(test_pt)[0][1]
    testA = np.sum(abs(elements - sol))
    msg = "Wrong result: returned " + str(elements) + ", expected: " + str(sol)
    assert testA == pytest.approx(0, abs=DELTA), msg

    # This node is outside but in the error margin, so it is considered "inside"
    test_pt = np.array([[-0.0001, 0.4]])
    sol = 1
    elements = mesh.find_element(test_pt)[0][1]
    testA = np.sum(abs(elements - sol))
    msg = "Wrong result: returned " + str(elements) + ", expected: " + str(sol)
    assert testA == pytest.approx(0, abs=DELTA), msg

    # This node is outside any element, so it must return None
    test_pt = np.array([[-0.1, 10]])
    elements = mesh.find_element(test_pt)
    testA = elements == [None]
    msg = "Wrong result: returned " + str(elements) + ", expected: " + str([None])
    assert testA is True


if __name__ == "__main__":
    test_line()
    test_triangle3()
