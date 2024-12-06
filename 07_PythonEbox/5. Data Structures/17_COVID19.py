# Step 1: Read input for patients in each center
C1 = set(input("Enter C1 patients list\n").split())
C2 = set(input("Enter C2 patients list\n").split())
C3 = set(input("Enter C3 patients list\n").split())

# Step 2: Patients in multiple centers (patients in at least two centers)
multiple_centers = (C1 & C2) | (C1 & C3) | (C2 & C3)

# Step 3: Patients in only one center (symmetric difference of the sets)
only_one_center = (C1 - C2 - C3) | (C2 - C1 - C3) | (C3 - C1 - C2)

# Step 4: Patients in exactly two centers (patients in exactly two sets)
two_centers = (C1 & C2) - C3 | (C1 & C3) - C2 | (C2 & C3) - C1

# Step 5: Identify which center has more patients
max_center = max(len(C1), len(C2), len(C3))
if max_center == len(C1):
    more_patients_center = "Center 1"
elif max_center == len(C2):
    more_patients_center = "Center 2"
else:
    more_patients_center = "Center 3"

# Step 6: Print the results in the required format
print("Patients name in multiple centers:")
print(sorted(multiple_centers))

print("Patients name in only one center:")
print(sorted(only_one_center))

print("Patients name in any two center:")
print(sorted(two_centers))

print(f"More patients in : {more_patients_center}")