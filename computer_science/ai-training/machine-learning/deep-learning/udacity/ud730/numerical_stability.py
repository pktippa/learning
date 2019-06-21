"""
Adding a small value several times to a large value leads to an error.
Adding 10^-6 to 10^9 over 10^6 times and then subtracting 10^9.
Ideally the answer should be 1, but the program gives output as 0.9537
which is large error. Run the same program by replacing 10^9 with 1
The error becomes very tiny.
"""
big_num = 10**9
#big_num = 1
small_num = 10**-6
total_sum = 10**9
#total_sum = 1
for _ in range(10**6):
    total_sum += small_num
total_sum -= big_num
print("total sum ", total_sum)