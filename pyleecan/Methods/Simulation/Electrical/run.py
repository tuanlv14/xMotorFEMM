from numpy.lib.shape_base import expand_dims
from ....Methods.Simulation.Input import InputError
from ....Classes.EEC_SCIM import EEC_SCIM
from ....Classes.EEC_PMSM import EEC_PMSM
from ....Classes.MachineSCIM import MachineSCIM
from ....Classes.MachineSIPMSM import MachineSIPMSM
from ....Classes.MachineIPMSM import MachineIPMSM


def run(self):
    """Run the Electrical module"""
    if self.parent is None:
        raise InputError("The Electrical object must be in a Simulation object to run")
    if self.parent.parent is None:
        raise InputError("The Simulation object must be in an Output object to run")

    self.get_logger().info("Starting Electric module")

    output = self.parent.parent

    machine = output.simu.machine

    if self.eec is None:
        # Init EEC depending on machine type
        if isinstance(machine, MachineSCIM):
            self.eec = EEC_SCIM()
        elif isinstance(machine, (MachineSIPMSM, MachineIPMSM)):
            self.eec = EEC_PMSM()

    else:
        # Check that EEC is consistent with machine type
        if isinstance(machine, MachineSCIM) and not isinstance(self.eec, EEC_SCIM):
            raise Exception(
                "Cannot run Electrical model if machine is SCIM and eec is not EEC_SCIM"
            )
        elif isinstance(machine, (MachineSIPMSM, MachineIPMSM)) and not isinstance(
            self.eec, EEC_PMSM
        ):
            raise Exception(
                "Cannot run Electrical model if machine is PMSM and eec is not EEC_PMSM"
            )

    # Compute and store time and angle axes from elec output
    # and returns additional axes in axes_dict
    if output.elec.Time is not None and output.elec.Angle is not None:
        axes_dict = {"time": output.elec.Time, "angle": output.elec.Angle}
    else:
        raise Exception("Time and Angle must not be None in Electrical.run()")

    # Generate drive
    # self.eec.gen_drive(output)

    if self.ELUT_enforced is not None:
        # enforce parameters of EEC coming from enforced ELUT at right temperatures
        self.eec.parameters = self.ELUT_enforced.get_param_dict()

    # Compute parameters of the electrical equivalent circuit if some parameters are missing in ELUT
    out_dict = self.eec.comp_parameters(output, Tsta=self.Tsta, Trot=self.Trot)

    # Solve the electrical equivalent circuit
    out_dict = self.eec.solve_EEC(output)

    # Compute losses due to Joule effects
    out_dict = self.eec.comp_joule_losses(output)

    # Compute electromagnetic power
    out_dict = self.comp_power(output)

    # Compute torque
    out_dict = self.comp_torque(output)

    # Store electrical quantities contained in out_dict in OutElec, as Data object if necessary
    out_dict.store(out_dict, axes_dict)
