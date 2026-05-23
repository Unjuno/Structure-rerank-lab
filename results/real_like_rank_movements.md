# Rank movement explanations

Baseline mode: **baseline**
Compare mode: **structure_rerank**
Cutoff: **top-10**

## rq1

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| r9 | 1 | down | 4 | 5 | -1 | 0.019231 | 0.203846 |
| r2 | 1 | down | 2 | 4 | -2 | 0.762821 | 0.352564 |
| r12 | 0 | up | 5 | 2 | 3 | 0.916667 | 0.383333 |
| r13 | 0 | up | 6 | 3 | 3 | 0.871795 | 0.374359 |
| r5 | 0 | up | 9 | 7 | 2 | 0.807692 | 0.161538 |
| r10 | 0 | entered_top_k | None | 8 | None | 0.807692 | 0.161538 |
| r11 | 0 | entered_top_k | None | 10 | None | 0.762821 | 0.152564 |
| r14 | 0 | entered_top_k | None | 9 | None | 0.807692 | 0.161538 |

## rq10

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| r3 | 1 | up | 5 | 4 | 1 | 0.764368 | 0.312874 |
| r5 | 0 | up | 6 | 5 | 1 | 0.764368 | 0.312874 |
| r1 | 0 | left_top_k | 10 | None | None | None | None |
| r8 | 0 | entered_top_k | None | 10 | None | 0.724138 | 0.144828 |
| r2 | 0 | down | 4 | 6 | -2 | 0.010345 | 0.162069 |

## rq2

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| r1 | 1 | down | 4 | 10 | -6 | 0.0 | 0.0 |
| r7 | 0 | up | 8 | 4 | 4 | 1.0 | 0.2 |
| r14 | 0 | up | 3 | 2 | 1 | 0.022556 | 0.271178 |
| r4 | 0 | up | 6 | 5 | 1 | 0.947368 | 0.189474 |
| r10 | 0 | entered_top_k | None | 6 | None | 0.947368 | 0.189474 |
| r11 | 0 | entered_top_k | None | 7 | None | 0.947368 | 0.189474 |
| r13 | 0 | entered_top_k | None | 9 | None | 0.894737 | 0.178947 |
| r6 | 0 | left_top_k | 7 | None | None | None | None |

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
| r5 | 0 | left_top_k | 9 | None | None | None | None |
| r2 | 0 | down | 7 | 9 | -2 | 0.670692 | 0.134138 |
| r3 | 0 | down | 8 | 10 | -2 | 0.670692 | 0.134138 |
| r12 | 0 | down | 5 | 8 | -3 | 0.007246 | 0.134783 |

## rq5

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| r11 | 2 | down | 3 | 5 | -2 | 0.009326 | 0.161865 |
| r15 | 0 | up | 6 | 3 | 3 | 0.678756 | 0.295751 |
| r3 | 0 | up | 9 | 7 | 2 | 0.689119 | 0.137824 |
| r14 | 0 | up | 5 | 4 | 1 | 0.65285 | 0.29057 |
| r2 | 0 | left_top_k | 8 | None | None | None | None |
| r4 | 0 | left_top_k | 10 | None | None | None | None |
| r8 | 0 | entered_top_k | None | 9 | None | 0.65285 | 0.13057 |
| r9 | 0 | entered_top_k | None | 8 | None | 0.689119 | 0.137824 |

## rq6

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| r15 | 1 | up | 7 | 3 | 4 | 0.884393 | 0.576879 |
| r4 | 0 | left_top_k | 10 | None | None | None | None |
| r8 | 0 | entered_top_k | None | 8 | None | 0.687861 | 0.137572 |
| r1 | 0 | down | 8 | 9 | -1 | 0.0 | 0.0 |
| r10 | 0 | down | 5 | 6 | -1 | 0.017341 | 0.403468 |
| r14 | 0 | down | 6 | 7 | -1 | 0.017341 | 0.403468 |
| r2 | 0 | down | 3 | 4 | -1 | 0.017341 | 0.403468 |
| r3 | 0 | down | 9 | 10 | -1 | 0.0 | 0.0 |

## rq7

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| r10 | 2 | entered_top_k | None | 6 | None | 0.688525 | 0.137705 |
| r11 | 1 | entered_top_k | None | 7 | None | 0.688525 | 0.137705 |
| r13 | 0 | up | 6 | 4 | 2 | 0.650273 | 0.263388 |
| r1 | 0 | left_top_k | 8 | None | None | None | None |
| r2 | 0 | left_top_k | 9 | None | None | None | None |
| r3 | 0 | left_top_k | 10 | None | None | None | None |
| r4 | 0 | entered_top_k | None | 5 | None | 0.688525 | 0.137705 |
| r15 | 0 | down | 7 | 10 | -3 | 0.008197 | 0.134973 |

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
