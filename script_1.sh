#!/bin/bash
# Shell Scripts Collection

# -------------------------------------------------------
# 1. Sum of Numbers
# -------------------------------------------------------
echo "Enter a number:"
read num
sum=0
for ((i=1; i<=num; i++)); do
  sum=$((sum + i))
done
echo "The sum of numbers from 1 to $num is: $sum"

# -------------------------------------------------------
# 2. Factorial of a Number
# -------------------------------------------------------
echo "Enter a number:"
read num
fact=1
for ((i=1; i<=num; i++)); do
  fact=$((fact * i))
done
echo "Factorial of $num is: $fact"

# -------------------------------------------------------
# 3. Fibonacci Sequence
# -------------------------------------------------------
echo "Enter the number of terms:"
read n
a=0
b=1
echo "Fibonacci series up to $n terms:"
for ((i=0; i<n; i++)); do
  echo -n "$a "
  fn=$((a + b))
  a=$b
  b=$fn
done
echo

# -------------------------------------------------------
# 4. Check if a Number is Prime
# -------------------------------------------------------
echo "Enter a number:"
read num
is_prime=1
for ((i=2; i<=num/2; i++)); do
  if ((num % i == 0)); then
    is_prime=0
    break
  fi
done
if ((is_prime == 1)); then
  echo "$num is a prime number."
else
  echo "$num is not a prime number."
fi

# -------------------------------------------------------
# 5. Reverse a String
# -------------------------------------------------------
echo "Enter a string:"
read str
len=${#str}
rev=""
for ((i=$len-1; i>=0; i--)); do
  rev="$rev${str:$i:1}"
done
echo "Reversed string: $rev"

# -------------------------------------------------------
# 6. Number Guessing Game
# -------------------------------------------------------
target=$(( RANDOM % 100 + 1 ))
guess=0
echo "Guess the number (between 1 and 100):"
while [ $guess -ne $target ]; do
  read guess
  if [ $guess -lt $target ]; then
    echo "Too low!"
  elif [ $guess -gt $target ]; then
    echo "Too high!"
  else
    echo "Congratulations! You've guessed the right number!"
  fi
done

# -------------------------------------------------------
# 7. Find Maximum of Three Numbers
# -------------------------------------------------------
echo "Enter three numbers:"
read a
read b
read c
if [ $a -ge $b ] && [ $a -ge $c ]; then
  max=$a
elif [ $b -ge $a ] && [ $b -ge $c ]; then
  max=$b
else
  max=$c
fi
echo "The maximum number is: $max"
