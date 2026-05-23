# Rank movement explanations

Baseline mode: **baseline**
Compare mode: **structure_rerank**
Cutoff: **top-10**

## q1

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p5 | 2 | up | 6 | 5 | 1 | 0.314815 | 0.462963 |
| p7 | 1 | entered_top_k | None | 10 | None | 0.296296 | 0.059259 |
| p6 | 0 | up | 7 | 4 | 3 | 0.333333 | 0.466667 |
| p14 | 0 | up | 3 | 2 | 1 | 0.314815 | 0.662963 |
| p16 | 0 | up | 8 | 7 | 1 | 0.052778 | 0.410556 |
| p2 | 0 | left_top_k | 10 | None | None | None | None |
| p9 | 0 | down | 2 | 3 | -1 | 0.041667 | 0.608333 |
| p3 | 0 | down | 4 | 6 | -2 | 0.052778 | 0.410556 |

## q10

No rank movements inside the cutoff.

## q2

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p4 | 1 | down | 4 | 5 | -1 | 0.047059 | 0.409412 |
| p5 | 1 | down | 6 | 8 | -2 | 0.052941 | 0.210588 |
| p18 | 0 | up | 9 | 6 | 3 | 0.352941 | 0.270588 |
| p15 | 0 | up | 5 | 4 | 1 | 0.05 | 0.41 |
| p16 | 0 | up | 8 | 7 | 1 | 0.055882 | 0.211176 |
| p19 | 0 | left_top_k | 10 | None | None | None | None |
| p20 | 0 | entered_top_k | None | 10 | None | 0.052941 | 0.210588 |
| p11 | 0 | down | 7 | 9 | -2 | 0.052941 | 0.210588 |

## q3

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p16 | 3 | up | 9 | 4 | 5 | 0.5 | 0.5 |
| p8 | 2 | down | 6 | 8 | -2 | 0.067105 | 0.413421 |
| p20 | 1 | up | 10 | 5 | 5 | 0.5 | 0.5 |
| p11 | 0 | up | 8 | 7 | 1 | 0.071053 | 0.414211 |
| p5 | 0 | down | 5 | 6 | -1 | 0.071053 | 0.414211 |
| p9 | 0 | down | 7 | 10 | -3 | 0.0 | 0.4 |
| p4 | 0 | down | 4 | 9 | -5 | 0.0 | 0.4 |

## q4

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p10 | 3 | up | 2 | 1 | 1 | 1.0 | 1.0 |
| p4 | 3 | down | 1 | 2 | -1 | 0.894737 | 0.978947 |
| p5 | 1 | down | 3 | 4 | -1 | 0.0 | 0.266667 |
| p18 | 0 | up | 9 | 3 | 6 | 0.047368 | 0.27614 |
| p11 | 0 | down | 6 | 7 | -1 | 0.0 | 0.266667 |
| p15 | 0 | down | 7 | 8 | -1 | 0.0 | 0.266667 |
| p16 | 0 | down | 8 | 9 | -1 | 0.0 | 0.266667 |
| p7 | 0 | down | 4 | 5 | -1 | 0.0 | 0.266667 |

## q5

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p17 | 3 | up | 4 | 2 | 2 | 0.62963 | 0.525926 |
| p4 | 2 | down | 6 | 8 | -2 | 0.022222 | 0.271111 |
| p5 | 0 | up | 7 | 5 | 2 | 0.157407 | 0.298148 |
| p11 | 0 | up | 8 | 7 | 1 | 0.025 | 0.271667 |
| p3 | 0 | down | 5 | 6 | -1 | 0.052778 | 0.277222 |
| p1 | 0 | down | 2 | 4 | -2 | 0.0 | 0.4 |

## q6

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p13 | 3 | up | 3 | 1 | 2 | 1.0 | 1.0 |
| p20 | 2 | entered_top_k | None | 5 | None | 0.666667 | 0.533333 |
| p1 | 1 | down | 5 | 6 | -1 | 0.084211 | 0.416842 |
| p14 | 0 | up | 9 | 7 | 2 | 0.047368 | 0.409474 |
| p12 | 0 | left_top_k | 8 | None | None | None | None |
| p15 | 0 | left_top_k | 10 | None | None | None | None |
| p18 | 0 | entered_top_k | None | 8 | None | 0.047368 | 0.409474 |
| p11 | 0 | down | 2 | 3 | -1 | 0.047368 | 0.809474 |

## q7

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p11 | 3 | up | 2 | 1 | 1 | 1.0 | 1.0 |
| p5 | 3 | down | 1 | 2 | -1 | 0.875 | 0.975 |
| p10 | 0 | up | 8 | 7 | 1 | 0.131944 | 0.226389 |
| p13 | 0 | up | 10 | 9 | 1 | 0.039583 | 0.207917 |
| p3 | 0 | up | 5 | 4 | 1 | 0.019792 | 0.303958 |
| p8 | 0 | up | 6 | 5 | 1 | 0.01875 | 0.30375 |
| p17 | 0 | entered_top_k | None | 8 | None | 0.125 | 0.225 |
| p7 | 0 | left_top_k | 7 | None | None | None | None |

## q8

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p13 | 1 | up | 8 | 6 | 2 | 0.039583 | 0.167917 |
| p17 | 0 | up | 10 | 5 | 5 | 0.25 | 0.21 |
| p5 | 0 | up | 6 | 4 | 2 | 0.25 | 0.21 |
| p16 | 0 | down | 9 | 10 | -1 | 0.0 | 0.16 |
| p12 | 0 | down | 7 | 9 | -2 | 0.0 | 0.16 |
| p1 | 0 | down | 4 | 7 | -3 | 0.0375 | 0.1675 |
| p4 | 0 | down | 5 | 8 | -3 | 0.0 | 0.16 |

## q9

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p18 | 3 | up | 3 | 2 | 1 | 0.158824 | 0.671765 |
| p7 | 1 | down | 2 | 3 | -1 | 0.0 | 0.64 |
| p5 | 0 | up | 5 | 4 | 1 | 0.0375 | 0.1675 |
| p2 | 0 | down | 4 | 5 | -1 | 0.035294 | 0.167059 |
