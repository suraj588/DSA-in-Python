# Computing GCD (Greatest Common Divisor)


<br />

#### `gcd(m, n)` = Largest number dividing both `m` and `n`


<br />

### Method-1 : [Naive method](https://github.com/suraj588/DSA-in-Python/blob/add-readme-for-gcd/GCD/1.py)

- List out factors of `m`
- List out factors of `n`
- Find out a list of common factors, `cf` from the above two lists
- Get the largest number from `cf`


<br/>

### Method-2 : [Optimised naive method](https://github.com/suraj588/DSA-in-Python/blob/add-readme-for-gcd/GCD/2.py)



### Method-3 : [Further optimised naive method](https://github.com/suraj588/DSA-in-Python/blob/add-readme-for-gcd/GCD/3.py)

#### From careful observation, it is evident that, gcd of two numbers can never be greater than the minimum of the two. Hence method 2 and 3 loops only till `min(m, n)`.


<br />

### Method-4 : [Eucledian's Difference Algorithm (Using recursion)](https://github.com/suraj588/DSA-in-Python/blob/add-readme-for-gcd/GCD/4.py)  



Let `d` divides both `m` and `n`,  
then, we can write, `m / d = a` and `n / d = b` => `m = ad` and `n = bd`.  

Considering `m > n`, `m - n = (a - b)d` => which signifies that `d` also divides `m - n`.  

Thus, this can be computed as : `gcd(m, n) = gcd(m, m - n) = gcd(n, m - n)`. In the program, `gcd(m, n) = gcd(n, m - n)` has been used.

### Method-5 : [Eucledian's Difference Algorithm (Without recursion)](https://github.com/suraj588/DSA-in-Python/blob/add-readme-for-gcd/GCD/5.py)


<br />

### Method-6 : [Eucledian's Remainder Algorithm (Without recursion)](https://github.com/suraj588/DSA-in-Python/blob/add-readme-for-gcd/GCD/6.py)


Let `d` divides both `m` and `n`,  
then, we can write, `m / d = a` and `n / d = b` => `m = ad` and `n = bd`.  

Suppose, `m % n != 0`. Therefore, `m = qn + r`; where `q` -> quotient and `r` -> remainder  
=> `ad = (qb)d + r`.  

Since, the left side is divisible by `d`, hence the individual items on the right side is also divisible by `d`.  
Hence, `m % n = r = cd`; where c -> constant.  

#### So, if `m` and `n` are divisible by `d`, then `m % n` is also divisible by `d`.

This can be written as : `gcd(m, n) = gcd(n, r)`


<br />

### Analysis : 

#### Consider the numbers to be in the order of 10^9. For the worst case scenarios :

- Method-1 :
3 loops, iterating in the order of 10^9. 🥵

- Method-2 and Method-3 : 
1 loop, iterating in the order of 10^9. 😳
