# Rank movement explanations

Baseline mode: **baseline**
Compare mode: **structure_rerank**
Cutoff: **top-10**

## q1

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p5 | 2 | up | 6 | 5 | 1 | 0.840866 | 0.568173 |
| p7 | 1 | entered_top_k | None | 10 | None | 0.794727 | 0.158945 |
| p6 | 0 | up | 7 | 4 | 3 | 0.887006 | 0.577401 |
| p14 | 0 | up | 3 | 2 | 1 | 0.840866 | 0.768173 |
| p16 | 0 | up | 8 | 7 | 1 | 0.008475 | 0.401695 |
| p2 | 0 | left_top_k | 10 | None | None | None | None |
| p9 | 0 | down | 2 | 3 | -1 | 0.008475 | 0.601695 |
| p3 | 0 | down | 4 | 6 | -2 | 0.008475 | 0.401695 |

## q10

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p13 | 1 | entered_top_k | None | 6 | None | 0.852564 | 0.170513 |
| p10 | 0 | entered_top_k | None | 8 | None | 0.717949 | 0.14359 |
| p16 | 0 | entered_top_k | None | 7 | None | 0.852564 | 0.170513 |
| p4 | 0 | left_top_k | 8 | None | None | None | None |
| p5 | 0 | left_top_k | 9 | None | None | None | None |
| p6 | 0 | left_top_k | 10 | None | None | None | None |
| p1 | 0 | down | 6 | 9 | -3 | 0.0 | 0.0 |
| p2 | 0 | down | 7 | 10 | -3 | 0.0 | 0.0 |

## q2

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p5 | 1 | down | 6 | 8 | -2 | 0.009804 | 0.201961 |
| p18 | 0 | up | 9 | 6 | 3 | 0.888889 | 0.377778 |
| p19 | 0 | up | 10 | 7 | 3 | 0.732026 | 0.346405 |
| p11 | 0 | down | 7 | 9 | -2 | 0.009804 | 0.201961 |
| p16 | 0 | down | 8 | 10 | -2 | 0.009804 | 0.201961 |

## q3

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p16 | 3 | up | 9 | 4 | 5 | 0.923567 | 0.584713 |
| p20 | 1 | up | 10 | 5 | 5 | 0.923567 | 0.584713 |
| p5 | 0 | down | 5 | 7 | -2 | 0.011465 | 0.402293 |
| p9 | 0 | down | 7 | 10 | -3 | 0.0 | 0.4 |
| p4 | 0 | down | 4 | 9 | -5 | 0.0 | 0.4 |

## q4

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p10 | 3 | up | 2 | 1 | 1 | 1.0 | 1.0 |
| p4 | 3 | down | 1 | 2 | -1 | 0.91411 | 0.982822 |
| p18 | 0 | up | 9 | 6 | 3 | 0.009202 | 0.268507 |
| p11 | 0 | up | 6 | 5 | 1 | 0.773006 | 0.421268 |
| p1 | 0 | left_top_k | 10 | None | None | None | None |
| p14 | 0 | entered_top_k | None | 10 | None | 0.773006 | 0.154601 |
| p15 | 0 | down | 7 | 8 | -1 | 0.0 | 0.266667 |
| p16 | 0 | down | 8 | 9 | -1 | 0.0 | 0.266667 |

## q5

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p17 | 3 | up | 4 | 2 | 2 | 0.854839 | 0.570968 |
| p4 | 2 | down | 6 | 9 | -3 | 0.008065 | 0.26828 |
| p14 | 0 | up | 9 | 6 | 3 | 0.639785 | 0.394624 |
| p5 | 0 | up | 7 | 4 | 3 | 0.693548 | 0.405376 |
| p11 | 0 | up | 8 | 7 | 1 | 0.602151 | 0.387097 |
| p1 | 0 | down | 2 | 3 | -1 | 0.677419 | 0.535484 |
| p9 | 0 | down | 3 | 5 | -2 | 0.016129 | 0.403226 |
| p3 | 0 | down | 5 | 8 | -3 | 0.016129 | 0.269892 |

## q6

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p13 | 3 | up | 3 | 1 | 2 | 1.0 | 1.0 |
| p20 | 2 | entered_top_k | None | 5 | None | 0.951768 | 0.590354 |
| p1 | 1 | down | 5 | 6 | -1 | 0.014469 | 0.402894 |
| p14 | 0 | up | 9 | 7 | 2 | 0.007235 | 0.401447 |
| p12 | 0 | left_top_k | 8 | None | None | None | None |
| p15 | 0 | left_top_k | 10 | None | None | None | None |
| p18 | 0 | entered_top_k | None | 8 | None | 0.007235 | 0.401447 |
| p11 | 0 | down | 2 | 3 | -1 | 0.007235 | 0.801447 |

## q7

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p11 | 3 | up | 2 | 1 | 1 | 1.0 | 1.0 |
| p5 | 3 | down | 1 | 2 | -1 | 0.959677 | 0.991935 |
| p10 | 0 | up | 8 | 4 | 4 | 0.755376 | 0.351075 |
| p7 | 0 | up | 7 | 6 | 1 | 0.677419 | 0.335484 |
| p12 | 0 | left_top_k | 9 | None | None | None | None |
| p13 | 0 | left_top_k | 10 | None | None | None | None |
| p17 | 0 | entered_top_k | None | 5 | None | 0.717742 | 0.343548 |
| p19 | 0 | entered_top_k | None | 10 | None | 0.639785 | 0.227957 |

## q8

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p17 | 0 | up | 10 | 5 | 5 | 0.793103 | 0.318621 |
| p5 | 0 | up | 6 | 4 | 2 | 0.793103 | 0.318621 |
| p16 | 0 | down | 9 | 10 | -1 | 0.0 | 0.16 |
| p4 | 0 | down | 5 | 6 | -1 | 0.683908 | 0.296782 |
| p12 | 0 | down | 7 | 9 | -2 | 0.0 | 0.16 |
| p1 | 0 | down | 4 | 7 | -3 | 0.010345 | 0.162069 |

## q9

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p5 | 0 | up | 5 | 4 | 1 | 0.792453 | 0.318491 |
| p1 | 0 | left_top_k | 6 | None | None | None | None |
| p10 | 0 | entered_top_k | None | 5 | None | 0.836478 | 0.167296 |
| p11 | 0 | entered_top_k | None | 7 | None | 0.792453 | 0.158491 |
| p14 | 0 | entered_top_k | None | 8 | None | 0.792453 | 0.158491 |
| p17 | 0 | entered_top_k | None | 9 | None | 0.792453 | 0.158491 |
| p3 | 0 | left_top_k | 7 | None | None | None | None |
| p6 | 0 | left_top_k | 9 | None | None | None | None |
