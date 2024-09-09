<section>

# Pure Fortran Machine Learning: Why and How?

_Milan Curcic_


_Department of Ocean Sciences, University of Miami_

_Frost Institute for Data Science & Computing, University of Miami_

_An ISSC Journal Club seminar_

_September 10, 2024_
</section>


<section>

## About me

* Assistant Professor of Ocean Science
* I study ocean waves and their role in the Earth system
* Mix of theory, field and laboratory measurements, and numerical modeling
* I wrote a popular book for Fortran beginners
* I'm not an ML practitioner, but I love learning new things
</section>


<section>

## Modern Fortran: Building Efficient Parallel Applications
<div style="display: flex; flex-direction: row;">

<div style="flex: 1; margin-top: 50px">

  <ul> 
    <li>Learn modern Fortran from the ground up</li>
    <li>Practical, hands-on, science-oriented examples</li>
    <li>Implements a parallel, nonlinear, shallow water equations solver</li>
    <li>Published in Q4 2020</li>
    <li>3774 copies sold as of Q1 2024</li>
    <li>4.8 stars on Amazon</li>
    <li>Early draft of Chapter 6 implemented a neural network</li>
  </ul> 
</div>

<div style="flex: 1;">
  <a href="https://www.manning.com/books/modern-fortran">
    <img height=500 src="assets/modern-fortran-cover.png"></img>
  </a>
</div>

</div>

</section>


<section>

## What's in a title?

* Pure **Fortran** ML
  - Many scientific and engineering applications remain written in Fortran
    for historical, cultural, and/or practical reasons;
* Pure Fortran **ML**
  - ML is a useful tool for classification and prediction given
    large amounts of data; state-of-the-art ML frameworks are written in Python,
    introducing an integration complexity when used in Fortran applications.
* **Pure Fortran** ML
  - Fortran itself provides all the necessary building blocks for ML,
    making a Pure Fortran approach one candidate to integrating ML in physics-based
    Fortran models.
* **Pure Fortran ML**
  - We will look at one candidate solution to this problem and the challenges in
    the design and implementation.
</section>