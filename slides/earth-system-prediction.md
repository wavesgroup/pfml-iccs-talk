<section>

<video
  width=800
  controls
  autoplay
  loop
  muted
  src="assets/sustain.mp4"
  type="video/mp4">
</video>
</section>


<section>

### Example of observational data that gets parameterized as Fortran code in weather prediction models

<img class="stretch" src="assets/Curcic_Haus_2020_GRL_fig02.jpg">

<div class="reference"><a href="https://doi.org/10.1029/2020GL087647">Curcic and Haus (2020, GRL)</a></div>
</section>

<section>

<video
  width=600
  controls
  autoplay
  loop
  src="assets/mpas_clouds_dyamond_judt.mp4"
  type="video/mp4">
</video>

<div class="fragment reference">MPAS simulation and animation courtesy of Dr. Falko Judt (NCAR)</it>
</section>

<!--
<section>

<video
  width=800
  controls
  autoplay
  loop
  src="assets/mpas_olr_t2m_judt.mp4"
  type="video/mp4">
</video>

<div class="reference">
MPAS simulation and animation courtesy of Dr. Falko Judt (NCAR)
</div>
</section>
-->

<section>

## Earth System is complex, non-linear, and crosses many scales

* A complex system of interacting components: Atmosphere, ocean, waves, land, sea-ice, chemistry, biomes, etc.
* Spatial scales from microns to thousands of kilometers
* Temporal scales from milliseconds to millennia
* Nonlinear feedback processes between Earth System components
* _Emerging patterns_ that are not prescribed in the physics or code
</section>


<section>

## Earth System Prediction is crucial for most of us in our daily lives

* Weather forecasts:
  - 0-3 days: Human safety, transportation, energy
  - 3-15 days: Infrastructure, water management, air quality
  - 15-90 days: Agriculture, likelihood of weather extremes
* Climate projections:
  - Long-term planning and mitigation
  - Existential risks: Population and crop displacements, food and water scarcity, reducing biodiversity
</section>


<section>

## Under the hood

<img class="stretch" src="assets/mpas_mesh_4panel.png">

<div class="reference">From the <a href="https://mpas-dev.github.io/atmosphere/atmosphere.html">MPAS-Atmosphere website</a></div>
</section>


<section>

## What's in a weather model codebase?

* [WRF](https://github.com/wrf-model/wrf) (Weather Research and Forecasting model) as a case study
* ~1M lines of code
* Domain code (radiation, convection, turbulence, etc.) in a variety of dialects,
  from FORTRAN 77 to Fortran 2003
* Parts of BLAS, LAPACK, FFTPACK, and more, inserted into the codebase
* HDF5, NetCDF, MPI linked in
* OpenMP directives

<p class="fragment">
$\rightarrow$ A complex codebase that scales well on CPUs but has not kept up with emerging hardware accelerators
</p>
</section>


<section>

## How to run weather models on GPUs?

* Use directives to offload (CUDA Fortran, OpenMP, OpenACC, HIP)
* Source-to-source translators ([Psyclone](https://github.com/stfc/PSyclone), [Loki](https://github.com/ecmwf-ifs/loki))
* Re-write in another language (C++, Python, Julia)
* Develop machine learning emulators
</section>


<!--
<section>

## Migration efforts in other languages

* C++: e.g. [HOMME](https://climatemodeling.science.energy.gov/projects/sensitivity-atmospheric-parametric-formulations-regional-mesh-refinement-global-climate), [OMEGA](https://e3sm.org/omega-future-e3sm-model/) (DOE)
* Julia: e.g. [CliMA](https://clima.caltech.edu/) (Climate Modeling Alliance)
* Python: e.g. [Veros](https://github.com/team-ocean/veros) (ocean model written in Jax)
* DSL: [GT4py](https://github.com/GridTools/gt4py) JIT generating optimized code for several backends

<p class="fragment">
$\rightarrow$ Very difficult and expensive task: ~100 person-years to create a production-grade system.
</p>
</section>

<section>

## But the cost of it!
### Quick napkin calculation based on PASC24 talks so far

* 3-5 FTEs * 3-5 project years = 9-25 person-years
* $150-200k/person-year = 1.35-5M for a GPU-porting project
* Up to 10x that for an implementation from scratch in a new language
* And this calculation doesn't even include any HPC cost.
* More than a dozen such porting or migration projects
* Cumulative cost so far? $\mathcal{O}($100M)$?

<p class="fragment">
$\rightarrow$ Can we put some of that money toward a high-quality, open-source, optimizing Fortran compilers?
</p>
</section>
-->
