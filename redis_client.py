# your_app/redis_client.py
import redis
from django.conf import settings

redis_client = redis.Redis(
    host='comic-alien-13646.upstash.io',
    port=6379,
    password='ATVOAAIjcDFmNjJhYjI0N2I4Nzg0ZjM4OGU1MmNjYzRkY2YzNjVkMnAxMA',
    ssl=True,
    decode_responses=True  # Optional: returns strings instead of bytes
)

# Function to cache data retrieval operations
def cache_data(key_prefix, timeout=3600):
    """
    Decorator to cache the results of data retrieval functions.
    
    Args:
        key_prefix (str): Prefix for the cache key
        timeout (int): Cache expiration time in seconds (default: 1 hour)
    
    Usage:
        @cache_data('user_profile')
        def get_user_profile(user_id):
            # Function implementation
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Create a unique cache key based on function name, args and kwargs
            key_parts = [key_prefix, func.__name__]
            for arg in args:
                key_parts.append(str(arg))
            for k, v in sorted(kwargs.items()):
                key_parts.append(f"{k}:{v}")
            
            cache_key = ":".join(key_parts)
            
            # Try to get cached result
            cached_result = cache_get(cache_key)
            if cached_result:
                return cached_result
            
            # If not cached, execute the function
            result = func(*args, **kwargs)
            
            # Cache the result
            cache_set(cache_key, result, timeout)
            
            return result
        return wrapper
    return decorator

def cache_get(key, default=None):
    """
    Get a value from the Redis cache.
    Returns default if the key doesn't exist.
    """
    value = redis_client.get(key)
    return value if value is not None else default

def cache_set(key, value, timeout=None):
    """
    Set a value in the Redis cache with an optional timeout in seconds.
    If timeout is None, the value will not expire.
    """
    return redis_client.set(key, value, ex=timeout)

def cache_delete(key):
    """
    Delete a key from the Redis cache.
    Returns True if the key was deleted, False otherwise.
    """
    return redis_client.delete(key) > 0

def cache_clear():
    """
    Clear all keys in the Redis cache.
    Use with caution!
    """
    return redis_client.flushdb()