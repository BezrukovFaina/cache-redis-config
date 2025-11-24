# Cache Redis Config
======================
## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Configuration Options](#configuration-options)
4. [Usage Examples](#usage-examples)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction
Cache Redis Config is a software project designed to simplify the configuration of Redis for caching purposes. It provides a straightforward way to manage Redis connections and cache expiration.

## Getting Started
To get started with Cache Redis Config, follow these steps:
1. Install the required dependencies: `npm install`
2. Create a new instance of the CacheRedisConfig class: `const cache = new CacheRedisConfig();`
3. Configure the Redis connection: `cache.configure({ host: 'localhost', port: 6379 });`
4. Set a cache value: `cache.set('key', 'value');`
5. Get a cache value: `cache.get('key');`

## Configuration Options
The following configuration options are available:
* `host`: The hostname or IP address of the Redis server
* `port`: The port number of the Redis server
* `password`: The password for the Redis server
* `tls`: A boolean indicating whether to use TLS encryption

## Usage Examples
```javascript
const CacheRedisConfig = require('./index');

const cache = new CacheRedisConfig();
cache.configure({ host: 'localhost', port: 6379 });

cache.set('key', 'value');
console.log(cache.get('key')); // Output: value

cache.expire('key', 3600); // Set expiration to 1 hour
console.log(cache.ttl('key')); // Output: 3600
```

## Contributing
Contributions are welcome and appreciated. To contribute, please fork the repository and submit a pull request.

## License
Cache Redis Config is licensed under the MIT License. See LICENSE for details.