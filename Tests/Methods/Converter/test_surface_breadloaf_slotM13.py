import pytest
from numpy import pi

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM13 import SlotM13

slotM13_test = list()

other_dict = {
    "[Dimensions]": {
        "Magnet_Thickness": 4,
        "Magnet_Arc_[ED]": 120,
        "MagnetReduction": 1,
    }
}

slotM13_test.append(
    {
        "other_dict": other_dict,
        "W1": 0.5197086425658616,
        "W0": 0.5197086425658616,
        "Rtopm": 0.9726990498218554,
    }
)

other_dict = {
    "[Dimensions]": {
        "Magnet_Thickness": 8,
        "Magnet_Arc_[ED]": 120,
        "MagnetReduction": 7,
    }
}

slotM13_test.append(
    {
        "other_dict": other_dict,
        "W1": 0.5217791949266818,
        "W0": 0.5217791949266818,
        "Rtopm": 0.8382690097619138,
    }
)


class TestComplexRuleSlotM13(object):
    @pytest.mark.parametrize("test_dict", slotM13_test)
    def test_surface_breadloaf_slotM13(self, test_dict):
        """test rule complex"""
        other_dict = test_dict["other_dict"]
        machine = MachineSIPMSM()
        machine.rotor = LamSlotMag()
        machine.rotor.slot = SlotM13()

        machine.rotor.slot.H0 = 0.01
        machine.rotor.slot.H1 = 0.02

        rule = RuleComplex(fct_name="surface_breadloaf_slotM13", folder="MotorCAD")
        # first rule complex use to define a slot
        machine = rule.convert_to_P(
            other_dict, machine, {"ED": (2 / 8) * (pi / 180), "m": 0.001}
        )

        W0 = test_dict["W0"]
        W1 = test_dict["W1"]
        Rtopm = test_dict["Rtopm"]

        msg = f"{machine.rotor.slot.W0} expected {W0}"
        assert machine.rotor.slot.W0 == pytest.approx(W0), msg
        msg = f"{machine.rotor.slot.W1} expected {W1}"
        assert machine.rotor.slot.W1 == pytest.approx(W1), msg
        msg = f"{machine.rotor.slot.Rtopm} expected {Rtopm}"
        assert machine.rotor.slot.Rtopm == pytest.approx(Rtopm), msg


if __name__ == "__main__":
    a = TestComplexRuleSlotM13()
    for test_dict in slotM13_test:
        a.test_surface_breadloaf_slotM13(test_dict)
    print("Test Done")
