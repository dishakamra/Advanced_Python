profile = {"name": "Disha", "skills": ["AWS", "Python"]}
profile["city"] = "Seattle"

# Safe lookup with default (does not insert into dict)
city = profile.get("city", "Unknown")

# setdefault for grouping: create a list at a new key, then append
by_len = {}
for word in ["aws","bedrock","lambda","ec2"]:
    by_len.setdefault(len(word), []).append(word)
print(by_len)


# iterating keys/items
for k, v in profile.items():
    print(k, v)