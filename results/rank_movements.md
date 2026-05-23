# Rank movement explanations

Baseline mode: **baseline**
Compare mode: **structure_rerank**
Cutoff: **top-10**

## q1

No rank movements inside the cutoff.

## q10

No rank movements inside the cutoff.

## q2

No rank movements inside the cutoff.

## q3

No rank movements inside the cutoff.

## q4

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p10 | 3 | up | 2 | 1 | 1 | 1.0 | 1.0 |
| p4 | 3 | down | 1 | 2 | -1 | 0.894737 | 0.978947 |

## q5

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p17 | 3 | up | 4 | 2 | 2 | 0.419753 | 0.483951 |
| p16 | 0 | entered_top_k | None | 10 | None | 0.005864 | 0.134506 |
| p2 | 0 | left_top_k | 10 | None | None | None | None |
| p1 | 0 | down | 2 | 4 | -2 | 0.0 | 0.4 |

## q6

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p13 | 3 | up | 3 | 1 | 2 | 1.0 | 1.0 |
| p20 | 2 | entered_top_k | None | 5 | None | 0.444444 | 0.488889 |
| p1 | 1 | down | 5 | 6 | -1 | 0.018713 | 0.403743 |
| p15 | 0 | left_top_k | 10 | None | None | None | None |
| p11 | 0 | down | 2 | 3 | -1 | 0.0 | 0.8 |
| p12 | 0 | down | 8 | 9 | -1 | 0.0 | 0.4 |
| p14 | 0 | down | 9 | 10 | -1 | 0.0 | 0.4 |
| p2 | 0 | down | 6 | 7 | -1 | 0.0 | 0.4 |

## q7

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p11 | 3 | up | 2 | 1 | 1 | 1.0 | 1.0 |
| p5 | 3 | down | 1 | 2 | -1 | 0.765625 | 0.953125 |
| p13 | 0 | up | 10 | 7 | 3 | 0.003299 | 0.20066 |
| p10 | 0 | down | 8 | 9 | -1 | 0.0 | 0.2 |
| p12 | 0 | down | 9 | 10 | -1 | 0.0 | 0.2 |
| p7 | 0 | down | 7 | 8 | -1 | 0.0 | 0.2 |

## q8

No rank movements inside the cutoff.

## q9

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| p18 | 3 | up | 3 | 2 | 1 | 0.052941 | 0.650588 |
| p7 | 1 | down | 2 | 3 | -1 | 0.0 | 0.64 |
