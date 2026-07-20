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
            combined_note = " .. ".join(notes_involved)
            
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


print("// DIABLERETS 06")
gun_id = [1120206506]
input_data = [
    ((1820235745, 557221067), "PVE AdClear- Subsi+KillTally"),
    ((831391274, 657025441), "PVE StrandUtil- Hatch+Megan"),
    ((831391274, 3108830275), "PVE StrandUtil- Hatch+Unrelent"),
    ((243981275, 657025441), "PVE StrandUtil- AttOrbs+Megan"),
    ((243981275, 3108830275), "PVE StrandUtil- AttOrbs+Unrelent"),
    ((3300816228, 365154968), "PVE ChampKill- AutoLoad+TargLock"),
    ((3300816228, 3201496230), "PVE ChampKill- AutoLoad+Redirect"),
    ((2846385770, 588594999), "PVP AllAround- RangeFind+MovTarg"),
    ((2846385770, 1194056669), "PVP AllAround- RangeFind+ClosingT")
]

results = get_annotated_combinations(input_data)


'''
# Print the results nicely
for items, notes in results:
    #print(f"Combination: {items} -> Notes: [{notes}]")
    #print(f"{items} //{notes} [axeraider15]")
    print(f"dimwishlist:item={gun_id}&perks={items} //{notes} [axeraider15]".replace(")", "").replace("(","").replace(", ",","))
'''
finallist = []

for gid in gun_id:
    # Print the results nicely
    for items, notes in results:
        #print(f"Combination: {items} -> Notes: [{notes}]")
        #print(f"{items} //{notes} [axeraider15]")
        #print(f"dimwishlist:item={gid}&perks={items} //{notes} [axeraider15]".replace(")", "").replace("(","").replace(", ",","))
        finallist.append(f"dimwishlist:item={gid}&perks={items} //{notes} [axeraider15]".replace(")", "").replace("(","").replace(", ",","))

finallist.reverse()
for x in finallist:
    print(x)

input('paused')
