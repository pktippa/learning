* Arithmetic Operators
* Relational Operators
* Bitwise Operators
* Logical Operators
* Assignment Operators
* Misc Operators

## Arithmetic Operators

Same data type as the variables it operated on.
```
+ Add a + b
- Subtract
* Multiply
/ Division
% Modulus
++ Increment a++
-- Decrement
```

## Relational Operators

Returns a boolean value

```
== Equal to
!= Not Equal to
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to
```

## Bitwise Operators

Bitwise operators which can be applied to the integer types, long, int, short, char, and byte

Assume if a = 60 and b = 13; now in binary format they will be as follows −

a = 0011 1100
b = 0000 1101

a =1

a= -2
0001

1101 1010
 << 2

01 1010 00
Returns same data type
```
& - bitwise and - a&b
| - bitwise or - a|b
^ - bitwise xor - a^b
~ - bitwise compliment - ~a
<< - Left shift - a << 2 -> 11 1100 00
>> - Right shift (sign extension) - a >> 2 -> 00 0011 11
>>> - zero fill right shift - a >>> 2 -> 00 0011 11

For difference between >> and >>>, see -2 >> 1, -2 >>> 1
```

```java
int a = -2;
		int b = 2;
		
		System.out.println(Integer.toBinaryString(-2));
		// Signed
		System.out.println(Integer.toBinaryString(a >> 2));
		// zero filled
		System.out.println(Integer.toBinaryString(a >>> 2));
		
		System.out.println(Integer.toBinaryString(b));
		System.out.println(Integer.toBinaryString(b >> 1));
		System.out.println(Integer.toBinaryString(b >>> 1));
```

## Logical Operators

Assume Boolean variables A holds true and variable B holds false

```
&& - (A && B) - false
|| - (A || B) - false
! - (!B) - true
```

## Assignment operators

```
=
+=
-=
*=
%=
/=
&=
|=
^=
>>=
<<=
```

byte a = 5;
a += 2; // a = a + 2;
// value of a ? = 7

// a ?
a -= 4;
// value of a 3

a >>= 2;
// a = a >> 2;

## Misc Operators

Conditional Operator ( ? : )

```
variable x = (expression) ? value if true : value if false
```

instanceof Operator (Need to understand classes)

```
( Object reference variable ) instanceof  (class/interface type)
```

## Operator Precedence

Read by own.