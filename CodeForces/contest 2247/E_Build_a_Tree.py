import sys

def solve():
    # Fast I/O: Read all contents from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t = int(input_data[0])
    idx = 1
    
    out = []
    
    for _ in range(t):
        n = int(input_data[idx])
        k = int(input_data[idx+1])
        idx += 2
        
        # Condition 1: k must be an even number
        if k % 2 != 0:
            out.append("-1")
            continue
            
        target = k // 2
        
        # Split nodes into evens and odds (excluding root 1)
        evens = list(range(2, n + 1, 2))
        odds = list(range(3, n + 1, 2))
        
        E = len(evens)
        O = len(odds)
        
        max_e = E * (E + 1) // 2
        max_o = O * (O + 1) // 2
        min_req = E + O
        max_req = max_e + max_o
        
        # Condition 2: Check if target sum is within possible bounds
        if target < min_req or target > max_req:
            out.append("-1")
            continue
            
        # Distribute the required depth sum to even and odd sets
        target_e = min(target - O, max_e)
        target_o = target - target_e
        
        def build_subtree(nodes, T):
            if not nodes: 
                return []
            
            M = len(nodes)
            
            # Find the longest main chain 'C' that doesn't exceed our target T
            C = 1
            while C < M and ((C + 1) * (C + 2) // 2 + M - (C + 1)) <= T:
                C += 1
            
            edges = []
            
            # Construct the main chain
            edges.append(f"1 {nodes[0]}")
            for i in range(1, C):
                edges.append(f"{nodes[i-1]} {nodes[i]}")
                
            # Connect the remainder
            rem = T - (C * (C + 1) // 2 + M - C)
            
            if C < M:
                parent = 1 if rem == 0 else nodes[rem - 1]
                edges.append(f"{parent} {nodes[C]}")
                
                # Connect any leftover nodes to the root (depth 1)
                for i in range(C + 1, M):
                    edges.append(f"1 {nodes[i]}")
                    
            return edges
            
        # Build and combine the edges for this test case
        edges = build_subtree(evens, target_e) + build_subtree(odds, target_o)
        out.append("\n".join(edges))

    # Print all outputs separated by a newline
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()