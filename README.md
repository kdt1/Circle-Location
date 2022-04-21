# Circle-Location-bayes-filter
 Estimate the location of an object on a circle


An object B moves randomly on a circle with radius 1. The distance to the object can be measured from a sensor installed at the observation point P. The goal is to estimate the location of the object, as shown in Figure 1.
The object B can only move in discrete steps. The object’s location at time k is given by xk ∈ {0, 1, · · · , N −
1}, where θk = 2πxk . N
The object dynamics is given by
xk =mod(xk−1+vk,N), k=1,2,···,
where vk = 1 with probability p and vk = −1 with probability 1 − p. Recall that the modulo operator has
the property mod(N, N) = 0 and mod(−1, N) = N − 1.
The distance sensor measures zk = 􏰪(L − cos θk )2 + (sin θk )2 + wk , where wk represents the sensor error which is uniformly distributed on [−e,e]. We assume that x0 is uniformly distributed and x0, vk and wk are independent.
(a) (15 points) Implement the python code to simulate the object movement and implement an estimation algorithm that calculates for each time step k the probability distribution p(xk | z1 , · · · , zk ). [Hint: the discrete filter code in self test question 5 may be helpful for you.]
(b) (10 points) Test the following settings and discuss the results: N = 100, x0 = N4 , e = 0.5.
1. L=2,p=0.5;
2. L=2,p=0.55; 3. L=0.1,p=0.55; 4. L=0,p=0.55.
(c)(15points)Howrobustisthealgorithm? SetN =100,x0 = N4,e=0.5,L=2,p=0.55inthe
simulation, but use slightly different values for p and e in your estimation algorithm, pˆ and eˆ, respectively. Test the algorithm and explain the result.
1. pˆ=0.45,eˆ=e; 2. pˆ=0.5,eˆ=e; 3. pˆ=0.9,eˆ=e; 4. pˆ=p,eˆ=0.9; 5. pˆ=p,eˆ=0.45.
