# Introduction to Algorithms (links below)
file:/a_syllabus/_COURSES/ALGO_00_Intro_2_Algorithms_MIT.rtf  
REPO: [algorithms](https://github.com/UnacceptableBehaviour/algorithms)  
See [References](#references) for links to course content  

## Abstract
Work notes from Introduction to [Algorithms MIT 6.006](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/syllabus/) course [lectures on ytube](https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)   
[MIT 6.006 course info]() ~ 
[Lectures & Recitations](http://courses.csail.mit.edu/6.006/fall11/notes.shtml) ~ 
[Resources - Python / Latex](http://courses.csail.mit.edu/6.006/fall11/resources.shtml) ~ 
[Quizzes/Exams](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/exams/)  



## Progress
KEY: (:white_check_mark:) watched, (:mag:) rewatch, (:flashlight:) unseen / to watch, (:question:) problem / open question  
CODE: (:seedling:) code complete, (:cactus:) incomplete / needs work, (:lemon:) not happy / code smells,  

| Lectures                                                                                                                                                              | Recitations                                                                                                                                                                                                                                    | Problem Sets                                                                                                                                                      | Solutions                                                                                                                                                        | Example Code                                                                                                              | Implementation                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| :white_check_mark: [01. Algorithmic Thinking, Peak Finding](https://www.youtube.com/watch?v=HtSuA80QTyo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=2&t=3s)         | :flashlight: [R01. Asymptotic Complexity, Peak Finding](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/recitation-videos/recitation-1-asymptotic-complexity-peak-finding/) | [Set 1 PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/assignments/MIT6_006F11_ps1.pdf)   | [Set 1](https://github.com/UnacceptableBehaviour/algorithms#problem-set-1)                                                                                       | [DocDistance Optimisations](https://github.com/UnacceptableBehaviour/algorithms/tree/master/lecture_code/L2_doc_distance) |                                                                                                                     |
| :white_check_mark: [02. Models of Computation, Document Distance](https://www.youtube.com/watch?v=Zc54gFhdpLA&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=3&t=117s) | :flashlight: [R02. Python Cost Model, Document Distance](https://www.youtube.com/watch?v=j0upQLUrpM8)                                                                                                                                          |                                                                                                                                                                   |                                                                                                                                                                  |                                                                                                                           |                                                                                                                     |
| :white_check_mark: [03. Insertion Sort, Merge Sort](https://www.youtube.com/watch?v=Kg4bqzAqRBM&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=4&t=1953s)              | :flashlight: [R03. Document Distance, Insertion and Merge Sort](https://www.youtube.com/watch?v=4iXLnF3hExw&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=27)                                                                                  | [Set 2 PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/assignments/MIT6_006F11_ps2.pdf)   |                                                                                                                                                                  |                                                                                                                           | :seedling: [merge.sort-P3](https://github.com/UnacceptableBehaviour/algorithms/blob/master/algos/merge_sort.py)     |
| :white_check_mark: [04. Heaps and Heap Sort](https://www.youtube.com/watch?v=B7hVxCmfPtM&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=5&t=2064s)                     |                                                                                                                                                                                                                                                |                                                                                                                                                                   |                                                                                                                                                                  |                                                                                                                           | :seedling: [Heap-P3](https://github.com/UnacceptableBehaviour/algorithms/blob/master/algos/heap_ify.py)             |
| :white_check_mark: [05. Binary Search Trees, BST Sort](https://www.youtube.com/watch?v=9Jry5-82I68&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=6&t=1s)              | :white_check_mark: [R05. Recursion Trees, Binary Search Trees](https://www.youtube.com/watch?v=r5pXu1PAUkI&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=28)                                                                                   |                                                                                                                                                                   |                                                                                                                                                                  |                                                                                                                           | :lemon: [BST-P3](https://github.com/UnacceptableBehaviour/algorithms/blob/master/algos/binary_search_tree.py)    |
| :white_check_mark: [06. AVL Trees, AVL Sort](https://www.youtube.com/watch?v=FNeL18KsWPc&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=7&t=1913s)                     | :flashlight: [R06. AVL Trees](https://www.youtube.com/watch?v=IWzYoXKaRIc&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=29)                                                                                                                    |                                                                                                                                                                   |                                                                                                                                                                  | [AVL / BST](https://github.com/UnacceptableBehaviour/algorithms/tree/master/lecture_code/L6_BST_AVL_trees)                | :seedling: [AVL-P3](https://github.com/UnacceptableBehaviour/algorithms/blob/master/algos/AVL.py)                   |
| :mag: [07. Counting Sort, Radix Sort, Lower Bounds for Sorting](https://www.youtube.com/watch?v=Nz1KZXbghj8&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=8&t=301s)   | :flashlight: R07. Comparison Sort, Counting and Radix Sort                                                                                                                                                                                     | [Set 3 PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/assignments/MIT6_006F11_ps3.pdf)   |                                                                                                                                                                  |                                                                                                                           |                                                                                                                     |
| :mag: [08. Hashing with Chaining](https://www.youtube.com/watch?v=0M_kIqhwbFo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=9&t=0s)                                   | :flashlight: R08. Simulation Algorithms                                                                                                                                                                                                        |                                                                                                                                                                   |                                                                                                                                                                  |                                                                                                                           | :cactus: [Hash.w.Chaining-P3](https://github.com/UnacceptableBehaviour/algorithms/blob/master/algos/assoc_array.py) |
| :flashlight: [09. Table Doubling, Karp](https://www.youtube.com/watch?v=BRO7mVIFt08&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=10&t=0s)                            | :flashlight: R09. Rolling Hashes, Amortized Analysis                                                                                                                                                                                           | [Set 4 PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/assignments/MIT6_006F11_ps4.pdf)   |                                                                                                                                                                  |                                                                                                                           |                                                                                                                     |
| :flashlight: 09b DNA Sequence Matching-                                                                                                                               | :flashlight: [R09b - DNA Sequence Matching](https://www.youtube.com/watch?v=-DwGrJ8JxDc)                                                                                                                                                       |                                                                                                                                                                   |                                                                                                                                                                  |                                                                                                                           |                                                                                                                     |
| :flashlight: 10. Open Addressing, Cryptographic Hashing                                                                                                               | :flashlight: R10. Quiz 1 Review-                                                                                                                                                                                                               | [Quiz 1](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/exams/MIT6_006F11_quiz1.pdf)          | [Quiz 1](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/exams/MIT6_006F11_quiz1_sol.pdf)     |                                                                                                                           |                                                                                                                     |
| :flashlight: 11. Integer Arithmetic, Karatsuba Multiplication                                                                                                         | :flashlight: R11. Principles of Algorithm Design                                                                                                                                                                                               | [Set 5 PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/assignments/MIT6_006F11_ps5.pdf)   |                                                                                                                                                                  |                                                                                                                           |                                                                                                                     |
| :flashlight: 12. Square Roots, Newton's Method                                                                                                                        | :flashlight: R12. Karatsuba Multiplication, Newton's Method                                                                                                                                                                                    |                                                                                                                                                                   |                                                                                                                                                                  |                                                                                                                           |                                                                                                                     |
| :flashlight: 13. Breadth                                                                                                                                              | :flashlight: R13. Breadth                                                                                                                                                                                                                      |                                                                                                                                                                   |                                                                                                                                                                  |                                                                                                                           |                                                                                                                     |
| :flashlight: 14. Depth                                                                                                                                                | :flashlight: R14. Depth                                                                                                                                                                                                                        | [Set 6 PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/assignments/MIT6_006F11_ps6.pdf)   |                                                                                                                                                                  |                                                                                                                           |                                                                                                                     |
| :flashlight: 15. Single                                                                                                                                               | :flashlight: R15. Shortest Paths                                                                                                                                                                                                               |                                                                                                                                                                   |                                                                                                                                                                  |                                                                                                                           |                                                                                                                     |
| :flashlight: 16. Dijkstra                                                                                                                                             | :flashlight: R16. Rubik's Cube, StarCraft Zero                                                                                                                                                                                                 |                                                                                                                                                                   |                                                                                                                                                                  |                                                                                                                           |                                                                                                                     |
| :flashlight: 17. Bellman                                                                                                                                              | :flashlight: R18. Quiz 2 Review                                                                                                                                                                                                                | [Quiz 2](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/exams/MIT6_006F11_quiz2.pdf)          | [Quiz 2](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/exams/MIT6_006F11_quiz2_sol.pdf)     |                                                                                                                           |                                                                                                                     |
| :flashlight: 18. Speeding up Dijkstra                                                                                                                                 | :flashlight: R19. Dynamic Programming - Crazy Eights, Shortest Path                                                                                                                                                                            | [Set 7 PDF](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/assignments/MIT6_006F11_ps7.pdf)   |                                                                                                                                                                  |                                                                                                                           |                                                                                                                     |
| :flashlight: 19. Dynamic Programming I - Fibonacci, Shortest Paths                                                                                                    | :flashlight: R20. Dynamic Programming - Blackjack                                                                                                                                                                                              |                                                                                                                                                                   |                                                                                                                                                                  |                                                                                                                           |                                                                                                                     |
| :flashlight: 20. Dynamic Programming II - Text Justification, Blackjack                                                                                               | :flashlight: R21. Dynamic Programming - Knapsack Problem                                                                                                                                                                                       |                                                                                                                                                                   |                                                                                                                                                                  |                                                                                                                           |                                                                                                                     |
| :flashlight: 21. DP III - Parenthesization, Edit Distance, Knapsack                                                                                                   | :flashlight: R22. Dynamic Programming - Dance Dance Revolution                                                                                                                                                                                 |                                                                                                                                                                   |                                                                                                                                                                  |                                                                                                                           |                                                                                                                     |
| :flashlight: 22. DP IV - Guitar Fingering, Tetris, Super Mario Bros.                                                                                                  | :flashlight: R23. Computational Complexity                                                                                                                                                                                                     |                                                                                                                                                                   |                                                                                                                                                                  |                                                                                                                           |                                                                                                                     |
| :flashlight: 23. Computational Complexity                                                                                                                             | :flashlight: R24. Final Exam Review                                                                                                                                                                                                            | [Final Exam](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/exams/MIT6_006F11_final.pdf)      | [Final Exam](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/exams/MIT6_006F11_final_sol.pdf) |                                                                                                                           |                                                                                                                     |
| :flashlight: 24. Topics in Algorithms Research                                                                                                                        |                                                                                                                                                                                                                                                |                                                                                                                                                                   |                                                                                                                                                                  |                                                                                                                           |                                                                                                                     |


## Contents  
1. [Abstract](#abstract)  
2. [Progress](#progress)  
3. [Contents](#contents)  
4. [AIM:](#aim)  
5. [Intoduction to algorithms MIT - part 1 / 3:](#intoduction-to-algorithms-mit---part-1--3)  
6. [Unit 1: Introduction](#unit-1-introduction)  
	1. [L1 - Algorithmic thinking, peak finding](#l1---algorithmic-thinking-peak-finding)  
		1. [Vid contents](#vid-contents)  
		2. [Notes on time complexity (always worst case complexity)](#notes-on-time-complexity-always-worst-case-complexity)  
		3. [**Symbols:**](#symbols)  
		4. [**Time Complexity - Order Severity**](#time-complexity---order-severity)  
		5. [Useful maths equations](#useful-maths-equations)  
	2. [R1 - maths & code](#r1---maths--code)  
		1. [Vid contents](#vid-contents)  
		2. [Maths notes](#maths-notes)  
	3. [L2 - Models of computation, Python cost model, document distance](#l2---models-of-computation-python-cost-model-document-distance)  
		1. [Vid contents](#vid-contents)  
		2. [Model of computation:](#model-of-computation)  
		3. [Python Model  - Computational Steps](#python-model----computational-steps)  
		4. [Document distance (problem and algorithms)](#document-distance-problem-and-algorithms)  
		5. [Examples Document distance code:](#examples-document-distance-code)  
		6. [Maths notes](#maths-notes)  
	4. [R2 - doc distance optimisation - python cost model](#r2---doc-distance-optimisation---python-cost-model)  
		1. [Vid contents](#vid-contents)  
		2. [Setting up for profiling](#setting-up-for-profiling)  
		3. [Code of code](#code-of-code)  
		4. [Comparing versions](#comparing-versions)  
		5. [Maths notes](#maths-notes)  
7. [Problem set 1.](#problem-set-1)  
	1. [Problem 1-1. [15 points] Asymptotic Practice   Calculating asymptotic complexity (Big O notation)](#problem-1-1-15-points-asymptotic-practice--calculating-asymptotic-complexity-big-o-notation)  
	2. [Problem 1-2. [15 points] Recurrence Relation Resolution](#problem-1-2-15-points-recurrence-relation-resolution)  
	3. [Problem 1-3. [16 points] Peak-Finding Correctness](#problem-1-3-16-points-peak-finding-correctness)  
	4. [Problem 1-4. [16 points] Peak-Finding Efficiency](#problem-1-4-16-points-peak-finding-efficiency)  
	5. [Problem 1-5. [19 points] Peak-Finding Proof](#problem-1-5-19-points-peak-finding-proof)  
	6. [Problem 1-6. [19 points] Peak-Finding Counterexamples 	data that shows how the python algorithms can fail](#problem-1-6-19-points-peak-finding-counterexamplesdata-that-shows-how-the-python-algorithms-can-fail)  
8. [Unit 2: Sorting and Trees](#unit-2-sorting-and-trees)  
	1. [L3 - Insertion sort, merge sort](#l3---insertion-sort-merge-sort)  
		1. [Insertion sort](#insertion-sort)  
		2. [Merge Sort](#merge-sort)  
	2. [L4 - Heaps and heap sort](#l4---heaps-and-heap-sort)  
		1. [**DATA STRUCTURE - Priority Q - L4 3m33**](#data-structure---priority-q---l4-3m33)  
		2. [Priority Queue](#priority-queue)  
		3. [Heap](#heap)  
			1. [Heap as a tree navigation](#heap-as-a-tree-navigation)  
			2. [Heap as a tree properties](#heap-as-a-tree-properties)  
			3. [Max_heapify](#maxheapify)  
	3. [L5 - Binary search trees, BST sort](#l5---binary-search-trees-bst-sort)  
		1. [**DATA STRUCTURE - BST - Binary search trees**](#data-structure---bst---binary-search-trees)  
		2. [Vid contents](#vid-contents)  
		3. [Augmented BST - 37m - node_count_before](#augmented-bst---37m---nodecountbefore)  
	4. [R5 - Recursion Trees, Binary Search Trees](#r5---recursion-trees-binary-search-trees)  
		1. [Vid contents](#vid-contents)  
		2. [Maths notes](#maths-notes)  
		3. [get_successor()](#getsuccessor)  
		4. [delete()](#delete)  
	5. [L6 - AVL trees, AVL sort](#l6---avl-trees-avl-sort)  
		1. [**DATA STRUCTURE - AVL tree - R6 50m**](#data-structure---avl-tree---r6-50m)  
		2. [Vid contents](#vid-contents)  
		3. [Example problem](#example-problem)  
		4. [TERMS](#terms)  
		5. [Maths notes - AVL tree (19-25m) - height analysis v1](#maths-notes---avl-tree-19-25m---height-analysis-v1)  
		6. [Maths notes - AVL tree (26m) - height analysis v2](#maths-notes---avl-tree-26m---height-analysis-v2)  
	6. [R6 - maths & code](#r6---maths--code)  
		1. [Vid contents](#vid-contents)  
		2. [BST review](#bst-review)  
		3. [AVL properties](#avl-properties)  
		4. [Maths notes](#maths-notes)  
	7. [Problem set 2 (due)](#problem-set-2-due)  
		1. [2-1 Fractal rendering [40pts]](#2-1-fractal-rendering-40pts)  
		2. [2-2 Digital Circuit Simulation [60pt]](#2-2-digital-circuit-simulation-60pt)  
	8. [L7 - Counting sort, radix sort, lower bounds for sorting and searching](#l7---counting-sort-radix-sort-lower-bounds-for-sorting-and-searching)  
		1. [Sorting in Linear-Time](#sorting-in-linear-time)  
	9. [R7 - maths & code - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -](#r7---maths--code------------------------------------------------------------)  
		1. [Vid contents](#vid-contents)  
		2. [Maths notes](#maths-notes)  
9. [Unit 3: Hashing](#unit-3-hashing)  
	1. [L8 - Hashing with chaining - (dictionary / associative array)](#l8---hashing-with-chaining---dictionary--associative-array)  
	2. [R8 - maths & code - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -](#r8---maths--code------------------------------------------------------------)  
		1. [Vid contents](#vid-contents)  
		2. [Maths notes](#maths-notes)  
	3. [L9 - Table doubling, Karp-Rabin](#l9---table-doubling-karp-rabin)  
	4. [R9 - maths & code - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -](#r9---maths--code------------------------------------------------------------)  
		1. [Vid contents](#vid-contents)  
		2. [Maths notes](#maths-notes)  
	5. [L10 - Open addressing, cryptographic hashing](#l10---open-addressing-cryptographic-hashing)  
		1. [**DATA STRUCTURE**](#data-structure)  
		2. [Vid contents](#vid-contents)  
		3. [Example problem](#example-problem)  
		4. [Maths notes](#maths-notes)  
	6. [R10 - maths & code - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -](#r10---maths--code------------------------------------------------------------)  
		1. [Vid contents](#vid-contents)  
		2. [Example problem](#example-problem)  
		3. [Maths notes](#maths-notes)  
10. [Problem set 4 due](#problem-set-4-due)  
11. [Quiz 1](#quiz-1)  
12. [Unit 4: Numerics](#unit-4-numerics)  
	1. [L11 - Integer arithmetic, Karatsuba multiplication](#l11---integer-arithmetic-karatsuba-multiplication)  
		1. [**DATA STRUCTURE**](#data-structure)  
		2. [Vid contents](#vid-contents)  
		3. [Example problem](#example-problem)  
		4. [Maths notes](#maths-notes)  
	2. [R11 - maths & code - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -](#r11---maths--code------------------------------------------------------------)  
		1. [Vid contents](#vid-contents)  
		2. [Example problem](#example-problem)  
		3. [Maths notes](#maths-notes)  
13. [Problem set 5 out](#problem-set-5-out)  
	1. [L12 - Square roots, Newton's method](#l12---square-roots-newtons-method)  
		1. [**DATA STRUCTURE**](#data-structure)  
		2. [Vid contents](#vid-contents)  
		3. [Example problem](#example-problem)  
		4. [Maths notes](#maths-notes)  
14. [Unit 5: Graphs](#unit-5-graphs)  
	1. [L13 - Breadth-first search (BFS)](#l13---breadth-first-search-bfs)  
		1. [**DATA STRUCTURE**](#data-structure)  
		2. [Vid contents](#vid-contents)  
		3. [Example problem](#example-problem)  
		4. [Maths notes](#maths-notes)  
	2. [L14	Depth-first search (DFS), topological sorting](#l14depth-first-search-dfs-topological-sorting)  
		1. [**DATA STRUCTURE**](#data-structure)  
		2. [Vid contents](#vid-contents)  
		3. [Example problem](#example-problem)  
		4. [Maths notes](#maths-notes)  
15. [Problem set 5 due](#problem-set-5-due)  
16. [Problem set 6 out](#problem-set-6-out)  
17. [Unit 6: Shortest Paths](#unit-6-shortest-paths)  
	1. [L15 - Single-source shortest paths problem](#l15---single-source-shortest-paths-problem)  
		1. [**DATA STRUCTURE**](#data-structure)  
		2. [Vid contents](#vid-contents)  
		3. [Example problem](#example-problem)  
		4. [Maths notes](#maths-notes)  
	2. [L16 - Dijkstra](#l16---dijkstra)  
		1. [**DATA STRUCTURE**](#data-structure)  
		2. [Vid contents](#vid-contents)  
		3. [Example problem](#example-problem)  
		4. [Maths notes](#maths-notes)  
	3. [L17 - Bellman-Ford](#l17---bellman-ford)  
		1. [**DATA STRUCTURE**](#data-structure)  
		2. [Vid contents](#vid-contents)  
		3. [Example problem](#example-problem)  
		4. [Maths notes](#maths-notes)  
	4. [L18 - Speeding up Dijkstra](#l18---speeding-up-dijkstra)  
		1. [**DATA STRUCTURE**](#data-structure)  
		2. [Vid contents](#vid-contents)  
		3. [Example problem](#example-problem)  
		4. [Maths notes](#maths-notes)  
18. [Unit 7: Dynamic Programming](#unit-7-dynamic-programming)  
	1. [L19 - Memoization, subproblems, guessing, bottom-up; Fibonacci, shortest paths](#l19---memoization-subproblems-guessing-bottom-up-fibonacci-shortest-paths)  
		1. [**DATA STRUCTURE**](#data-structure)  
		2. [Vid contents](#vid-contents)  
		3. [Example problem](#example-problem)  
		4. [Maths notes](#maths-notes)  
19. [Problem set 7 out](#problem-set-7-out)  
	1. [L20 - Parent pointers; text justification, perfect-information blackjack](#l20---parent-pointers-text-justification-perfect-information-blackjack)  
		1. [**DATA STRUCTURE**](#data-structure)  
		2. [Vid contents](#vid-contents)  
		3. [Example problem](#example-problem)  
		4. [Maths notes](#maths-notes)  
	2. [L21 - String subproblems, psuedopolynomial time; parenthesization, edit distance, knapsack](#l21---string-subproblems-psuedopolynomial-time-parenthesization-edit-distance-knapsack)  
		1. [**DATA STRUCTURE**](#data-structure)  
		2. [Vid contents](#vid-contents)  
		3. [Example problem](#example-problem)  
		4. [Maths notes](#maths-notes)  
	3. [L22 - Two kinds of guessing; piano/guitar fingering, Tetris training, Super Mario Bros.[vid]()](#l22---two-kinds-of-guessing-pianoguitar-fingering-tetris-training-super-mario-brosvid)  
		1. [**DATA STRUCTURE**](#data-structure)  
		2. [Vid contents](#vid-contents)  
		3. [Example problem](#example-problem)  
		4. [Maths notes](#maths-notes)  
20. [Problem set 7 due](#problem-set-7-due)  
21. [Unit 8: Advanced Topics](#unit-8-advanced-topics)  
	1. [L23 - Computational complexity](#l23---computational-complexity)  
		1. [**DATA STRUCTURE**](#data-structure)  
		2. [Vid contents](#vid-contents)  
		3. [Example problem](#example-problem)  
		4. [Maths notes](#maths-notes)  
	2. [24 - Algorithms research topics](#24---algorithms-research-topics)  
		1. [**DATA STRUCTURE**](#data-structure)  
		2. [Vid contents](#vid-contents)  
		3. [Example problem](#example-problem)  
		4. [Maths notes](#maths-notes)  
22. [Glossary of terms](#glossary-of-terms)  
23. [How To s](#how-to-s)  
	1. [How so I plot a chart with python?](#how-so-i-plot-a-chart-with-python)  
	2. [How to setup autogenerate README.md file from RTF notes?](#how-to-setup-autogenerate-readmemd-file-from-rtf-notes)  
	3. [How do I autogenerate README.md file from RTF?](#how-do-i-autogenerate-readmemd-file-from-rtf)  
	4. [How can I add maths formulas to README.md?](#how-can-i-add-maths-formulas-to-readmemd)  
		1. [Manually: Generate math image and embed it.](#manually-generate-math-image-and-embed-it)  
		2. [Automagically:  Install texify.](#automagically--install-texify)  
		3. [How can I get rid of ref numbers, or get them to increment at least?](#how-can-i-get-rid-of-ref-numbers-or-get-them-to-increment-at-least)  
24. [References](#references)  
	1. [Intoduction to algorithms MIT (part 1 / 3):](#intoduction-to-algorithms-mit-part-1--3)  
	2. [LaTex example setup and doc repo: https://github.com/UnacceptableBehaviour/latex_maths](#latex-example-setup-and-doc-repo-httpsgithubcomunacceptablebehaviourlatexmaths)  
	3. [Design & Analysis of Algorithms (part 2 / 3)](#design--analysis-of-algorithms-part-2--3)  
	4. [Advanced Algorithms 2008 (part 3 / 3)](#advanced-algorithms-2008-part-3--3)  


## AIM:  

Create an algorithms reference, and aide-memoire  

In the mean time here are two great resources:  
Big O Cheat Sheet: [https://www.bigocheatsheet.com/](https://www.bigocheatsheet.com/)  
Open data structures: [http://opendatastructures.org/](http://opendatastructures.org/)  


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Intoduction to algorithms MIT - part 1 / 3:  
[LECTURE PLAYLIST on YOUTUBE](https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)  
[COURSE INFO @ MIT](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/)  
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



## Unit 1: Introduction
### L1 - Algorithmic thinking, peak finding	
[vid](https://www.youtube.com/watch?v=HtSuA80QTyo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=2&t=423s) ~ 
[lect notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec01.pdf)  

#### Vid contents
0m - 15m45  Introduction to course and 8 units its separated into - mentions prerequisite Maths 6.042  
15m45 - 36m20 Peak finding 1D  
17m50 defining the solution to 1D algorithm  
27m40 Divide & conquer (binary search)  
32m30 Recurence relation overview  
36m20 -  Peak finding 2D  
37m13 defining the solution to 2D algorithm - note a >= b - means   
38m Greedy ascent algorithm - find highest neighbour, go in that direction, loop  
40m43 Greedy ascent algorithm complexity Θ(mn) (rown x columns) O(n^2) IE BAD!  
43m 2D binary search  
46m EG 1 - incorrect search  
47m45 EG2 - working version  
51m25 Recurrence for 2D algorithm  
54m15 Note on PS1 - Prove one algorithm is correct & find counter examples for the rest (which are not)  
  
Peak finding: assuming **single peak**, and   
Initial look at 1d peak finding (an single index array)
a) linear
b) search by halves - height of a binary tree is logn (log base 2)

34m50	T(n) = Θ(1) + . . . Θ(1) = Θ(logn)  
Binary search tree is formed by the search by halves algorithm and the number of **steps to find the target is the height of the tree.**  
See R1 31m & 43m

Question: What comprises work due to n and what can be counted as constant time Θ(1) and disregarded!  

51m48  
<p align="center"><img src="/tex/345071e71619869b5189c43f93597997.svg?invert_in_darkmode&sanitize=true" align=middle width=546.9241338pt height=114.95363879999998pt/></p>
m = columns  
n = rows  
**That all makes sense but binary search relies on sorted data and the data in the example is NOT sorted.**  
Swapping 14 & 20 would result in a fail, maybe itll make sense later!  


#### Notes on time complexity (always worst case complexity)
aka: Big O notation / Bachmann-Landau notation / asymptotic notation.  

See [Time Complexity of Common Data Structures](https://www.bigocheatsheet.com/) great summary of array sorting algorithm complexity and data structure operations   

#### **Symbols:**  
Big O Notation [wikipedia](https://en.wikipedia.org/wiki/Big_O_notation) Family of Bachmann-Landau notations    
Big O Notation [notes from MIT](https://web.mit.edu/16.070/www/lecture/big_o.pdf) p3 - from wikipedia?  
Maths [Symbols by subject](https://en.wikipedia.org/wiki/List_of_mathematical_symbols_by_subject) Asymptotic behaviour   

The following symbols o, Ω, ω, and Θ, are used to describe differing kinds of bounds on asymptotic growth rates.  
O - big O - describes the asymptotic behaviour of functions WORST case or UPPER bound (common in **CompSci**)  
Θ - big Theta - describes the asymptotic behaviour of functions AVERAGE case - LOWER BOUND & UPPER BOUND (common in **CompSci**)  
(note the upper and lower bounds are the same function that only differs by a constant)
Ω - big Omega - BEST case or LOWER bound (common in **CompSci**)  
o - little O - loose upper bound (common in Maths rare in CompSci)  
ω - little omega - rough estimate of the order of the growth (rarely used)  
T(n) - function defining the exact Time or number of steps to complete an algorithm for n items  

The rate of growth of a function is also known as its **order**.  

Great resource about [Common Time Complexities](https://en.wikipedia.org/wiki/Time_complexity#Table_of_common_time_complexities)  

#### **Time Complexity - Order Severity**
Where c is a constant and n is the number of steps:  
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

![Big O graphs](https://upload.wikimedia.org/wikipedia/commons/7/7e/Comparison_computational_complexity.svg)  
Image source: [wikipedia](https://upload.wikimedia.org/wikipedia/commons/7/7e/Comparison_computational_complexity.svg) 
Licence: [Attribution-Share Alike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/deed.en)  

The above list is useful because of the following fact: if a function f(n) is a sum of functions, one of which grows faster than the others, then the faster growing one determines the order of f(n).

If a function is made up of multiple components, (nearly always) the highest order is used:
(this is because big O is the upper bound (worst case) and highest order will be fastest growing and eventually dwarf the other terms)  
Egs
<p align="center"><img src="/tex/f1ebe4d3468c6d3f2f6243ce83e00dad.svg?invert_in_darkmode&sanitize=true" align=middle width=474.77859989999996pt height=18.312383099999998pt/></p>

Simplified set theory? Some people (mostly mathematicians, as opposed to computer scientists) prefer to define O(g(x)) as a set-valued function, whose value is all functions that do not grow faster then g(x), and use set membership notation to indicate that a specific function is a member of the set thus defined. Both forms are in common use, but the sloppier equality notation is more common at present.  
		
[Time Complexity Graph](https://en.wikipedia.org/wiki/Time_complexity)  
[Python matplotlib chart browser](https://python-graph-gallery.com/122-multiple-lines-chart/)  
[Python matplotlib multiple line simple](https://stackoverflow.com/questions/4805048/how-to-get-different-colored-lines-for-different-plots-in-a-single-figure)  
[Setting yAxis logarithmic](https://matplotlib.org/3.1.1/gallery/scales/scales.html)  

#### Useful maths equations
Fundamental to binary tree algorithms:
<p align="center"><img src="/tex/4cd8fa5dbdeb7a9567601dd345719d75.svg?invert_in_darkmode&sanitize=true" align=middle width=450.19701375pt height=16.438356pt/></p>




### R1 - maths & code
[vid](https://www.youtube.com/watch?v=P7frcB_-g4w&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=25) ~ 
[lect notes](https://courses.csail.mit.edu/6.006/fall11/rec/) ~ 
[Code - PSet 1](https://github.com/UnacceptableBehaviour/algorithms/tree/master/problems/MIT6_006F11_ps1)  
Reading: 

#### Vid contents
2m - 13m40 Asymptotic complexity Ω, Θ, O  
13m40 - common worst case runtimes  
16m - example asymptotic notation  
23m - log(log(n))  
25m - log ( N choose N/2 ) = Θ(n)    
31m - 43m peak finding 1d - running time T(n)
43m - 53m peak finding - running time T(n)

NOTE
g(x) = O(f(x)) - UPPER bound - O - big O
g(x) = Θ(f(x)) - UPPER & LOWER bound - Θ - big Theta
g(x) = Ω(f(x)) - LOWER bound - Ω - big Omega

but in this course where big O is written it usually mean big Θ 13m - thanks for the confusion

31m 1d Peak finding - running timeT(n)
WRITE OUT - in hand written notes L1

43m 2d Peak finding - running timeT(n)
WRITE OUT - in hand written notes L1

Finish R1 notes from - Recurrence Traps & 2-D Peak Finding: Algorithm 5


#### Maths notes  
(26m) [Stirlings approximation - equation for n!](https://en.wikipedia.org/wiki/Stirling%27s_approximation)  
<p align="center"><img src="/tex/17789aec953e515f4d4dbbcbe79c0588.svg?invert_in_darkmode&sanitize=true" align=middle width=411.75196425pt height=31.070567549999996pt/></p>
(26m) [Equation for Series - summation](https://en.wikipedia.org/wiki/Stirling%27s_approximation)  
<p align="center"><img src="/tex/8182cc03706f858356e39b08f4cc0a9d.svg?invert_in_darkmode&sanitize=true" align=middle width=409.5568059pt height=44.89738935pt/></p>


### L2 - Models of computation, Python cost model, document distance	   
[vid](https://www.youtube.com/watch?v=Zc54gFhdpLA&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=2) ~ 
[lect notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec02.pdf) ~ 
DocDistance 8 versions Code see R2 ~ 
[DocDistance 8 versions R2 notes](https://courses.csail.mit.edu/6.006/fall11/rec/rec02.pdf)  

#### Vid contents
0-6m - Whats an algorithm  
6m - model of computation  
7m50 - Random access machine (model of computation)  
13m40 - Pointer machine (model of computation)  
19m - 32m - Python model
32m -  44m - Document distance
44m - 8 version of doc distance and optimisations


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

Add item to linked list:  
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

<p align="center"><img src="/tex/a5a3fa25cf152acc801491db474d6460.svg?invert_in_darkmode&sanitize=true" align=middle width=407.98942304999997pt height=64.10978970000001pt/></p>

#### Examples Document distance code:
[this repo](https://github.com/UnacceptableBehaviour/algorithms/tree/master/lecture_code/L2_doc_distance) 
or [on web](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lec02_code.zip)  

#### Maths notes  
41m angle of two vectors  
more detail? 

REFS  
[Time Complexity of Common Data Structures](https://www.bigocheatsheet.com/)  
[Look into this Latex insertion solution](https://stackoverflow.com/questions/35498525/latex-rendering-in-readme-md-on-github)  
[using pdfLatex may work](https://tex.stackexchange.com/questions/885/how-can-i-use-latex-from-python)  
Or use LaTeXiT from the command line to parse and auto generate equations  
Or [readme2tex](https://github.com/leegao/readme2tex)  



### R2 - doc distance optimisation - python cost model
[vid](https://www.youtube.com/watch?v=j0upQLUrpM8) ~ 
[lect notes - CODE handout](https://courses.csail.mit.edu/6.006/fall11/rec/rec02_code_handout.pdf) ~ 
[python cost model 8 sources compared](https://courses.csail.mit.edu/6.006/fall11/rec/rec02.pdf) ~ 
[Doc Distance 7 stages optimisation local code](https://github.com/UnacceptableBehaviour/algorithms/tree/master/lecture_code/L2_doc_distance) ~ 
[Code - PSet 1](https://github.com/UnacceptableBehaviour/algorithms/tree/master/problems/MIT6_006F11_ps1)  

#### Vid contents
0-7m - inner product  
7m - got through docdist1  
13m - cost of code by line - docdist1: get_words_from_string() - [CODE handout](https://courses.csail.mit.edu/6.006/fall11/rec/rec02_code_handout.pdf)  
 One line, N = characters, w = word size, number of word = N / w + 1 (1 for each space)  
 



#### Setting up for profiling
```
```

#### Code of code
```
9
10
11
12
13
14 
```

#### Comparing versions
Compare dd1 vs dd2
optimisation 


#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  






- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Problem set 1.
[PDF here](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/assignments/MIT6_006F11_ps1.pdf)  




### Problem 1-1. [15 points] Asymptotic Practice   Calculating asymptotic complexity (Big O notation)  
For each group of functions, sort the functions in increasing order of asymptotic (big-O) complexity:  
Order of complexity here [**Time Complexity - Order Severity**](#time-complexity--order-severity)  
Plotting functions to get a feel for them [./matplotlib/time_complexity_plot_q.py](https://github.com/UnacceptableBehaviour/algorithms/blob/master/matplotlib/time_complexity_plot_q.py)   
Comment functions in/out of the source or add custom functions!   

Problem 1.1a
<p align="center"><img src="/tex/5c6d2a50d62a2677f5bcb2524aba5432.svg?invert_in_darkmode&sanitize=true" align=middle width=349.90844955pt height=94.4878902pt/></p>

Problem 1.1b
<p align="center"><img src="/tex/cbde0d11ea8f1ebd27ab4ac5526ed78a.svg?invert_in_darkmode&sanitize=true" align=middle width=373.18578164999997pt height=122.87297219999999pt/></p>
Note for f3() boils down to this [proof I think . . ](https://github.com/UnacceptableBehaviour/algorithms/blob/master/formulae/1st_stab_nCr_proof.jpeg)  
<p align="center"><img src="/tex/c25acae12157db0472ada055c7a1f07d.svg?invert_in_darkmode&sanitize=true" align=middle width=588.0255678pt height=32.990165999999995pt/></p>
with the left dominating the right give nlog(n)  


Problem 1.1c  
<p align="center"><img src="/tex/ead0e3753b23a641f6e42c4f3e27c3af.svg?invert_in_darkmode&sanitize=true" align=middle width=390.7235673pt height=131.8078443pt/></p>

### Problem 1-2. [15 points] Recurrence Relation Resolution
For each of the following recurrence relations, pick the correct asymptotic runtime:  
asymptotic complexity of an algorithm with runtime T (n, n)  
(a)  
(b)  
(c)  
Maths course: 

[Lots of resources for recurrence relations]()

### Problem 1-3. [16 points] Peak-Finding Correctness 
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
	iterate through list and call each algo w problem, trace
		trace object is a list of dictionaries, each method appends a result of each step in the algorithm as a dict
		the list of dicts is coverted into json file (trace.jsonp) 
	print results

Once run the results can be visualised with visualizer.html which loads data created by the tracer (in trace.jsonp)
	json file loaded by visualiser: <script type="text/javascript" src="./trace.jsonp"></script>	
```
Asses each algorithm to see if it is correct, and if it is efficient:  
a)  algo 1 correct? r x c    
  p1 (4,4) yes  
  p2 (2,7) yes  
  p3 (3,5) no - 11 surrounded by 3 11s finds peak right there  
  p4 (3,4) yes    
  p5 (3,8) no - stops on consecutive same values
  
     efficient?   
b) algo 2 correct? r x c  
  p1 (4,4) yes  
  p2 (4,3) no - stops on consecutive same values - CHANGE TEST   
  p3 (4,3) no - stops on consecutive same values - CHANGE TEST     
  p4 (4,4) yes    
  p5 (4,5) no - 
  

     efficient?   
c) algo 3 correct? r x c     
  p1 (4,4) yes  
  p2 (5,4) no - goes left - stops on consecutive same values - CHANGE? TEST - recursion required    
  p3 (6,5) no - stops on consecutive same values - > test
  p4 (4,4) yes    
  p5 (5,8) no - 
  

     efficient?   
d) algo4 correct? r x c     
  p1 (4,4) yes  
  p2 (5,4) no - goes left - stops on consecutive same values - CHANGE? TEST - recursion required
  p3 (6,5) no - stops on consecutive same values - > test
  p4 (4,4) yes    
  p5 (5,8) no - 
     efficient?   
 
e) algo 5 brute force scan - CORRECT
  p1 (4,4) yes  
  p2 (2,7) yes  
  p3 (4,6) yes  
  p4 (4,4) yes    
  p5 (6,6) yes    





### Problem 1-4. [16 points] Peak-Finding Efficiency 
	Look at 4 alorithms in algorithms.py 
	Assess correctness, efficiency
### Problem 1-5. [19 points] Peak-Finding Proof 
	proof for one of the algorithms
### Problem 1-6. [19 points] Peak-Finding Counterexamples 	data that shows how the python algorithms can fail

REFERENCES:
[Correctness - various proofs](https://www.youtube.com/user/intrigano/search?query=correctness)  
[Reccurence relation by Induction](https://www.youtube.com/watch?v=t_3ACuzEe_8)  




- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Unit 2: Sorting and Trees
### L3 - Insertion sort, merge sort
[vid](https://www.youtube.com/watch?v=Kg4bqzAqRBM&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=3)
[recitation]()  
[lect notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec03.pdf)  

#### Insertion sort
Sorted list have various properties:   
	simple to find median (constant time)  
	find item:  
		scan to find O(n) in sorted & unsorted list  
		binary search O(log n) (halves the list at each step)

Application: compression (frequency counting), graphic z-order etc

Insertion sort - also in doc distance python files (/algorithms/lecture_code/L2_doc_distance)

**Bubble sort** (scan list swap values in the wrong order, repeat) O(n^2)  

**Insertion Sort**  
a) Vanilla insertion sort (L2_doc_distance)  
Move 1st item to new list, move next item to new list **scan** until correct place found, insert, repeat  
**n^2** - breaks down as: (n for number of items) * (n for search & insert )

b) Binary insertion sort  
Move 1st item to new list, move next item to new list **binary search** until correct place found, insert, repeat  
**n log n** - breaks down as: (n for number of items) *  (log n for binary search & insert )

#### Merge Sort  
[Merge sort in 3mins](https://www.youtube.com/watch?v=4VqmGXwpLqc)  
Pseudocode: (@ 2m32 in above link)
Split array into 2,  
repeat until only 2 items in each leaf,  
sort those two items,  
go up a layer and merge leaves   

[Python implementation here] (https://github.com/UnacceptableBehaviour/algorithms/blob/master/algos/merge_sort.py) likely naive.  

**Concept of auxiliary space**, in the above python code that would be stack I assume.


Instrument the merge sort code - s

[Difference between theta, omega complexity and big O](https://www.youtube.com/watch?v=6Ol2JbwoJp0)  
  

		Problem set 2 out - Event simulation

### L4 - Heaps and heap sort  
[vid](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-4-heaps-and-heap-sort)
[lect notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec04.pdf)  
Reading: none listed  
Code: [Python](https://github.com/UnacceptableBehaviour/algorithms/blob/master/algos/heap_ify.py)  


#### **DATA STRUCTURE - Priority Q - L4 3m33**  
**type:**  -  (maxheap or minheap) - prefered implementation ?  
**use cases:** finding min or max value in sorted set (not both), scheduling, flattening linked list, finding non overlaping intervals, ROAM  
**queries:** min/max  
**updates:** pop_min/max - Θ(logn), insert item - Θ(logn), delete item - Θ(logn), change priority  
**RI max heap:** Node is larger than or equal child nodes, complete binary tree  
**RI min heap:** Node is less than or equal child nodes, complete binary tree  
**properties:** root contains max/min value  
node positions in array:  
root i=1  
parent = i/2  
lc_i = 2i  
rc_i = 2i+1     
![array implementation allocation](https://github.com/UnacceptableBehaviour/algorithms/blob/master/formulae/Heap-as-array.svg.png)  
Credit: https://en.wikipedia.org/wiki/Heap_(data_structure)#/media/File:Heap-as-array.svg  
RI - representation invariant  



#### Priority Queue
Implements a set of elements associated with a key - methods:
insert(x, into set S),  
get max priority (of set S),  
extract_max (of set S)  -  get max and remove it!  
inc_key (in set S, increase element xs key, to value k)  
get min priority (of set S),  
delete, change priority in Q.  

#### Heap
Is an implementation of a priority Q, array structure visualised as a nearly complete binary tree - p4  

Root of tree is array index 0, (tree node i=1)  
1,2 are LEFT & RIGHT split  
3,4 - 5,6 are next layer LEFT & RIGHT split  
counting on like that [see page 4](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec04.pdf)  

##### Heap as a tree navigation
[see page 5](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-4-heaps-and-heap-sort)  
**Using array to implement the heap**  
root i=1  
parent = i/2  
left = 2i  
right = 2i+1  

No pointers required.

##### Heap as a tree properties
**Max heap property:**  
the key of a node >=  keys of its children  
(the key being the value in the circle)  

**Min heap property:**  
the key of a node <=  keys of its parent  

##### Max_heapify  
[Python source exercise here](https://github.com/UnacceptableBehaviour/algorithms/blob/master/algos/heap_ify.py)

Note for array of **any** size: element A[n/2+1 . . n] are ALL leaves!





### L5 - Binary search trees, BST sort	 
[vid](https://www.youtube.com/watch?v=9Jry5-82I68&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=5) ~ 
[lect notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec05.pdf) ~ 
[Code 1st guess](https://github.com/UnacceptableBehaviour/algorithms/blob/master/algos/binary_search_tree.py) ~ 
[Code MIT](https://github.com/UnacceptableBehaviour/algorithms/blob/master/lecture_code/L6_BST_AVL_trees/bst.py) ~ 
Reading: CLRS Chapter 10, 12.1-3

#### **DATA STRUCTURE - BST - Binary search trees**  
**type:** BST  - [binary search tree](https://en.wikipedia.org/wiki/Binary_search_tree)  
**use cases:** sorted data, priority queue 
**queries:** next_smaller, next_larger, search/find, min, max, node_count_before  
**updates:** insert, delete  
**representation invariant (RI):** ALL children to left are smaller, ALL children to the right are larger.  
**properties:** sorted data  
See [R5 - Recursion Trees, Binary Search Trees](#r5---recursion-trees-binary-search-trees) for queries / updates walkthrough

#### Vid contents
0-6m	define problem - runway scheduling - to demonstrate BST ADT  
6m-21m	EGs things that dont work: sorted array, sorted list(no fast insertion), heap(no successor/ predecessor or pointers)  
21m	intro to BSTs  
24m	BST RI  
26m	insert() - O(h) - height of tree - **O(logn)** - n=number of nodes  
35m	min() - O(h) - go farthest left   
36m	max() - O(h) - go farthest right  
37m-43	Functional **AUGMENTATION** - Rank(t) - how many planes land before time t?   
              Add number of nodes below node to it. (number includes node itself)  
43m	AUGMENTATION - Rank k - algorithm code   



Concept: Representation Invariant - property of the data structure  
Invariant (RI): All children to left are smaller, all children to the right are larger.  
Each node has 3 pointers: parent, lchild, rchild  
```
      x
     / \
   <x   >x
```

Runway scheduling problem. Insert aircraft landing  at least k minutes (3 min in this case) away from any other scheduled landings.  
Plane landing @:	2  5  37  44  99  
**Steps**  
Find position  
Check if theres 3min space either side  
Insert new landing  

Implemented as **sorted array**  
Find insertion point: use binary search - O(logn)  logarithmic time  
Check space to land (3minutes) - O(1) constant time  
Insert (requires shifting each element to make space for insertion - worst case front of array) O(n) - linear time  

Implemented as **sorted (linked) list**  
Insert is pointer manipulation - O(1) constant time - better  
No binary search on a list! - so brute force O(n)  

Implemented as **heap**  
Check for element n1 <= k <= n2 requires searching whole tree - O(n)  

Implemented as **binary search tree (BST)**  
Find, navigate tree left if looking for an earlier time, right if larger. worst case from root of tree to leaf - ie height O(h)  
Check do check at each node O(1)  
Insert pointer manipulation O(1)  

**Other O(h) operations**  
Min - far left leaf  
Max - far right leaf  
Next largest value - Up a node? NO its next right node - parent.min() - smallest node of parent subtree. (or parent if no subtree)  

#### Augmented BST - 37m - node_count_before  
Augmented BST add subtree size to the data in the node. Includes the node and its children (number after dash in tree below).    
Maintained by incrementing the tree size by one as theyre traversed to an insertion.  

To find how many planes scheduled to land before time t?  
Find highest node that is smaller than t return tree size to the left of the node including it.  
Which is node subtree size - right_child subtree size (since all these nodes are higher) - **ALMOST**  
To the left of the tree including back up the tree! Work through example!    

```
                    129-12

        104-5                   158-6

   82-3       116-1     **138-3       184-2    

77-1 103-1  -     -    134-1 141-1 175-1  -   
```

For t=138 number planes scheduled before are - 43m  
All of left subtree: left_child.tree_size = 1  
plus  
(find first **parent** node less than 138) = 129.left_child.tree_size + 1(node 129) = 6  
gives  
total: 7  

**Algorithm:**
```
Start at root is **t** larger than node?  
YES - add left_child.tree_size + 1 to total, move to right_child  
NO - move to left_child  
Repeat until no more children or t = node  
Return total  
```

### R5 - Recursion Trees, Binary Search Trees
[vid](https://www.youtube.com/watch?v=r5pXu1PAUkI&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=28) ~ 
[lect notes](https://courses.csail.mit.edu/6.006/fall11/rec/rec05.pdf) ~ 
[Code 1st guess](https://github.com/UnacceptableBehaviour/algorithms/blob/master/algos/binary_search_tree.py) ~ 
[Code MIT](https://github.com/UnacceptableBehaviour/algorithms/blob/master/lecture_code/L6_BST_AVL_trees/bst.py) ~ 

#### Vid contents
3m-14m 	Solving Recurrence for merge sort. (PS2 problem 1)
14m-26m	Data structures, HEAP
26m-35m	Data structures, BST, (unbalanced)
35m-42m 	BST find successor/predecessor
42m-54m 	BST delete, 3 cases O(h) height of tree
54m-end	BST augmentation - Uses example min - needed for problem set

#### Maths notes  
Solving Recurrence for merge sort:
```
def merge_sort(unsorted_array)						# n elements
    bisect unsorted_array into aL & aR
	while aL elements > 1: left = merge_sort(aL)	# keep going if more than one element
	while aR elements > 1: right = merge_sort(aR)	
	return merge(left, right)						# nulls removed in merge
```

1st term: merge_sort calls itself twice with n/2 elements 2T(n/2)
2nd term: merge take O(n)? but n=1 in final node so O(1) constant time

T(n) = 2T(n/2) + O(n)             # recurrence
T(1) = Θ(1)                       # base case - merge (1 element)

```
merge_sort call with number of elements
              n
       n/2            n/2
  n/4      n/4    n/4      n/4             # each recursion
	|
until reach base case
	|
1   1   1   1  . . .  1   1   1   1        # base case
```


Binary Search Tree (BST) 
Local: algos/binary_search_tree.py


#### get_successor()
```
Example tree
                                               67                                               

                       45                                             129                       

           15                      57                     104                     158           

     -           29          -           66          82         116         138         184     

  -     -     17    35    -     -     -     -     77   103    -     -    134   141   175    -   

 -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  90 -  -  -  -  -  -  -  -  -  -  -  -  - 
rc = right_child   rp = right_parent(node == node.parent.left)

# case 1 - node has rc
return rc.min


# case 2 - node has no rc (dont care about lc always smaller)
         - has rp (left of parent : node == node.parent.left)
return parent


# case 3 - node has no rc or rp
         - right of parent : node == node.parent.right
go up parent until one has a right parent
return that

Case 3 covers case two - so no need to implement case 2
```

#### delete()
```
Example tree - BST (Binary search tree - unusually flat! Can be very lopsided)
                                               67                                               

                       45                                             129                       

           15                      57                     104                     158           

     -           29          -           66          82         116         138         184     

  -     -     17    35    -     -     -     -     77   103    -     -    134   141   175    -   

 -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  90 -  -  -  -  -  -  -  -  -  -  -  -  - 
rc = right_child   rp = right_parent(node == node.parent.left)

case 1: leaf
	simply delete

case 2: delete single node with only one sub-tree
	EG delete 15, 57 or 184
	replace parent pointer to node to point at subtree
	straight or zig/zag its the same

case 2: deleting a node that has 2 subtrees
	replace node with successor - smallest element in right subtree
	successor may have a subtree so need to call delete on it first
	replace original deleted node with it
	(from R5-44m50)


	running time 
		find key O(h) +
		delete - possible 2 subtrees O(h)
		link swaps constant time O(1)
		= O(h) + O(h) + O(1) = 2 * O(h) + O(1) = O(h)

```



### L6 - AVL trees, AVL sort	
[vid](https://www.youtube.com/watch?v=FNeL18KsWPc&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=6) - 
[lect notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec06.pdf) - 
[MIT EG code](https://github.com/UnacceptableBehaviour/algorithms/blob/master/lecture_code/L6_BST_AVL_trees/avl.py) - 
[guess implementation code](https://github.com/UnacceptableBehaviour/algorithms/blob/master/algos/AVL.py)  
 

#### **DATA STRUCTURE - AVL tree - R6 50m**  
**type:**  tree (balanced )  
**use cases:** sort & retrieve data set, prefered in search intensive application, insert more costly  
**queries:** min, max, successor, predecessor, search - Θ(logn), in-order traversal - Θ(n)  
**updates:** insert item - Θ(logn), insert n items - Θ(nlogn), delete item - Θ(logn), rebalance    
**RI:** height left/right trees only every differ by 1 - balanced tree   
**RI from BST:** ALL children to left are smaller, ALL children to the right are larger.  
**properties:** height = logn => tree balanced - height & balance maintained in each node   
RI - representation invariant  

#### Vid contents  
0-2m - BST summary - in-order traversal using recursion  
2m-11m - importance of being balanced -  getting HEIGHT to be logn - local HEIGHT calculation  
11m - AVL trees definition and balance  
18m - showing height is logn  
10-28m - height of balanced tree maths  
19m-25m - Analyse Nh min nodes in a tree of height h - v1  
26m-XXm - Analyse Nh min nodes in a tree of height h - v2 - ps3  
32m-48m -  Rotations  
48m-52  - AVL sort  
50m - summary of heap / bst AVL reasons for use  

#### Example problem


#### TERMS  
AVL - inventors Adelson-Velsky and Landis   
[Visualisation of AVL tree](https://www.cs.usfca.edu/~galles/visualization/AVLtree.html)  

**In order traversal** - process nodes by key order  
**successor** - Next larger  
**predecessor** - next smaller  
**height** of a node - longest path down to a leaf from node  including itself (the +1 below)  
**depth** of a node - node in path from root to node
**balanced** tree - height of left child = height of right child  +/-1 - height h = **logn**

IMPORTANCE OF A BALANCED TREE - height being log n   
Unbalance tree worst case height - n average n/2  << V.BAD!  

```
height  = max(lchild height, rchild height) +1  max(3,8)+1 = 9  (maintained in each node)  
```

NOTE:  NULL child node have a height of -1 so cal works - max(-1,-1)+1 = 0  
information local to node has low (constant time) maintenance over head   
largest_height also store which height is larger +1 left,  0 equal, -1 right


#### Maths notes - AVL tree (19-25m) - height analysis v1
Min number of nodes in a balanced tree

![Total nodes in AVL tree](https://github.com/UnacceptableBehaviour/algorithms/blob/master/formulae/L6_AVL_trees_00_22m33.png)  

<p align="center"><img src="/tex/383c5c1963e50e762b29e138eb72d9e5.svg?invert_in_darkmode&sanitize=true" align=middle width=576.5765841pt height=75.6164376pt/></p>

IE In a tree of height h, number of nodes n,  is the sum of: the root + the two sub trees (that differ in height by 1).   

The above recurrence is similar to the Fibonacci sequence, defined as:
<p align="center"><img src="/tex/879e4c656816fb13d3336800ffc32155.svg?invert_in_darkmode&sanitize=true" align=middle width=416.60102385pt height=16.438356pt/></p>

an approximation for which is  (Fibonacci number = nearest integer . . .
<p align="center"><img src="/tex/10bc491a11e7caa7ce2adf0dc2bb4654.svg?invert_in_darkmode&sanitize=true" align=middle width=519.082245pt height=40.66383749999999pt/></p>

[paper showing the above here](https://sites.math.northwestern.edu/~mlerma/problem_solving/results/recurrences.pdf)  

<p align="center"><img src="/tex/3507b4c628b099bdc90c8d77576a879e.svg?invert_in_darkmode&sanitize=true" align=middle width=488.94835109999997pt height=40.364374049999995pt/></p>

Since Nh = min nodes in a tree of height h, and phi = 1.618.

<p align="center"><img src="/tex/4605c59e9c2d5e486a9018ec99ad8368.svg?invert_in_darkmode&sanitize=true" align=middle width=479.47994324999996pt height=40.364374049999995pt/></p>
<p align="center"><img src="/tex/513de2a713c2b966f334198bbcc3f720.svg?invert_in_darkmode&sanitize=true" align=middle width=475.66339754999996pt height=17.031940199999998pt/></p>

#### Maths notes - AVL tree (26m) - height analysis v2





Method of maintaining property: balanced AVL tree.  << WHOLE LECTURE ABOUT THIS!

**insert(x)** - steps to do an insert
```
insert as normal for BST
update each nodes height while parsing tree (and largest_height L M R - left middle right)
largest_height = hL - hR 
from inserted node walk up the tree checking largest_height if abs(largest_height) > 2
	if largest_height > 2 right-rotate	(left height too large)
	if largest_height < -2 anti-rotate	(right height too large)
```

What the above is saying is - if the difference in height between to children is more than +/-1 then tree need rebalancing
	
Rotation Cases (@ 32m)
```
      29
     /
   26
  /
23              # left height too large 
      
   26           # right-rotate 29
  /  \
23    29
```
2nd case
```
      65
     /
   50
     \
      55        # zig zag requires 2 rotations:
					
      65        # left-rotate 50
     /
   55
  /
50              # right-rotate 65:

   55
  /  \
50    65

```



50m good summary of heap / bst AVL reasons for use



### R6 - maths & code
[vid]()  
[lect notes](https://courses.csail.mit.edu/6.006/fall11/rec/rec06.pdf)  
[Code Handout](https://courses.csail.mit.edu/6.006/fall11/rec/rec06_code_handout.pdf)
Reading: 

#### Vid contents
0-7m - BST review, height,
7m-  AVL balance



#### BST review
height h = longest path to leaf

**4m28** - diagram on board show a single node has a height of 0
then he writes 
```
height  = max(lchild height, rchild height) +1  max(3,8)+1 = 9  (maintained in each node)  
```
which means tit should be 1 - ?? 
The code line - Height Augmentation ln 7 says 1
```
def update_height(node): 8 node.height = max(height(node.left), height(node.right)) + 1
```
**6m** for case where node is a leaf height returns -1!
so the root evaluates to max(-1,-1)+1 = 0

#### AVL properties
<p align="center"><img src="/tex/e7aac7e676b9fa8a486e5a3b49b6af71.svg?invert_in_darkmode&sanitize=true" align=middle width=157.18425854999998pt height=89.49772094999999pt/></p>
<p align="center"><img src="/tex/f57a1206b4d8107434bf43e707ba7447.svg?invert_in_darkmode&sanitize=true" align=middle width=180.9113328pt height=63.92694825pt/></p>
<p align="center"><img src="/tex/e995c36961b11f1a0347824daca8f22f.svg?invert_in_darkmode&sanitize=true" align=middle width=139.04518815pt height=40.182651299999996pt/></p>
Reads **for all** n, height of left and right subtree differs by 1 or less - basically says this tree is **balanced**


#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  



 	
### Problem set 2 (due)
#### 2-1 Fractal rendering [40pts]
Koch snowflake rendering: computational requirements of 4 ways of rendering LoD n (Level of Detail 0-n)
	Recitation 5 (0m - 13m) explains how to do this - dont be scared if you costs at each level arent the same sum them up and youll get the right answer
	Recursion tree - forrest of trees in this case
	Run example code fractal.html (/algorithms/problems/MIT6_006F11_ps2/fractal)
First - 3D hardware accelerated rendering . .
Surface > triangles > CPU co-ords list > GPU renders
a) [1pt] height of recursion tree for rendering snowflake of LoD n?
b) [1pt] how many node in the tree at level n
c) [1pt] whats the rendering time (triangle count) for a node at depth i
d) [1pt] whats the rendering time (triangle count) at each level i (all nodes on that level)
e) [1pt] total asymptotic cost for the CPU to render LoD n (using this method)

Second - 2D accelerated rendering . .
Surface oulines > open/closed paths > CPU co-ords list > GPU renders (used in laser cutters & plotters)
Properties of a koch snowflake 
f) [1pt] height of recursion tree for rendering snowflake of LoD n?
g) [1pt] how many node in the tree at level n
h) [1pt] whats the rendering time (line segment count) for a node at depth i
i) [1pt] whats the asymptotic rendering time (line segment count) for a node in the last level n
j) [1pt] whats asymptotic rendering time (line segment count) at each level of the tree
k) [1pt] whats the asymptotic rendering time (line segment count) at the last level n	
l) [1pt] total asymptotic cost for the CPU to render LoD n (using this method)

Third - 2D unaccelerated rendering . . aka software rendering (CPU only) (used in laser cutters & plotters)
Surface oulines > open/closed paths > CPU co-ords list > CPU rasterises co-ords 
NOTE the rasterised pixels represent the ink required to print or the the power required for laser to cut the image!!
m) [1pt] height of recursion tree for rendering snowflake of LoD n?
n) [1pt] how many node in the tree at level n
o) [1pt] whats the rendering time (line segment length) for a node at depth i (assume original triangle side length = 1)
p) [1pt] whats the asymptotic rendering time (line segment length) for a node in the last level n
q) [1pt] whats asymptotic rendering time (line segment length) at each level of the tree
r) [1pt] whats the asymptotic rendering time (line segment length) at the last level n	
s) [1pt] total asymptotic cost for the CPU to render LoD n (using this method)

Fourth - 3D unaccelerated rendering . . (CPU only)
Surface > triangles > CPU co-ords list > CPU rasterises
t) [4pt] total asymptotic cost for the CPU to render LoD n (using this method - assume initial triangle side length = 1)
u) [15pt] prove using recursion tree method

#### 2-2 Digital Circuit Simulation [60pt]

a) What name of method w highest CPU usage? _find_min part of class

Profiler Qs
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     15/6    0.000    0.000    0.001    0.000 sre_parse.py:414(_parse)
Whats the 15/6 mean under ncalls? Recursive call here: 6 primitive call 15 in total

Profiler column meanings: https://docs.python.org/3/library/profile.html
```
ncalls
    for the number of calls.
tottime
    for the total time spent in the given function (and excluding time made in calls to sub-functions)
percall
    is the quotient of tottime divided by ncalls
cumtime
    is the cumulative time spent in this and all subfunctions (from invocation till exit). This figure is accurate even for recursive functions.
percall
    is the quotient of cumtime divided by primitive calls
filename:lineno(function)
    provides the respective data of each function
```

Full result of profiler in: circuit/profiler_output.txt
```
        628290079 function calls (628095620 primitive calls) in 474.045 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   259964  275.241    0.001  471.218    0.002 circuit.py:381(_find_min)         ** CULPRIT
625762426  195.969    0.000  195.969    0.000 circuit.py:286(__lt__)            # less than dunder function
    64400    0.788    0.000  473.659    0.007 circuit.py:423(step)		# simulation time step > _find_min > __lt__
828936/634537    0.264    0.000    0.340    0.000 {len}
    65554    0.233    0.000    0.421    0.000 circuit.py:163(transition_output)
   194381    0.216    0.000  471.437    0.002 circuit.py:361(min)
        1    0.173    0.173  473.948  473.948 circuit.py:456(run)
        1    0.001    0.001  474.045  474.045 circuit.py:3(<module>)
```

To run tests:
```
> python circuit_test.py                                               # whole suite - 6min

> python circuit.py  < tests/1gate.in > out                            # run single test write results out

> diff out tests/1gate.gold                                            # compare result to verified result

> python -m cProfile -s time circuit.py < tests/5devadas13.in          # profile test - take nearly 8min!

> TRACE=jsonp python circuit.py < tests/1gate.in > circuit.jsonp		# create a trace for visualiser
> TRACE=jsonp python circuit.py < tests/2gates.in > circuit.jsonp		# create a trace for visualiser
> TRACE=jsonp python circuit.py < tests/3xor.in > circuit.jsonp
> TRACE=jsonp python circuit.py < tests/4sort.in > circuit.jsonp

EG
> python circuit_test.py 
Testing correctness:
Testing 1gate.in ...... OK
Testing 2gates.in ...... OK
Testing 3xor.in ...... OK
Testing 4sort.in ...... OK
Testing 5devadas13.in ...... OK
.
----------------------------------------------------------------------
Ran 1 test in 360.847s
OK

> python circuit.py  < tests/1gate.in 
19 axb 1
29 axb 0

```

b) How many time is this method called? 259964
c) What tightest asymptotic bound of the worst case running time of the method with the bottleneck?
d) If implemented optimally whats the tightest asymptotic bound of the re-implemented method?
e) Re-write the data structure using the most efficient method from class (no lib imports)


### L7 - Counting sort, radix sort, lower bounds for sorting and searching
[vid](https://www.youtube.com/watch?v=Nz1KZXbghj8&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=8&t=0s)  
[lect notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec07.pdf)  

#### Sorting in Linear-Time  
- **comparison model**   (computation model)  
- lower bounds  
. . searching: Ω(lg n) - binary search is optimal  
. . sorting: Ω(n lg n) - merge sort is optimal  
  
- **ram model**   (computation model)  
- O(n) sorting algorithms  
. . counting sort  
. . radix sort  

CONCEPTS: Models of computation: 

Proofs up to 32m  upt to here all comparison model.

### R7 - maths & code - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
[vid]()  
[lect notes](https://courses.csail.mit.edu/6.006/fall11/rec/)  
Code:
Reading: 

#### Vid contents

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  




		Problem set 3 out
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Unit 3: Hashing
### L8 - Hashing with chaining - (dictionary / associative array)	 
[vid](https://www.youtube.com/watch?v=0M_kIqhwbFo&t=758s)  
[lect notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec08.pdf)  
[succinct vid on hashing, open addressing & chaining](https://www.youtube.com/watch?v=KyUTuwz_b7Q)  

Python built in hash() - should be called prehash - but basically return and integer based on the input. (to use as a key for dict for example)
```
Python dunder function __hash__ is called when built in hash(object) is called.
if you dont implement hash hash(obj) used id(obj) to create hash
```

Methods for dealing with collisions (Chaining @ 30m & open addressing (next week) )
  one type of open addressing is linear probing


I you have a space of keys, run those through hash function to generate indexes (ideally they should be equally distributed through the target array)
The ratio of number of indexes (entries) (n) : number of array spaces (m)  is the load factor 
Check understanding here!
See L9 1m-
Sunccict sunopsis of last lecture!!  Including above
note the n may end up in a linked list for chaining

LAST 10m re-watch 

### R8 - maths & code - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
[vid]()  
[lect notes](https://courses.csail.mit.edu/6.006/fall11/rec/)  
Code:
Reading: 

#### Vid contents

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  



### L9 - Table doubling, Karp-Rabin
[vid](https://www.youtube.com/watch?v=BRO7mVIFt08) ~ [lect notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec09.pdf)  
Code:
Reading:


How to choose m (table size)  - (on overflow double it)

Amortisation 15m

When array becomes full n=m,  double in size m*2
When shrinking shrink when n gets to m/4 shrink m to m/2

** Invariant property: n <= m <= 4n ***
n has to be smaller than m (size of structure) or entries wont fit in the data structure
If n falls to m/4 halve structure size m = m/2

27m - listen to concept
Term: constant amortised - note on python lists
Means  amortized time


Rolling hash ADT - pseudo code. 41m - 47m  - 1987? getting more recent
	use choosing size using random prime 

### R9 - maths & code - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
[vid]()  
[lect notes](https://courses.csail.mit.edu/6.006/fall11/rec/)  
Code:
Reading: 

#### Vid contents

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  




		Problem set 3 due
		Problem set 4 out

### L10 - Open addressing, cryptographic hashing  
[vid]()  
[lect notes]()  
Code:
Reading:

#### **DATA STRUCTURE**  
type:  
use cases: good for bla  
queries:  
updates:  
representation invariant (RI):   
properties:  

#### Vid contents  

#### Example problem

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  

### R10 - maths & code - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
[vid]()  
[lect notes](https://courses.csail.mit.edu/6.006/fall11/rec/)  
Code:
Reading: 

#### Vid contents  

#### Example problem

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  



## Problem set 4 due
## Quiz 1	 

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Unit 4: Numerics
### L11 - Integer arithmetic, Karatsuba multiplication	
[vid]()  
[lect notes]()  
Code:
Reading:

#### **DATA STRUCTURE**  
type:  
use cases: good for bla  
queries:  
updates:  
representation invariant (RI):   
properties:  

#### Vid contents  

#### Example problem

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  

### R11 - maths & code - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
COPY RECITATION TEMPLATE into further lectures
[vid]()  
[lect notes](https://courses.csail.mit.edu/6.006/fall11/rec/)  
Code:
Reading: 

#### Vid contents  

#### Example problem

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  



## Problem set 5 out

### L12 - Square roots, Newton's method	 
[vid]()  
[lect notes]()  
Code:
Reading:

#### **DATA STRUCTURE**  
type:  
use cases: good for bla  
queries:  
updates:  
representation invariant (RI):   
properties:  

#### Vid contents  

#### Example problem

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Unit 5: Graphs
### L13 - Breadth-first search (BFS)	 
[vid]()  
[lect notes]()  
Code:
Reading:

#### **DATA STRUCTURE**  
type:  
use cases: good for bla  
queries:  
updates:  
representation invariant (RI):   
properties:  

#### Vid contents  

#### Example problem

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  



### L14	Depth-first search (DFS), topological sorting
[vid]()  
[lect notes]()  
Code:
Reading:

#### **DATA STRUCTURE**  
type:  
use cases: good for bla  
queries:  
updates:  
representation invariant (RI):   
properties:  

#### Vid contents  

#### Example problem

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  



## Problem set 5 due
## Problem set 6 out

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Unit 6: Shortest Paths
### L15 - Single-source shortest paths problem	 
[vid]()  
[lect notes]()  
Code:
Reading:

#### **DATA STRUCTURE**  
type:  
use cases: good for bla  
queries:  
updates:  
representation invariant (RI):   
properties:  

#### Vid contents  

#### Example problem

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  



### L16 - Dijkstra	 
[vid]()  
[lect notes]()  
Code:
Reading:

#### **DATA STRUCTURE**  
type:  
use cases: good for bla  
queries:  
updates:  
representation invariant (RI):   
properties:  

#### Vid contents  

#### Example problem

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  



### L17 - Bellman-Ford	 
[vid]()  
[lect notes]()  
Code:
Reading:

#### **DATA STRUCTURE**  
type:  
use cases: good for bla  
queries:  
updates:  
representation invariant (RI):   
properties:  

#### Vid contents  

#### Example problem

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  



### L18 - Speeding up Dijkstra
[vid]()  
[lect notes]()  
Code:
Reading:

#### **DATA STRUCTURE**  
type:  
use cases: good for bla  
queries:  
updates:  
representation invariant (RI):   
properties:  

#### Vid contents  

#### Example problem

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  



		Problem set 6 due
	 	Quiz 2	 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Unit 7: Dynamic Programming
### L19 - Memoization, subproblems, guessing, bottom-up; Fibonacci, shortest paths
[vid]()  
[lect notes]()  
Code:
Reading:

#### **DATA STRUCTURE**  
type:  
use cases: good for bla  
queries:  
updates:  
representation invariant (RI):   
properties:  

#### Vid contents  
0-5m - Introduction to Dynamic Programming (DP) recursion + memoization + guessing
5m-11m20 - Solving Fibonacci w/ Memoization - naive version
11m20-15m40 - Memoized version
15m40- running cost Θ(n) - **rule 30m49 flashback** for acyclic sub problems
19m30-23m - DP generalisation, running cost
23m-29m Bottom-up DP algorithm (topological sort)
29m-51m shortest paths, converting cyclic paths to acyclic & bellman-ford

#### Example problem

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  



## Problem set 7 out

### L20 - Parent pointers; text justification, perfect-information blackjack	 
[vid]()  
[lect notes]()  
Code:
Reading:

#### **DATA STRUCTURE**  
type:  
use cases: good for bla  
queries:  
updates:  
representation invariant (RI):   
properties:  

#### Vid contents  

#### Example problem

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  




### L21 - String subproblems, psuedopolynomial time; parenthesization, edit distance, knapsack  
[vid]()  
[lect notes]()  
Code:
Reading:

#### **DATA STRUCTURE**  
type:  
use cases: good for bla  
queries:  
updates:  
representation invariant (RI):   
properties:  

#### Vid contents  

#### Example problem

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  



### L22 - Two kinds of guessing; piano/guitar fingering, Tetris training, Super Mario Bros.[vid]()  
[vid]()  
[lect notes]()  
Code:
Reading:

#### **DATA STRUCTURE**  
type:  
use cases: good for bla  
queries:  
updates:  
representation invariant (RI):   
properties:  

#### Vid contents  

#### Example problem

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  



## Problem set 7 due

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
## Unit 8: Advanced Topics
### L23 - Computational complexity	 
[vid]()  
[lect notes]()  
Code:
Reading:

#### **DATA STRUCTURE**  
type:  
use cases: good for bla  
queries:  
updates:  
representation invariant (RI):   
properties:  

#### Vid contents  

#### Example problem

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  



### 24 - Algorithms research topics
[vid]()  
[lect notes]()  
Code:
Reading:

#### **DATA STRUCTURE**  
type:  
use cases: good for bla  
queries:  
updates:  
representation invariant (RI):   
properties:  

#### Vid contents  

#### Example problem

#### Maths notes  
Any equation identities / topics for this lecture include context and uses for later reference  





## Glossary of terms

The following symbols o, Ω, ω, and Θ, are used to describe differing kinds of bounds on asymptotic growth rates.  
O - big O - describes the asymptotic behaviour of functions WORST case or UPPER bound (common in **CompSci**)  
Θ - big Theta - describes the asymptotic behaviour of functions AVERAGE case (common in **CompSci**)  
Ω - big Omega - BEST case or LOWER bound (common in **CompSci**)  
o - little O - loose upper bound (common in Maths rare in CompSci)  
ω - little omega - rough estimate of the order of the growth (rarely used)  
T(n) - function defining the exact Time or number of steps to complete an algorithm for n items  

Binary tree types:  
Full			All nodes have 2 children or 0 children (one child not allowed)  
Complete	Filled top to bottom left to right (and removed in reverse, data position likely re-ordered to preserve RI - EG Heap)  
Perfect		All layers have all their nodes  
Balanced	Usually refers to weight height balance leaf depths differ by no more than 1 (can also be weight balanced)

ADT - Abstract Data Type (interface definition, methods & properties)  
DS - Data Structure (actual implementation of the ADT)  
RI - representation invariant  

Note for array of **any** size tree: element A[n/2+1 . . n] are ALL leaves! 


## How To s
### How so I plot a chart with python?
```
> .pe						# alias .pe='. venv/bin/activate'
> pip install matplotlib			# plotting lib
> pip install numpy				# math sci lib 
> ./matplotlib/plot.py				# super basic 2d plot example - in maths repo
```
[./matplotlib/time_complexity_plot_q.py](https://github.com/UnacceptableBehaviour/algorithms/blob/master/matplotlib/time_complexity_plot_q.py)  

### How to setup autogenerate README.md file from RTF notes?
```
> python --version			# Python 2.7.16
> python3 -m venv venv
> .pe					# alias .pe='. venv/bin/activate'
> python --version			# Python 3.7.5
> pip install --upgrade pip
> pip install striprtf			# for rtf processing
```

### How do I autogenerate README.md file from RTF?
```
> .pe				# alias .pe='. venv/bin/activate'
> ./create_TOC_for_md.py -p	# takes MATHS_00_MIT_6.042.rtf course notes and add TOC > README.md
				# also add README.md to git, commits, and pushes
				# -p = commit & push
```

### How can I add maths formulas to README.md?
#### Manually: Generate math image and embed it.
Install Latex tools [notes here](https://github.com/UnacceptableBehaviour/latex_maths/blob/master/context.md)  
Open LaTeXit edit equation click text and hit the LaTeXit button to check its good.  
Export as png and upload it to git (need to do this so the URL and be used to embed the image)  
Embed image with  
```
![uses dot product of the vector of each document](https://github.com/UnacceptableBehaviour/algorithms/blob/master/formulae/20200228_1715_dot_prod_doc_distance.png)  
Note the ! before opening [ denotes image
```
#### Automagically:  Install texify.
[Find texify here](https://github.com/agurodriguez/github-texify)  
Use LaTeXit to check formula correctness then past it into doc surrounded by consecutive \$ symbols like so
![latex script](https://github.com/UnacceptableBehaviour/latex_maths/blob/master/images/latex_example.png)  

Will display the following document distance equation  
<p align="center"><img src="/tex/a5a3fa25cf152acc801491db474d6460.svg?invert_in_darkmode&sanitize=true" align=middle width=407.98942304999997pt height=64.10978970000001pt/></p>

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
 