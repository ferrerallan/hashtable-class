

# Hash Table Implementations: Collision Handling and General Use

## Description

This repository contains two implementations of a hash table in Python:

1. **`hash_colision.py`**:
   - Demonstrates intentional hash collisions by overriding the hash function to always return the same index.
   - This implementation is useful for understanding hash collisions and their effects on hash table functionality.

2. **`hashtable.py`**:
   - Implements a general-purpose hash table with a basic hashing function.
   - Demonstrates how to store, retrieve, and delete key-value pairs efficiently.

## Requirements

- Python 3.7 or higher

## Mode of Use

### 1. Collision Simulation (`hash_colision.py`)

#### Steps:
1. Run the script directly to observe the behavior when multiple keys are assigned to the same hash index.
2. The `_hash` function is overridden to always return `1`, causing collisions for every key.

#### Example:
```python
ht = HashTable()
ht.insert("rm", "real madrid")
ht.insert("barca", "barcelona")

print(ht.get("rm"))     # Outputs: "barcelona" due to collision
print(ht.get("barca"))  # Outputs: "barcelona"
```

#### Run:
```bash
python hash_colision.py
```

#### Expected Output:
```
barcelona
barcelona
```

### 2. General Hash Table (`hashtable.py`)

#### Steps:
1. Run the script to observe basic hash table functionality.
2. The `_hash` function generates a hash index using Python's built-in `hash` function modulo the table size.

#### Example:
```python
ht = HashTable()
ht.insert("rm", "real madrid")
print(ht.get("rm"))  # Outputs: "real madrid"
```

#### Run:
```bash
python hashtable.py
```

#### Expected Output:
```
real madrid
```

## Key Features

### `hash_colision.py`
- Simulates hash collisions intentionally by forcing all keys to map to the same index.
- Demonstrates how collisions can overwrite stored values.
- Educational use case for understanding the importance of collision resolution.

### `hashtable.py`
- Implements a scalable and general-purpose hash table.
- Efficient storage and retrieval of key-value pairs.
- Uses Python's built-in `hash` function for a simple and effective hashing mechanism.

## License

This project is provided as-is, and no specific licensing applies. Feel free to use and adapt it for learning or production purposes.
