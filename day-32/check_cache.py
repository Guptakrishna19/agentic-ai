import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

print("Connected:", r.ping())

print("\nKeys:")
print(r.keys("*"))

print("\nCached Value:")
print(r.get("news:artificial intelligence"))

print("\nTTL:")
print(r.ttl("news:artificial intelligence"))