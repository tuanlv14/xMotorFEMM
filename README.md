# <img alt="Pyleecan" src="https://www.pyleecan.org/_static/favicon.png" height="120">

[![PyPI version](https://badge.fury.io/py/pyleecan.svg)](https://badge.fury.io/py/pyleecan)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

## Presentation
PYLEECAN objective is to provide a **user-friendly, unified, flexible simulation framework for the multiphysic design and optimization of electrical machines and drives**.

It is meant to be used by researchers, R&D engineers and teachers in electrical engineering, both on standard topologies of electrical machines and on novel topologies (e.g. during a PhD work). Pyleecan is **open source** with a very permissive license (Apache V2 license).

The main objective of PYLEECAN is to boost **reproduicible research** and **open-science** in electrical engineering. For example, every PhD student should start with PYLEECAN. Instead of implementing your own scripts on your side (e.g. coupling Scilab or Matlab with Femm), you could benefit from the community support to help you in your research.  

## Getting Started
The procedure to install and use Pyleecan is detailed on [pyleecan website](https://www.pyleecan.org/get.pyleecan.html)

## Origin and Current Status of the Project
[EOMYS ENGINEERING](https://eomys.com/?lang=en) initiated this open-source project in 2018 for the study of electric motors. The project is now backed by [Green Forge Coop](https://www.linkedin.com/company/greenforgecoop/) non profit organization, who also supports the development of [Mosqito](https://github.com/Eomys/MoSQITo) for sound quality and [SciDataTool](https://github.com/Eomys/SciDataTool) for efficient scientific data exploitation. 

**Main Models and Couplings:**
* PYLEECAN is fully coupled to [FEMM](http://www.femm.info) to carry **non-linear magnetostatic** analysis including sliding band and symmetries. For now this coupling is available (only on Windows OS). 
* PYLEECAN includes an iron losses model (based on FEMM coupling output).
* PYLEECAN includes an electrical model to solve the equivalent circuit of PMSM and SCIM machines.
* PYLEECAN is coupled to [GMSH](http://gmsh.info/) **2D/3D finite element mesh generator** to run third-party multiphysic solvers. 
* PYLEECAN is coupled to a **multiobjective optimization** library to carry design optimization of electrical machines.
* PYLEECAN enables to define **Parameter Sweep** of variable speed simulations.

**Main Topologies Features:**
* PYLEECAN includes a **Graphical User Interface** to define main 2D radial flux topologies parametrized geometries (**SPMSM, IPMSM, SCIM, DFIM, WRSM, SRM, SynRM**) including material library.
* Possibility to import Slot or Hole from DXF files
* User Defined Winding or automatic algorithm
* Generic Geometry modeler to draw complex machines in the software coupled with PYLEECAN
* Notches (Yoke and Bore) / Uneven Bore shape (Lamination without slot only) / Machine with more than 2 laminations

If you are interested by a topology or a specific model, you can [open an issue](https://github.com/Eomys/pyleecan/issues) or a [discussion](https://github.com/Eomys/pyleecan/discussions) on this Github repository to talk about it. We will gladly explain how to develop it yourself or we will add it to the development list. We are always looking for experimental data and model validation based on the last scientific research work. 
Even if you don't have time to work on pyleecan, sharing your expertise will be valued by the community. 

## RoadMap
The mid/long term roadmap of the project is detailed [here](https://github.com/Eomys/pyleecan/issues/214)

## Documentation / Website
All the information on the project are available at [www.pyleecan.org](http://www.pyleecan.org). In particular, the [media page](https://pyleecan.org/media.html) gathers the publications, video and screenshots of the project.

## Contact
You can contact us:
* By opening an [issue](https://github.com/Eomys/pyleecan/issues) on Github (to request a feature, ask a question or report a bug) or starting a [discussion](https://github.com/Eomys/pyleecan/discussions)
* By sending an email at pyleecan(at)framalistes.org that redirect to all the maintainers.

You can follow us:
* On our [newsletter](https://pyleecan.org/)
* On [GFC youtube channel](https://www.youtube.com/channel/UCfp83IQbz9znqsU28keMjZw) (with webinars and tutorials video)
* On [GFC Linkedin page](https://www.linkedin.com/company/greenforgecoop/)
