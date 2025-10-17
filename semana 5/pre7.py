A = input()
B = input()
N = A[0:5]+B[0]
Pin = len(A)*1000+len(B)
P = Pin % 10000
print(f"Nick: {N.lower()}")
print(f"Pin: {P}")
print(f"ID: C3-{N.lower()}-{P}")