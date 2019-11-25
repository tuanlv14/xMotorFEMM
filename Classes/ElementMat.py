# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from os import linesep
from pyleecan.Classes.check import set_array, check_init_dict, check_var, raise_
from pyleecan.Functions.save import save
from pyleecan.Classes.Element import Element

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from pyleecan.Methods.Mesh.ElementMat.get_submesh import get_submesh
except ImportError as error:
    get_submesh = error

try:
    from pyleecan.Methods.Mesh.ElementMat.get_group import get_group
except ImportError as error:
    get_group = error

try:
    from pyleecan.Methods.Mesh.ElementMat.get_node import get_node
except ImportError as error:
    get_node = error

try:
    from pyleecan.Methods.Mesh.ElementMat.get_element import get_element
except ImportError as error:
    get_element = error

try:
    from pyleecan.Methods.Mesh.ElementMat.get_node2element import get_node2element
except ImportError as error:
    get_node2element = error

try:
    from pyleecan.Methods.Mesh.ElementMat.convert_element import convert_element
except ImportError as error:
    convert_element = error


from numpy import array, array_equal
from pyleecan.Classes.check import InitUnKnowClassError


class ElementMat(Element):
    """Define the connectivity under matricial format containing one type of element (example: only triangles with 3 nodes). """

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Mesh.ElementMat.get_submesh
    if isinstance(get_submesh, ImportError):
        get_submesh = property(fget=lambda x: raise_(ImportError("Can't use ElementMat method get_submesh: " + str(get_submesh))))
    else:
        get_submesh = get_submesh
    # cf Methods.Mesh.ElementMat.get_group
    if isinstance(get_group, ImportError):
        get_group = property(fget=lambda x: raise_(ImportError("Can't use ElementMat method get_group: " + str(get_group))))
    else:
        get_group = get_group
    # cf Methods.Mesh.ElementMat.get_node
    if isinstance(get_node, ImportError):
        get_node = property(fget=lambda x: raise_(ImportError("Can't use ElementMat method get_node: " + str(get_node))))
    else:
        get_node = get_node
    # cf Methods.Mesh.ElementMat.get_element
    if isinstance(get_element, ImportError):
        get_element = property(fget=lambda x: raise_(ImportError("Can't use ElementMat method get_element: " + str(get_element))))
    else:
        get_element = get_element
    # cf Methods.Mesh.ElementMat.get_node2element
    if isinstance(get_node2element, ImportError):
        get_node2element = property(fget=lambda x: raise_(ImportError("Can't use ElementMat method get_node2element: " + str(get_node2element))))
    else:
        get_node2element = get_node2element
    # cf Methods.Mesh.ElementMat.convert_element
    if isinstance(convert_element, ImportError):
        convert_element = property(fget=lambda x: raise_(ImportError("Can't use ElementMat method convert_element: " + str(convert_element))))
    else:
        convert_element = convert_element
    # save method is available in all object
    save = save

    def __init__(self, connectivity=None, group=None, nb_elem=None, nb_node_per_element=None, init_dict=None):
        """Constructor of the class. Can be use in two ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary wiht every properties as keys

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_dict is not None:  # Initialisation by dict
            check_init_dict(init_dict, ["connectivity", "group", "nb_elem", "nb_node_per_element"])
            # Overwrite default value with init_dict content
            if "connectivity" in list(init_dict.keys()):
                connectivity = init_dict["connectivity"]
            if "group" in list(init_dict.keys()):
                group = init_dict["group"]
            if "nb_elem" in list(init_dict.keys()):
                nb_elem = init_dict["nb_elem"]
            if "nb_node_per_element" in list(init_dict.keys()):
                nb_node_per_element = init_dict["nb_node_per_element"]
        # Initialisation by argument
        # connectivity can be None, a ndarray or a list
        set_array(self, "connectivity", connectivity)
        # group can be None, a ndarray or a list
        set_array(self, "group", group)
        self.nb_elem = nb_elem
        self.nb_node_per_element = nb_node_per_element
        # Call Element init
        super(ElementMat, self).__init__()
        # The class is frozen (in Element init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        ElementMat_str = ""
        # Get the properties inherited from Element
        ElementMat_str += super(ElementMat, self).__str__() + linesep
        ElementMat_str += "connectivity = " + linesep + str(self.connectivity) + linesep + linesep
        ElementMat_str += "group = " + linesep + str(self.group) + linesep + linesep
        ElementMat_str += "nb_elem = " + str(self.nb_elem) + linesep
        ElementMat_str += "nb_node_per_element = " + str(self.nb_node_per_element)
        return ElementMat_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Element
        if not super(ElementMat, self).__eq__(other):
            return False
        if not array_equal(other.connectivity, self.connectivity):
            return False
        if not array_equal(other.group, self.group):
            return False
        if other.nb_elem != self.nb_elem:
            return False
        if other.nb_node_per_element != self.nb_node_per_element:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Element
        ElementMat_dict = super(ElementMat, self).as_dict()
        if self.connectivity is None:
            ElementMat_dict["connectivity"] = None
        else:
            ElementMat_dict["connectivity"] = self.connectivity.tolist()
        if self.group is None:
            ElementMat_dict["group"] = None
        else:
            ElementMat_dict["group"] = self.group.tolist()
        ElementMat_dict["nb_elem"] = self.nb_elem
        ElementMat_dict["nb_node_per_element"] = self.nb_node_per_element
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        ElementMat_dict["__class__"] = "ElementMat"
        return ElementMat_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.connectivity = None
        self.group = None
        self.nb_elem = None
        self.nb_node_per_element = None
        # Set to None the properties inherited from Element
        super(ElementMat, self)._set_None()

    def _get_connectivity(self):
        """getter of connectivity"""
        return self._connectivity

    def _set_connectivity(self, value):
        """setter of connectivity"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("connectivity", value, "ndarray")
        self._connectivity = value

    # Matrix of connectivity for one element type
    # Type : ndarray
    connectivity = property(fget=_get_connectivity, fset=_set_connectivity,
                            doc=u"""Matrix of connectivity for one element type""")

    def _get_group(self):
        """getter of group"""
        return self._group

    def _set_group(self, value):
        """setter of group"""
        if type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("group", value, "ndarray")
        self._group = value

    # Attribute a number (int) to each subpart of the machine
    # Type : ndarray
    group = property(fget=_get_group, fset=_set_group,
                     doc=u"""Attribute a number (int) to each subpart of the machine""")

    def _get_nb_elem(self):
        """getter of nb_elem"""
        return self._nb_elem

    def _set_nb_elem(self, value):
        """setter of nb_elem"""
        check_var("nb_elem", value, "int")
        self._nb_elem = value

    # Total number of elements
    # Type : int
    nb_elem = property(fget=_get_nb_elem, fset=_set_nb_elem,
                       doc=u"""Total number of elements""")

    def _get_nb_node_per_element(self):
        """getter of nb_node_per_element"""
        return self._nb_node_per_element

    def _set_nb_node_per_element(self, value):
        """setter of nb_node_per_element"""
        check_var("nb_node_per_element", value, "int")
        self._nb_node_per_element = value

    # Define the number of node per element
    # Type : int
    nb_node_per_element = property(fget=_get_nb_node_per_element, fset=_set_nb_node_per_element,
                                   doc=u"""Define the number of node per element""")
