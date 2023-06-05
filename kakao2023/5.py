def solution(commands):
    
    # (r,c) -> (r-1,c-1)
    # 1. UPDATE r c v1
    #       (r,c) = v1
    # 2. UPDATE v1 v2
    #       all (i,j) with v1 = v2
    # 3. MERGE r1 c1 r2 c2
    #       (r1,c1) (r2,c2) connect
    #       take available value, (r1,c1) prioritized
    # 4. UNMERGE r c
    #       all value = 0
    #       except (r,c)
    # 5. PRINT r c
    
    from collections import defaultdict
    
    answer = []
    
    group = {}                # (i,j) -> gid
    g2v = {}                  # gid   -> v
    g2coor = defaultdict(set) # gid   -> set((i,j), ..)
    v2g = defaultdict(set)    # v     -> set(gid, ..)
    
    gid_c = 1 # gid_counter
    for cmd_ in commands:
        cmd = cmd_.split()
        
        # 1
        if cmd[0] == "UPDATE" and len(cmd) == 4:
            _,r,c,v = cmd
            gid = group.get((r,c))
            if gid:
                old_v = g2v.get(gid)
                if old_v == v:
                    continue
                if old_v: # value was assigned
                    g2v[gid] = v
                    v2g[old_v].discard(gid)
                    v2g[v].add(gid)
                else: # value was NOT assigned
                    g2v[gid] = v
                    v2g[v].add(gid)
            else:
                group[(r,c)] = gid_c
                g2coor[gid_c].add((r,c))
                g2v[gid_c] = v
                v2g[v].add(gid_c)
                
                gid_c += 1
        
        # 2
        elif cmd[0] == "UPDATE" and len(cmd) == 3:
            _,v1,v2 = cmd
            if v1 == v2:
                continue
            gid1s = v2g.get(v1)
            if gid1s:
                for gid in gid1s:
                    g2v[gid] = v2
                    v2g[v2].add(gid)
                v2g[v1] = set() # shold be right ..?
            else:
                pass
            
        # 3
        elif cmd[0] == "MERGE" and len(cmd) == 5:
            _,r1,c1,r2,c2 = cmd
            gid1 = group.get((r1,c1), None)
            gid2 = group.get((r2,c2), None)
            if gid1 and gid2 and gid1 == gid2: # has group, same group
                pass
            elif gid1 and gid2 and gid1 != gid2: # has group, diff group
                v1 = g2v.get(gid1)
                v2 = g2v.get(gid2)
                
                if not v1 and not v2:
                    for coor2 in g2coor[gid2]:
                        group[coor2] = gid1
                        g2coor[gid1].add(coor2)
                    g2coor.pop(gid2)
                elif v1 and not v2:
                    for coor2 in g2coor[gid2]:
                        group[coor2] = gid1
                        g2coor[gid1].add(coor2)
                    g2coor.pop(gid2)
                elif not v1 and v2:
                    for coor1 in g2coor[gid1]:
                        group[coor1] = gid2
                        g2coor[gid2].add(coor1)
                    g2coor.pop(gid1)
                else: # v1 and v2
                    for coor2 in g2coor[gid2]:
                        group[coor2] = gid1
                        g2coor[gid1].add(coor2)
                    g2coor.pop(gid2)
                    g2v.pop(gid2)
                    v2g[v2].discard(gid2)
                    
            elif gid1 and not gid2:            # only gid1 
                group[(r2,c2)] = gid1
                # g2v
                g2coor[gid1].add((r2,c2))
                # v2g
    
            elif not gid1 and gid2:            # only gid2
                group[(r1,c1)] = gid2
                # g2v
                g2coor[gid2].add((r1,c1))
                # v2g
            else:                              # both no group
                group[(r1,c1)] = gid_c
                group[(r2,c2)] = gid_c
                g2coor[gid_c].add((r1,c1))
                g2coor[gid_c].add((r2,c2))
                gid_c += 1
            
        
        # 4
        elif cmd[0] == "UNMERGE":
            _,r,c = cmd
            gid = group.get((r,c), None)
            if not gid: continue
            # value = g2v.get(gid, None)
            for coor in g2coor[gid]:
                if coor == (r,c): continue
                group.pop(coor)
            g2coor[gid] = set([(r,c)])
            
        
        # 5
        elif cmd[0] == "PRINT":
            _,r,c = cmd
            gid = group.get((r,c), None)
            if not gid:
                answer.append("EMPTY")
                continue
            value = g2v.get(gid, None)
            if not value:
                answer.append("EMPTY")
                continue
            answer.append(value)
        
        # wrong
        else:
            print('wrong')
            exit(0)
    
    # print('group', group)
    # print('g2coor', g2coor)
    # print('g2v', g2v)
    # print('v2g', v2g)
    return answer

# print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
# print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))

print(solution([
    "UPDATE 1 1 menu", "MERGE 1 1 1 2", 
    "MERGE 1 1 1 3", "MERGE 1 1 1 4", 
    "UNMERGE 1 2",
    "MERGE 1 2 1 3", "UPDATE 1 1 hansik", 
    "PRINT 1 1", "PRINT 1 2", 
    "PRINT 1 3", "PRINT 1 4"
    ]))
# print(solution(["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4", "MERGE 1 1 4 4", "UNMERGE 3 3", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]))