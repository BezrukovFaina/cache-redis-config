# cache-redis-config
======================

## Description
---------------

cache-redis-config is a configurable Redis cache library designed to provide a simple and efficient way to integrate Redis into your application. This library allows you to easily manage Redis connections, set cache timeouts, and store cache data with a robust set of features.

## Features
------------

*   **Configurable Redis Connections**: Easily connect to multiple Redis servers with customizable connection settings.
*   **Cache Timeouts**: Set cache timeouts to ensure data is updated at regular intervals.
*   **Cache Data Storage**: Store and retrieve cache data with support for various data types (strings, hashes, lists, sets, maps).
*   **Cache Eviction**: Automatically remove expired cache data to prevent memory leaks.
*   **Multi-Environment Support**: Seamlessly switch between development, testing, and production environments using environment-specific configurations.

## Technologies Used
--------------------

*   **Redis**: A popular in-memory data store for fast and efficient caching.
*   **Node.js**: A JavaScript runtime built on Chrome's V8 JavaScript engine for efficient server-side development.
*   **TypeScript**: A statically typed superset of JavaScript for building robust and maintainable codebases.

## Installation
---------------

To install cache-redis-config, run the following command in your terminal:

```bash
npm install cache-redis-config
```

## Usage
---------

### Importing the Library

```typescript
import { RedisCache } from 'cache-redis-config';
```

### Creating a Redis Cache Instance

```typescript
const redisCache = new RedisCache({
    host: 'localhost',
    port: 6379,
    db: 0,
    password: 'your_redis_password',
    maxAttempts: 3,
    timeout: 10000,
});
```

### Setting Cache Data

```typescript
redisCache.set('my_key', 'Hello, World!', 60);
```

### Retrieving Cache Data

```typescript
const cachedValue = await redisCache.get('my_key');
console.log(cachedValue); // Output: Hello, World!
```

### Checking Cache Expiration

```typescript
const isExpired = await redisCache.isExpired('my_key');
console.log(isExpired); // Output: false
```

## Contributing
--------------

We welcome contributions from the community! If you'd like to contribute to cache-redis-config, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Commit your changes with a clear and descriptive commit message.
4.  Push your branch to the repository.
5.  Open a pull request to the main branch.

## License
----------

cache-redis-config is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Code of Conduct
-------------------

cache-redis-config follows the [Contributor Covenant](https://www.contributor-covenant.org/) Code of Conduct. By participating in this project, you agree to abide by these guidelines.

## Support
----------

If you have any questions or need help with cache-redis-config, please don't hesitate to reach out to us at [support@cache-redis-config.com](mailto:support@cache-redis-config.com).