def minimize_range_sum(arr, L, R):
    # Split the array into three segments
    A = arr[:L]
    B = arr[L:R+1]
    C = arr[R+1:]
    
    # Sort B descending to find the largest elements that we want to replace
    B_sorted_desc = sorted([(val, i) for i, val in enumerate(B)], key=lambda x: x[0], reverse=True)
    
    # -------------------------------------------------------------
    # Strategy 1: Swap with elements from the Left (Segment A)
    # -------------------------------------------------------------
    A_sorted = sorted([(val, i) for i, val in enumerate(A)], key=lambda x: x[0])
    
    k1 = 0
    while k1 < len(A_sorted) and k1 < len(B_sorted_desc) and A_sorted[k1][0] < B_sorted_desc[k1][0]:
        k1 += 1
        
    B_final_1 = list(B)
    if k1 > 0:
        chosen_A_idx = sorted([item[1] for item in A_sorted[:k1]])
        chosen_B_idx = sorted([item[1] for item in B_sorted_desc[:k1]])
        # Elements from A map to B's chosen indices in reverse order
        for i in range(k1):
            B_final_1[chosen_B_idx[i]] = A[chosen_A_idx[k1 - 1 - i]]
            
    sum_1 = sum(B_final_1)
    
    # -------------------------------------------------------------
    # Strategy 2: Swap with elements from the Right (Segment C)
    # -------------------------------------------------------------
    C_sorted = sorted([(val, i) for i, val in enumerate(C)], key=lambda x: x[0])
    
    k2 = 0
    while k2 < len(C_sorted) and k2 < len(B_sorted_desc) and C_sorted[k2][0] < B_sorted_desc[k2][0]:
        k2 += 1
        
    B_final_2 = list(B)
    if k2 > 0:
        chosen_B_idx = sorted([item[1] for item in B_sorted_desc[:k2]])
        chosen_C_idx = sorted([item[1] for item in C_sorted[:k2]])
        # Elements from C map to B's chosen indices in reverse order
        for i in range(k2):
            B_final_2[chosen_B_idx[i]] = C[chosen_C_idx[k2 - 1 - i]]
            
    sum_2 = sum(B_final_2)
    
    # -------------------------------------------------------------
    # Compare both strategies and return the best outcome
    # -------------------------------------------------------------
    if sum_1 <= sum_2:
        return sum_1, B_final_1
    else:
        return sum_2, B_final_2

# --- Example Execution ---
# Array: [4, 2, 9, 7, 8, 1, 3]
# Target Range indices: 2 to 4 (which holds [9, 7, 8])
array = [4, 2, 9, 7, 8, 1, 3]
L, R = 2, 4

min_sum, edited_segment = minimize_range_sum(array, L, R)

print(f"Minimum Sum: {min_sum}")
print(f"Final Edited Segment: {edited_segment}")