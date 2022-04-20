Select U.name, Sum(T.amount) as balance
From Users as U
Inner Join Transactions as T
On U.account = T.account
Group By T.account
Having Sum(T.amount) >= 10000;