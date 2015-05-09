Title: Monte-Carlo error propagation with Numpy
Date: 2015-01-12
Category: Coding
Tags: Python, Astropy
Author: Thomas Robitaille
Slug: monte-carlo-error-propagation-numpy

I am a big fan of Monte-Carlo techniques - and one of the many fun applications
of the principles of Monte-Carlo is for error propagation. Using
[Numpy](http://www.numpy.org), you can very easily propagate your errors both
more efficiently and more accurately than using error propagation rules, which
are often taught at university, but are not always easy to remember, and are
inaccurate for large errors.

The aim of this blog post is to show those of you who don't use Monte-Carlo
error propagation just how easy it is using Numpy. The idea behind Monte-Carlo
error propagation is to samples many possible realizations of each variable in
an equation, and to use these to compute many possible realizations of the
result. To take a very simple case, if we consider the equation $E=mc^2$, then
to find the uncertainty on $E$, we can sample $N$ values from the probability
distribution for $m$, and then compute $E$ for each value of $m$. Provided $N$
is large enough, the output values can be used to represent the probability
distribution of the output $E$ values.

If we take a slighly more complicated example such as $E_{\rm kin}=mv^2/2$, we
can sample $N$ values for $m$ and $N$ values for $v$, then combine these
pair-wise to find $N$ values for $E_{\rm kin}$::

    import numpy as np
    m = np.random.normal(10., 2., 1000)
    v = np.random.normal(10., 2., 1000)
    E = 0.5 * m * v**2

Of course, for this case and the above case, provided the errors on the input
variables are small enough, standard error propagation works fine, though even
then I'd argue that Monte-Carlo is easier and more fool-proof.

Let's now consider the case of an equation that gives us the mass of a planet
based on its observer radial velocity amplitude (assuming circular orbits, and
assuming that the mass of the planet is much less than that of the star):

$$M_{\rm planet} \approx \left(\frac{P}{2\pi G M_\star}\right)^{1/3} \frac{v_{\rm obs,star}}{\sin{i}}\,M_\star$$

where $M_\star$ is the mass of the star, $v_{\rm obs,star}$ is the radial
velocity amplitude of the star, $i$ is the inclination angle of the orbit, and
$P$ is the period of the orbit. Now let's assume that we know all of these
quantities within uncertainties, except the viewing angle, which is completely
unconstained. We start off by sampling many random values from normal or
uniform distributions depending on what we know::

    import numpy
    
    N = 1000000  # number of samples
    
    # The mass of the star is between 0.5 and 1.5 solar masses
    M_star = np.random.uniform(0.5, 1.5, N)  # M_sun
    
    # The period and radial velocity amplitude have normal distributions
    P = np.random.normal(5.6, 0.2, N)  # days
    v_obs = np.random.normal(56. 3., N)  # km/s
    
We now need to sample inclination values - to sample isotropic 3-d angles, we
need to sample $cos(i)$ from a uniform distribution and then transform to $i$::

    cos_i = np.random.random(N)
    i = np.arccos(cos_i)  # radians
    
We now simply need to put all this together to determine the stellar mass::


