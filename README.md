# TRIE online

"TRIE online" is a cloud-based TRIE data structure. There are server and CLI component of the system.

### Server
- Python based server using Flask module
- REST endpoints are implemeted for various operations
- Server is deployed on Heroku Cloud Application Platform

**Searching for a keyword on TRIE**
```sh
curl "http://my-trie.herokuapp.com/search/?word=house"
```

**Inserting a keyword onto TRIE**
```sh
curl "http://my-trie.herokuapp.com/insert/?word=house"
```

**Deleting a keyword from TRIE**
```sh
curl "http://my-trie.herokuapp.com/delete/?word=house"
```

**Suggestion from TRIE for a string**
```sh
curl "http://my-trie.herokuapp.com/suggest/?word=ho"
```

### Command line interface
- CLI is written in python
- Converted to executable using pytinstaller
- CLI interacts with REST endpoints using "requests" python module
- search, insert, delete, suggest operations are allowed operations using CLI


**Searching for a keyword on TRIE using CLI**
```sh
my-trie search house
```

**Inserting a keyword onto TRIE using CLI**
```sh
my-trie insert house
```

**Deleting a keyword from TRIE**
```sh
my-trie delete house
```

**Suggestion from TRIE for a string**
```sh
my-trie suggest house
```
