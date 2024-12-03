one, two = map(int, input().split())

three = two - one
MOD = 1000000007

a = [-three, one, two, three, -one, -two]
n = int(input())

mod = n % 6

print(a[mod] % MOD)


