# Introduction to Algorithms (links below)
file:/a_syllabus/_COURSES/ALGO_00_Intro_2_Algorithms_MIT.rtf  
REPO: [algorithms](https://github.com/UnacceptableBehaviour/algorithms)  
See [References](#references) for links to course content  

## Abstract
Work notes from Introduction to Algorithms MIT 6.006 course

## Contents  
1. [Abstract](#abstract)  
2. [Contents](#contents)  
3. [AIM:](#aim)  
4. [Intoduction to algorithms MIT - part 1 / 3:](#intoduction-to-algorithms-mit--part-1--3)  
5. [Unit 1: Introduction](#unit-1-introduction)  
	1. [1	Algorithmic thinking, peak finding](#1algorithmic-thinking-peak-finding)  
		1. [Notes on time complexity (always worst case complexity)](#notes-on-time-complexity-always-worst-case-complexity)  
	2. [2	Models of computation, Python cost model, document distance](#2models-of-computation-python-cost-model-document-distance)  
		1. [Model of computation:](#model-of-computation)  
		2. [Python Model  - Computational Steps](#python-model---computational-steps)  
		3. [Document distance (problem and algorithms)](#document-distance-problem-and-algorithms)  
		4. [Problem set 1.](#problem-set-1)  
			1. [Problem 1-1. [15 points] Asymptotic Practice Calculating asymptotic complexity (Big O notation)](#problem-11-15-points-asymptotic-practicecalculating-asymptotic-complexity-big-o-notation)  
			2. [Problem 1-2. [15 points] Recurrence Relation Resolution](#problem-12-15-points-recurrence-relation-resolution)  
			3. [Problem 1-3. [16 points] Peak-Finding Correctness](#problem-13-16-points-peakfinding-correctness)  
			4. [Problem 1-4. [16 points] Peak-Finding Efficiency](#problem-14-16-points-peakfinding-efficiency)  
			5. [Problem 1-5. [19 points] Peak-Finding Proof](#problem-15-19-points-peakfinding-proof)  
			6. [Problem 1-6. [19 points] Peak-Finding Counterexamples 	data that shows how the python algorithms can fail](#problem-16-19-points-peakfinding-counterexamplesdata-that-shows-how-the-python-algorithms-can-fail)  
6. [Unit 2: Sorting and Trees](#unit-2-sorting-and-trees)  
	1. [3	Insertion sort, merge sort](#3insertion-sort-merge-sort)  
			1. [Insertion sort](#insertion-sort)  
	2. [4	Heaps and heap sort](#4heaps-and-heap-sort)  
	3. [5	Binary search trees, BST sort](#5binary-search-trees-bst-sort)  
	4. [6	AVL trees, AVL sort](#6avl-trees-avl-sort)  
	5. [7	Counting sort, radix sort, lower bounds for sorting and searching](#7counting-sort-radix-sort-lower-bounds-for-sorting-and-searching)  
7. [Unit 3: Hashing](#unit-3-hashing)  
	1. [8	Hashing with chaining](#8hashing-with-chaining)  
	2. [9	Table doubling, Karp-Rabin](#9table-doubling-karprabin)  
	3. [10	Open addressing, cryptographic hashing](#10open-addressing-cryptographic-hashing)  
8. [Unit 4: Numerics](#unit-4-numerics)  
	1. [11	Integer arithmetic, Karatsuba multiplication](#11integer-arithmetic-karatsuba-multiplication)  
	2. [12	Square roots, Newton's method](#12square-roots-newtons-method)  
9. [Unit 5: Graphs](#unit-5-graphs)  
	1. [13	Breadth-first search (BFS)](#13breadthfirst-search-bfs)  
	2. [14	Depth-first search (DFS), topological sorting](#14depthfirst-search-dfs-topological-sorting)  
10. [Unit 6: Shortest Paths](#unit-6-shortest-paths)  
	1. [15	Single-source shortest paths problem](#15singlesource-shortest-paths-problem)  
	2. [16	Dijkstra](#16dijkstra)  
	3. [17	Bellman-Ford](#17bellmanford)  
	4. [18	Speeding up Dijkstra](#18speeding-up-dijkstra)  
11. [Unit 7: Dynamic Programming](#unit-7-dynamic-programming)  
	1. [19	Memoization, subproblems, guessing, bottom-up; Fibonacci, shortest paths](#19memoization-subproblems-guessing-bottomup-fibonacci-shortest-paths)  
	2. [20	Parent pointers; text justification, perfect-information blackjack](#20parent-pointers-text-justification-perfectinformation-blackjack)  
	3. [21	String subproblems, psuedopolynomial time; parenthesization, edit distance, knapsack](#21string-subproblems-psuedopolynomial-time-parenthesization-edit-distance-knapsack)  
	4. [22	Two kinds of guessing; piano/guitar fingering, Tetris training, Super Mario Bros.](#22two-kinds-of-guessing-pianoguitar-fingering-tetris-training-super-mario-bros)  
12. [Unit 8: Advanced Topics](#unit-8-advanced-topics)  
	1. [23	Computational complexity](#23computational-complexity)  
	2. [24	Algorithms research topics](#24algorithms-research-topics)  
13. [How Tos](#how-tos)  
	1. [How do I autogenerate README.md file from RTF?](#how-do-i-autogenerate-readmemd-file-from-rtf)  
	2. [How can I add maths formulas to README.md?](#how-can-i-add-maths-formulas-to-readmemd)  
		1. [Generate math image and embed it.](#generate-math-image-and-embed-it)  
		2. [Solution 2 install texify.](#solution-2-install-texify)  
		3. [How can I get rid of ref numbers, or get them to increment at least?](#how-can-i-get-rid-of-ref-numbers-or-get-them-to-increment-at-least)  
14. [References](#references)  
	1. [Intoduction to algorithms MIT (part 1 / 3):](#intoduction-to-algorithms-mit-part-1--3)  
	2. [LaTex example setup and doc repo: https://github.com/UnacceptableBehaviour/latex_maths](#latex-example-setup-and-doc-repo-httpsgithubcomunacceptablebehaviourlatexmaths)  
	3. [Design & Analysis of Algorithms (part 2 / 3)](#design--analysis-of-algorithms-part-2--3)  
	4. [Advanced Algorithms 2008 (part 3 / 3)](#advanced-algorithms-2008-part-3--3)  


## AIM:  

Create an algorithms reference, and aide-memoire

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Intoduction to algorithms MIT - part 1 / 3:  
https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb  
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/  
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



## Unit 1: Introduction
### 1	Algorithmic thinking, peak finding	
yt_vid: [here](https://www.youtube.com/watch?v=HtSuA80QTyo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=2&t=423s)

Peak finding: assumin **single peak**, and   
Initial look at 1d peak finding (an single index array)
a) linear
b) search by halves

34m50	T(n) = Θ(1) + . . . Θ(1) = Θ(log2n) ??

Greedy Ascent Algorithm

52m30  start complexity - final solution @ 52m52

#### Notes on time complexity (always worst case complexity)
aka: Big O notation / Bachmann-Landau notation / asymptotic notation.  

See [Time Complexity of Common Data Structures](https://www.bigocheatsheet.com/)  
Big O Notation [notes from MIT](https://web.mit.edu/16.070/www/lecture/big_o.pdf)  
**LOW**  
constant time - O(1)  
logarithmic time - O(log n)  
linear time - O(n)  
quasilinear time  - O(n log n)  
polylogarithmic time  - O((log n) ^ c)  
quadratic time - O(n^2)  
polynomial time - O(n^c) where constant c > 1  
exponential time - O(2^n)  
factorial time - O(n!)  
**HIGH**  

If a function is made up of multiple components, (nearly always) the highest order is used:
(this is because big O is the upper bound (worst case) and highest order will be fastest growing and eventually dwarf the other terms)
Egs
$$
\begin{align}
f(n) = 10log(n) + 5(log(n))^3 + 7n + 3n^2 + 6n^3,  then f(n) = O(n^3)
\end{align}
$$


**Symbols:**  
Θ - -    
O - - Landaus Symbol  
Ω - -   
o - -   
ω - -   



		
[Time Complexity Graph](https://en.wikipedia.org/wiki/Time_complexity)  
[Python matplotlib chart browser](https://python-graph-gallery.com/122-multiple-lines-chart/) 
[Python matplotlib multiple line simple](https://stackoverflow.com/questions/4805048/how-to-get-different-colored-lines-for-different-plots-in-a-single-figure)  
[Setting yAxis logarithmic](https://matplotlib.org/3.1.1/gallery/scales/scales.html)  



### 2	Models of computation, Python cost model, document distance	 
Algorithm: computational procedure for solving a problem  
What is time (complexity)? **O(1) = constant time**  
#### Model of computation:
Operations an algorithm can perform
Time cost of those operations
Models of computation:  
a) random access machine RAM - word array  
	- load O(1)  
	- compute O(1)  
	- store O(1)  
	- word log(size of memory)  
b) pointer machine (OO programming)  
	- dynamically allocated objects O(1)  
	- object has constant no of fields O(1)  
	- word or pointer / references / null or None O(1)  

#### Python Model  - Computational Steps

Increment array item:
	list[i] = list[i] + 5    is **O(1)**  

Object attribute access:
	obj w/ O(1) number of attributes (constant no. of attributes)  
	attribute access is **O(1)** - pointer/ref access  

Access next item in linked list:
	x = x.next is **O(1)**  

Add item to liked list:	
	list.append(x) ? python uses table doubling **O(1)**  

Adding two linked lists together
	list1 + list2  **O(n)**  
	Code steps:  
	L = []	 O(1)    
	for x in list1: L.append(x) O( len(list1) )     - for list L - len(L) also written | L |  
	for x in list2: L.append(x) O( len(list2) )     - len, length, size, no of elements  
	total:  **O(1 + len(list1) + len(list2) ) = O(n) **  

Checking existence of item in list:
	x in L  **O(n)** - linear time  
		from python check to see if x is in list L  
		required search through whole list (worst case)

Sorting a list:	
	L.sort()   **O(| L | log | L |)**					- ie **O(n log n)**  
	Covered [Lecture 3	Insertion sort, merge sort](#3insertion-sort-merge-sort)  

Retrieving item from hash w/ key:
	retrieve dict[key]	  **O(1)** constant time (uses lookup hash)  
	Covered in [Lectures 8-10 Hashing with chaining](#8hashing-with-chaining)  

Adding two longs (many word numbers)  
	add two number of x words & y words:  
	x+y    **O(|x| + |y|)**  
	x*y    **O((|x| + |y|)^lg3)**  
	NOTE lg  used instead of log base 2 (log_2)  
	lg3 = 1.6 so better than quadratic time 
  	Covered in [Lecture 11 - Integer arithmetic, Karatsuba multiplication](#11integer-arithmetic-karatsuba-multiplication)  

**heapq** covered in lecture [4 - Heaps and heap sort](#4heaps-and-heap-sort)  


#### Document distance (problem and algorithms)  
d(D1, D2)  like a correlation function, similarity of two documents

The idea is to look for shared words:  
Start by creating the vector of a document, hash of words (key = word) with a count of each one as value.  
Create a vector common words, it contains only the word in both doc vectors  
Sum them up to give a value.  
The larger the value the more correlated they are.  
Obviously bigger documents will naturally give bigger numbers do the value is normalised by dividing by the size of the original vectors.  

$$
\begin{equation}
  D_1.D_2\\
\end{equation}
\begin{equation}
  \sum_{w}D_1[w].D_2[w]
  \label{sum}  
\end{equation}
$$



REFS
[Time Complexity of Common Data Structures](https://www.bigocheatsheet.com/)
[Look into this Latex insertion solution](https://stackoverflow.com/questions/35498525/latex-rendering-in-readme-md-on-github)  
[using pdfLatex may work](https://tex.stackexchange.com/questions/885/how-can-i-use-latex-from-python)  
Or use LaTeXiT from the command line to parse and auto generate equations
Or [readme2tex](https://github.com/leegao/readme2tex)  



Watch vids - add refs - from math text
Add big O symbols

#### Problem set 1.
[PDF here](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/assignments/MIT6_006F11_ps1.pdf)  

![Big O graphs](https://upload.wikimedia.org/wikipedia/commons/7/7e/Comparison_computational_complexity.svg)  
Image source:
Licence: [Attribution-Share Alike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/deed.en)  

##### Problem 1-1. [15 points] Asymptotic Practice Calculating asymptotic complexity (Big O notation) 
For each group of functions, sort the functions in increasing order of asymptotic (big-O) complexity:  

Problem 1.1a
$$
\begin{align}
f2(n) = 10000000n = O(n) = linear\\
f1(n) = n^{0.999999}log n = O(n log n) = quasilinear \\
f4(n) = n^2 = O(n^2) = quadratic\\
f3(n) = 1.000001^n = O(c^n) = exponential
\end{align}
$$

Problem 1.1b
$$
\begin{align}
f1(n) = 2^{2^{1000000}} = O(1) = constant\\
f3(n) = 
  \begin{bmatrix}
  n\\
  2\\  
  \end{bmatrix} = O(n) = linear ? notation?\\
f4(n) = n \sqrt{n} = n^1{n^\frac{1}{2}} = n^{1.5} = O(n^c) = polynomial\\
f2(n) = 2^{2100000n} = O(c^n) = exponential
\end{align}
$$



Problem 1.1c
$$
\begin{align}
f2(n) = 2^n = O(c^n) = constant.exponential\\
f1(n) = n^{\sqrt{n}} = n^{n^{\frac{1}{2}}} = O(n^n) = linear . exponential\\
f3(n) = n^{10}.2^{\frac{n}{2}} = O(n^c.c^n) = polynomial.exponential\\
f4(n) = \sum_{i=1}^{n}(i+1) = ? = O(?)
\end{align}
$$

##### Problem 1-2. [15 points] Recurrence Relation Resolution
For each of the following recurrence relations, pick the correct asymptotic runtime:
asymptotic complexity of an algorithm with runtime T (n, n) 
(a)
(b)
(c)

##### Problem 1-3. [16 points] Peak-Finding Correctness 
Double click /problems/MIT6_006F11_ps1/visualizer.html to see algorithms in operation.  
Python code notes:  
Its python2 so run with  
```
> cd /algorithms/problems/MIT6_006F11_ps1				# source unzip directory
> python ./main.py 
Enter a file name to load from (default: problem.py): 
Algorithm 1 : (4, 4) => is a peak
Algorithm 2 : (4, 4) => is a peak
Algorithm 3 : (4, 4) => is a peak
Algorithm 4 : (4, 4) => is a peak
```

OK so whats going on here?  
```
main.py
	load problem(matrix) from problem.py(or pas file name via CLI arg)
	create list of algos, tuples of (name, algo_no_func)
	iterate through list and call each algo w problem, tracee and default args
	print results

Once run the results can be visualised with visualizer.html which loads data created by the tracer (in trace.jsonp)	
```




##### Problem 1-4. [16 points] Peak-Finding Efficiency 
	Look at 4 alorithms in algorithms.py 
	Assess correctness, efficiency
##### Problem 1-5. [19 points] Peak-Finding Proof 
	proof for one of the algorithms
##### Problem 1-6. [19 points] Peak-Finding Counterexamples 	data that shows how the python algorithms can fail


## Unit 2: Sorting and Trees
### 3	Insertion sort, merge sort
##### Insertion sort
How is this better than bubble sort?

[Merge sort in 3mins](https://www.youtube.com/watch?v=4VqmGXwpLqc)
Pseudocode @ 2m32

[Difference between theta, omega complexity and big O](https://www.youtube.com/watch?v=6Ol2JbwoJp0)  

  

		Problem set 2 out - Event simulation

### 4	Heaps and heap sort	 
### 5	Binary search trees, BST sort	 
### 6	AVL trees, AVL sort	
	
		Problem set 2 due

### 7	Counting sort, radix sort, lower bounds for sorting and searching

		Problem set 3 out

## Unit 3: Hashing
### 8	Hashing with chaining	 
### 9	Table doubling, Karp-Rabin

		Problem set 3 due
		Problem set 4 out

### 10	Open addressing, cryptographic hashing

		Problem set 4 due
	 	Quiz 1	 

## Unit 4: Numerics
### 11	Integer arithmetic, Karatsuba multiplication	
		
		Problem set 5 out

### 12	Square roots, Newton's method	 

## Unit 5: Graphs
### 13	Breadth-first search (BFS)	 
### 14	Depth-first search (DFS), topological sorting

		Problem set 5 due
		Problem set 6 out

## Unit 6: Shortest Paths
### 15	Single-source shortest paths problem	 
### 16	Dijkstra	 
### 17	Bellman-Ford	 
### 18	Speeding up Dijkstra

		Problem set 6 due
	 	Quiz 2	 

## Unit 7: Dynamic Programming
### 19	Memoization, subproblems, guessing, bottom-up; Fibonacci, shortest paths

		Problem set 7 out

### 20	Parent pointers; text justification, perfect-information blackjack	 
### 21	String subproblems, psuedopolynomial time; parenthesization, edit distance, knapsack	 
### 22	Two kinds of guessing; piano/guitar fingering, Tetris training, Super Mario Bros.	

		Problem set 7 due

## Unit 8: Advanced Topics
### 23	Computational complexity	 
### 24	Algorithms research topics


## How Tos
### How do I autogenerate README.md file from RTF?
```
> .pe				# alias .pe='. venv/bin/activate'
> ./create_TOC_for_md.py -p	# takes ALGO_00_Intro_2_Algorithms_MIT.rtf course notes and add TOC > README.md
				# also add README.md to git, commits, and pushes
				# -p = commit & push
```

### How can I add maths formulas to README.md?
#### Generate math image and embed it.
Install Latex tools [notes here](https://github.com/UnacceptableBehaviour/latex_maths/blob/master/context.md)  
Open LaTeXit edit equation click text and hit the LaTeXit button to check its good.
Export as png and upload it to git (need to do this so the URL and be used to embed the image)
Embed image with 
```
![uses dot product of the vector of each document](https://github.com/UnacceptableBehaviour/algorithms/blob/master/formulae/20200228_1715_dot_prod_doc_distance.png)  
Note the ! before opening [ denotes image
```
#### Solution 2 install texify.
[Find texify here](https://github.com/agurodriguez/github-texify)  
Use LaTeXit to check formula correctness then past it into doc surrounded by consecutive $ symbols like so
```
$$
\begin{equation}
  D_1.D_2\\
\end{equation}
\begin{equation}
  \sum_{w}D_1[w].D_2[w]
  \label{sum}  
\end{equation}
$$
```  

#### How can I get rid of ref numbers, or get them to increment at least?
open problem . .

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## References
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Courses / Books Found w/ Summary:

MIT 2011 course
Prerequisite: Maths for CS: 
2015 https://www.youtube.com/watch?v=wIq4CssPoO0&list=PLUl4u3cNGP60UlabZBeeqOuoLuj_KNphQ  
	[L3.2.1 Asymptotic Notation] (https://www.youtube.com/watch?v=CWkh5kb4TGc&list=PLUl4u3cNGP60UlabZBeeqOuoLuj_KNphQ&index=72)  
	[L 3.2.3 Asymptotic Properties] (https://www.youtube.com/watch?v=HeyEK0TWiBw&list=PLUl4u3cNGP60UlabZBeeqOuoLuj_KNphQ&index=73)  
	[L 3.2.6 Asymptotic Blunder inc Big O] (https://www.youtube.com/watch?v=Y9Blo_G-Mvg&list=PLUl4u3cNGP60UlabZBeeqOuoLuj_KNphQ&index=74)  
2010 https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/video-lectures/  
	[L12 Sums] (https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/video-lectures/lecture-12-sums/)  
	[L12 Sums and Asymptotics] (https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/video-lectures/lecture-13-sums-and-asymptotics/)  

Topics: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/readings/  
Prerequisite: Probability: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-041-probabilistic-systems-analysis-and-applied-probability-spring-2006/   
Assignments w solutions: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-041-probabilistic-systems-analysis-and-applied-probability-spring-2006/assignments/    

### Intoduction to algorithms MIT (part 1 / 3):  
https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb  
Paper version: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/  
How Lectures Match problem sets:  
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/calendar/  
Problem Sets (inc code):  
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/assignments/  
Problem Local (inc code):/a_syllabus/_COURSES_03_TO_SORT/_algorithms/MIT_introduction_to_algorithms/_problems_exams  
Final exams & mocks: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/exams/  
Play list video: /a_syllabus/_COURSES_03_TO_SORT/_algorithms/MIT_introduction_to_algorithms/_Alogrithms_MIT_2011_vid.m3u  
Play list audio: /a_syllabus/_COURSES_03_TO_SORT/_algorithms/MIT_introduction_to_algorithms/_mp3/_Alogrithms_MIT_2011.m3u  

### LaTex example setup and doc repo: https://github.com/UnacceptableBehaviour/latex_maths  
Installing LaTex: http://tug.org/mactex/  
Latex Tutorial: https://www.youtube.com/watch?v=xnD4kHHvKhQ  
Maths in Latex: https://www.youtube.com/results?search_query=maths+formula+latex  

Follow up courses
### Design & Analysis of Algorithms (part 2 / 3)  
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2015/index.htm  
  
### Advanced Algorithms 2008 (part 3 / 3)  
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-854j-advanced-algorithms-fall-2008/  
  
 -   
 