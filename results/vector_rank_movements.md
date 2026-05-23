# Rank movement explanations

Baseline mode: **vector_baseline**
Compare mode: **vector_structure_rerank**
Cutoff: **top-10**

## q1

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p7 | 1 | entered_top_k | None | 10 | None | 0.296296 | 0.059259 |
| p6 | 0 | up | 7 | 6 | 1 | 0.333333 | 0.435269 |
| p2 | 0 | left_top_k | 10 | None | None | None | None |
| p4 | 0 | down | 6 | 7 | -1 | 0.0 | 0.409192 |

## q10

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p8 | 2 | up | 3 | 2 | 1 | 1.0 | 0.7007 |
| p15 | 0 | down | 2 | 3 | -1 | 0.0 | 0.662268 |

## q2

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p12 | 3 | up | 3 | 2 | 1 | 0.745098 | 0.712437 |
| p4 | 1 | down | 4 | 5 | -1 | 0.047059 | 0.404282 |
| p18 | 0 | up | 5 | 4 | 1 | 0.352941 | 0.435778 |
| p15 | 0 | down | 2 | 3 | -1 | 0.05 | 0.575216 |

## q3

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p16 | 3 | up | 6 | 5 | 1 | 0.5 | 0.447043 |
| p3 | 3 | up | 4 | 3 | 1 | 1.0 | 0.675621 |
| p8 | 2 | down | 8 | 9 | -1 | 0.067105 | 0.241918 |
| p20 | 1 | up | 3 | 2 | 1 | 0.5 | 0.676833 |
| p11 | 0 | up | 9 | 8 | 1 | 0.071053 | 0.242573 |
| p9 | 0 | down | 5 | 6 | -1 | 0.0 | 0.414906 |
| p12 | 0 | down | 2 | 4 | -2 | 0.075 | 0.63632 |

## q4

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p18 | 0 | up | 4 | 3 | 1 | 0.047368 | 0.071201 |
| p16 | 0 | down | 3 | 4 | -1 | 0.0 | 0.063183 |

## q5

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p5 | 0 | up | 8 | 7 | 1 | 0.157407 | 0.200793 |
| p11 | 0 | down | 7 | 8 | -1 | 0.025 | 0.193099 |

## q6

No rank movements inside the cutoff.

## q7

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p11 | 3 | up | 2 | 1 | 1 | 1.0 | 0.982925 |
| p5 | 3 | down | 1 | 2 | -1 | 0.875 | 0.975 |
| p17 | 0 | up | 8 | 6 | 2 | 0.125 | 0.184412 |
| p10 | 0 | up | 10 | 9 | 1 | 0.131944 | 0.165446 |
| p1 | 0 | down | 9 | 10 | -1 | 0.016667 | 0.158729 |
| p12 | 0 | down | 6 | 7 | -1 | 0.019792 | 0.182107 |
| p3 | 0 | down | 7 | 8 | -1 | 0.019792 | 0.1663 |

## q8

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p13 | 1 | down | 7 | 8 | -1 | 0.039583 | 0.143155 |
| p5 | 0 | up | 9 | 6 | 3 | 0.25 | 0.166376 |
| p17 | 0 | up | 5 | 4 | 1 | 0.25 | 0.216544 |
| p12 | 0 | down | 4 | 5 | -1 | 0.0 | 0.175168 |
| p16 | 0 | down | 6 | 7 | -1 | 0.0 | 0.145934 |
| p4 | 0 | down | 8 | 9 | -1 | 0.0 | 0.120082 |

## q9

No rank movements inside the cutoff.
