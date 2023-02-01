# SigmaGeek-Polyhedral-Challenge

Solution to the Polyhedral Computational Challenge made by SigmaGeek

Libraries used: numpy

Challenge question:
"The regular octahedron is a polyhedron formed by 12 edges, 6 vertices, and 8 faces. Its faces have the shape of an equilateral triangle, as shown below.
...
Given a regular octahedron, consider the set formed by its vertices and the centers of its faces. How many distinct tetrahedrons are possible to construct with vertices in this set?"

Answer:
The script uses itertools to generate a unique set of arrays with 4 points in each array. Then it sweeps through that set excluding the arrays in wich these points are coplanar.
