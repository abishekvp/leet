# ls = [1,2,3,4,5]
# sum_ls = sum(ls)
# for i in range(len(ls)-1, 0, -1):
#     print(sum_ls - ls[i], end=' ')
#     sum_ls -= ls[i]

# ls = [1,2,3,4,5]
# for i in range(len(ls)):
#     val = 0
#     for j in range(i+1):
#         if i != j:
#             val += ls[i]+ls[j]
#     print(val, end=' ')


from openai import OpenAI
client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4o",
    store=True,
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)
