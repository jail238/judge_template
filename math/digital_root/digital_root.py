def digital_root_sum(n, base=10):
    if n == 0: return 0
    cycle = base*(base-1)//2
    complete = n//(base-1)
    remains = n%(base-1)
    return complete*cycle+((remains)*(remains+1)//2)
