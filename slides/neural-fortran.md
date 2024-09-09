

<section style="display: flex; flex-direction: column;">

<div style="flex: 8">

## neural-fortran: A parallel deep learning framework for Fortran applications

* Created to enable pure Fortran ML in Fortran applications
* Training and inference of arbitrarily deep dense and convolutional networks
* Optimizers: SGD, RMSProp, Adagrad, Adam, AdamW
* Data parallelism with Fortran 2018 collectives
* Used in over a dozen published studies from chemistry and combustion to weather and climate
* https://github.com/modern-fortran/neural-fortran

<div class="reference"><a href="https://doi.org/10.1145/3323057.3323059">Curcic (2019)</a></div>
</div>

<div style="flex: 2">
  <img height=90 src="assets/nasa.png"></img>
  <img height=60 src="assets/gsoc.png"></img>
</div>    
</section>



<section>

## Origin story of neural-fortran

* First draft of Chapter 6 in my Fortran book
* Pushed a working prototype to GitHub (2018)
* Invited to write a paper to ACM Fortran Forum ([Curcic, 2019](https://doi.org/10.1145/3323057.3323059))
* Fortran Keras Bridge ([Ott et al., 2020](https://doi.org/10.1155/2020/8888811))
* NASA contract and re-design for more general layer types (2021-2022)
* Optimizers implementation via Google Summer of Code (2023)
</section>


<section>

## Design principles

1. **Easy to use**: nice, concise, high-level API;
2. **Easy to extend**: modular design;
3. **Be hardware-agnostic**: let the compiler optimize when possible;
4. **Be self-contained**: no external dependencies when possible;
</section>


<section>

## Minimal training example

```fortran
program simple
  use nf, only: dense, input, network, sgd
  implicit none
  type(network) :: net
  real, allocatable :: x(:), y(:)
  integer, parameter :: num_iterations = 500
  integer :: n

  net = network([ &
    input(3), &
    dense(5), &
    dense(2) &
  ])

  call net % print_info()

  x = [0.2, 0.4, 0.6]
  y = [0.123456, 0.246802]

  do n = 0, num_iterations

    call net % forward(x)
    call net % backward(y)
    call net % update(optimizer=sgd(learning_rate=1.))

    if (mod(n, 50) == 0) &
      print '(i4,2(3x,f8.6))', n, net % predict(x)

  end do

end program simple
```

</section>


<section>

## Creating, training, and running a CNN with neural-fortran

```fortran
use nf
type(network) :: net

! Create the model
net = network([ &
  input(784), &
  reshape([1,28,28]), &
  conv2d(filters=8, kernel_size=3, activation=relu()), &
  maxpool2d(pool_size=2), &
  conv2d(filters=16, kernel_size=3, activation=relu()), &
  maxpool2d(pool_size=2), &
  dense(10, activation=softmax()) &
])

! Run training
call net % train( &
  training_images, &
  label_digits(training_labels), &
  batch_size=128, &
  epochs=10, &
  optimizer=adam(),
)

! Run inference
print *, net % predict(test_images)
```
</section>


<section>

## More Fortran ML goodness

* [inference-engine](https://github.com/BerkeleyLab/inference-engine) - A deep learning library for HPC applications
* [athena](https://github.com/nedtaylor/athena) - Another ML framework, inspired by neural-fortran
* [fastGPT](https://github.com/certik/fastGPT) - Fast GPT-2 inference in Fortran
* [llm.f90](https://github.com/rbitr/llm.f90) - Pure Fortran Llama2 inference
* [ferrite](https://github.com/rbitr/ferrite) - Simple, lightweight transformers in Fortran
</section>