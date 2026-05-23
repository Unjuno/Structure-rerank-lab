# Rank movement explanations

Baseline mode: **vector_baseline**
Compare mode: **vector_structure_rerank**
Cutoff: **top-10**

## rq1

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| r2 | 1 | up | 5 | 4 | 1 | 0.762821 | 0.355361 |
| r9 | 1 | down | 4 | 5 | -1 | 0.019231 | 0.214055 |
| r12 | 0 | up | 6 | 3 | 3 | 0.916667 | 0.375583 |
| r5 | 0 | up | 9 | 7 | 2 | 0.807692 | 0.161538 |
| r10 | 0 | entered_top_k | None | 8 | None | 0.807692 | 0.161538 |
| r11 | 0 | entered_top_k | None | 10 | None | 0.762821 | 0.152564 |
| r14 | 0 | entered_top_k | None | 9 | None | 0.807692 | 0.161538 |
| r3 | 0 | left_top_k | 7 | None | None | None | None |

## rq10

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| r3 | 1 | up | 9 | 4 | 5 | 0.764368 | 0.21685 |
| r9 | 1 | up | 4 | 2 | 2 | 0.764368 | 0.274902 |
| r5 | 0 | up | 5 | 3 | 2 | 0.764368 | 0.248993 |
| r1 | 0 | left_top_k | 10 | None | None | None | None |
| r11 | 0 | left_top_k | 8 | None | None | None | None |
| r15 | 0 | entered_top_k | None | 8 | None | 0.683908 | 0.136782 |
| r8 | 0 | entered_top_k | None | 7 | None | 0.724138 | 0.144828 |
| r12 | 0 | down | 2 | 5 | -3 | 0.02069 | 0.159473 |

## rq2

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| r12 | 1 | left_top_k | 9 | None | None | None | None |
| r10 | 0 | up | 10 | 6 | 4 | 0.947368 | 0.193995 |
| r4 | 0 | up | 6 | 4 | 2 | 0.947368 | 0.197415 |
| r7 | 0 | up | 5 | 3 | 2 | 1.0 | 0.208025 |
| r11 | 0 | entered_top_k | None | 7 | None | 0.947368 | 0.190982 |
| r3 | 0 | entered_top_k | None | 9 | None | 0.894737 | 0.180926 |
| r6 | 0 | left_top_k | 8 | None | None | None | None |
| r5 | 0 | down | 3 | 5 | -2 | 0.0 | 0.196521 |

## rq3

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| r9 | 0 | up | 9 | 4 | 5 | 0.689119 | 0.137824 |
| r5 | 0 | up | 6 | 3 | 3 | 0.689119 | 0.137824 |
| r10 | 0 | left_top_k | 10 | None | None | None | None |
| r14 | 0 | entered_top_k | None | 5 | None | 0.65285 | 0.13057 |
| r15 | 0 | entered_top_k | None | 6 | None | 0.61658 | 0.123316 |
| r7 | 0 | left_top_k | 8 | None | None | None | None |
| r6 | 0 | down | 7 | 10 | -3 | 0.0 | 0.0 |
| r1 | 0 | down | 3 | 7 | -4 | 0.0 | 0.0 |

## rq4

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| r7 | 1 | up | 10 | 3 | 7 | 0.749597 | 0.149919 |
| r11 | 1 | entered_top_k | None | 5 | None | 0.710145 | 0.142029 |
| r1 | 0 | left_top_k | 6 | None | None | None | None |
| r10 | 0 | entered_top_k | None | 4 | None | 0.710145 | 0.142029 |
| r13 | 0 | entered_top_k | None | 9 | None | 0.670692 | 0.134138 |
| r5 | 0 | left_top_k | 9 | None | None | None | None |
| r8 | 0 | left_top_k | 5 | None | None | None | None |
| r9 | 0 | down | 3 | 6 | -3 | 0.007246 | 0.135458 |

## rq5

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| r11 | 2 | down | 5 | 9 | -4 | 0.009326 | 0.09607 |
| r3 | 0 | up | 9 | 5 | 4 | 0.689119 | 0.137824 |
| r14 | 0 | up | 6 | 4 | 2 | 0.65285 | 0.220998 |
| r15 | 0 | up | 3 | 2 | 1 | 0.678756 | 0.288632 |
| r2 | 0 | left_top_k | 8 | None | None | None | None |
| r4 | 0 | left_top_k | 10 | None | None | None | None |
| r8 | 0 | entered_top_k | None | 7 | None | 0.65285 | 0.13057 |
| r9 | 0 | entered_top_k | None | 6 | None | 0.689119 | 0.137824 |

## rq6

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| r9 | 1 | up | 5 | 3 | 2 | 0.919075 | 0.500078 |
| r4 | 0 | left_top_k | 10 | None | None | None | None |
| r8 | 0 | entered_top_k | None | 8 | None | 0.687861 | 0.137572 |
| r1 | 0 | down | 8 | 9 | -1 | 0.0 | 0.0 |
| r14 | 0 | down | 3 | 4 | -1 | 0.017341 | 0.434577 |
| r2 | 0 | down | 4 | 5 | -1 | 0.017341 | 0.424072 |
| r3 | 0 | down | 9 | 10 | -1 | 0.0 | 0.0 |

## rq7

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| r10 | 2 | entered_top_k | None | 6 | None | 0.688525 | 0.137705 |
| r11 | 1 | entered_top_k | None | 7 | None | 0.688525 | 0.137705 |
| r13 | 0 | up | 6 | 3 | 3 | 0.650273 | 0.21025 |
| r2 | 0 | up | 9 | 8 | 1 | 0.650273 | 0.130055 |
| r3 | 0 | up | 10 | 9 | 1 | 0.650273 | 0.130055 |
| r1 | 0 | left_top_k | 8 | None | None | None | None |
| r4 | 0 | entered_top_k | None | 5 | None | 0.688525 | 0.137705 |
| r6 | 0 | left_top_k | 5 | None | None | None | None |

## rq8

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| r3 | 1 | up | 4 | 2 | 2 | 0.820988 | 0.164198 |
| r10 | 1 | left_top_k | 10 | None | None | None | None |
| r9 | 0 | up | 9 | 4 | 5 | 0.820988 | 0.164198 |
| r5 | 0 | up | 6 | 3 | 3 | 0.820988 | 0.164198 |
| r14 | 0 | entered_top_k | None | 5 | None | 0.777778 | 0.155556 |
| r15 | 0 | entered_top_k | None | 6 | None | 0.734568 | 0.146914 |
| r7 | 0 | left_top_k | 8 | None | None | None | None |
| r6 | 0 | down | 7 | 10 | -3 | 0.0 | 0.0 |

## rq9

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| r5 | 1 | up | 6 | 3 | 3 | 0.747191 | 0.149438 |
| r8 | 0 | up | 9 | 4 | 5 | 0.707865 | 0.141573 |
| r3 | 0 | up | 4 | 2 | 2 | 0.747191 | 0.149438 |
| r10 | 0 | left_top_k | 10 | None | None | None | None |
| r14 | 0 | entered_top_k | None | 5 | None | 0.707865 | 0.141573 |
| r15 | 0 | entered_top_k | None | 6 | None | 0.668539 | 0.133708 |
| r7 | 0 | left_top_k | 8 | None | None | None | None |
| r6 | 0 | down | 7 | 10 | -3 | 0.0 | 0.0 |
