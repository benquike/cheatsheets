# des related

https://en.wikipedia.org/wiki/DES_supplementary_material

## block cypher features

* Block size
* Key size
* Number of rounds
* Encryption modes

## Feistel Network

## attack

* Exhaustive search
* meet-in-the-middle attack
* Davies Attack
* Differential cryptanalysis
* Linear cryptanalysis
* Differential-linear cryptanalysis

## Differential Cryptanalysis

http://www.cs.technion.ac.il/~biham/Reports/differential-cryptanalysis-of-the-data-encryption-standard-biham-shamir-authors-latex-version.pdf

http://www.merkle.com/papers/Attempt%20to%20Cryptanalyze%20DES%201976-11-10.pdf

http://www.cs.technion.ac.il/~biham/Reports/differential-cryptanalysis-of-the-data-encryption-standard-biham-shamir-authors-latex-version.pdf

https://piazza-resources.s3.amazonaws.com/ixlc30gojpe5fs/iyduia2bc9e7ac/BihamShamir.pdf?AWSAccessKeyId=AKIAIEDNRLJ4AZKBW6HA&Expires=1504813972&Signature=vC5uBDeXqWkKXngI4WyekyW%2FQ7Y%3D

http://www.cs.haifa.ac.il/~orrd/BlockCipherSeminar/Lecture2-Differential.pdf

### difference distribution tables

Difference Distribution Tables of DES

The algo for building this table:

```
InLength; // input length of the S-Box in bits
OutLengh; // output length of the S-Box  in bits
Table[In][Out]; // the table, In is the XOR of the in-going pair, Out is the resulting XOR, the table returns the number of occurences

// Initialize the table:
for(in = 0;in<2^InLength;in++) 
{
  for(out = 0;out<2^OutLength;out++)
  {
    Table[in][out] = 0;
  }
}

// this makes us go through all the possible value of p1
for(p1 = 0;p1<2^InLength;p1++) 
{
  // this makes us go through all the possible value of p2
  for(p2 = 0;p2<2^InLength;p2++)
  {
    XOR_IN = p1 XOR p2;
    XOR_OUT = SBOX(p1) XOR SBOX(p2);
    Table[XOR_IN][XOR_OUT]++;
  }
} 
```

## reference
1. http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
2. https://www.lri.fr/~fmartignon/documenti/systemesecurite/4-DES.pdf
3. https://paginas.fe.up.pt/~ei10109/ca/des.html
4. http://people.scs.carleton.ca/~maheshwa/courses/4109/Seminar11/atttack%20on%20DES.pdf
5. https://lasec.epfl.ch/memo/memo_des.shtml
6. http://cs.ucsb.edu/~koc/ccs130h/notes/dc1.pdf
