# Rank movement explanations

Baseline mode: **vector_baseline**
Compare mode: **vertical_vector_rerank**
Cutoff: **top-10**

## PLAIN-1008

No rank movements inside the cutoff.

## PLAIN-1018

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-5093 | 1 | up | 9 | 7 | 2 | 0.773644 | 0.580112 |
| MED-1832 | 1 | up | 7 | 6 | 1 | 0.723232 | 0.585256 |
| MED-3012 | 1 | up | 6 | 5 | 1 | 0.826244 | 0.643996 |
| MED-5091 | 1 | up | 4 | 3 | 1 | 1.0 | 0.854557 |
| MED-5092 | 1 | down | 8 | 9 | -1 | 0.281151 | 0.492198 |
| MED-4936 | 1 | down | 2 | 4 | -2 | 0.172611 | 0.804793 |
| MED-839 | 0 | up | 3 | 2 | 1 | 0.687674 | 0.875963 |
| MED-928 | 0 | down | 5 | 8 | -3 | 0.253288 | 0.556759 |

## PLAIN-102

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4247 | 0 | up | 9 | 7 | 2 | 0.783483 | 0.637837 |
| MED-4616 | 0 | up | 10 | 8 | 2 | 0.783483 | 0.637837 |
| MED-5194 | 0 | up | 6 | 4 | 2 | 0.801034 | 0.732287 |
| MED-1175 | 0 | left_top_k | 7 | None | None | None | None |
| MED-2590 | 0 | entered_top_k | None | 9 | None | 0.595744 | 0.59064 |
| MED-4783 | 0 | down | 4 | 5 | -1 | 0.332094 | 0.72365 |
| MED-5141 | 0 | down | 5 | 6 | -1 | 0.494574 | 0.679969 |
| MED-1999 | 0 | down | 8 | 10 | -2 | 0.451729 | 0.581559 |

## PLAIN-1028

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2096 | 0 | up | 8 | 5 | 3 | 0.478885 | 0.726383 |
| MED-1553 | 0 | up | 5 | 4 | 1 | 0.281807 | 0.729327 |
| MED-2423 | 0 | up | 7 | 6 | 1 | 0.389813 | 0.715111 |
| MED-1558 | 0 | entered_top_k | None | 10 | None | 0.642789 | 0.672038 |
| MED-1861 | 0 | left_top_k | 6 | None | None | None | None |
| MED-4019 | 0 | entered_top_k | None | 7 | None | 0.637617 | 0.69046 |
| MED-4627 | 0 | left_top_k | 10 | None | None | None | None |
| MED-2412 | 0 | down | 4 | 8 | -4 | 0.0 | 0.689931 |

## PLAIN-1039

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2754 | 0 | up | 6 | 5 | 1 | 0.329093 | 0.199379 |
| MED-4628 | 0 | entered_top_k | None | 7 | None | 0.205476 | 0.162026 |
| MED-846 | 0 | left_top_k | 10 | None | None | None | None |
| MED-1067 | 0 | down | 5 | 6 | -1 | 0.169926 | 0.168088 |
| MED-4634 | 0 | down | 9 | 10 | -1 | 0.116006 | 0.152063 |
| MED-4092 | 0 | down | 7 | 9 | -2 | 0.127118 | 0.156673 |

## PLAIN-1050

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2498 | 0 | up | 4 | 3 | 1 | 0.829847 | 0.693487 |
| MED-2509 | 0 | up | 7 | 6 | 1 | 0.571232 | 0.459155 |
| MED-2510 | 0 | up | 2 | 1 | 1 | 1.0 | 0.982096 |
| MED-1021 | 0 | down | 3 | 4 | -1 | 0.817348 | 0.691357 |
| MED-1712 | 0 | down | 1 | 2 | -1 | 0.0 | 0.8 |
| MED-3283 | 0 | down | 6 | 7 | -1 | 0.294971 | 0.451547 |

## PLAIN-1066

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2498 | 0 | up | 4 | 3 | 1 | 0.829847 | 0.693487 |
| MED-2509 | 0 | up | 7 | 6 | 1 | 0.571232 | 0.459155 |
| MED-2510 | 0 | up | 2 | 1 | 1 | 1.0 | 0.982096 |
| MED-1021 | 0 | down | 3 | 4 | -1 | 0.817348 | 0.691357 |
| MED-1712 | 0 | down | 1 | 2 | -1 | 0.0 | 0.8 |
| MED-3283 | 0 | down | 6 | 7 | -1 | 0.294971 | 0.451547 |

## PLAIN-1088

No rank movements inside the cutoff.

## PLAIN-1098

No rank movements inside the cutoff.

## PLAIN-1109

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2627 | 1 | up | 9 | 7 | 2 | 0.346401 | 0.284113 |
| MED-1100 | 1 | entered_top_k | None | 10 | None | 0.581691 | 0.275228 |
| MED-2087 | 0 | up | 7 | 6 | 1 | 0.230316 | 0.288697 |
| MED-1003 | 0 | entered_top_k | None | 8 | None | 0.524471 | 0.278003 |
| MED-1777 | 0 | left_top_k | 6 | None | None | None | None |
| MED-919 | 0 | left_top_k | 10 | None | None | None | None |
| MED-4728 | 0 | down | 8 | 9 | -1 | 0.23665 | 0.275726 |

## PLAIN-1119

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4025 | 0 | up | 7 | 3 | 4 | 1.0 | 0.734568 |
| MED-2719 | 0 | up | 8 | 7 | 1 | 0.319406 | 0.559996 |
| MED-3371 | 0 | up | 3 | 2 | 1 | 0.704786 | 0.747514 |
| MED-4286 | 0 | left_top_k | 10 | None | None | None | None |
| MED-5310 | 0 | entered_top_k | None | 10 | None | 0.479023 | 0.546541 |
| MED-3091 | 0 | down | 2 | 4 | -2 | 0.240761 | 0.711103 |
| MED-1627 | 0 | down | 4 | 8 | -4 | 0.0 | 0.558717 |

## PLAIN-112

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3382 | 2 | up | 5 | 4 | 1 | 0.616955 | 0.52947 |
| MED-2738 | 0 | up | 10 | 9 | 1 | 0.136729 | 0.147062 |
| MED-3383 | 0 | up | 4 | 3 | 1 | 0.46533 | 0.531153 |
| MED-4655 | 0 | up | 7 | 6 | 1 | 0.656685 | 0.487538 |
| MED-2616 | 0 | down | 6 | 7 | -1 | 0.348616 | 0.433964 |
| MED-2742 | 0 | down | 9 | 10 | -1 | 0.058884 | 0.139527 |
| MED-1153 | 0 | down | 3 | 5 | -2 | 0.240399 | 0.508931 |

## PLAIN-1130

No rank movements inside the cutoff.

## PLAIN-1141

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3001 | 0 | up | 10 | 8 | 2 | 0.671305 | 0.470179 |
| MED-4531 | 0 | up | 9 | 7 | 2 | 0.696677 | 0.493514 |
| MED-1037 | 0 | down | 7 | 9 | -2 | 0.359105 | 0.454789 |
| MED-5346 | 0 | down | 8 | 10 | -2 | 0.429739 | 0.443311 |

## PLAIN-1151

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2738 | 1 | down | 8 | 10 | -2 | 0.296478 | 0.406241 |
| MED-761 | 0 | up | 10 | 6 | 4 | 0.885226 | 0.47898 |
| MED-3372 | 0 | down | 6 | 8 | -2 | 0.291098 | 0.44812 |

## PLAIN-1161

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4991 | 0 | up | 8 | 5 | 3 | 1.0 | 0.585827 |
| MED-2010 | 0 | up | 10 | 8 | 2 | 0.985163 | 0.507234 |
| MED-1880 | 0 | up | 3 | 2 | 1 | 0.661727 | 0.793256 |
| MED-2147 | 0 | up | 7 | 6 | 1 | 0.754788 | 0.567581 |
| MED-3138 | 0 | down | 2 | 3 | -1 | 0.430492 | 0.781456 |
| MED-2140 | 0 | down | 5 | 7 | -2 | 0.313336 | 0.525922 |
| MED-3136 | 0 | down | 6 | 10 | -4 | 0.0 | 0.429092 |

## PLAIN-1172

No rank movements inside the cutoff.

## PLAIN-1183

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4070 | 1 | up | 8 | 7 | 1 | 0.406166 | 0.305967 |
| MED-10 | 0 | up | 5 | 4 | 1 | 1.0 | 0.559847 |
| MED-5192 | 0 | up | 9 | 8 | 1 | 0.495827 | 0.29243 |
| MED-1201 | 0 | left_top_k | 7 | None | None | None | None |
| MED-3981 | 0 | entered_top_k | None | 9 | None | 0.424847 | 0.250969 |
| MED-2582 | 0 | down | 4 | 5 | -1 | 0.421111 | 0.46623 |

## PLAIN-1193

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4000 | 1 | up | 10 | 9 | 1 | 0.371553 | 0.374963 |
| MED-4004 | 1 | up | 7 | 6 | 1 | 0.384956 | 0.434445 |
| MED-1390 | 0 | up | 9 | 8 | 1 | 0.429317 | 0.387664 |
| MED-1523 | 0 | entered_top_k | None | 10 | None | 0.429064 | 0.372065 |
| MED-3868 | 0 | left_top_k | 8 | None | None | None | None |
| MED-927 | 0 | down | 6 | 7 | -1 | 0.301168 | 0.422684 |

## PLAIN-12

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2603 | 0 | up | 9 | 7 | 2 | 0.473285 | 0.303486 |
| MED-4884 | 0 | up | 7 | 6 | 1 | 0.739035 | 0.366591 |
| MED-1376 | 0 | entered_top_k | None | 10 | None | 0.478431 | 0.260005 |
| MED-2136 | 0 | left_top_k | 10 | None | None | None | None |
| MED-4695 | 0 | down | 8 | 9 | -1 | 0.262407 | 0.261492 |
| MED-2333 | 0 | down | 6 | 8 | -2 | 0.028261 | 0.261679 |

## PLAIN-1203

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1528 | 0 | up | 9 | 5 | 4 | 0.587896 | 0.327133 |
| MED-1067 | 0 | up | 10 | 9 | 1 | 0.276815 | 0.259826 |
| MED-2754 | 0 | entered_top_k | None | 7 | None | 0.487293 | 0.301095 |
| MED-4872 | 0 | left_top_k | 7 | None | None | None | None |
| MED-5208 | 0 | left_top_k | 8 | None | None | None | None |
| MED-5270 | 0 | entered_top_k | None | 10 | None | 0.2634 | 0.249823 |
| MED-3275 | 0 | down | 5 | 6 | -1 | 0.307669 | 0.301566 |
| MED-4600 | 0 | down | 6 | 8 | -2 | 0.336394 | 0.29987 |

## PLAIN-1214

No rank movements inside the cutoff.

## PLAIN-1225

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1261 | 1 | up | 9 | 8 | 1 | 0.405098 | 0.562527 |
| MED-1674 | 1 | up | 3 | 2 | 1 | 0.644695 | 0.870329 |
| MED-1675 | 1 | down | 8 | 9 | -1 | 0.263938 | 0.552739 |
| MED-717 | 0 | up | 4 | 3 | 1 | 1.0 | 0.840497 |
| MED-918 | 0 | down | 2 | 4 | -2 | 0.297851 | 0.830157 |

## PLAIN-123

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2489 | 0 | up | 4 | 3 | 1 | 0.450098 | 0.438414 |
| MED-4804 | 0 | up | 6 | 5 | 1 | 0.413523 | 0.389416 |
| MED-1347 | 0 | left_top_k | 9 | None | None | None | None |
| MED-1982 | 0 | left_top_k | 10 | None | None | None | None |
| MED-2265 | 0 | entered_top_k | None | 8 | None | 0.398525 | 0.257766 |
| MED-3436 | 0 | entered_top_k | None | 10 | None | 0.250118 | 0.254009 |
| MED-4256 | 0 | down | 5 | 6 | -1 | 0.0 | 0.326505 |
| MED-4465 | 0 | down | 8 | 9 | -1 | 0.1769 | 0.257213 |

## PLAIN-1236

No rank movements inside the cutoff.

## PLAIN-1249

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4939 | 0 | up | 6 | 3 | 3 | 0.912691 | 0.565236 |
| MED-1442 | 0 | up | 9 | 7 | 2 | 0.544351 | 0.453821 |
| MED-2674 | 0 | up | 5 | 4 | 1 | 0.471489 | 0.492084 |
| MED-1780 | 0 | left_top_k | 7 | None | None | None | None |
| MED-2848 | 0 | entered_top_k | None | 5 | None | 0.959221 | 0.462629 |
| MED-3173 | 0 | left_top_k | 10 | None | None | None | None |
| MED-3648 | 0 | entered_top_k | None | 10 | None | 0.810668 | 0.434907 |
| MED-3706 | 0 | down | 8 | 9 | -1 | 0.500901 | 0.446673 |

## PLAIN-1262

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2082 | 1 | entered_top_k | None | 10 | None | 0.660345 | 0.36156 |
| MED-4932 | 0 | up | 7 | 5 | 2 | 0.401778 | 0.392659 |
| MED-4096 | 0 | up | 10 | 9 | 1 | 0.405923 | 0.370889 |
| MED-4132 | 0 | up | 9 | 8 | 1 | 0.364033 | 0.376046 |
| MED-4911 | 0 | left_top_k | 8 | None | None | None | None |
| MED-2211 | 0 | down | 6 | 7 | -1 | 0.312934 | 0.381222 |
| MED-3174 | 0 | down | 5 | 6 | -1 | 0.146762 | 0.386919 |

## PLAIN-1275

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2886 | 1 | up | 3 | 2 | 1 | 0.713641 | 0.767237 |
| MED-2924 | 1 | down | 2 | 3 | -1 | 0.132203 | 0.68877 |
| MED-2665 | 0 | up | 8 | 6 | 2 | 0.495174 | 0.459327 |
| MED-3929 | 0 | left_top_k | 10 | None | None | None | None |
| MED-4366 | 0 | entered_top_k | None | 10 | None | 0.25359 | 0.252972 |
| MED-1671 | 0 | down | 7 | 8 | -1 | 0.133267 | 0.392428 |
| MED-2076 | 0 | down | 6 | 7 | -1 | 0.382996 | 0.449747 |

## PLAIN-1288

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-5065 | 1 | up | 9 | 5 | 4 | 0.61723 | 0.30097 |
| MED-4029 | 1 | up | 8 | 6 | 2 | 0.524735 | 0.285887 |
| MED-3700 | 1 | entered_top_k | None | 10 | None | 0.583751 | 0.234034 |
| MED-4585 | 1 | left_top_k | 10 | None | None | None | None |
| MED-2663 | 1 | down | 3 | 4 | -1 | 0.0 | 0.358258 |
| MED-1795 | 1 | down | 4 | 8 | -4 | 0.0 | 0.264927 |
| MED-3728 | 0 | up | 6 | 3 | 3 | 0.633298 | 0.3639 |
| MED-2083 | 0 | entered_top_k | None | 7 | None | 0.701453 | 0.272382 |

## PLAIN-1299

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4747 | 1 | up | 8 | 3 | 5 | 1.0 | 0.65167 |
| MED-5341 | 1 | entered_top_k | None | 10 | None | 0.387192 | 0.44847 |
| MED-1601 | 0 | left_top_k | 10 | None | None | None | None |
| MED-1229 | 0 | down | 4 | 5 | -1 | 0.311757 | 0.574797 |
| MED-2123 | 0 | down | 5 | 6 | -1 | 0.311757 | 0.574797 |
| MED-2498 | 0 | down | 3 | 4 | -1 | 0.328585 | 0.603264 |
| MED-4239 | 0 | down | 7 | 8 | -1 | 0.111626 | 0.480737 |
| MED-4890 | 0 | down | 6 | 7 | -1 | 0.26548 | 0.531699 |

## PLAIN-1309

No rank movements inside the cutoff.

## PLAIN-1320

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2760 | 1 | up | 10 | 9 | 1 | 0.504981 | 0.449602 |
| MED-1986 | 0 | up | 8 | 6 | 2 | 1.0 | 0.589305 |
| MED-1549 | 0 | up | 4 | 3 | 1 | 0.502392 | 0.627747 |
| MED-2112 | 0 | up | 5 | 4 | 1 | 0.396331 | 0.594331 |
| MED-1543 | 0 | down | 6 | 7 | -1 | 0.559624 | 0.558724 |
| MED-3759 | 0 | down | 7 | 8 | -1 | 0.228433 | 0.489917 |
| MED-727 | 0 | down | 9 | 10 | -1 | 0.455696 | 0.445133 |
| MED-1545 | 0 | down | 3 | 5 | -2 | 0.313015 | 0.590153 |

## PLAIN-133

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4116 | 0 | up | 10 | 3 | 7 | 1.0 | 0.72849 |
| MED-2923 | 0 | up | 7 | 4 | 3 | 0.807789 | 0.702137 |
| MED-2523 | 0 | up | 8 | 6 | 2 | 0.737739 | 0.684954 |
| MED-1666 | 0 | up | 2 | 1 | 1 | 0.652976 | 0.861181 |
| MED-1170 | 0 | entered_top_k | None | 7 | None | 0.68383 | 0.664404 |
| MED-2216 | 0 | left_top_k | 9 | None | None | None | None |
| MED-2522 | 0 | entered_top_k | None | 10 | None | 0.506265 | 0.602578 |
| MED-3696 | 0 | left_top_k | 5 | None | None | None | None |

## PLAIN-1331

No rank movements inside the cutoff.

## PLAIN-1342

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1403 | 1 | up | 4 | 3 | 1 | 0.587984 | 0.682458 |
| MED-2845 | 0 | down | 3 | 4 | -1 | 0.410275 | 0.673725 |

## PLAIN-1353

No rank movements inside the cutoff.

## PLAIN-1363

No rank movements inside the cutoff.

## PLAIN-1374

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4747 | 1 | entered_top_k | None | 5 | None | 1.0 | 0.463922 |
| MED-1647 | 0 | up | 7 | 6 | 1 | 0.640003 | 0.45756 |
| MED-3247 | 0 | left_top_k | 9 | None | None | None | None |
| MED-1010 | 0 | down | 8 | 9 | -1 | 0.397454 | 0.355247 |
| MED-3428 | 0 | down | 6 | 7 | -1 | 0.325906 | 0.394833 |
| MED-828 | 0 | down | 5 | 8 | -3 | 0.153085 | 0.368982 |

## PLAIN-1387

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3383 | 1 | up | 6 | 5 | 1 | 0.753177 | 0.434626 |
| MED-3382 | 1 | entered_top_k | None | 9 | None | 0.32593 | 0.257671 |
| MED-3384 | 1 | left_top_k | 10 | None | None | None | None |
| MED-1153 | 0 | up | 5 | 4 | 1 | 0.757941 | 0.451228 |
| MED-4655 | 0 | up | 7 | 6 | 1 | 0.710713 | 0.414045 |
| MED-3013 | 0 | down | 9 | 10 | -1 | 0.0 | 0.244297 |
| MED-2078 | 0 | down | 4 | 7 | -3 | 0.305773 | 0.362842 |

## PLAIN-1398

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1720 | 1 | up | 10 | 8 | 2 | 0.904355 | 0.706237 |
| MED-4216 | 1 | up | 4 | 3 | 1 | 1.0 | 0.801 |
| MED-4897 | 1 | up | 7 | 6 | 1 | 0.756107 | 0.735802 |
| MED-1719 | 1 | down | 3 | 4 | -1 | 0.758321 | 0.754836 |
| MED-1722 | 1 | down | 6 | 7 | -1 | 0.682464 | 0.726223 |
| MED-1712 | 1 | down | 8 | 10 | -2 | 0.253282 | 0.601124 |

## PLAIN-1409

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-5101 | 1 | up | 8 | 6 | 2 | 0.469428 | 0.512297 |
| MED-1572 | 0 | up | 4 | 2 | 2 | 0.828301 | 0.797511 |
| MED-1144 | 0 | up | 9 | 8 | 1 | 0.434022 | 0.477587 |
| MED-1689 | 0 | up | 5 | 4 | 1 | 1.0 | 0.754449 |
| MED-1570 | 0 | down | 2 | 3 | -1 | 0.438605 | 0.763436 |
| MED-5073 | 0 | down | 6 | 7 | -1 | 0.228296 | 0.48168 |
| MED-1272 | 0 | down | 7 | 9 | -2 | 0.0 | 0.42909 |
| MED-1697 | 0 | down | 3 | 5 | -2 | 0.343679 | 0.720775 |

## PLAIN-1419

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-5156 | 0 | up | 3 | 2 | 1 | 1.0 | 0.787818 |
| MED-2327 | 0 | down | 2 | 3 | -1 | 0.0 | 0.781362 |

## PLAIN-1429

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4057 | 0 | up | 10 | 2 | 8 | 1.0 | 0.720266 |
| MED-4802 | 0 | up | 5 | 4 | 1 | 0.612148 | 0.717458 |
| MED-1210 | 0 | entered_top_k | None | 10 | None | 0.469486 | 0.605527 |
| MED-1381 | 0 | left_top_k | 8 | None | None | None | None |
| MED-2304 | 0 | down | 4 | 5 | -1 | 0.562968 | 0.712643 |
| MED-5196 | 0 | down | 2 | 3 | -1 | 0.47766 | 0.719705 |
| MED-5344 | 0 | down | 7 | 8 | -1 | 0.591902 | 0.676643 |
| MED-3793 | 0 | down | 3 | 7 | -4 | 0.434401 | 0.691169 |

## PLAIN-143

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3639 | 0 | up | 10 | 9 | 1 | 0.407842 | 0.400741 |
| MED-4026 | 0 | up | 8 | 7 | 1 | 0.368459 | 0.4174 |
| MED-1858 | 0 | entered_top_k | None | 8 | None | 0.648044 | 0.413574 |
| MED-2093 | 0 | left_top_k | 9 | None | None | None | None |
| MED-3640 | 0 | entered_top_k | None | 10 | None | 0.380518 | 0.394542 |
| MED-5097 | 0 | left_top_k | 7 | None | None | None | None |

## PLAIN-1441

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3629 | 1 | left_top_k | 10 | None | None | None | None |
| MED-3973 | 1 | entered_top_k | None | 9 | None | 0.689885 | 0.375824 |
| MED-4410 | 0 | up | 8 | 7 | 1 | 0.510257 | 0.397918 |
| MED-2218 | 0 | down | 7 | 8 | -1 | 0.369896 | 0.390172 |
| MED-3659 | 0 | down | 9 | 10 | -1 | 0.457306 | 0.371876 |

## PLAIN-1453

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1144 | 1 | up | 7 | 5 | 2 | 0.777728 | 0.710728 |
| MED-1140 | 1 | entered_top_k | None | 8 | None | 0.806745 | 0.659806 |
| MED-1761 | 1 | entered_top_k | None | 10 | None | 0.801198 | 0.629878 |
| MED-3060 | 1 | left_top_k | 9 | None | None | None | None |
| MED-3376 | 1 | left_top_k | 10 | None | None | None | None |
| MED-2738 | 0 | up | 5 | 3 | 2 | 0.865695 | 0.813916 |
| MED-1150 | 0 | up | 8 | 7 | 1 | 0.818933 | 0.691688 |
| MED-1955 | 0 | down | 6 | 9 | -3 | 0.156311 | 0.645332 |

## PLAIN-1463

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2141 | 1 | entered_top_k | None | 10 | None | 0.603623 | 0.603106 |
| MED-3136 | 1 | left_top_k | 10 | None | None | None | None |
| MED-2140 | 1 | down | 8 | 9 | -1 | 0.266424 | 0.712694 |
| MED-3138 | 1 | down | 4 | 7 | -3 | 0.36604 | 0.768566 |
| MED-2147 | 0 | up | 9 | 6 | 3 | 0.898896 | 0.772813 |
| MED-1880 | 0 | up | 7 | 5 | 2 | 0.562655 | 0.773441 |
| MED-2352 | 0 | up | 5 | 4 | 1 | 0.547359 | 0.789201 |
| MED-2777 | 0 | down | 6 | 8 | -2 | 0.280716 | 0.729667 |

## PLAIN-1473

No rank movements inside the cutoff.

## PLAIN-1485

No rank movements inside the cutoff.

## PLAIN-1496

No rank movements inside the cutoff.

## PLAIN-1506

No rank movements inside the cutoff.

## PLAIN-1516

No rank movements inside the cutoff.

## PLAIN-1527

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1307 | 1 | up | 6 | 2 | 4 | 1.0 | 0.637418 |
| MED-2158 | 1 | up | 7 | 5 | 2 | 0.741671 | 0.576006 |
| MED-1302 | 1 | up | 9 | 8 | 1 | 0.580434 | 0.528689 |
| MED-1304 | 1 | entered_top_k | None | 6 | None | 0.823206 | 0.558655 |
| MED-1309 | 1 | entered_top_k | None | 10 | None | 0.686269 | 0.510598 |
| MED-4101 | 1 | left_top_k | 10 | None | None | None | None |
| MED-4874 | 1 | left_top_k | 8 | None | None | None | None |
| MED-3491 | 1 | down | 2 | 3 | -1 | 0.181581 | 0.59389 |

## PLAIN-153

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3690 | 1 | up | 7 | 6 | 1 | 0.60372 | 0.460225 |
| MED-3691 | 1 | up | 8 | 7 | 1 | 0.540211 | 0.443789 |
| MED-1248 | 0 | left_top_k | 10 | None | None | None | None |
| MED-1712 | 0 | entered_top_k | None | 9 | None | 0.30723 | 0.362624 |
| MED-1719 | 0 | entered_top_k | None | 10 | None | 0.249134 | 0.359215 |
| MED-2105 | 0 | left_top_k | 9 | None | None | None | None |
| MED-1724 | 0 | down | 6 | 8 | -2 | 0.224967 | 0.397398 |

## PLAIN-1537

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2588 | 1 | entered_top_k | None | 8 | None | 0.337796 | 0.230365 |
| MED-4514 | 1 | entered_top_k | None | 9 | None | 0.440093 | 0.229818 |
| MED-1714 | 0 | up | 9 | 6 | 3 | 0.295998 | 0.242693 |
| MED-1257 | 0 | up | 6 | 4 | 2 | 0.277189 | 0.259526 |
| MED-4831 | 0 | up | 4 | 3 | 1 | 0.263869 | 0.263045 |
| MED-3273 | 0 | left_top_k | 7 | None | None | None | None |
| MED-5016 | 0 | left_top_k | 10 | None | None | None | None |
| MED-2943 | 0 | down | 8 | 10 | -2 | 0.176358 | 0.22825 |

## PLAIN-1547

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4013 | 0 | up | 7 | 6 | 1 | 0.130401 | 0.10834 |
| MED-4496 | 0 | up | 10 | 9 | 1 | 0.131677 | 0.103775 |
| MED-975 | 0 | up | 4 | 3 | 1 | 0.20901 | 0.153253 |
| MED-3964 | 0 | entered_top_k | None | 10 | None | 0.161107 | 0.102513 |
| MED-5030 | 0 | left_top_k | 9 | None | None | None | None |
| MED-2303 | 0 | down | 6 | 7 | -1 | 0.114784 | 0.106208 |
| MED-983 | 0 | down | 3 | 4 | -1 | 0.147156 | 0.147243 |

## PLAIN-1557

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4313 | 1 | down | 6 | 7 | -1 | 0.0 | 0.159098 |
| MED-1528 | 0 | up | 7 | 6 | 1 | 0.30264 | 0.192246 |

## PLAIN-1568

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-5057 | 0 | up | 7 | 5 | 2 | 0.228879 | 0.116233 |
| MED-1672 | 0 | up | 8 | 7 | 1 | 0.147071 | 0.096275 |
| MED-1674 | 0 | entered_top_k | None | 10 | None | 0.128195 | 0.068221 |
| MED-3734 | 0 | left_top_k | 10 | None | None | None | None |
| MED-4782 | 0 | down | 5 | 6 | -1 | 0.0 | 0.108151 |
| MED-2054 | 0 | down | 6 | 8 | -2 | 0.0 | 0.091208 |

## PLAIN-1579

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4667 | 1 | up | 2 | 1 | 1 | 1.0 | 0.944371 |
| MED-4801 | 0 | down | 1 | 2 | -1 | 0.549217 | 0.909843 |

## PLAIN-1590

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4234 | 0 | up | 9 | 8 | 1 | 0.180309 | 0.297909 |
| MED-2086 | 0 | entered_top_k | None | 10 | None | 0.280217 | 0.267139 |
| MED-3001 | 0 | left_top_k | 10 | None | None | None | None |
| MED-4079 | 0 | entered_top_k | None | 9 | None | 0.421798 | 0.292952 |
| MED-5347 | 0 | left_top_k | 8 | None | None | None | None |

## PLAIN-1601

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3537 | 1 | up | 5 | 3 | 2 | 0.813561 | 0.752598 |
| MED-2668 | 1 | down | 7 | 8 | -1 | 0.0 | 0.435256 |
| MED-5002 | 1 | down | 3 | 4 | -1 | 0.431741 | 0.720137 |
| MED-1506 | 0 | up | 8 | 7 | 1 | 0.478863 | 0.471403 |
| MED-1700 | 0 | down | 4 | 5 | -1 | 0.0 | 0.623361 |

## PLAIN-1611

No rank movements inside the cutoff.

## PLAIN-1621

No rank movements inside the cutoff.

## PLAIN-1635

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1337 | 1 | up | 9 | 5 | 4 | 0.977763 | 0.785167 |
| MED-4902 | 1 | up | 6 | 2 | 4 | 0.985314 | 0.808217 |
| MED-1229 | 1 | up | 7 | 6 | 1 | 0.895317 | 0.777417 |
| MED-2123 | 1 | up | 8 | 7 | 1 | 0.895317 | 0.777417 |
| MED-2055 | 1 | entered_top_k | None | 4 | None | 1.0 | 0.785895 |
| MED-4897 | 1 | entered_top_k | None | 10 | None | 0.904805 | 0.745706 |
| MED-4899 | 1 | left_top_k | 4 | None | None | None | None |
| MED-4753 | 1 | down | 2 | 3 | -1 | 0.592299 | 0.788683 |

## PLAIN-1645

No rank movements inside the cutoff.

## PLAIN-165

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3768 | 1 | up | 10 | 8 | 2 | 0.745113 | 0.628555 |
| MED-3696 | 1 | up | 5 | 4 | 1 | 0.754017 | 0.745154 |
| MED-2424 | 0 | down | 9 | 10 | -1 | 0.461372 | 0.582279 |
| MED-2437 | 0 | down | 4 | 5 | -1 | 0.715508 | 0.743136 |
| MED-4450 | 0 | down | 8 | 9 | -1 | 0.52968 | 0.605596 |

## PLAIN-1656

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2437 | 0 | up | 5 | 2 | 3 | 1.0 | 0.730923 |
| MED-3699 | 0 | up | 7 | 4 | 3 | 0.870361 | 0.692551 |
| MED-3551 | 0 | up | 8 | 6 | 2 | 0.700297 | 0.647472 |
| MED-1721 | 0 | up | 9 | 8 | 1 | 0.600134 | 0.626754 |
| MED-1362 | 0 | left_top_k | 10 | None | None | None | None |
| MED-1718 | 0 | entered_top_k | None | 10 | None | 0.86754 | 0.610361 |
| MED-1817 | 0 | entered_top_k | None | 7 | None | 0.888064 | 0.632435 |
| MED-4470 | 0 | left_top_k | 6 | None | None | None | None |

## PLAIN-1667

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3462 | 1 | up | 5 | 4 | 1 | 0.652876 | 0.801781 |
| MED-4828 | 1 | up | 4 | 3 | 1 | 0.720906 | 0.829663 |
| MED-4829 | 1 | up | 10 | 9 | 1 | 0.729614 | 0.613333 |
| MED-1473 | 1 | left_top_k | 9 | None | None | None | None |
| MED-4315 | 0 | entered_top_k | None | 10 | None | 0.613325 | 0.578769 |
| MED-4166 | 0 | down | 3 | 5 | -2 | 0.577068 | 0.801457 |

## PLAIN-1679

No rank movements inside the cutoff.

## PLAIN-1690

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1493 | 0 | up | 5 | 2 | 3 | 0.344408 | 0.620146 |
| MED-1774 | 0 | up | 10 | 9 | 1 | 0.18137 | 0.441901 |
| MED-4599 | 0 | up | 7 | 6 | 1 | 0.184178 | 0.495986 |
| MED-4674 | 0 | up | 8 | 7 | 1 | 0.184178 | 0.495986 |
| MED-2295 | 0 | down | 9 | 10 | -1 | 0.045555 | 0.423084 |
| MED-2327 | 0 | down | 3 | 4 | -1 | 0.058166 | 0.58659 |
| MED-3692 | 0 | down | 4 | 5 | -1 | 0.023789 | 0.563997 |
| MED-3726 | 0 | down | 2 | 3 | -1 | 0.05987 | 0.59153 |

## PLAIN-1700

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1100 | 0 | up | 7 | 6 | 1 | 0.59709 | 0.369851 |
| MED-2213 | 0 | left_top_k | 9 | None | None | None | None |
| MED-4107 | 0 | entered_top_k | None | 8 | None | 0.438974 | 0.293181 |
| MED-1708 | 0 | down | 8 | 9 | -1 | 0.191706 | 0.287919 |
| MED-4095 | 0 | down | 6 | 7 | -1 | 0.356701 | 0.336273 |

## PLAIN-1710

No rank movements inside the cutoff.

## PLAIN-1721

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4983 | 1 | up | 10 | 8 | 2 | 0.462911 | 0.371209 |
| MED-4823 | 1 | up | 6 | 5 | 1 | 0.752511 | 0.687861 |
| MED-1606 | 1 | down | 8 | 9 | -1 | 0.0 | 0.36989 |
| MED-1230 | 0 | down | 5 | 6 | -1 | 0.208031 | 0.603112 |
| MED-1377 | 0 | down | 9 | 10 | -1 | 0.0 | 0.292168 |

## PLAIN-1731

No rank movements inside the cutoff.

## PLAIN-1741

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4314 | 1 | up | 7 | 5 | 2 | 0.562108 | 0.618487 |
| MED-2381 | 1 | up | 9 | 8 | 1 | 0.496958 | 0.506821 |
| MED-2595 | 1 | up | 3 | 2 | 1 | 0.729168 | 0.788505 |
| MED-4295 | 1 | entered_top_k | None | 10 | None | 0.393751 | 0.380212 |
| MED-4286 | 1 | down | 2 | 3 | -1 | 0.452173 | 0.785702 |
| MED-4707 | 1 | down | 8 | 9 | -1 | 0.0 | 0.409735 |
| MED-2597 | 1 | down | 5 | 7 | -2 | 0.352953 | 0.610812 |
| MED-1499 | 0 | left_top_k | 10 | None | None | None | None |

## PLAIN-175

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-5200 | 0 | up | 9 | 6 | 3 | 0.179436 | 0.169484 |
| MED-2459 | 0 | left_top_k | 8 | None | None | None | None |
| MED-4985 | 0 | entered_top_k | None | 10 | None | 0.183627 | 0.147144 |
| MED-825 | 0 | left_top_k | 10 | None | None | None | None |
| MED-836 | 0 | entered_top_k | None | 8 | None | 0.19975 | 0.16009 |
| MED-4854 | 0 | down | 6 | 7 | -1 | 0.138764 | 0.167118 |
| MED-4347 | 0 | down | 7 | 9 | -2 | 0.06251 | 0.149583 |

## PLAIN-1752

No rank movements inside the cutoff.

## PLAIN-1762

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3558 | 0 | up | 9 | 8 | 1 | 0.6871 | 0.639811 |
| MED-4512 | 0 | down | 8 | 9 | -1 | 0.28577 | 0.59401 |

## PLAIN-1772

No rank movements inside the cutoff.

## PLAIN-1784

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4261 | 0 | up | 5 | 2 | 3 | 0.964545 | 0.908312 |
| MED-4482 | 0 | up | 4 | 3 | 1 | 0.80902 | 0.888043 |
| MED-4485 | 0 | up | 10 | 9 | 1 | 0.714125 | 0.753806 |
| MED-4493 | 0 | down | 3 | 4 | -1 | 0.496468 | 0.841854 |
| MED-5235 | 0 | down | 9 | 10 | -1 | 0.593915 | 0.741444 |
| MED-5195 | 0 | down | 2 | 5 | -3 | 0.401536 | 0.836876 |

## PLAIN-1794

No rank movements inside the cutoff.

## PLAIN-1805

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3932 | 1 | up | 8 | 5 | 3 | 0.993893 | 0.495584 |
| MED-3935 | 1 | up | 7 | 6 | 1 | 0.856786 | 0.475785 |
| MED-4939 | 1 | up | 4 | 3 | 1 | 1.0 | 0.634794 |
| MED-5196 | 1 | up | 2 | 1 | 1 | 0.916841 | 0.981583 |
| MED-2173 | 1 | left_top_k | 10 | None | None | None | None |
| MED-3930 | 1 | entered_top_k | None | 8 | None | 0.652017 | 0.374337 |
| MED-3931 | 1 | down | 3 | 4 | -1 | 0.535341 | 0.570031 |
| MED-3938 | 1 | down | 1 | 2 | -1 | 0.3395 | 0.8679 |

## PLAIN-1817

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2150 | 1 | down | 4 | 5 | -1 | 0.0 | 0.5552 |
| MED-2382 | 0 | up | 5 | 4 | 1 | 0.506027 | 0.60316 |
| MED-2792 | 0 | up | 10 | 9 | 1 | 0.1841 | 0.24451 |
| MED-3385 | 0 | up | 9 | 8 | 1 | 0.336586 | 0.276848 |
| MED-1534 | 0 | down | 8 | 10 | -2 | 0.0 | 0.234385 |

## PLAIN-1827

No rank movements inside the cutoff.

## PLAIN-1837

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3936 | 1 | up | 8 | 3 | 5 | 1.0 | 0.734173 |
| MED-1161 | 1 | up | 9 | 8 | 1 | 0.500414 | 0.614186 |
| MED-1167 | 1 | up | 3 | 2 | 1 | 0.686776 | 0.783149 |
| MED-1139 | 1 | entered_top_k | None | 10 | None | 0.659243 | 0.583206 |
| MED-1174 | 1 | left_top_k | 10 | None | None | None | None |
| MED-2748 | 1 | down | 2 | 5 | -3 | 0.244702 | 0.706257 |
| MED-4178 | 1 | down | 5 | 9 | -4 | 0.0 | 0.585632 |

## PLAIN-1847

No rank movements inside the cutoff.

## PLAIN-1857

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2988 | 1 | up | 2 | 1 | 1 | 1.0 | 0.899689 |
| MED-2544 | 1 | down | 1 | 2 | -1 | 0.370097 | 0.874019 |
| MED-2986 | 0 | up | 7 | 5 | 2 | 0.541892 | 0.357926 |
| MED-2754 | 0 | up | 10 | 9 | 1 | 0.32773 | 0.257136 |
| MED-2979 | 0 | entered_top_k | None | 8 | None | 0.480467 | 0.268001 |
| MED-5231 | 0 | left_top_k | 8 | None | None | None | None |
| MED-1067 | 0 | down | 9 | 10 | -1 | 0.201051 | 0.232579 |
| MED-3215 | 0 | down | 5 | 6 | -1 | 0.250878 | 0.306237 |

## PLAIN-186

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2061 | 0 | up | 10 | 9 | 1 | 0.52575 | 0.489819 |
| MED-2053 | 0 | entered_top_k | None | 10 | None | 0.574074 | 0.443257 |
| MED-2060 | 0 | entered_top_k | None | 8 | None | 0.660326 | 0.503441 |
| MED-2100 | 0 | left_top_k | 8 | None | None | None | None |
| MED-4641 | 0 | left_top_k | 9 | None | None | None | None |

## PLAIN-1867

No rank movements inside the cutoff.

## PLAIN-1877

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1250 | 0 | up | 6 | 4 | 2 | 1.0 | 0.812821 |
| MED-3931 | 0 | entered_top_k | None | 10 | None | 0.806647 | 0.577314 |
| MED-4349 | 0 | left_top_k | 10 | None | None | None | None |
| MED-4255 | 0 | down | 4 | 5 | -1 | 0.463916 | 0.707837 |
| MED-4613 | 0 | down | 5 | 6 | -1 | 0.463916 | 0.707837 |

## PLAIN-1887

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1397 | 0 | up | 7 | 5 | 2 | 1.0 | 0.663983 |
| MED-2824 | 0 | entered_top_k | None | 7 | None | 0.947625 | 0.589376 |
| MED-3522 | 0 | left_top_k | 10 | None | None | None | None |
| MED-4915 | 0 | entered_top_k | None | 10 | None | 0.517778 | 0.500954 |
| MED-915 | 0 | left_top_k | 9 | None | None | None | None |
| MED-2332 | 0 | down | 5 | 6 | -1 | 0.42924 | 0.641971 |
| MED-3532 | 0 | down | 8 | 9 | -1 | 0.29534 | 0.507351 |
| MED-1293 | 0 | down | 6 | 8 | -2 | 0.219165 | 0.547596 |

## PLAIN-1897

No rank movements inside the cutoff.

## PLAIN-1909

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4593 | 1 | up | 9 | 5 | 4 | 0.9166 | 0.51342 |
| MED-2340 | 1 | entered_top_k | None | 10 | None | 0.89048 | 0.396943 |
| MED-3891 | 1 | left_top_k | 10 | None | None | None | None |
| MED-1983 | 1 | down | 6 | 7 | -1 | 0.62925 | 0.511232 |
| MED-2352 | 1 | down | 5 | 6 | -1 | 0.456916 | 0.51165 |
| MED-3171 | 1 | down | 8 | 9 | -1 | 0.423364 | 0.423154 |
| MED-3288 | 0 | down | 7 | 8 | -1 | 0.728633 | 0.497389 |

## PLAIN-1919

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4431 | 1 | up | 2 | 1 | 1 | 1.0 | 0.972133 |
| MED-4433 | 1 | up | 6 | 5 | 1 | 0.51155 | 0.555874 |
| MED-3320 | 1 | down | 8 | 9 | -1 | 0.259334 | 0.38475 |
| MED-3321 | 1 | down | 1 | 2 | -1 | 0.572681 | 0.914536 |
| MED-4182 | 0 | up | 9 | 8 | 1 | 0.430036 | 0.397628 |
| MED-3545 | 0 | left_top_k | 10 | None | None | None | None |
| MED-4429 | 0 | entered_top_k | None | 10 | None | 0.333831 | 0.368682 |
| MED-3790 | 0 | down | 5 | 6 | -1 | 0.21413 | 0.505065 |

## PLAIN-1929

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-951 | 0 | up | 10 | 7 | 3 | 0.566575 | 0.497964 |
| MED-3452 | 0 | up | 4 | 3 | 1 | 0.712316 | 0.629646 |
| MED-2905 | 0 | left_top_k | 8 | None | None | None | None |
| MED-3032 | 0 | left_top_k | 9 | None | None | None | None |
| MED-5097 | 0 | entered_top_k | None | 10 | None | 0.32958 | 0.422894 |
| MED-5099 | 0 | entered_top_k | None | 9 | None | 0.675506 | 0.442676 |
| MED-4038 | 0 | down | 7 | 8 | -1 | 0.529735 | 0.495654 |
| MED-4470 | 0 | down | 3 | 4 | -1 | 0.605885 | 0.61188 |

## PLAIN-1940

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1198 | 0 | up | 5 | 4 | 1 | 0.392399 | 0.20842 |
| MED-4114 | 0 | up | 4 | 3 | 1 | 0.381776 | 0.230719 |
| MED-4946 | 0 | down | 3 | 5 | -2 | 0.0 | 0.191555 |

## PLAIN-1950

No rank movements inside the cutoff.

## PLAIN-196

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-5326 | 1 | entered_top_k | None | 8 | None | 0.188492 | 0.156522 |
| MED-3970 | 1 | down | 8 | 10 | -2 | 0.0 | 0.144643 |
| MED-2014 | 0 | entered_top_k | None | 9 | None | 0.287126 | 0.153492 |
| MED-3800 | 0 | left_top_k | 9 | None | None | None | None |
| MED-5133 | 0 | left_top_k | 10 | None | None | None | None |

## PLAIN-1962

No rank movements inside the cutoff.

## PLAIN-1972

No rank movements inside the cutoff.

## PLAIN-1983

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2507 | 1 | up | 6 | 4 | 2 | 0.830963 | 0.513415 |
| MED-2134 | 1 | up | 3 | 2 | 1 | 1.0 | 0.878742 |
| MED-2504 | 1 | up | 9 | 8 | 1 | 0.40964 | 0.365887 |
| MED-2517 | 1 | down | 8 | 9 | -1 | 0.362944 | 0.364385 |
| MED-2521 | 1 | down | 2 | 3 | -1 | 0.316171 | 0.768879 |
| MED-2520 | 1 | down | 4 | 6 | -2 | 0.0 | 0.405792 |

## PLAIN-1995

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1635 | 0 | up | 6 | 5 | 1 | 0.83385 | 0.883749 |
| MED-4330 | 0 | up | 5 | 4 | 1 | 0.767059 | 0.893502 |
| MED-4902 | 0 | up | 3 | 2 | 1 | 0.806668 | 0.942234 |
| MED-4779 | 0 | entered_top_k | None | 10 | None | 0.887063 | 0.779767 |
| MED-5047 | 0 | left_top_k | 10 | None | None | None | None |
| MED-4776 | 0 | down | 2 | 3 | -1 | 0.650558 | 0.91508 |
| MED-1647 | 0 | down | 4 | 6 | -2 | 0.68622 | 0.881322 |

## PLAIN-2

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2431 | 2 | up | 6 | 5 | 1 | 0.863725 | 0.608261 |
| MED-4829 | 1 | up | 5 | 4 | 1 | 0.614175 | 0.612264 |
| MED-4830 | 1 | down | 4 | 6 | -2 | 0.341529 | 0.565415 |
| MED-1193 | 0 | entered_top_k | None | 10 | None | 0.634792 | 0.509297 |
| MED-4827 | 0 | left_top_k | 10 | None | None | None | None |

## PLAIN-2009

No rank movements inside the cutoff.

## PLAIN-2019

No rank movements inside the cutoff.

## PLAIN-2030

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4051 | 1 | up | 2 | 1 | 1 | 1.0 | 0.988481 |
| MED-2816 | 0 | down | 1 | 2 | -1 | 0.701858 | 0.940372 |

## PLAIN-2040

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4964 | 0 | up | 6 | 5 | 1 | 0.2452 | 0.390657 |
| MED-4943 | 0 | down | 5 | 6 | -1 | 0.0 | 0.386659 |

## PLAIN-2051

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1454 | 1 | down | 8 | 9 | -1 | 0.550751 | 0.658114 |
| MED-4556 | 1 | down | 5 | 6 | -1 | 0.608456 | 0.719844 |
| MED-4005 | 1 | down | 7 | 10 | -3 | 0.390665 | 0.647739 |
| MED-3355 | 0 | up | 9 | 8 | 1 | 0.727894 | 0.685766 |
| MED-1072 | 0 | left_top_k | 10 | None | None | None | None |
| MED-1873 | 0 | entered_top_k | None | 5 | None | 1.0 | 0.728034 |
| MED-3356 | 0 | down | 6 | 7 | -1 | 0.612352 | 0.696676 |

## PLAIN-2061

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-5101 | 1 | up | 4 | 3 | 1 | 0.591325 | 0.60455 |
| MED-2406 | 1 | left_top_k | 10 | None | None | None | None |
| MED-4960 | 1 | entered_top_k | None | 10 | None | 0.328137 | 0.268156 |
| MED-2262 | 1 | down | 5 | 6 | -1 | 0.466776 | 0.455112 |
| MED-2344 | 1 | down | 3 | 4 | -1 | 0.288672 | 0.576595 |
| MED-3295 | 0 | up | 6 | 5 | 1 | 1.0 | 0.55777 |

## PLAIN-207

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-5197 | 1 | up | 4 | 2 | 2 | 1.0 | 0.801468 |
| MED-4053 | 1 | down | 5 | 6 | -1 | 0.534741 | 0.688759 |
| MED-5326 | 1 | down | 3 | 4 | -1 | 0.546406 | 0.712564 |
| MED-3000 | 0 | up | 9 | 5 | 4 | 0.965294 | 0.702698 |
| MED-2106 | 0 | up | 10 | 7 | 3 | 0.716437 | 0.629666 |
| MED-2170 | 0 | down | 7 | 8 | -1 | 0.524486 | 0.623421 |
| MED-4482 | 0 | down | 2 | 3 | -1 | 0.688152 | 0.775499 |
| MED-4977 | 0 | down | 8 | 9 | -1 | 0.524486 | 0.623421 |

## PLAIN-2071

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4306 | 1 | up | 3 | 2 | 1 | 0.91567 | 0.77639 |
| MED-3526 | 1 | entered_top_k | None | 8 | None | 0.158761 | 0.14952 |
| MED-3540 | 1 | left_top_k | 10 | None | None | None | None |
| MED-3546 | 1 | entered_top_k | None | 10 | None | 0.237281 | 0.137644 |
| MED-3658 | 0 | up | 9 | 7 | 2 | 0.495687 | 0.226707 |
| MED-1245 | 0 | left_top_k | 8 | None | None | None | None |
| MED-3661 | 0 | entered_top_k | None | 9 | None | 0.294253 | 0.140152 |
| MED-5365 | 0 | left_top_k | 7 | None | None | None | None |

## PLAIN-2081

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2700 | 0 | up | 6 | 3 | 3 | 1.0 | 0.526334 |
| MED-2303 | 0 | up | 7 | 6 | 1 | 0.249118 | 0.373287 |
| MED-2505 | 0 | up | 3 | 2 | 1 | 0.312234 | 0.553982 |
| MED-1223 | 0 | entered_top_k | None | 8 | None | 0.273745 | 0.36491 |
| MED-2769 | 0 | left_top_k | 10 | None | None | None | None |
| MED-3762 | 0 | down | 4 | 5 | -1 | 0.185834 | 0.384554 |
| MED-1182 | 0 | down | 2 | 4 | -2 | 0.0 | 0.522954 |
| MED-2309 | 0 | down | 8 | 10 | -2 | 0.173806 | 0.355437 |

## PLAIN-2092

No rank movements inside the cutoff.

## PLAIN-2102

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1498 | 1 | left_top_k | 10 | None | None | None | None |
| MED-2252 | 1 | entered_top_k | None | 9 | None | 0.451447 | 0.247384 |
| MED-3033 | 0 | up | 5 | 4 | 1 | 0.870232 | 0.56537 |
| MED-5256 | 0 | down | 9 | 10 | -1 | 0.0 | 0.231973 |
| MED-759 | 0 | down | 4 | 5 | -1 | 0.660528 | 0.525166 |

## PLAIN-2113

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2521 | 0 | up | 9 | 7 | 2 | 0.346171 | 0.30518 |
| MED-1505 | 0 | up | 7 | 6 | 1 | 0.319532 | 0.311982 |
| MED-1542 | 0 | entered_top_k | None | 8 | None | 0.256675 | 0.286828 |
| MED-1546 | 0 | left_top_k | 6 | None | None | None | None |
| MED-2296 | 0 | entered_top_k | None | 9 | None | 0.266477 | 0.285165 |
| MED-3768 | 0 | entered_top_k | None | 10 | None | 0.245321 | 0.284348 |
| MED-4598 | 0 | left_top_k | 10 | None | None | None | None |
| MED-762 | 0 | left_top_k | 8 | None | None | None | None |

## PLAIN-2124

No rank movements inside the cutoff.

## PLAIN-2134

No rank movements inside the cutoff.

## PLAIN-2145

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3967 | 0 | up | 10 | 8 | 2 | 0.220645 | 0.19219 |
| MED-3145 | 0 | entered_top_k | None | 10 | None | 0.141006 | 0.170746 |
| MED-3372 | 0 | entered_top_k | None | 9 | None | 0.218374 | 0.182757 |
| MED-3882 | 0 | left_top_k | 8 | None | None | None | None |
| MED-4525 | 0 | left_top_k | 9 | None | None | None | None |

## PLAIN-2156

No rank movements inside the cutoff.

## PLAIN-2167

No rank movements inside the cutoff.

## PLAIN-217

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1250 | 0 | up | 10 | 6 | 4 | 1.0 | 0.638639 |
| MED-1997 | 0 | down | 9 | 10 | -1 | 0.124813 | 0.492507 |
| MED-4984 | 0 | down | 6 | 7 | -1 | 0.563496 | 0.61616 |
| MED-4389 | 0 | down | 7 | 9 | -2 | 0.515758 | 0.599931 |

## PLAIN-2177

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1421 | 1 | up | 4 | 2 | 2 | 1.0 | 0.506934 |
| MED-1185 | 1 | down | 2 | 3 | -1 | 0.59549 | 0.441837 |
| MED-3228 | 0 | up | 7 | 5 | 2 | 0.633133 | 0.350403 |
| MED-1953 | 0 | down | 5 | 6 | -1 | 0.0 | 0.302444 |
| MED-4320 | 0 | down | 3 | 4 | -1 | 0.634686 | 0.435606 |
| MED-4499 | 0 | down | 6 | 7 | -1 | 0.0 | 0.248232 |

## PLAIN-2187

No rank movements inside the cutoff.

## PLAIN-227

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3466 | 0 | up | 9 | 7 | 2 | 0.506525 | 0.471689 |
| MED-1474 | 0 | up | 3 | 2 | 1 | 0.717561 | 0.607209 |
| MED-4829 | 0 | up | 4 | 3 | 1 | 0.525238 | 0.560251 |
| MED-3459 | 0 | entered_top_k | None | 10 | None | 0.346773 | 0.424332 |
| MED-4830 | 0 | left_top_k | 10 | None | None | None | None |
| MED-3462 | 0 | down | 8 | 9 | -1 | 0.42774 | 0.467112 |
| MED-4166 | 0 | down | 7 | 8 | -1 | 0.408717 | 0.471289 |
| MED-3534 | 0 | down | 2 | 4 | -2 | 0.220348 | 0.559652 |

## PLAIN-23

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2661 | 2 | entered_top_k | None | 7 | None | 0.811871 | 0.457155 |
| MED-2644 | 2 | down | 3 | 5 | -2 | 0.368963 | 0.487799 |
| MED-2643 | 1 | up | 5 | 3 | 2 | 1.0 | 0.583747 |
| MED-4170 | 1 | left_top_k | 10 | None | None | None | None |
| MED-1171 | 0 | left_top_k | 8 | None | None | None | None |
| MED-1221 | 0 | entered_top_k | None | 8 | None | 0.576924 | 0.444 |
| MED-1374 | 0 | left_top_k | 9 | None | None | None | None |
| MED-2292 | 0 | entered_top_k | None | 9 | None | 0.716049 | 0.436102 |

## PLAIN-238

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2182 | 0 | up | 10 | 6 | 4 | 0.56925 | 0.444447 |
| MED-2501 | 0 | up | 6 | 5 | 1 | 0.490609 | 0.473331 |
| MED-3651 | 0 | left_top_k | 8 | None | None | None | None |
| MED-5104 | 0 | entered_top_k | None | 10 | None | 0.374467 | 0.384807 |
| MED-2105 | 0 | down | 5 | 8 | -3 | 0.03687 | 0.429125 |

## PLAIN-248

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4886 | 0 | up | 10 | 6 | 4 | 1.0 | 0.837918 |
| MED-3782 | 0 | up | 6 | 5 | 1 | 0.881326 | 0.840964 |
| MED-3790 | 0 | entered_top_k | None | 9 | None | 0.829081 | 0.78845 |
| MED-4888 | 0 | entered_top_k | None | 7 | None | 0.959434 | 0.827766 |
| MED-5359 | 0 | left_top_k | 9 | None | None | None | None |
| MED-951 | 0 | left_top_k | 7 | None | None | None | None |
| MED-2769 | 0 | down | 8 | 10 | -2 | 0.578175 | 0.756114 |
| MED-5355 | 0 | down | 5 | 8 | -3 | 0.720033 | 0.822421 |

## PLAIN-259

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1586 | 0 | up | 8 | 7 | 1 | 0.32113 | 0.250974 |
| MED-2430 | 0 | entered_top_k | None | 10 | None | 0.547894 | 0.232312 |
| MED-2904 | 0 | entered_top_k | None | 8 | None | 0.402316 | 0.23245 |
| MED-3026 | 0 | entered_top_k | None | 9 | None | 0.402316 | 0.23245 |
| MED-3619 | 0 | left_top_k | 9 | None | None | None | None |
| MED-752 | 0 | left_top_k | 10 | None | None | None | None |
| MED-862 | 0 | left_top_k | 7 | None | None | None | None |

## PLAIN-270

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4331 | 1 | up | 4 | 2 | 2 | 0.925222 | 0.954363 |
| MED-1635 | 0 | up | 7 | 5 | 2 | 0.855827 | 0.903917 |
| MED-1645 | 0 | up | 8 | 7 | 1 | 0.81838 | 0.863257 |
| MED-5257 | 0 | up | 2 | 1 | 1 | 1.0 | 0.992532 |
| MED-1647 | 0 | down | 5 | 8 | -3 | 0.615735 | 0.860279 |
| MED-4776 | 0 | down | 1 | 4 | -3 | 0.60425 | 0.92085 |

## PLAIN-280

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4376 | 1 | down | 1 | 2 | -1 | 0.621626 | 0.924325 |
| MED-3023 | 0 | up | 8 | 5 | 3 | 1.0 | 0.733747 |
| MED-2385 | 0 | up | 9 | 8 | 1 | 0.727317 | 0.650871 |
| MED-4733 | 0 | up | 2 | 1 | 1 | 0.86763 | 0.93632 |
| MED-2904 | 0 | entered_top_k | None | 9 | None | 0.955214 | 0.633469 |
| MED-3026 | 0 | entered_top_k | None | 10 | None | 0.955214 | 0.633469 |
| MED-4947 | 0 | left_top_k | 7 | None | None | None | None |
| MED-4948 | 0 | left_top_k | 10 | None | None | None | None |

## PLAIN-291

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2417 | 0 | up | 10 | 8 | 2 | 0.786973 | 0.785917 |
| MED-14 | 0 | up | 6 | 5 | 1 | 0.911773 | 0.862632 |
| MED-3832 | 0 | entered_top_k | None | 10 | None | 0.626786 | 0.744919 |
| MED-4050 | 0 | left_top_k | 8 | None | None | None | None |
| MED-2424 | 0 | down | 5 | 6 | -1 | 0.651887 | 0.83975 |

## PLAIN-307

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-714 | 2 | up | 7 | 5 | 2 | 1.0 | 0.847217 |
| MED-716 | 2 | up | 3 | 2 | 1 | 0.952417 | 0.91506 |
| MED-4566 | 0 | up | 10 | 8 | 2 | 0.920972 | 0.783909 |
| MED-4575 | 0 | entered_top_k | None | 10 | None | 0.800566 | 0.753193 |
| MED-921 | 0 | left_top_k | 9 | None | None | None | None |
| MED-3990 | 0 | down | 2 | 3 | -1 | 0.648051 | 0.871143 |
| MED-920 | 0 | down | 8 | 9 | -1 | 0.710696 | 0.774634 |
| MED-4570 | 0 | down | 5 | 7 | -2 | 0.938059 | 0.841331 |

## PLAIN-320

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-14 | 0 | up | 3 | 2 | 1 | 0.839229 | 0.872385 |
| MED-2258 | 0 | up | 8 | 7 | 1 | 0.562136 | 0.733067 |
| MED-2417 | 0 | up | 7 | 6 | 1 | 0.724651 | 0.773146 |
| MED-3832 | 0 | up | 9 | 8 | 1 | 0.540018 | 0.716302 |
| MED-2424 | 0 | down | 2 | 3 | -1 | 0.630196 | 0.857014 |
| MED-4050 | 0 | down | 6 | 9 | -3 | 0.352017 | 0.705132 |

## PLAIN-33

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-5286 | 0 | up | 9 | 6 | 3 | 0.870196 | 0.778449 |
| MED-1056 | 0 | up | 10 | 8 | 2 | 0.673326 | 0.72459 |
| MED-4202 | 0 | up | 5 | 3 | 2 | 0.754399 | 0.830104 |
| MED-1718 | 0 | left_top_k | 7 | None | None | None | None |
| MED-1997 | 0 | entered_top_k | None | 9 | None | 0.781712 | 0.720785 |
| MED-1334 | 0 | down | 3 | 4 | -1 | 0.61272 | 0.814823 |
| MED-4768 | 0 | down | 4 | 5 | -1 | 0.59076 | 0.809828 |
| MED-5093 | 0 | down | 6 | 7 | -1 | 0.591473 | 0.758608 |

## PLAIN-332

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2780 | 0 | up | 7 | 4 | 3 | 0.935556 | 0.671931 |
| MED-5330 | 0 | up | 9 | 8 | 1 | 0.780523 | 0.607897 |
| MED-3583 | 0 | entered_top_k | None | 9 | None | 0.96911 | 0.607274 |
| MED-5277 | 0 | left_top_k | 8 | None | None | None | None |
| MED-5261 | 0 | down | 4 | 7 | -3 | 0.541791 | 0.647433 |

## PLAIN-344

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1962 | 0 | up | 4 | 3 | 1 | 0.935687 | 0.86146 |
| MED-2847 | 0 | left_top_k | 10 | None | None | None | None |
| MED-4940 | 0 | entered_top_k | None | 7 | None | 0.727284 | 0.598997 |
| MED-1238 | 0 | down | 7 | 8 | -1 | 0.4065 | 0.598213 |
| MED-2495 | 0 | down | 3 | 4 | -1 | 0.593161 | 0.805282 |
| MED-1681 | 0 | down | 8 | 10 | -2 | 0.47669 | 0.586625 |

## PLAIN-358

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3155 | 0 | up | 3 | 2 | 1 | 0.569398 | 0.597203 |
| MED-4315 | 0 | up | 4 | 3 | 1 | 0.592013 | 0.591939 |
| MED-5333 | 0 | up | 6 | 5 | 1 | 0.515489 | 0.571975 |
| MED-4884 | 0 | left_top_k | 10 | None | None | None | None |
| MED-5253 | 0 | entered_top_k | None | 4 | None | 1.0 | 0.578399 |
| MED-1129 | 0 | down | 8 | 9 | -1 | 0.431511 | 0.496911 |
| MED-1366 | 0 | down | 9 | 10 | -1 | 0.395971 | 0.478797 |
| MED-4956 | 0 | down | 5 | 8 | -3 | 0.302501 | 0.530629 |

## PLAIN-371

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4618 | 1 | up | 5 | 4 | 1 | 0.678079 | 0.353039 |
| MED-4619 | 0 | up | 10 | 6 | 4 | 0.766253 | 0.342729 |
| MED-5009 | 0 | up | 8 | 7 | 1 | 0.65423 | 0.326331 |
| MED-1291 | 0 | entered_top_k | None | 9 | None | 0.51254 | 0.274264 |
| MED-5115 | 0 | left_top_k | 7 | None | None | None | None |
| MED-5011 | 0 | down | 4 | 5 | -1 | 0.662091 | 0.351834 |
| MED-5341 | 0 | down | 9 | 10 | -1 | 0.394794 | 0.273066 |
| MED-4452 | 0 | down | 6 | 8 | -2 | 0.361953 | 0.280425 |

## PLAIN-383

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4299 | 1 | down | 5 | 6 | -1 | 0.428791 | 0.684466 |
| MED-1021 | 0 | up | 6 | 5 | 1 | 0.726073 | 0.696276 |
| MED-2510 | 0 | up | 2 | 1 | 1 | 0.881634 | 0.956837 |
| MED-4469 | 0 | up | 3 | 2 | 1 | 1.0 | 0.887342 |
| MED-1712 | 0 | down | 1 | 3 | -2 | 0.019368 | 0.803874 |

## PLAIN-395

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2783 | 0 | up | 5 | 2 | 3 | 0.956662 | 0.806565 |
| MED-3512 | 0 | up | 6 | 4 | 2 | 0.914194 | 0.795142 |
| MED-5137 | 0 | up | 10 | 8 | 2 | 1.0 | 0.646841 |
| MED-1937 | 0 | left_top_k | 9 | None | None | None | None |
| MED-5000 | 0 | entered_top_k | None | 10 | None | 0.644377 | 0.555597 |
| MED-2820 | 0 | down | 8 | 9 | -1 | 0.671898 | 0.620882 |
| MED-3511 | 0 | down | 2 | 3 | -1 | 0.690786 | 0.801436 |
| MED-2825 | 0 | down | 3 | 5 | -2 | 0.666726 | 0.775566 |

## PLAIN-407

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2817 | 0 | up | 5 | 4 | 1 | 0.249374 | 0.193708 |
| MED-4205 | 0 | up | 9 | 8 | 1 | 0.158191 | 0.148553 |
| MED-2202 | 0 | left_top_k | 10 | None | None | None | None |
| MED-2725 | 0 | entered_top_k | None | 10 | None | 0.19903 | 0.125807 |
| MED-2994 | 0 | down | 4 | 5 | -1 | 0.017223 | 0.177112 |
| MED-4796 | 0 | down | 8 | 9 | -1 | 0.073203 | 0.133796 |

## PLAIN-418

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1790 | 0 | up | 10 | 8 | 2 | 0.341676 | 0.481199 |
| MED-2074 | 0 | up | 3 | 1 | 2 | 1.0 | 0.932135 |
| MED-4414 | 0 | up | 8 | 7 | 1 | 0.360458 | 0.493563 |
| MED-3203 | 0 | left_top_k | 7 | None | None | None | None |
| MED-967 | 0 | entered_top_k | None | 10 | None | 0.41523 | 0.450124 |
| MED-2453 | 0 | down | 1 | 3 | -2 | 0.592342 | 0.918468 |

## PLAIN-430

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4943 | 0 | up | 9 | 5 | 4 | 0.878107 | 0.541291 |
| MED-1831 | 0 | up | 5 | 4 | 1 | 0.543733 | 0.544346 |
| MED-118 | 0 | left_top_k | 10 | None | None | None | None |
| MED-1390 | 0 | entered_top_k | None | 10 | None | 0.598065 | 0.424951 |
| MED-2412 | 0 | down | 6 | 7 | -1 | 0.452866 | 0.4904 |
| MED-4004 | 0 | down | 8 | 9 | -1 | 0.467877 | 0.462605 |
| MED-4731 | 0 | down | 7 | 8 | -1 | 0.41013 | 0.475062 |
| MED-1620 | 0 | down | 4 | 6 | -2 | 0.418628 | 0.534932 |

## PLAIN-44

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2810 | 2 | up | 7 | 6 | 1 | 0.651386 | 0.755146 |
| MED-1948 | 0 | up | 5 | 3 | 2 | 0.949959 | 0.828773 |
| MED-2785 | 0 | up | 9 | 8 | 1 | 0.553093 | 0.726974 |
| MED-1939 | 0 | left_top_k | 8 | None | None | None | None |
| MED-2599 | 0 | entered_top_k | None | 10 | None | 0.693449 | 0.721383 |
| MED-2605 | 0 | left_top_k | 10 | None | None | None | None |
| MED-2782 | 0 | entered_top_k | None | 9 | None | 0.531712 | 0.721776 |
| MED-2607 | 0 | down | 6 | 7 | -1 | 0.612327 | 0.748352 |

## PLAIN-441

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4090 | 0 | up | 9 | 7 | 2 | 0.371577 | 0.275181 |
| MED-3109 | 0 | up | 7 | 6 | 1 | 0.290202 | 0.284694 |
| MED-3908 | 0 | down | 8 | 9 | -1 | 0.255778 | 0.253625 |
| MED-5082 | 0 | down | 6 | 8 | -2 | 0.141429 | 0.264713 |

## PLAIN-457

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2710 | 0 | up | 9 | 7 | 2 | 0.407238 | 0.430614 |
| MED-3359 | 0 | up | 5 | 3 | 2 | 1.0 | 0.611177 |
| MED-3776 | 0 | up | 8 | 6 | 2 | 0.434653 | 0.437664 |
| MED-1378 | 0 | left_top_k | 10 | None | None | None | None |
| MED-4236 | 0 | entered_top_k | None | 8 | None | 0.50266 | 0.42346 |
| MED-4465 | 0 | down | 3 | 5 | -2 | 0.287306 | 0.499079 |
| MED-2335 | 0 | down | 6 | 9 | -3 | 0.274715 | 0.420123 |
| MED-4354 | 0 | down | 7 | 10 | -3 | 0.195082 | 0.393071 |

## PLAIN-468

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3988 | 0 | up | 2 | 1 | 1 | 1.0 | 0.999229 |
| MED-4574 | 0 | entered_top_k | None | 9 | None | 0.205359 | 0.229501 |
| MED-4866 | 0 | left_top_k | 10 | None | None | None | None |
| MED-716 | 0 | entered_top_k | None | 10 | None | 0.203997 | 0.229037 |
| MED-922 | 0 | left_top_k | 9 | None | None | None | None |
| MED-3987 | 0 | down | 1 | 2 | -1 | 0.69834 | 0.939668 |

## PLAIN-478

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3636 | 0 | up | 3 | 2 | 1 | 1.0 | 0.442109 |
| MED-1144 | 0 | down | 2 | 3 | -1 | 0.0 | 0.266116 |

## PLAIN-488

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1800 | 1 | up | 8 | 7 | 1 | 0.817582 | 0.394073 |
| MED-1806 | 1 | up | 10 | 9 | 1 | 0.474203 | 0.267356 |
| MED-4767 | 1 | entered_top_k | None | 10 | None | 0.433584 | 0.241217 |
| MED-1796 | 1 | down | 7 | 8 | -1 | 0.724729 | 0.386239 |
| MED-4766 | 0 | left_top_k | 9 | None | None | None | None |

## PLAIN-499

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4095 | 1 | up | 5 | 4 | 1 | 0.455048 | 0.645024 |
| MED-2213 | 1 | down | 4 | 5 | -1 | 0.232153 | 0.610062 |
| MED-1412 | 0 | up | 8 | 7 | 1 | 0.396828 | 0.413783 |
| MED-1475 | 0 | entered_top_k | None | 8 | None | 0.656542 | 0.405382 |
| MED-3033 | 0 | entered_top_k | None | 9 | None | 0.343482 | 0.382064 |
| MED-4893 | 0 | left_top_k | 7 | None | None | None | None |
| MED-5201 | 0 | left_top_k | 9 | None | None | None | None |

## PLAIN-510

No rank movements inside the cutoff.

## PLAIN-520

No rank movements inside the cutoff.

## PLAIN-531

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4531 | 1 | up | 7 | 6 | 1 | 0.899098 | 0.626073 |
| MED-2112 | 0 | up | 5 | 4 | 1 | 0.647263 | 0.637944 |
| MED-1037 | 0 | left_top_k | 10 | None | None | None | None |
| MED-3726 | 0 | entered_top_k | None | 7 | None | 1.0 | 0.579837 |
| MED-3625 | 0 | down | 4 | 5 | -1 | 0.570761 | 0.630029 |
| MED-4128 | 0 | down | 6 | 10 | -4 | 0.0 | 0.466591 |

## PLAIN-541

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1858 | 0 | entered_top_k | None | 6 | None | 0.782846 | 0.439127 |
| MED-1988 | 0 | left_top_k | 10 | None | None | None | None |
| MED-5097 | 0 | down | 6 | 10 | -4 | 0.241586 | 0.404114 |

## PLAIN-551

No rank movements inside the cutoff.

## PLAIN-56

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2420 | 0 | entered_top_k | None | 10 | None | 0.219078 | 0.227978 |
| MED-2572 | 0 | left_top_k | 10 | None | None | None | None |

## PLAIN-561

No rank movements inside the cutoff.

## PLAIN-571

No rank movements inside the cutoff.

## PLAIN-583

No rank movements inside the cutoff.

## PLAIN-593

No rank movements inside the cutoff.

## PLAIN-603

No rank movements inside the cutoff.

## PLAIN-613

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1198 | 1 | entered_top_k | None | 8 | None | 0.681424 | 0.429134 |
| MED-4468 | 0 | up | 4 | 2 | 2 | 1.0 | 0.689674 |
| MED-3215 | 0 | up | 7 | 6 | 1 | 0.391243 | 0.441762 |
| MED-3476 | 0 | left_top_k | 10 | None | None | None | None |
| MED-1846 | 0 | down | 2 | 3 | -1 | 0.288639 | 0.676426 |
| MED-2983 | 0 | down | 3 | 4 | -1 | 0.241216 | 0.545238 |
| MED-4901 | 0 | down | 6 | 7 | -1 | 0.343168 | 0.435911 |
| MED-859 | 0 | down | 8 | 10 | -2 | 0.288892 | 0.416763 |

## PLAIN-623

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-5200 | 0 | up | 8 | 7 | 1 | 0.221752 | 0.488579 |
| MED-5207 | 0 | up | 9 | 8 | 1 | 0.210623 | 0.484704 |
| MED-2459 | 0 | left_top_k | 10 | None | None | None | None |
| MED-825 | 0 | entered_top_k | None | 10 | None | 0.13629 | 0.446547 |
| MED-4347 | 0 | down | 7 | 9 | -2 | 0.066816 | 0.469177 |

## PLAIN-634

No rank movements inside the cutoff.

## PLAIN-645

No rank movements inside the cutoff.

## PLAIN-660

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4991 | 1 | up | 8 | 5 | 3 | 1.0 | 0.585827 |
| MED-2010 | 1 | up | 10 | 8 | 2 | 0.985163 | 0.507234 |
| MED-1880 | 1 | up | 3 | 2 | 1 | 0.661727 | 0.793256 |
| MED-2147 | 1 | up | 7 | 6 | 1 | 0.754788 | 0.567581 |
| MED-3138 | 1 | down | 2 | 3 | -1 | 0.430492 | 0.781456 |
| MED-2140 | 1 | down | 5 | 7 | -2 | 0.313336 | 0.525922 |
| MED-3136 | 1 | down | 6 | 10 | -4 | 0.0 | 0.429092 |

## PLAIN-671

No rank movements inside the cutoff.

## PLAIN-68

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3086 | 1 | down | 8 | 9 | -1 | 0.188677 | 0.195065 |
| MED-4882 | 0 | up | 7 | 5 | 2 | 0.184662 | 0.204901 |
| MED-1610 | 0 | up | 9 | 8 | 1 | 0.19445 | 0.19531 |
| MED-1138 | 0 | down | 6 | 7 | -1 | 0.104886 | 0.201811 |
| MED-2339 | 0 | down | 5 | 6 | -1 | 0.101755 | 0.202382 |

## PLAIN-681

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2381 | 0 | up | 10 | 9 | 1 | 0.256282 | 0.269688 |
| MED-4314 | 0 | up | 8 | 7 | 1 | 0.28988 | 0.329288 |
| MED-4292 | 0 | down | 7 | 8 | -1 | 0.267671 | 0.325702 |
| MED-4707 | 0 | down | 9 | 10 | -1 | 0.0 | 0.219667 |

## PLAIN-691

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-928 | 0 | up | 10 | 6 | 4 | 0.683721 | 0.500964 |
| MED-2607 | 0 | left_top_k | 9 | None | None | None | None |
| MED-5131 | 0 | entered_top_k | None | 8 | None | 0.551558 | 0.44691 |
| MED-2265 | 0 | down | 6 | 7 | -1 | 0.203905 | 0.466754 |
| MED-3209 | 0 | down | 8 | 9 | -1 | 0.313307 | 0.441061 |
| MED-3922 | 0 | down | 7 | 10 | -3 | 0.256026 | 0.437024 |

## PLAIN-701

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3721 | 1 | left_top_k | 10 | None | None | None | None |
| MED-4302 | 0 | up | 5 | 4 | 1 | 0.239497 | 0.407823 |
| MED-5137 | 0 | up | 8 | 7 | 1 | 0.276518 | 0.343698 |
| MED-1637 | 0 | entered_top_k | None | 10 | None | 0.177848 | 0.2999 |
| MED-4331 | 0 | left_top_k | 9 | None | None | None | None |
| MED-4905 | 0 | entered_top_k | None | 9 | None | 0.261063 | 0.302783 |
| MED-2922 | 0 | down | 7 | 8 | -1 | 0.0 | 0.325766 |
| MED-5078 | 0 | down | 4 | 5 | -1 | 0.182136 | 0.405937 |

## PLAIN-711

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2077 | 1 | down | 4 | 5 | -1 | 0.201131 | 0.690913 |
| MED-1192 | 0 | up | 5 | 4 | 1 | 0.573078 | 0.695985 |
| MED-1862 | 0 | up | 10 | 9 | 1 | 0.543463 | 0.6065 |
| MED-2523 | 0 | up | 3 | 2 | 1 | 0.894566 | 0.889846 |
| MED-5295 | 0 | up | 7 | 6 | 1 | 0.503219 | 0.652773 |
| MED-3520 | 0 | entered_top_k | None | 10 | None | 0.560909 | 0.606262 |
| MED-5047 | 0 | left_top_k | 9 | None | None | None | None |
| MED-2522 | 0 | down | 2 | 3 | -1 | 0.781303 | 0.881921 |

## PLAIN-721

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1289 | 1 | up | 7 | 4 | 3 | 0.817013 | 0.749664 |
| MED-1290 | 1 | up | 6 | 3 | 3 | 1.0 | 0.800905 |
| MED-1278 | 1 | up | 3 | 2 | 1 | 0.928912 | 0.85374 |
| MED-1267 | 1 | down | 5 | 6 | -1 | 0.63843 | 0.730963 |
| MED-1282 | 1 | down | 2 | 5 | -3 | 0.254171 | 0.734764 |
| MED-1287 | 1 | down | 4 | 7 | -3 | 0.336937 | 0.701883 |

## PLAIN-731

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1339 | 1 | up | 7 | 6 | 1 | 1.0 | 0.762339 |
| MED-1341 | 1 | up | 9 | 8 | 1 | 0.777361 | 0.628322 |
| MED-1340 | 1 | entered_top_k | None | 9 | None | 0.669614 | 0.575434 |
| MED-3227 | 1 | down | 6 | 7 | -1 | 0.523013 | 0.694082 |
| MED-5243 | 0 | up | 2 | 1 | 1 | 0.934833 | 0.972535 |
| MED-3216 | 0 | left_top_k | 8 | None | None | None | None |
| MED-4226 | 0 | down | 1 | 2 | -1 | 0.692057 | 0.938411 |

## PLAIN-741

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4230 | 1 | entered_top_k | None | 10 | None | 0.334454 | 0.206244 |
| MED-2831 | 0 | left_top_k | 10 | None | None | None | None |

## PLAIN-751

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1748 | 0 | up | 10 | 9 | 1 | 0.227271 | 0.472979 |
| MED-5037 | 0 | up | 7 | 6 | 1 | 0.196069 | 0.503719 |
| MED-3482 | 0 | left_top_k | 9 | None | None | None | None |
| MED-5333 | 0 | entered_top_k | None | 8 | None | 0.455303 | 0.489397 |
| MED-2568 | 0 | down | 6 | 7 | -1 | 0.0 | 0.495885 |
| MED-1101 | 0 | down | 8 | 10 | -2 | 0.0 | 0.462031 |

## PLAIN-761

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3800 | 0 | up | 7 | 2 | 5 | 1.0 | 0.834635 |
| MED-1006 | 0 | up | 8 | 7 | 1 | 0.612134 | 0.748884 |
| MED-2103 | 0 | up | 10 | 9 | 1 | 0.475355 | 0.712843 |
| MED-2417 | 0 | entered_top_k | None | 10 | None | 0.545798 | 0.691814 |
| MED-4050 | 0 | left_top_k | 9 | None | None | None | None |
| MED-3551 | 0 | down | 5 | 6 | -1 | 0.524657 | 0.75276 |
| MED-2424 | 0 | down | 6 | 8 | -2 | 0.457158 | 0.733659 |
| MED-3944 | 0 | down | 2 | 5 | -3 | 0.527553 | 0.786616 |

## PLAIN-771

No rank movements inside the cutoff.

## PLAIN-78

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4482 | 0 | up | 9 | 7 | 2 | 0.445969 | 0.443593 |
| MED-5235 | 0 | up | 10 | 8 | 2 | 0.399992 | 0.431315 |
| MED-1802 | 0 | entered_top_k | None | 9 | None | 0.482516 | 0.425646 |
| MED-2170 | 0 | entered_top_k | None | 10 | None | 0.365214 | 0.419341 |
| MED-5195 | 0 | left_top_k | 7 | None | None | None | None |
| MED-5229 | 0 | left_top_k | 8 | None | None | None | None |

## PLAIN-782

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1055 | 0 | up | 2 | 1 | 1 | 1.0 | 0.8931 |
| MED-2617 | 0 | entered_top_k | None | 10 | None | 0.410724 | 0.395232 |
| MED-3209 | 0 | entered_top_k | None | 9 | None | 0.183731 | 0.397628 |
| MED-3987 | 0 | left_top_k | 9 | None | None | None | None |
| MED-4390 | 0 | left_top_k | 10 | None | None | None | None |
| MED-1248 | 0 | down | 1 | 2 | -1 | 0.440295 | 0.888059 |

## PLAIN-792

No rank movements inside the cutoff.

## PLAIN-806

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2502 | 1 | up | 10 | 8 | 2 | 0.47589 | 0.482885 |
| MED-2138 | 1 | up | 4 | 3 | 1 | 1.0 | 0.773106 |
| MED-2506 | 1 | up | 7 | 6 | 1 | 0.860929 | 0.671249 |
| MED-3273 | 1 | up | 5 | 4 | 1 | 0.925437 | 0.7578 |
| MED-2324 | 1 | entered_top_k | None | 10 | None | 0.347546 | 0.453086 |
| MED-3271 | 1 | down | 6 | 7 | -1 | 0.271627 | 0.603992 |
| MED-3283 | 1 | down | 8 | 9 | -1 | 0.322834 | 0.482569 |
| MED-2325 | 1 | down | 3 | 5 | -2 | 0.339606 | 0.679271 |

## PLAIN-817

No rank movements inside the cutoff.

## PLAIN-827

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-1602 | 1 | up | 7 | 6 | 1 | 0.336937 | 0.313373 |
| MED-4472 | 1 | up | 9 | 8 | 1 | 0.22831 | 0.260504 |
| MED-4492 | 1 | up | 6 | 5 | 1 | 0.462473 | 0.355009 |
| MED-1605 | 1 | entered_top_k | None | 10 | None | 0.198912 | 0.254011 |
| MED-4194 | 1 | left_top_k | 10 | None | None | None | None |
| MED-4451 | 1 | down | 8 | 9 | -1 | 0.211364 | 0.260464 |
| MED-5207 | 0 | down | 5 | 7 | -2 | 0.0 | 0.263172 |

## PLAIN-838

No rank movements inside the cutoff.

## PLAIN-850

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2066 | 1 | up | 4 | 3 | 1 | 1.0 | 0.633658 |
| MED-2075 | 1 | up | 6 | 5 | 1 | 0.902174 | 0.505238 |
| MED-4455 | 1 | up | 2 | 1 | 1 | 0.957033 | 0.951461 |
| MED-2064 | 1 | down | 1 | 2 | -1 | 0.0 | 0.8 |
| MED-2070 | 1 | down | 3 | 4 | -1 | 0.0 | 0.602953 |
| MED-3199 | 0 | down | 5 | 6 | -1 | 0.0 | 0.351559 |

## PLAIN-872

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-3986 | 0 | up | 9 | 7 | 2 | 0.5627 | 0.442223 |
| MED-3991 | 0 | up | 6 | 4 | 2 | 0.818127 | 0.548254 |
| MED-1291 | 0 | up | 2 | 1 | 1 | 1.0 | 0.948525 |
| MED-3712 | 0 | down | 4 | 5 | -1 | 0.539648 | 0.531659 |
| MED-3985 | 0 | down | 5 | 6 | -1 | 0.26347 | 0.449356 |
| MED-4098 | 0 | down | 1 | 2 | -1 | 0.38335 | 0.87667 |
| MED-4916 | 0 | down | 7 | 9 | -2 | 0.251759 | 0.411452 |

## PLAIN-882

No rank movements inside the cutoff.

## PLAIN-892

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2145 | 1 | up | 5 | 3 | 2 | 0.91875 | 0.804827 |
| MED-2008 | 1 | up | 6 | 5 | 1 | 1.0 | 0.789654 |
| MED-2148 | 1 | up | 3 | 2 | 1 | 0.995153 | 0.946205 |
| MED-3132 | 1 | down | 2 | 4 | -2 | 0.0 | 0.793424 |
| MED-4347 | 1 | down | 4 | 6 | -2 | 0.0 | 0.683186 |

## PLAIN-902

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4195 | 1 | up | 2 | 1 | 1 | 1.0 | 0.981262 |
| MED-4197 | 1 | down | 1 | 2 | -1 | 0.0 | 0.8 |
| MED-3555 | 0 | up | 4 | 3 | 1 | 0.722417 | 0.741271 |
| MED-4849 | 0 | down | 3 | 4 | -1 | 0.0 | 0.631688 |

## PLAIN-91

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4593 | 0 | up | 10 | 7 | 3 | 0.987928 | 0.556981 |
| MED-1983 | 0 | up | 9 | 8 | 1 | 0.658576 | 0.528905 |
| MED-1167 | 0 | left_top_k | 8 | None | None | None | None |
| MED-4963 | 0 | entered_top_k | None | 10 | None | 0.916906 | 0.496517 |
| MED-2352 | 0 | down | 7 | 9 | -2 | 0.500465 | 0.526576 |

## PLAIN-913

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-5084 | 1 | down | 9 | 10 | -1 | 0.19398 | 0.125 |
| MED-3810 | 0 | up | 10 | 9 | 1 | 0.223187 | 0.12676 |

## PLAIN-924

No rank movements inside the cutoff.

## PLAIN-934

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2161 | 1 | up | 8 | 5 | 3 | 0.746792 | 0.819558 |
| MED-1621 | 1 | up | 5 | 4 | 1 | 0.77138 | 0.877241 |
| MED-1640 | 1 | up | 7 | 6 | 1 | 0.581693 | 0.812993 |
| MED-2156 | 1 | entered_top_k | None | 10 | None | 0.671061 | 0.744185 |
| MED-2159 | 1 | left_top_k | 9 | None | None | None | None |
| MED-1636 | 1 | down | 6 | 7 | -1 | 0.499472 | 0.806818 |
| MED-1649 | 1 | down | 4 | 8 | -4 | 0.395356 | 0.805378 |
| MED-5249 | 0 | up | 10 | 9 | 1 | 0.772014 | 0.790127 |

## PLAIN-946

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4380 | 1 | down | 4 | 5 | -1 | 0.0 | 0.454422 |
| MED-1570 | 0 | up | 5 | 2 | 3 | 1.0 | 0.576739 |
| MED-855 | 0 | down | 2 | 3 | -1 | 0.0 | 0.534633 |
| MED-866 | 0 | down | 3 | 4 | -1 | 0.0 | 0.51024 |

## PLAIN-956

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-5076 | 1 | up | 8 | 7 | 1 | 0.604913 | 0.491775 |
| MED-1165 | 1 | down | 7 | 8 | -1 | 0.200114 | 0.457265 |
| MED-4471 | 0 | up | 10 | 9 | 1 | 0.417625 | 0.429765 |
| MED-2697 | 0 | entered_top_k | None | 10 | None | 0.601419 | 0.426874 |
| MED-884 | 0 | left_top_k | 9 | None | None | None | None |

## PLAIN-966

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4103 | 1 | down | 9 | 10 | -1 | 0.0 | 0.258446 |
| MED-4192 | 0 | up | 10 | 6 | 4 | 0.436483 | 0.343356 |
| MED-4323 | 0 | up | 4 | 2 | 2 | 0.404958 | 0.468079 |
| MED-1613 | 0 | down | 8 | 9 | -1 | 0.0 | 0.270878 |
| MED-1618 | 0 | down | 6 | 7 | -1 | 0.0 | 0.280394 |
| MED-2039 | 0 | down | 3 | 4 | -1 | 0.0 | 0.450527 |
| MED-3465 | 0 | down | 7 | 8 | -1 | 0.0 | 0.280058 |
| MED-4789 | 0 | down | 2 | 3 | -1 | 0.0 | 0.461456 |

## PLAIN-977

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-4402 | 1 | up | 10 | 8 | 2 | 0.623428 | 0.61666 |
| MED-2770 | 0 | up | 5 | 4 | 1 | 0.715343 | 0.803066 |
| MED-4891 | 0 | up | 3 | 2 | 1 | 0.356248 | 0.811908 |
| MED-1276 | 0 | left_top_k | 8 | None | None | None | None |
| MED-4315 | 0 | left_top_k | 9 | None | None | None | None |
| MED-4427 | 0 | entered_top_k | None | 9 | None | 0.620648 | 0.59254 |
| MED-4462 | 0 | entered_top_k | None | 10 | None | 0.484843 | 0.586988 |
| MED-2162 | 0 | down | 2 | 3 | -1 | 0.270284 | 0.809591 |

## PLAIN-987

| post_id | relevance | direction | baseline rank | compare rank | rank delta | structure score | rerank score |
|---|---:|---|---:|---:|---:|---:|---:|
| MED-2780 | 0 | up | 2 | 1 | 1 | 1.0 | 0.89432 |
| MED-1293 | 0 | down | 1 | 2 | -1 | 0.0 | 0.8 |

## PLAIN-997

No rank movements inside the cutoff.
