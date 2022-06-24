# -*- coding: utf-8 -*-
"""File generated by generate_code() - 
WARNING! All changes made in this file will be lost!
"""

from ..Classes.import_all import *

load_switch = {
    "Arc": Arc,
    "Arc1": Arc1,
    "Arc2": Arc2,
    "Arc3": Arc3,
    "Bore": Bore,
    "BoreFlower": BoreFlower,
    "BoreLSRPM": BoreLSRPM,
    "BoreUD": BoreUD,
    "CellMat": CellMat,
    "Circle": Circle,
    "CondType11": CondType11,
    "CondType12": CondType12,
    "CondType13": CondType13,
    "CondType21": CondType21,
    "CondType22": CondType22,
    "Conductor": Conductor,
    "DXFImport": DXFImport,
    "DataKeeper": DataKeeper,
    "Drive": Drive,
    "DriveWave": DriveWave,
    "EEC": EEC,
    "EEC_LSRPM": EEC_LSRPM,
    "EEC_PMSM": EEC_PMSM,
    "EEC_SCIM": EEC_SCIM,
    "ElecLUTdq": ElecLUTdq,
    "Electrical": Electrical,
    "Elmer": Elmer,
    "ElmerResults": ElmerResults,
    "ElmerResultsVTU": ElmerResultsVTU,
    "EndWinding": EndWinding,
    "EndWindingCirc": EndWindingCirc,
    "EndWindingRect": EndWindingRect,
    "FPGNSeg": FPGNSeg,
    "FPGNTri": FPGNTri,
    "Force": Force,
    "ForceMT": ForceMT,
    "ForceTensor": ForceTensor,
    "Frame": Frame,
    "FrameBar": FrameBar,
    "GUIOption": GUIOption,
    "GaussPoint": GaussPoint,
    "Hole": Hole,
    "HoleM50": HoleM50,
    "HoleM51": HoleM51,
    "HoleM52": HoleM52,
    "HoleM53": HoleM53,
    "HoleM54": HoleM54,
    "HoleM57": HoleM57,
    "HoleM58": HoleM58,
    "HoleMLSRPM": HoleMLSRPM,
    "HoleMag": HoleMag,
    "HoleUD": HoleUD,
    "Import": Import,
    "ImportData": ImportData,
    "ImportGenMatrixSin": ImportGenMatrixSin,
    "ImportGenPWM": ImportGenPWM,
    "ImportGenToothSaw": ImportGenToothSaw,
    "ImportGenVectLin": ImportGenVectLin,
    "ImportGenVectSin": ImportGenVectSin,
    "ImportMatlab": ImportMatlab,
    "ImportMatrix": ImportMatrix,
    "ImportMatrixVal": ImportMatrixVal,
    "ImportMatrixXls": ImportMatrixXls,
    "ImportMeshMat": ImportMeshMat,
    "ImportMeshUnv": ImportMeshUnv,
    "ImportVectorField": ImportVectorField,
    "Input": Input,
    "InputCurrent": InputCurrent,
    "InputFlux": InputFlux,
    "InputForce": InputForce,
    "InputVoltage": InputVoltage,
    "Interpolation": Interpolation,
    "LUT": LUT,
    "LUTdq": LUTdq,
    "LUTslip": LUTslip,
    "LamH": LamH,
    "LamHole": LamHole,
    "LamHoleNS": LamHoleNS,
    "LamSlot": LamSlot,
    "LamSlotMag": LamSlotMag,
    "LamSlotMulti": LamSlotMulti,
    "LamSlotMultiWind": LamSlotMultiWind,
    "LamSlotWind": LamSlotWind,
    "LamSquirrelCage": LamSquirrelCage,
    "LamSquirrelCageMag": LamSquirrelCageMag,
    "Lamination": Lamination,
    "Line": Line,
    "Loss": Loss,
    "LossFEMM": LossFEMM,
    "LossModel": LossModel,
    "LossModelBertotti": LossModelBertotti,
    "LossModelIron": LossModelIron,
    "LossModelJordan": LossModelJordan,
    "LossModelMagnet": LossModelMagnet,
    "LossModelProximity": LossModelProximity,
    "LossModelSteinmetz": LossModelSteinmetz,
    "LossModelWinding": LossModelWinding,
    "Machine": Machine,
    "MachineAsync": MachineAsync,
    "MachineDFIM": MachineDFIM,
    "MachineIPMSM": MachineIPMSM,
    "MachineLSPM": MachineLSPM,
    "MachineSCIM": MachineSCIM,
    "MachineSIPMSM": MachineSIPMSM,
    "MachineSRM": MachineSRM,
    "MachineSyRM": MachineSyRM,
    "MachineSync": MachineSync,
    "MachineUD": MachineUD,
    "MachineWRSM": MachineWRSM,
    "MagElmer": MagElmer,
    "MagFEMM": MagFEMM,
    "Magnet": Magnet,
    "Magnetics": Magnetics,
    "MatEconomical": MatEconomical,
    "MatElectrical": MatElectrical,
    "MatHT": MatHT,
    "MatMagnetics": MatMagnetics,
    "MatStructural": MatStructural,
    "Material": Material,
    "Mesh": Mesh,
    "MeshMat": MeshMat,
    "MeshSolution": MeshSolution,
    "MeshVTK": MeshVTK,
    "Mode": Mode,
    "ModelBH": ModelBH,
    "ModelBH_Langevin": ModelBH_Langevin,
    "ModelBH_arctangent": ModelBH_arctangent,
    "ModelBH_exponential": ModelBH_exponential,
    "ModelBH_linear_sat": ModelBH_linear_sat,
    "NodeMat": NodeMat,
    "Notch": Notch,
    "NotchEvenDist": NotchEvenDist,
    "OP": OP,
    "OPdq": OPdq,
    "OPslip": OPslip,
    "OptiBayesAlg": OptiBayesAlg,
    "OptiBayesAlgSmoot": OptiBayesAlgSmoot,
    "OptiConstraint": OptiConstraint,
    "OptiDesignVar": OptiDesignVar,
    "OptiGenAlg": OptiGenAlg,
    "OptiGenAlgNsga2Deap": OptiGenAlgNsga2Deap,
    "OptiObjective": OptiObjective,
    "OptiProblem": OptiProblem,
    "OptiSolver": OptiSolver,
    "OutElec": OutElec,
    "OutForce": OutForce,
    "OutGeo": OutGeo,
    "OutGeoLam": OutGeoLam,
    "OutInternal": OutInternal,
    "OutLoss": OutLoss,
    "OutLossMinimal": OutLossMinimal,
    "OutLossModel": OutLossModel,
    "OutMag": OutMag,
    "OutMagElmer": OutMagElmer,
    "OutMagFEMM": OutMagFEMM,
    "OutPost": OutPost,
    "OutStruct": OutStruct,
    "Output": Output,
    "ParamExplorer": ParamExplorer,
    "ParamExplorerInterval": ParamExplorerInterval,
    "ParamExplorerSet": ParamExplorerSet,
    "PolarArc": PolarArc,
    "Post": Post,
    "PostFunction": PostFunction,
    "PostLUT": PostLUT,
    "PostMethod": PostMethod,
    "PostPlot": PostPlot,
    "RefCell": RefCell,
    "RefLine3": RefLine3,
    "RefQuad4": RefQuad4,
    "RefQuad9": RefQuad9,
    "RefSegmentP1": RefSegmentP1,
    "RefTriangle3": RefTriangle3,
    "RefTriangle6": RefTriangle6,
    "ScalarProduct": ScalarProduct,
    "ScalarProductL2": ScalarProductL2,
    "Section": Section,
    "Segment": Segment,
    "Shaft": Shaft,
    "Simu1": Simu1,
    "Simulation": Simulation,
    "Skew": Skew,
    "SliceModel": SliceModel,
    "Slot": Slot,
    "Slot19": Slot19,
    "SlotCirc": SlotCirc,
    "SlotDC": SlotDC,
    "SlotM10": SlotM10,
    "SlotM11": SlotM11,
    "SlotM12": SlotM12,
    "SlotM13": SlotM13,
    "SlotM14": SlotM14,
    "SlotM15": SlotM15,
    "SlotM16": SlotM16,
    "SlotM17": SlotM17,
    "SlotM18": SlotM18,
    "SlotUD": SlotUD,
    "SlotUD2": SlotUD2,
    "SlotW10": SlotW10,
    "SlotW11": SlotW11,
    "SlotW12": SlotW12,
    "SlotW13": SlotW13,
    "SlotW14": SlotW14,
    "SlotW15": SlotW15,
    "SlotW16": SlotW16,
    "SlotW21": SlotW21,
    "SlotW22": SlotW22,
    "SlotW23": SlotW23,
    "SlotW24": SlotW24,
    "SlotW25": SlotW25,
    "SlotW26": SlotW26,
    "SlotW27": SlotW27,
    "SlotW28": SlotW28,
    "SlotW29": SlotW29,
    "SlotW60": SlotW60,
    "SlotW61": SlotW61,
    "SlotWLSRPM": SlotWLSRPM,
    "Solution": Solution,
    "SolutionData": SolutionData,
    "SolutionMat": SolutionMat,
    "SolutionVector": SolutionVector,
    "SolverInputFile": SolverInputFile,
    "StructElmer": StructElmer,
    "Structural": Structural,
    "SurfLine": SurfLine,
    "SurfRing": SurfRing,
    "Surface": Surface,
    "Trapeze": Trapeze,
    "Unit": Unit,
    "VarLoad": VarLoad,
    "VarLoadCurrent": VarLoadCurrent,
    "VarLoadVoltage": VarLoadVoltage,
    "VarParam": VarParam,
    "VarSimu": VarSimu,
    "VentilationCirc": VentilationCirc,
    "VentilationPolar": VentilationPolar,
    "VentilationTrap": VentilationTrap,
    "Winding": Winding,
    "WindingSC": WindingSC,
    "WindingUD": WindingUD,
    "XOutput": XOutput,
}
