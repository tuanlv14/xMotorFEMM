def convert_slot_to_other(self):
    """Selection correct slot and implementation in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """

    # Single type
    # Signle set

    # conversion to pyleecan
    slot_type = type(self.machine.stator.slot).__name__

    # selection type of Slot
    if slot_type == "SlotW11":
        name_slot = "Parallel_Tooth"

    elif slot_type == "SlotW14":
        name_slot = "Parallel_tooth_SqB"

    elif slot_type == "SlotW21":
        name_slot = "Parallel_Slot"

    elif slot_type == "SlotW23":
        name_slot = "Tapered_slot"

    elif slot_type == "SlotW29":
        name_slot = "Form_Wound"

    else:
        raise NotImplementedError(
            f"Type of slot {name_slot} has not equivalent or has not implement"
        )
    self.get_logger().info(f"Conversion {slot_type} into {name_slot}")

    # writting in dict
    if "[Calc_Options]" not in self.other_dict:
        self.other_dict["[Calc_Options]"] = {"Slot_Type": name_slot}
    else:
        self.other_dict["[Calc_Options]"]["Slot_Type"] = name_slot
