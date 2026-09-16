# 1. Our starting data (a mixed list of system names)
devices = ["web-prod-01", "db-prod-01", "web-stage-02", "firewall-01", "db-stage-02"]

# Pattern A: Filtering with a "List Comprehension"
# This instantly extracts only the production servers
prod_only = [item for item in devices if "prod" in item]
print(f"Production: {prod_only}")

# Pattern B: Slicing (Extracting parts of a list)
# [start:stop] -> Get the first two items
first_two = devices[0:2]
print(f"First Two: {first_two}")

# Pattern C: Sorting seamlessly
devices.sort()
print(f"Alphabetical: {devices}")
