import itertools

def get_annotated_combinations(annotated_pairs):
    all_combinations = {}
    
    # Process inputs so that the pairs act as sets for merging
    processed_pairs = [(set(pair), note) for pair, note in annotated_pairs]
    
    # Generate every possible combination of the pairs
    for r in range(1, len(processed_pairs) + 1):
        for combo in itertools.combinations(processed_pairs, r):
            
            # 1. Merge the elements using union
            merged_items = set().union(*(item_set for item_set, _ in combo))
            sorted_items = tuple(sorted(merged_items))
            
            # 2. Combine the notes from all pairs involved in this combination
            notes_involved = []
            for _, note in combo:
                if note not in notes_involved:  # Avoid repeating duplicate notes
                    notes_involved.append(note)
            combined_note = " + ".join(notes_involved)
            
            # 3. Store the result 
            if sorted_items not in all_combinations:
                all_combinations[sorted_items] = set()
            all_combinations[sorted_items].add(combined_note)
            
    # Format and sort the final output cleanly
    final_results = []
    for items, notes_set in sorted(all_combinations.items(), key=lambda x: (len(x[0]), x[0])):
        for note in sorted(notes_set):
            final_results.append((items, note))
            
    return final_results

# --- Example Usage ---
input_data = [
    (("RR", "BnS"), "Fast Track"),
    (("RR", "EH"), "Heavy Load"),
    (("Sl", "Hat"), "Express Route")
]

results = get_annotated_combinations(input_data)

# Print the results nicely
for items, notes in results:
    print(f"Combination: {items} -> Notes: [{notes}]")
