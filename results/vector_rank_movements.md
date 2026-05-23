# Rank movement explanations

Baseline mode: **vector_baseline**
Compare mode: **vector_structure_rerank**
Cutoff: **top-10**

## q1

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p5 | 2 | up | 9 | 7 | 2 | 0.840866 | 0.43672 |
| p7 | 1 | entered_top_k | None | 10 | None | 0.794727 | 0.158945 |
| p6 | 0 | up | 7 | 4 | 3 | 0.887006 | 0.546004 |
| p2 | 0 | left_top_k | 10 | None | None | None | None |
| p10 | 0 | down | 4 | 5 | -1 | 0.0 | 0.489286 |
| p16 | 0 | down | 8 | 9 | -1 | 0.008475 | 0.338451 |
| p3 | 0 | down | 5 | 6 | -1 | 0.008475 | 0.458625 |
| p4 | 0 | down | 6 | 8 | -2 | 0.0 | 0.409192 |

## q10

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p8 | 2 | up | 3 | 2 | 1 | 1.0 | 0.7007 |
| p13 | 1 | entered_top_k | None | 6 | None | 0.852564 | 0.170513 |
| p3 | 0 | up | 5 | 4 | 1 | 0.852564 | 0.443276 |
| p10 | 0 | entered_top_k | None | 8 | None | 0.717949 | 0.14359 |
| p16 | 0 | entered_top_k | None | 7 | None | 0.852564 | 0.170513 |
| p4 | 0 | left_top_k | 8 | None | None | None | None |
| p5 | 0 | left_top_k | 9 | None | None | None | None |
| p6 | 0 | left_top_k | 10 | None | None | None | None |

## q2

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p12 | 3 | up | 3 | 2 | 1 | 1.0 | 0.763417 |
| p4 | 1 | down | 4 | 5 | -1 | 0.009804 | 0.396831 |
| p19 | 0 | up | 9 | 7 | 2 | 0.732026 | 0.312075 |
| p18 | 0 | up | 5 | 4 | 1 | 0.888889 | 0.542967 |
| p11 | 0 | left_top_k | 10 | None | None | None | None |
| p2 | 0 | entered_top_k | None | 10 | None | 0.823529 | 0.164706 |
| p15 | 0 | down | 2 | 3 | -1 | 0.009804 | 0.567177 |
| p16 | 0 | down | 8 | 9 | -1 | 0.009804 | 0.188861 |

## q3

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p16 | 3 | up | 6 | 5 | 1 | 0.923567 | 0.531757 |
| p3 | 3 | up | 4 | 3 | 1 | 1.0 | 0.675621 |
| p8 | 2 | up | 8 | 7 | 1 | 0.802548 | 0.389007 |
| p20 | 1 | up | 3 | 2 | 1 | 0.923567 | 0.761547 |
| p4 | 0 | down | 7 | 8 | -1 | 0.0 | 0.244403 |
| p9 | 0 | down | 5 | 6 | -1 | 0.0 | 0.414906 |
| p12 | 0 | down | 2 | 4 | -2 | 0.011465 | 0.623613 |

## q4

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p5 | 1 | up | 7 | 4 | 3 | 0.773006 | 0.204987 |
| p7 | 0 | up | 9 | 5 | 4 | 0.773006 | 0.202556 |
| p11 | 0 | up | 5 | 3 | 2 | 0.773006 | 0.210577 |
| p1 | 0 | left_top_k | 10 | None | None | None | None |
| p14 | 0 | entered_top_k | None | 6 | None | 0.773006 | 0.154601 |
| p15 | 0 | left_top_k | 8 | None | None | None | None |
| p17 | 0 | entered_top_k | None | 7 | None | 0.773006 | 0.154601 |
| p19 | 0 | entered_top_k | None | 8 | None | 0.730061 | 0.146012 |

## q5

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p4 | 2 | down | 5 | 8 | -3 | 0.008065 | 0.250148 |
| p11 | 0 | up | 7 | 4 | 3 | 0.602151 | 0.308529 |
| p14 | 0 | up | 9 | 6 | 3 | 0.639785 | 0.289576 |
| p5 | 0 | up | 8 | 5 | 3 | 0.693548 | 0.308022 |
| p13 | 0 | left_top_k | 10 | None | None | None | None |
| p2 | 0 | entered_top_k | None | 9 | None | 0.655914 | 0.208598 |
| p3 | 0 | left_top_k | 6 | None | None | None | None |
| p7 | 0 | entered_top_k | None | 10 | None | 0.655914 | 0.206781 |

## q6

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p10 | 0 | entered_top_k | None | 7 | None | 0.720257 | 0.298331 |
| p12 | 0 | left_top_k | 9 | None | None | None | None |
| p16 | 0 | entered_top_k | None | 8 | None | 0.855305 | 0.279634 |
| p18 | 0 | left_top_k | 10 | None | None | None | None |
| p14 | 0 | down | 8 | 10 | -2 | 0.007235 | 0.24768 |
| p5 | 0 | down | 7 | 9 | -2 | 0.0 | 0.259746 |

## q7

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p10 | 0 | up | 10 | 5 | 5 | 0.755376 | 0.290132 |
| p17 | 0 | up | 8 | 3 | 5 | 0.717742 | 0.302961 |
| p1 | 0 | left_top_k | 9 | None | None | None | None |
| p19 | 0 | entered_top_k | None | 10 | None | 0.639785 | 0.166272 |
| p3 | 0 | left_top_k | 7 | None | None | None | None |
| p7 | 0 | entered_top_k | None | 7 | None | 0.677419 | 0.234293 |
| p15 | 0 | down | 3 | 4 | -1 | 0.006048 | 0.290152 |
| p13 | 0 | down | 4 | 6 | -2 | 0.012097 | 0.260502 |

## q8

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p13 | 1 | left_top_k | 7 | None | None | None | None |
| p5 | 0 | up | 9 | 5 | 4 | 0.793103 | 0.274996 |
| p4 | 0 | up | 8 | 6 | 2 | 0.683908 | 0.256863 |
| p17 | 0 | up | 5 | 4 | 1 | 0.793103 | 0.325165 |
| p1 | 0 | left_top_k | 10 | None | None | None | None |
| p10 | 0 | entered_top_k | None | 9 | None | 0.764368 | 0.152874 |
| p11 | 0 | entered_top_k | None | 8 | None | 0.793103 | 0.158621 |
| p12 | 0 | down | 4 | 7 | -3 | 0.0 | 0.175168 |

## q9

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p18 | 3 | down | 2 | 3 | -1 | 0.037736 | 0.555384 |
| p7 | 1 | up | 3 | 2 | 1 | 0.792453 | 0.584091 |
| p1 | 0 | left_top_k | 6 | None | None | None | None |
| p10 | 0 | entered_top_k | None | 5 | None | 0.836478 | 0.167296 |
| p11 | 0 | entered_top_k | None | 6 | None | 0.792453 | 0.158491 |
| p14 | 0 | entered_top_k | None | 7 | None | 0.792453 | 0.158491 |
| p17 | 0 | entered_top_k | None | 8 | None | 0.792453 | 0.158491 |
| p3 | 0 | left_top_k | 7 | None | None | None | None |
