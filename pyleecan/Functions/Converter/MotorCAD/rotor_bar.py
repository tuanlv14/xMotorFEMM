def other_to_P(self, machine, other_dict, other_unit_dict):
    """Converts motor-cad notch into pyleecan notch slotM19

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    machine : Machine
        A pyleecan machine
    other_dict : dict
        A dict with the conversion obj machine
    other_unit_dict : dict
        dict with unit to make conversion (key: unit family, value: factor)

    Returns
    ---------
    machine : Machine
        A pyleecan machine
    """
    self.unit_type = "m"
    other_path_list = ["[Dimensions]", "EndRing_Inner_Add_F"]
    H0 = self.get_other(other_dict, other_path_list, other_unit_dict)

    self.unit_type = "m"
    other_path_list = ["[Dimensions]", "EndRing_Outer_Add_F"]
    H1 = self.get_other(other_dict, other_path_list, other_unit_dict)

    H = machine.rotor.slot.comp_height()

    machine.rotor.Hscr = H + H0 + H1
    machine.rotor.winding.Lewout = 0
    return machine


def P_to_other(self, machine, other_dict, other_unit_dict=None):
    """conversion obj machine in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    machine : Machine
        A pyleecan machine
    other_dict : dict
        A dict with the conversion obj machine
    other_unit_dict : dict
        dict with unit to make conversion (key: unit family, value: factor)


    Returns
    ---------
    other_dict : dict
        A dict with the conversion obj machine
    """

    return other_dict
