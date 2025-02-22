def solve(n, start, finish, cost):
    # Write your code here

    start_ind = start - 1
    end_ind = finish - 1
    if start_ind > end_ind:
        end_ind, start_ind = start_ind, end_ind

    return min(sum(cost[start_ind:end_ind]), sum(cost[end_ind:] + cost[:start_ind]))
