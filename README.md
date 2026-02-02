# Competitive Programming Python Snippets

This repository contains a collection of Python,CPP code snippets and templates, Hacking Test Case Generator, Stress Tester, and a code to json format converter designed to assist with competitive programming and a lot more. These snippets cover a range of algorithms, data structures, and problem-solving techniques commonly used in competitive programming contests. This repository will mostly benefit people who do CP in Python.

## Overview

- Python Snipeets
- CPP Snippets
- Code to json converter
- Stress Tester
- Hack Generator
- Other Templates

## Current Contents

- **Python**:
    The repository includes the following code snippets in the python version:

    - **CP**: FastIO, with solve function for multiple test cases, with hashing, gcd and lcm snippet.
    - **TCP**: CP Snippet for a single testcase, particularly for Atcoder Problems.
    - **DETCP**: CP Snippet with logs, and I/O from files.
    - **String Hashing(shclass)**: String Hashing.
    - **Fenwick Sorted List(fsortl)**: Fenwick Tree Based Sorted List, slow when numbers are large.
    - **Number Theory 1(numtheory)**: 
        - **miller_isprime**: Calculates if a number is prime or not in 7log2n, better for bigger numbers.
        - **is_prime**: Checks if number if prime or not in root n.
        - **sieve**: Precomputes primes upto the given number.
        - **all_fact**: Returns a sorted list of all factors of the given number in root n.
        - **prime_factors**: Returns the prime factors in the form of a Counter in log n.
        - **all_factors**: Returns all factors of a number in log n + (num of fact) complexity.
    - **Number Theory 2(numrare)**:
        - **pollard_rho**: Returns a random factor of n.
        - **prime_factors_large**: Probablistic algo, returns prime factors in n^(1/4).
        - **Discrete Log**: returns smallest x such that pow(a,x,mod)=b
        - **extended_gcd**: Extended GCD. **
        - **composite_crt**: Chinese Remainder Theorem. **
        - **phi**: Computes Phi(n) for all n. **
    - **Number Theory 3(nummat)**:
        - **Transpose**: Transpose.
        - **matmul**: Matrix Multiplication.
        - **matpow**: Power of a matrix.
        - **gauss**: Solves Linear Equations.
    - **Linear Algebra**:
        - **solve_quadratic**: Solves ax2+bx+c=0 for integer roots.
        - **solve_cubic**: Solves ax3+bx2+cx+d=0 for integer roots.
        - **Xor Basis**: Returns array of elements such that any element added to the data structure can be made using their combination.
        - **Simplex Bland**: Solves LPP Problems using Simplex Method.
        - **s_lr**: Computer Summation of i**power for l<=i<=r, given power<=3
    - **Sparse Table**: Sparse Table.
    - **Bucket Sorted List(bsortl)**: Bucket based sorted list.
    - **SegmentTree**: Faster Lazy propogated Segment Tree, but the operation can only have functions such that f(a,a) = a.
    - **SegmentTree(SegmentOther)**: Lazy Propogated Segment Tree for all operations.
    - **bootstrap**: Code snippet to make recursion possible in python.
    - **tries**: Tries
    - **Binary Indexed Tree(BIT)**: Binary Indexed Tree.
    - **Segment Tree(Segment Point)**: Segment Tree with point updates.
    - **Convex Hull(hull)**: Convex Hull, with three different implementations.
        - **First**: Need to define the max values of ai, bi (N).
        - **Second**: Need to define range of operations (log N).
        - **Third**: Need to define number of lines.
    - **BitArray**: Bitarray.
    - **Combinatorics(pnc)**: Combinatorics.
        - **fac**: Factorial
        - **fac_inv**: Inverse of Factorial
        - **combi**: nCr
        - **permu**: nPr
        - **catalan**: (1/(n+1)) * (2nCn)
        - **inv**: Inverse of n
        - **derangements**: Number of permutations of n objects where no object appears in its original position
        - **stirling_2**: Number of ways to partition n elements into k non-empty subsets
        - **partition**: Ways to partition n into k or fewer parts of size 1 or greater
    - **Diophantine Equation(dpheq)**: Solving Linear Equation.
    - **Disjoint Set Union(DSU)**: Also has the Union Find implementation.
    - **Geometry**: All Geometry formulas.
    - **Fast Fourier Transformation(FFT)**: Polynomial Multiplication.
    - **XOR_dict**: Dictionary Having inbuilt hashing, has Xdict and Xset.
    - **Persistent Segment Tree(perseg)**: Persistent Segment Tree.
    - **Binary Trie(b_trie)**: Trie with each node having two children, faster.
    - **Heavy Light Decomposition(hld)**: Segment Tree Based Implementation.
    - **String Functions(sf)**:
        - **Z-function**: Longest Prefix Matching.
        - **Manacher's Algorithm**: Longest Palindrome.
        - **Suffix Array**: Suffix Array. **
            - **SuffArr**: O(N) theoretical complexity but slower
            - **SuffArray**: O(NlogN) but faster, due to less constant time
        - **LCP**: Longest common prefix between adjacent elements in Suffix Array.
    - **Graph 1(graphadv)**:
        - **Dinic**: Max Flow Problem. **
        - **Binary Lifting**: Binary Lifting.
        - **Virtual Tree**: Auxillary/Virtual Tree **
    - **Graph 2(2sat)**:
        - **2-SAT**: 2 Sat implementation.
        - **Strongly Connected Component**: Finds the different SCCs. **
        - **Khan's Algorithm**: Topological Sorting.
    - **Graph 3(graphflattern)**:
        - **Flattening of Tree**: Flattens tree using DFS.
        - **Bipartite Graph**: Bipartite Graph.
    - **Graph 4(graphoth)**:
        - **Euler's Path**: Euler's Path. **
        - **Topological Sorting**: Better Topological Sorting.
        - **Floyd Warshall**: All Pairs shortest distance.
        - **Bellman Ford**: Single to All.
    - **Graph 5(graph)**:
        - **Djikstra**: Djikstra.
        - **Breadth First Search**: BFS.
        - **Depth First Seatch**: DFS.
    - **Graph 6(dfsin)**: DFS within the main.
    - **Graph 7(graph_dmgt)**: For undirected graphs
        - **Bridges**: Finds all the bridges in the graph.
        - **Bridges_on_path**: Finds all the bridges in the graph in path from 1 to n.
        - **lowlink**: Returns all the articulation points and bridges in iterative way. **
        - **find_2ecc**: Returns the Two Edge Connected Component. **
    - **Graph 8(graph_decom)**: Centroid Decompositon (Similar to Merge Sort)
        - **Shallowest Decomposition Tree**: O(N) Decomposition
        - **Centroid Decomposition Tree**: O(N log N) Standard Decomposition
    - **utils**: Smaller Less relevant function and other constants and graph input.
    - **Persistent Disjoint Setunion(perdsu)**: Persistent Disjoint Setunion.
    - **Merge Sort Tree(sorttree)**: Merge Sort Tree.
    - **2-D Binary Indexed Tree(2DBIT)**: 2- Dimensional Binary Indexed Tree.
    - **Mono Deque**: Monotonic Deque, gives the cumulative assosciative function value of the elements within the deque in amortized O(1).
    - **Suffix Automaton(sautomaton)**: Online String Data Structure: All_occurence, Missing_Substring, LCSubstring, AllSubstring, kth distinct, count distinct, count occurences, is_substring, add.
    - **Square Root Decomposition(sqrt)**: Precompute answers of root n windows and answer queries in root n.
    - **DP Optimizations**:
        - **Knuth's Optimization**: 
        
            dp[i][j] = min(dp[i][k]+dp[k+1][j] over all k)+cost(i,j)
        
            Condition: 
                
                For all a<=b<=c<=d:
                	cost(a,c)+cost(b,d)<=cost(a,d)+cost(b,c)
                opt[l][r-1] <= opt[l][r] <= opt[l+1][r]
        
        - **Divide and Conquer Optimization**:
            
            dp[i][j] = min(dp[l][j-1]+cost(l,i) over all l)
            
            Condition:
            
                opt[i][j] <= opt[i][j+1]
    - **FWHT**: Convolution such that ans[i] = summation of a[j]*b[k], where j logical condition k = i

- **CPP**:
    The repository includes the following code snippets in the CPP version:

    - **CP**: FastIO, with solve function for multiple test cases, with hashing, gcd, lcm, pbds snippet.
    - **String Hashing(shclass)**: String Hashing.
    - **Fenwick Sorted List(fsortl)**: Fenwick Tree Based Sorted List, slow when numbers are large.
    - **Number Theory(numtheory)**: 
        - **matmul**: Matrix Multiplication
        - **matpow**: Power of a matrix
        - **mod_exp**
        - **sieve**
        - **isprime**
        - **all_factors**
        - **sieve_unique**
        - **prime_factors**
        - **mod_inverse**
    - **Sparse Table**: Sparse Table.
    - **Sorted List(sortl)**: sorted list using ordered multiset.
    - **SegmentTree**: Lazy Propogated Segment Tree for all operations.
    - **tries**: Tries
    - **Binary Indexed Tree(BIT)**: Binary Indexed Tree.
    - **Segment Tree(Segment Point)**: Segment Tree with point updates.
    - **Convex Hull(hull)**: Convex Hull, with two different implementations.
    - **Combinatorics(pnc)**: Combinatorics.
    - **Diophantine Equation(dpheq)**: Solving Linear Equation.
    - **Disjoint Set Union(DSU)**: Also has the Union Find implementation.
    - **Geometry**: All Geometry formulas.
    - **Fast Fourier Transformation(FFT)**: Polynomial Multiplication.
    - **Persistent Segment Tree(perseg)**: Persistent Segment Tree.
    - **Graph 1 (bgraph)**: DFS, BFS, Dijkstra
    - **Graph 2 (graphoth)**: TopoSort
    - **Merge Sort Tree(sorttree)**: Merge Sort Tree.

## Note:
Website to convert the .json format to appropriate codes: 
https://json-to-zip-codes-converter.onrender.com/ (website might take some time to load)

Github Repository of the same:
https://github.com/OmAmar106/JSON-To-Zip-Codes-Converter

## Definitions
- **Extended GCD**: Computes x,y,gcd(a,b) such that ax+by=gcd(a,b).
- **Chinese Remainder Theorem**: given a mod m and a mod m1, m and m1, it returns smallest possible value of a.
- **Phi(n)**: Number of Integers less than n coprime with n
- **Suffix Array**: Starting position of Suffixes sorted according to there lexographical value
- **Max Flow Problems**: Max Flow that can go from start to end without exceeding capacity
- **Auxillary/Virtual Tree**: Create a subtree given a set of edges, by adding all possible LCAs.
- **SCC**: Connected Components, such that any vertex is reachable from any other vertex within the component.
- **Euler's Path**: Visit every edges exactly once, start and end can be different.
- **Bridges**: Edges which on removal increases number of components.
- **Articulation Points**: Vertex which on removal increase number of components.
- **2ECC**: Divides graph into subgraphs, where two elements within the same component share a cycle.

## In Progress

- Additional algorithms and data structures will be added over time to expand the utility of the repository. Issue Raising for new snippets are welcome.

## Usage

To integrate these snippets into Visual Studio Code:

1. Open Visual Studio Code.
2. Navigate to the `python.json` file located in the AppData directory.
3. Copy and paste the relevant snippets from this repository into the `python.json` file.

## Steps to Update

1. Add snippet in ChangeSnippetToJson file.
2. Generate Snippet.
3. Remove snippet from the file.
4. Update README.md with the new added function.
5. Add the snippet to python.json.
6. Copy the python.json file to python.jsonc.
7. Push the file.

Happy coding!
