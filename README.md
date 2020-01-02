# rating-affinity
A program to detertmine the affinity between a set of ratings using an inner product vector space model. This is inspired partly by 
https://dl.acm.org/doi/10.1145/361219.361220 methodology for determining document distance. Each set of ratings is represented as a multidimensional vector with each coordinate representing the rating of a given category. As the dot product of vectors is commutative with respect to summing the product of corresponding components, there is not a notion of orientation here.

Affinity is the term used here, whcih is given by the cosine of the angle between the vectors. This was deliberately chosen for two reasons:
- While useful to consider the two ratings as multidimensional vectors, describing their angle is a geometric concept odd to visualize. Having a percentage makes it far more easier to work with and understand. On a further note, this felt more natural than taking a linear map of the angle from zero to one hundred beacuse the range of the cosine already handles that. The range of the cosine also helps with differentiating perpendicular vectors (0% affinity) with opposite vectors (negative affinity).
- It takes one fewer step to compute.

## Usage

The `main(f1, f2)` function computes the affinity between the two documents `f1` and `f2`. You can use this function directly, or you can change the name of the arguments in the `if __name__ == '__main__'` part to whatever your file name is. This will output the affinity to four decimal places.
