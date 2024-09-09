<section>

## Fortran continues to improve in many ways..

* MPI+Fortran keeps getting better (Thanks, Jeff)
* Native parallel Fortran continues to improve (Thanks, Kate, Damian & CLaSS team)
* Fortran 2028 will bring type-safe generics (Thanks, Tom & The Generics team)
* The modern ecosystem of Fortran tools and libraries is growing rapidly
</section>

<section>

## [Fortran-lang](https://github.com/fortran-lang)

* Open-source community to build modern tooling and nurture the library ecosystem for Fortran
* Started in December 2019, rapidly grew to 100+ contributors 
* Flagship projects: [Standard Library](https://github.com/fortran-lang/stdlib), [Package Manager](https://github.com/fortran-lang/fpm), [fortran-lang.org](https://fortran-lang.org), [Fortran Discourse](https://fortran-lang.discourse.group)
* Active collaboration with the [LFortran](https://lfortran.org) compiler
  and the US Fortran Standards Committee
* Supported by the Google Summer of Code Program 4 years in a row (19 student projects to date)
* Grants from the Sovereign Tech Fund in 2022 and 2023
* And now a [NumFOCUS](https://numfocus.org) fiscally sponsored project

</section>


<section>

## fpm: Fortran Package Manager

```shell
$ fpm
USAGE: fpm [ SUBCOMMAND [SUBCOMMAND_OPTIONS] ]|[--list|--help|--version]
       where SUBCOMMAND is commonly new|build|run|test

 subcommand may be one of

  build     Compile the package placing results in the "build" directory
  help      Display help
  list      Display this list of subcommand descriptions
  new       Create a new Fortran package directory with sample files
  run       Run the local package application programs
  test      Run the test programs
  update    Update and manage project dependencies
  install   Install project
  clean     Delete the build
  publish   Publish package to the registry

 Enter "fpm --list" for a brief list of subcommand options. Enter
 "fpm --help" or "fpm SUBCOMMAND --help" for detailed descriptions.
```

<div class="reference"><a href="https://github.com/fortran-lang/fpm">https://github.com/fortran-lang/fpm</a></div>
</section>

<section>

<iframe src='https://lfortran.org' style='height:600px; width:1200px'></iframe>
</section>


<section>

### Compile and run Fortran code in your browser (LFortran)

<iframe src='https://dev.lfortran.org' style='height:600px; width:1200px'></iframe>

<div class="reference"><a href="https://lfortran.org">lfortran.org</a></div>
</section>


<section>

## Fortran MNIST classification in the browser
## LFortran WASM backend

<iframe src='https://lfortran.github.io/mnist-classifier-blas-wasm/' style='height:400px; width:1200px'></iframe>
</section>