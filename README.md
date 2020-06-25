# Error-correcting Codes

## 1 Introduction

`hammingGeneratorMatrix(r)` is provided and returns the generator matrix of the (2<sup>`r`</sup> − 1, 2<sup>`r`</sup> − `r` − 1, 3)-Hamming code.

## 2 Functions for Hamming codes

Hamming codes can only encode messages of length `k`, where `k` = 2<sup>`r`</sup> − `r` − 1 for some `r` ≥ 2.

In this assignment, you will have to convert any vector into an encodable message.

This must be done as follows:

- Let __`a`__ be a vector of length `l` ≥ 1.

- Choose `r` ≥ 2 so that `k` − `r` = 2<sup>`r`</sup> − 2`r` − 1 ≥ `l` and is as small as possible, then let `m` = (_m_<sub>1</sub>, ... , _m<sub>k</sub>_) such that:

  - (_m_<sub>1</sub>, ... , _m<sub>r</sub>_) represents `l` in binary,
  - (_m_<sub>_r_+1</sub>, ... , _m<sub>r+l</sub>_) = `a`,
  - (_m_<sub>_r+l_+1</sub>, ... , _m<sub>k</sub>_) = (0, . . . , 0).

### Implement the following functions

1. `message(a)`, where `a` is a vector of any positive length: converts it to a message for a Hamming code.

2. `hammingEncoder(m)`, where `m` is a vector of length 2<sup>`r`</sup> − `r` − 1 for some `r` ≥ 2: encoder for Hamming codes.

3. `hammingDecoder(v)`, where `v` is a vector of length 2<sup>`r`</sup> − 1 for some `r` ≥ 2: decoder for Hamming codes.

4. `messageFromCodeword(c)`, where `c` is a vector of length 2<sup>`r`</sup> − 1 for some `r` ≥ 2: recovering the message from the codeword of a Hamming code.

5. `dataFromMessage(m)`, where `m` is a vector of length 2<sup>`r`</sup> − `r` − 1 for some `r` ≥ 2: recovering the raw data from the message.

## 3 Functions for repetition codes

### Implement the following functions

6. `repetitionEncoder(m,n)`, where `m` is a vector of length 1 and `n` a positive integer: encoder for repetition codes.

7. `repetitionDecoder(v)`, where `v` is a vector of any positive length: decoder for repetition codes.
