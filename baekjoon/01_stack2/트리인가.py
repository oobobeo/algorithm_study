# 6416
# input -> sys.stdin.readline().strip()

import sys

# for each Cases
all_cases_done_flag = 0
cases = {} # {1: Bool}
counter = 0
while True:
    counter += 1
    # line = sys.stdin.readline().strip()

    # for a Case:
    case_end_flag = 0
    out_in = {} # {out: [in's], .. }
    in_out = {}
    while True:
        line = sys.stdin.readline().strip()
        if line == "-1 -1":  # Cases done
            all_cases_done_flag = 1
            # print("DOOOONE")
            break
        if line == "": # newline
            continue
        # print(f"line: {line}")
        numbers = line.split('  ') # ['n n','n n' ..]
        numbers.reverse()
        # print(f"1: {numbers}")
        while numbers:
            # print(f"numbers: {numbers}")
            nums = numbers.pop()
            a,b = nums.split()
            # print(a,b)
            if a == '0' and b == '0': # Case done
                case_end_flag = 1
                break

            # update out_in, in_out
            if a not in out_in.keys():
                out_in[a] = []
            if b not in out_in.keys():
                out_in[b] = []
            if a not in in_out.keys():
                in_out[a] = []
            if b not in in_out.keys():
                in_out[b] = []
            out_in[b].append(a)
            in_out[a].append(b)

            if not numbers:
                break
        if case_end_flag:
            break
    if all_cases_done_flag:
        break

    # check validity
    # no node is a tree LIKE WHAT?
    if len(out_in.items()) == 0:
        cases[counter] = 1
        continue


    not_tree_flag = 0
    if case_end_flag == 1:
        # print(out_in)
        root = []
        for k,v in out_in.items():
            if len(v) >= 2: # 2+ routes
                not_tree_flag = 1
                break
            if len(v) == 0: # root candidate
                root.append(k)
        if len(root) != 1: # 1 root should exist
            not_tree_flag = 1

    # check flow
    # there could be unreachable nodes
    if not not_tree_flag:
        new_nodes = [root[0]]
        reachable_nodes = []
        for _ in range(len(in_out.keys())):
            # print(new_nodes)
            new_nodes_count = len(new_nodes)
            if len(new_nodes) == 0: # all reachable nodes reached
                break
            reachable_nodes += new_nodes
            new_nodes = []
            for i in range(new_nodes_count):
                new_nodes += in_out[reachable_nodes[-(i+1)]]
        if len(reachable_nodes) != len(out_in.keys()):
            # print(f"AA {reachable_nodes}, {out_in.keys()}")
            not_tree_flag = 1
        
    
    # store validity
    cases[counter] = not not_tree_flag



for k,v in cases.items():
    if v:
        string = "is a tree."
    else:
        string = "is not a tree."
    print(f"Case {k} {string}")


