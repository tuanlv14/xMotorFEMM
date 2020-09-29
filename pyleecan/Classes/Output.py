# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/Output.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/Output
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Output.Output.getter.get_angle_rotor import get_angle_rotor
except ImportError as error:
    get_angle_rotor = error

try:
    from ..Methods.Output.Output.getter.get_BH_rotor import get_BH_rotor
except ImportError as error:
    get_BH_rotor = error

try:
    from ..Methods.Output.Output.getter.get_BH_stator import get_BH_stator
except ImportError as error:
    get_BH_stator = error

try:
    from ..Methods.Output.Output.getter.get_path_result import get_path_result
except ImportError as error:
    get_path_result = error

try:
    from ..Methods.Output.Output.plot.Magnetic.plot_B_space import plot_B_space
except ImportError as error:
    plot_B_space = error

try:
    from ..Methods.Output.Output.plot.plot_A_cfft2 import plot_A_cfft2
except ImportError as error:
    plot_A_cfft2 = error

try:
    from ..Methods.Output.Output.plot.plot_A_fft2 import plot_A_fft2
except ImportError as error:
    plot_A_fft2 = error

try:
    from ..Methods.Output.Output.plot.plot_A_space import plot_A_space
except ImportError as error:
    plot_A_space = error

try:
    from ..Methods.Output.Output.plot.plot_A_surf import plot_A_surf
except ImportError as error:
    plot_A_surf = error

try:
    from ..Methods.Output.Output.plot.plot_A_time import plot_A_time
except ImportError as error:
    plot_A_time = error

try:
    from ..Methods.Output.Output.plot.plot_A_time_space import plot_A_time_space
except ImportError as error:
    plot_A_time_space = error

try:
    from ..Methods.Output.Output.plot.Structural.plot_force_space import (
        plot_force_space,
    )
except ImportError as error:
    plot_force_space = error

try:
    from ..Methods.Output.Output.plot.plot_A_quiver_2D import plot_A_quiver_2D
except ImportError as error:
    plot_A_quiver_2D = error

try:
    from ..Methods.Output.Output.getter.get_rot_dir import get_rot_dir
except ImportError as error:
    get_rot_dir = error

try:
    from ..Methods.Output.Output.getter.get_angle_offset_initial import (
        get_angle_offset_initial,
    )
except ImportError as error:
    get_angle_offset_initial = error

try:
    from ..Methods.Output.Output.plot.plot_A_fft_space import plot_A_fft_space
except ImportError as error:
    plot_A_fft_space = error

try:
    from ..Methods.Output.Output.plot.plot_A_fft_time import plot_A_fft_time
except ImportError as error:
    plot_A_fft_time = error


from ._check import InitUnKnowClassError
from .Simulation import Simulation
from .OutGeo import OutGeo
from .OutElec import OutElec
from .OutMag import OutMag
from .OutStruct import OutStruct
from .OutPost import OutPost
from .OutForce import OutForce
from .OutLoss import OutLoss


class Output(FrozenClass):
    """Main Output object: gather all the outputs of all the modules"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Output.Output.getter.get_angle_rotor
    if isinstance(get_angle_rotor, ImportError):
        get_angle_rotor = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method get_angle_rotor: " + str(get_angle_rotor)
                )
            )
        )
    else:
        get_angle_rotor = get_angle_rotor
    # cf Methods.Output.Output.getter.get_BH_rotor
    if isinstance(get_BH_rotor, ImportError):
        get_BH_rotor = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method get_BH_rotor: " + str(get_BH_rotor)
                )
            )
        )
    else:
        get_BH_rotor = get_BH_rotor
    # cf Methods.Output.Output.getter.get_BH_stator
    if isinstance(get_BH_stator, ImportError):
        get_BH_stator = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method get_BH_stator: " + str(get_BH_stator)
                )
            )
        )
    else:
        get_BH_stator = get_BH_stator
    # cf Methods.Output.Output.getter.get_path_result
    if isinstance(get_path_result, ImportError):
        get_path_result = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method get_path_result: " + str(get_path_result)
                )
            )
        )
    else:
        get_path_result = get_path_result
    # cf Methods.Output.Output.plot.Magnetic.plot_B_space
    if isinstance(plot_B_space, ImportError):
        plot_B_space = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method plot_B_space: " + str(plot_B_space)
                )
            )
        )
    else:
        plot_B_space = plot_B_space
    # cf Methods.Output.Output.plot.plot_A_cfft2
    if isinstance(plot_A_cfft2, ImportError):
        plot_A_cfft2 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method plot_A_cfft2: " + str(plot_A_cfft2)
                )
            )
        )
    else:
        plot_A_cfft2 = plot_A_cfft2
    # cf Methods.Output.Output.plot.plot_A_fft2
    if isinstance(plot_A_fft2, ImportError):
        plot_A_fft2 = property(
            fget=lambda x: raise_(
                ImportError("Can't use Output method plot_A_fft2: " + str(plot_A_fft2))
            )
        )
    else:
        plot_A_fft2 = plot_A_fft2
    # cf Methods.Output.Output.plot.plot_A_space
    if isinstance(plot_A_space, ImportError):
        plot_A_space = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method plot_A_space: " + str(plot_A_space)
                )
            )
        )
    else:
        plot_A_space = plot_A_space
    # cf Methods.Output.Output.plot.plot_A_surf
    if isinstance(plot_A_surf, ImportError):
        plot_A_surf = property(
            fget=lambda x: raise_(
                ImportError("Can't use Output method plot_A_surf: " + str(plot_A_surf))
            )
        )
    else:
        plot_A_surf = plot_A_surf
    # cf Methods.Output.Output.plot.plot_A_time
    if isinstance(plot_A_time, ImportError):
        plot_A_time = property(
            fget=lambda x: raise_(
                ImportError("Can't use Output method plot_A_time: " + str(plot_A_time))
            )
        )
    else:
        plot_A_time = plot_A_time
    # cf Methods.Output.Output.plot.plot_A_time_space
    if isinstance(plot_A_time_space, ImportError):
        plot_A_time_space = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method plot_A_time_space: "
                    + str(plot_A_time_space)
                )
            )
        )
    else:
        plot_A_time_space = plot_A_time_space
    # cf Methods.Output.Output.plot.Structural.plot_force_space
    if isinstance(plot_force_space, ImportError):
        plot_force_space = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method plot_force_space: " + str(plot_force_space)
                )
            )
        )
    else:
        plot_force_space = plot_force_space
    # cf Methods.Output.Output.plot.plot_A_quiver_2D
    if isinstance(plot_A_quiver_2D, ImportError):
        plot_A_quiver_2D = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method plot_A_quiver_2D: " + str(plot_A_quiver_2D)
                )
            )
        )
    else:
        plot_A_quiver_2D = plot_A_quiver_2D
    # cf Methods.Output.Output.getter.get_rot_dir
    if isinstance(get_rot_dir, ImportError):
        get_rot_dir = property(
            fget=lambda x: raise_(
                ImportError("Can't use Output method get_rot_dir: " + str(get_rot_dir))
            )
        )
    else:
        get_rot_dir = get_rot_dir
    # cf Methods.Output.Output.getter.get_angle_offset_initial
    if isinstance(get_angle_offset_initial, ImportError):
        get_angle_offset_initial = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method get_angle_offset_initial: "
                    + str(get_angle_offset_initial)
                )
            )
        )
    else:
        get_angle_offset_initial = get_angle_offset_initial
    # cf Methods.Output.Output.plot.plot_A_fft_space
    if isinstance(plot_A_fft_space, ImportError):
        plot_A_fft_space = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method plot_A_fft_space: " + str(plot_A_fft_space)
                )
            )
        )
    else:
        plot_A_fft_space = plot_A_fft_space
    # cf Methods.Output.Output.plot.plot_A_fft_time
    if isinstance(plot_A_fft_time, ImportError):
        plot_A_fft_time = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Output method plot_A_fft_time: " + str(plot_A_fft_time)
                )
            )
        )
    else:
        plot_A_fft_time = plot_A_fft_time
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class"""
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        simu=-1,
        path_res="",
        geo=-1,
        elec=-1,
        mag=-1,
        struct=-1,
        post=-1,
        logger_name="Pyleecan.Output",
        force=-1,
        loss=-1,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "simu" in list(init_dict.keys()):
                simu = init_dict["simu"]
            if "path_res" in list(init_dict.keys()):
                path_res = init_dict["path_res"]
            if "geo" in list(init_dict.keys()):
                geo = init_dict["geo"]
            if "elec" in list(init_dict.keys()):
                elec = init_dict["elec"]
            if "mag" in list(init_dict.keys()):
                mag = init_dict["mag"]
            if "struct" in list(init_dict.keys()):
                struct = init_dict["struct"]
            if "post" in list(init_dict.keys()):
                post = init_dict["post"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "force" in list(init_dict.keys()):
                force = init_dict["force"]
            if "loss" in list(init_dict.keys()):
                loss = init_dict["loss"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.simu = simu
        self.path_res = path_res
        self.geo = geo
        self.elec = elec
        self.mag = mag
        self.struct = struct
        self.post = post
        self.logger_name = logger_name
        self.force = force
        self.loss = loss

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Output_str = ""
        if self.parent is None:
            Output_str += "parent = None " + linesep
        else:
            Output_str += "parent = " + str(type(self.parent)) + " object" + linesep
        if self.simu is not None:
            tmp = self.simu.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Output_str += "simu = " + tmp
        else:
            Output_str += "simu = None" + linesep + linesep
        Output_str += 'path_res = "' + str(self.path_res) + '"' + linesep
        if self.geo is not None:
            tmp = self.geo.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Output_str += "geo = " + tmp
        else:
            Output_str += "geo = None" + linesep + linesep
        if self.elec is not None:
            tmp = self.elec.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Output_str += "elec = " + tmp
        else:
            Output_str += "elec = None" + linesep + linesep
        if self.mag is not None:
            tmp = self.mag.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Output_str += "mag = " + tmp
        else:
            Output_str += "mag = None" + linesep + linesep
        if self.struct is not None:
            tmp = self.struct.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Output_str += "struct = " + tmp
        else:
            Output_str += "struct = None" + linesep + linesep
        if self.post is not None:
            tmp = self.post.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Output_str += "post = " + tmp
        else:
            Output_str += "post = None" + linesep + linesep
        Output_str += 'logger_name = "' + str(self.logger_name) + '"' + linesep
        if self.force is not None:
            tmp = self.force.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Output_str += "force = " + tmp
        else:
            Output_str += "force = None" + linesep + linesep
        if self.loss is not None:
            tmp = self.loss.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Output_str += "loss = " + tmp
        else:
            Output_str += "loss = None" + linesep + linesep
        return Output_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.simu != self.simu:
            return False
        if other.path_res != self.path_res:
            return False
        if other.geo != self.geo:
            return False
        if other.elec != self.elec:
            return False
        if other.mag != self.mag:
            return False
        if other.struct != self.struct:
            return False
        if other.post != self.post:
            return False
        if other.logger_name != self.logger_name:
            return False
        if other.force != self.force:
            return False
        if other.loss != self.loss:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)"""

        Output_dict = dict()
        if self.simu is None:
            Output_dict["simu"] = None
        else:
            Output_dict["simu"] = self.simu.as_dict()
        Output_dict["path_res"] = self.path_res
        if self.geo is None:
            Output_dict["geo"] = None
        else:
            Output_dict["geo"] = self.geo.as_dict()
        if self.elec is None:
            Output_dict["elec"] = None
        else:
            Output_dict["elec"] = self.elec.as_dict()
        if self.mag is None:
            Output_dict["mag"] = None
        else:
            Output_dict["mag"] = self.mag.as_dict()
        if self.struct is None:
            Output_dict["struct"] = None
        else:
            Output_dict["struct"] = self.struct.as_dict()
        if self.post is None:
            Output_dict["post"] = None
        else:
            Output_dict["post"] = self.post.as_dict()
        Output_dict["logger_name"] = self.logger_name
        if self.force is None:
            Output_dict["force"] = None
        else:
            Output_dict["force"] = self.force.as_dict()
        if self.loss is None:
            Output_dict["loss"] = None
        else:
            Output_dict["loss"] = self.loss.as_dict()
        # The class name is added to the dict fordeserialisation purpose
        Output_dict["__class__"] = "Output"
        return Output_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.simu is not None:
            self.simu._set_None()
        self.path_res = None
        if self.geo is not None:
            self.geo._set_None()
        if self.elec is not None:
            self.elec._set_None()
        if self.mag is not None:
            self.mag._set_None()
        if self.struct is not None:
            self.struct._set_None()
        if self.post is not None:
            self.post._set_None()
        self.logger_name = None
        if self.force is not None:
            self.force._set_None()
        if self.loss is not None:
            self.loss._set_None()

    def _get_simu(self):
        """getter of simu"""
        return self._simu

    def _set_simu(self, value):
        """setter of simu"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "simu")
            value = class_obj(init_dict=value)
        elif value is -1:  # Default constructor
            value = Simulation()
        check_var("simu", value, "Simulation")
        self._simu = value

        if self._simu is not None:
            self._simu.parent = self

    simu = property(
        fget=_get_simu,
        fset=_set_simu,
        doc=u"""Simulation object that generated the Output

        :Type: Simulation
        """,
    )

    def _get_path_res(self):
        """getter of path_res"""
        return self._path_res

    def _set_path_res(self, value):
        """setter of path_res"""
        check_var("path_res", value, "str")
        self._path_res = value

    path_res = property(
        fget=_get_path_res,
        fset=_set_path_res,
        doc=u"""Path to the folder to same the results

        :Type: str
        """,
    )

    def _get_geo(self):
        """getter of geo"""
        return self._geo

    def _set_geo(self, value):
        """setter of geo"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "geo")
            value = class_obj(init_dict=value)
        elif value is -1:  # Default constructor
            value = OutGeo()
        check_var("geo", value, "OutGeo")
        self._geo = value

        if self._geo is not None:
            self._geo.parent = self

    geo = property(
        fget=_get_geo,
        fset=_set_geo,
        doc=u"""Geometry output

        :Type: OutGeo
        """,
    )

    def _get_elec(self):
        """getter of elec"""
        return self._elec

    def _set_elec(self, value):
        """setter of elec"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "elec")
            value = class_obj(init_dict=value)
        elif value is -1:  # Default constructor
            value = OutElec()
        check_var("elec", value, "OutElec")
        self._elec = value

        if self._elec is not None:
            self._elec.parent = self

    elec = property(
        fget=_get_elec,
        fset=_set_elec,
        doc=u"""Electrical module output

        :Type: OutElec
        """,
    )

    def _get_mag(self):
        """getter of mag"""
        return self._mag

    def _set_mag(self, value):
        """setter of mag"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "mag")
            value = class_obj(init_dict=value)
        elif value is -1:  # Default constructor
            value = OutMag()
        check_var("mag", value, "OutMag")
        self._mag = value

        if self._mag is not None:
            self._mag.parent = self

    mag = property(
        fget=_get_mag,
        fset=_set_mag,
        doc=u"""Magnetic module output

        :Type: OutMag
        """,
    )

    def _get_struct(self):
        """getter of struct"""
        return self._struct

    def _set_struct(self, value):
        """setter of struct"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "struct"
            )
            value = class_obj(init_dict=value)
        elif value is -1:  # Default constructor
            value = OutStruct()
        check_var("struct", value, "OutStruct")
        self._struct = value

        if self._struct is not None:
            self._struct.parent = self

    struct = property(
        fget=_get_struct,
        fset=_set_struct,
        doc=u"""Structural module output

        :Type: OutStruct
        """,
    )

    def _get_post(self):
        """getter of post"""
        return self._post

    def _set_post(self, value):
        """setter of post"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "post")
            value = class_obj(init_dict=value)
        elif value is -1:  # Default constructor
            value = OutPost()
        check_var("post", value, "OutPost")
        self._post = value

        if self._post is not None:
            self._post.parent = self

    post = property(
        fget=_get_post,
        fset=_set_post,
        doc=u"""Post-Processing settings

        :Type: OutPost
        """,
    )

    def _get_logger_name(self):
        """getter of logger_name"""
        return self._logger_name

    def _set_logger_name(self, value):
        """setter of logger_name"""
        check_var("logger_name", value, "str")
        self._logger_name = value

    logger_name = property(
        fget=_get_logger_name,
        fset=_set_logger_name,
        doc=u"""Name of the logger to use

        :Type: str
        """,
    )

    def _get_force(self):
        """getter of force"""
        return self._force

    def _set_force(self, value):
        """setter of force"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "force"
            )
            value = class_obj(init_dict=value)
        elif value is -1:  # Default constructor
            value = OutForce()
        check_var("force", value, "OutForce")
        self._force = value

        if self._force is not None:
            self._force.parent = self

    force = property(
        fget=_get_force,
        fset=_set_force,
        doc=u"""Force module output

        :Type: OutForce
        """,
    )

    def _get_loss(self):
        """getter of loss"""
        return self._loss

    def _set_loss(self, value):
        """setter of loss"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class("pyleecan.Classes", value.get("__class__"), "loss")
            value = class_obj(init_dict=value)
        elif value is -1:  # Default constructor
            value = OutLoss()
        check_var("loss", value, "OutLoss")
        self._loss = value

        if self._loss is not None:
            self._loss.parent = self

    loss = property(
        fget=_get_loss,
        fset=_set_loss,
        doc=u"""Loss module output

        :Type: OutLoss
        """,
    )
