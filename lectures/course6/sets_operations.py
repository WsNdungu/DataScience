# Set opertaions
cookies_jason_ate = set(["chocolate chip", "oatmeal cream", "peanut butter"])
cookies_hugo_ate = set(["chocolate chip", "anzac"])

print(cookies_jason_ate)
print(cookies_hugo_ate)

# .union() method - Returns all unique elements from both sets as new one (or)
hugo_jason_unique = cookies_jason_ate.union(cookies_hugo_ate) 
print(hugo_jason_unique)


# .intrstion() method - Return overlaping elements found on both sets
hugo_and_jason_ate = cookies_jason_ate.intersection(cookies_hugo_ate)
print(hugo_and_jason_ate)

# .difference() method - Identifies data present in the set on which the method was used that is not in the argument (-)

# Find cookies jason ate that hugo didn't
print(cookies_jason_ate.difference(cookies_hugo_ate))

# Find cookies hudo ate that jason didn't
print(cookies_hugo_ate.difference(cookies_jason_ate))
