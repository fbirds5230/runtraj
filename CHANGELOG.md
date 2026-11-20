# Changelog

All notable changes to runtraj are listed here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow
[PEP 440](https://peps.python.org/pep-0440/). runtraj is alpha software: before
1.0, a minor or pre-release version may change the public API.

## [Unreleased]

## [0.1.0a2] - 2026-11-19

### Added

- Met sampling from any format arlmet converts, such as GFS and ERA5 GRIB:
  `sample_met` and `calc_pbl_height` take a Dataset in
  `arlmet.open_dataset`'s layout in place of ARL files. A transport model
  whose met files are not ARL files opens them for this with an optional
  `open_met` method, which `runtraj.models.open_met` calls.

### Changed

- runtraj requires arlmet 0.1.0b12 or later.

### Fixed

- Met sampling takes pressure from the met's vertical levels where the met
  has no `PRES` field, and refuses terrain-following and WRF met without it.
- Particle times that are not whole microseconds are sampled at their own
  time.
- Air density is the dry-air density where the met has no `SPHU`.
- `calc_pbl_height` gives no mixed-layer height where the met lacks the
  surface fluxes (`SHTF`, `USTR`); between a met time without them and one
  with them, it takes the height that exists.
- Met files that do not all hold the same variables are sampled for the
  ones they share, and one error names every variable that is missing. No
  met files at all is a clear error.

## [0.1.0a1] - 2026-11-19

The first release. runtraj runs particle dispersion models at scale: you give
it the times and places particles are released from, the meteorology, and the
settings to run under, and it runs the transport model once for each release,
on your computer or as a Slurm job array, and keeps the particles where you
can find them again.

### Added

- Projects: a folder holding `config.yaml` and `releases.csv`, whose
  simulations are every release under every variant (`runtraj.Project`).
- Releases: `PointRelease`, `ColumnRelease` and `MultiPointRelease`, read from
  and written to `releases.csv`.
- Variants and realizations: several sets of settings in one project, each
  writing to its own settings folder, and repeated runs with different seeds.
- HYSPLIT (`hycs_std`) as the built-in transport model, with its settings in
  a `hysplit` block; runtraj does not include HYSPLIT itself.
- The met catalog: finding the met files each release needs, checking them
  before a run, and downloading NOAA's archives (`runtraj fetch`, with the
  `download` extra).
- Stages, for what is made from the particles after a run, and other
  transport models, both plugged in by the import path of a class.
- Particle transforms for a lifetime, deposition, oxidation, pressure
  weighting and an averaging kernel.
- Met sampling: the met's mixed-layer height, air density, pressure and
  ground height at each particle, read from ARL files as HYSPLIT reads them
  (`runtraj.sampling.sample_met`), and HYSPLIT's mixed-layer height computed
  from the met's profile (`calc_pbl_height`).
- Running: `runtraj run` (or `Project.run()`) on your computer, `runtraj
  submit` as a Slurm job array, and `runtraj status`. A simulation is complete
  when its files exist, so an interrupted run picks up where it stopped.
- `runtraj check`, which finds what would stop a project's runs from its
  inputs alone.
- Output on a local disk or an object store, read back as plain DataFrames
  with the `.runtraj` accessor, and maps with the `visualization` extra.
