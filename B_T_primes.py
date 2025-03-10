n = int(input())
arr = list(map(int, input().split(" ")))

def prime_sieve(n):
   is_prime: list[bool] = [True for _ in range(n + 1)]
   is_prime[0] = is_prime[1] = False

   i = 2
   while i * i <= n:
       if is_prime[i]:
           j = i * i
           while j <= n:
               is_prime[j] = False
               j += i
       i += 1

   return is_prime
for ind in range(n):
    print(prime_sieve(arr[ind]))