# Competitive Programming Python Snippets

This repository contains a collection of Python,CPP code snippets and templates, Hacking Test Case Generator, Stress Tester, and a code to json format converter designed to assist with competitive programming. These snippets cover a range of algorithms, data structures, and problem-solving techniques commonly used in competitive programming contests.

## Overview

- Python Snipeets
- CPP Snippets
- Code to json converter
- Stress Tester
- Hack Generator

## Current Contents

- **Python**:
    The repository includes the following code snippets in the python version:

    - **CP**: FastIO, with solve function for multiple test cases, with hashing, gcd and lcm snippet.
    - **TCP**: CP Snippet for a single testcase, particularly for Atcoder Problems.
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
        - **extended_gcd**: Extended GCD.
        - **composite_crt**: Chinese Remainder Theorem.
        - **phi**: Computes Phi(n) for all n.
    - **Number Theory 3(nummat)**:
        - **Transpose**: Transpose
        - **matmul**: Matrix Multiplication
        - **matpow**: Power of a matrix
        - **gauss**: Solves Linear Equations
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
    - **Diophantine Equation(dpheq)**: Solving Linear Equation.
    - **Disjoint Set Union(DSU)**: Also has the Union Find implementation.
    - **Geometry**: All Geometry formulas.
    - **Fast Fourier Transformation(FFT)**: Polynomial Multiplication.
    - **XOR_dict**: Dictionary Having inbuilt hashing.
    - **Persistent Segment Tree(perseg)**: Persistent Segment Tree.
    - **Binary Trie(b_trie)**: Trie with each node having two children, faster.
    - **Heavy Light Decomposition(hld)**: Segment Tree Based Implementation.
    - **String Functions(sf)**:
        - **Z-function**: Longest Prefix Matching.
        - **Manacher's Algorithm**: Longest Palindrome.
        - **Suffix Array**: Suffix Array.
        - **LCP**: Longest common prefix between adjacent.
    - **Graph 1(graphadv)**:
        - **Dinic**: Max Flow Problem.
        - **Binary Lifting**: Binary Lifting.
        - **Virtual Tree**: Auxillary/Virtual Tree
    - **Graph 2(2sat)**:
        - **2-SAT**: 2 Sat implementation.
        - **Khan's Algorithm**: Topological Sorting.
    - **Graph 3(graphflattern)**:
        - **Flattening of Tree**: Flattens tree using DFS.
        - **Bipartite Graph**: Bipartite Graph.
    - **Graph 4(graphoth)**:
        - **Euler's Path**: Euler's Path.
        - **Topological Sorting**: Better Topological Sorting.
        - **Floyd Warshall**: All Pairs shortest distance.
        - **Bellman Ford**: Single to All.
    - **Graph 5(graph)**:
        - **Djikstra**: Djikstra.
        - **Breadth First Search**: BFS.
        - **Depth First Seatch**: DFS.
    - **Graph6(dfsin)**: DFS within the main.
    - **Graph7(bridges)**:
        - **Bridges**: Finds all the bridges in the graph.
        - **Bridges_on_path**: Finds all the bridges in the graph in path from 1 to n.
    - **utils**: Smaller Less relevant function and other constants and graph input.
    - **Persistent Disjoint Setunion(perdsu)**: Persistent Disjoint Setunion.
    - **Merge Sort Tree(sorttree)**: Merge Sort Tree.
    - **2-D Binary Indexed Tree(2DBIT)**: 2- Dimensional Binary Indexed Tree.
    - **Mono Deque**: Monotonic Deque, gives the cumulative assosciative function value of the elements within the deque in amortized O(1).
    - **Suffix Automaton(sautomaton)**: Online String Data Structure: All_occurence, Missing_Substring, LCSubstring, AllSubstring, kth distinct, count distinct, count occurences, is_substring, add.
    - **Linear Algebra**:
        - **Max Xor**: Returns array of elements such that their XOR is maximized.
    - **Square Root Decomposition(sqrt)**: Precompute answers of root n windows and answer queries in root n.

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
    - **Graph 1 (graphs)**
    - **Graph 2 (bgraph)**
    - **Merge Sort Tree(sorttree)**: Merge Sort Tree.

## In Progress

- Additional algorithms and data structures will be added over time to expand the utility of the repository. Contributions and suggestions for new snippets are welcome.

## Usage

To integrate these snippets into Visual Studio Code:

1. Open Visual Studio Code.
2. Navigate to the `python.json` file located in the AppData directory.
3. Copy and paste the relevant snippets from this repository into the `python.json` file.

## Contribution

Feel free to contribute by submitting pull requests with new snippets or improvements. Your contributions can help enhance the utility of this repository for the competitive programming community.

Happy coding!
