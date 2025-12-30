# Cache Redis Config

This is a simple configuration module for Redis cache in a Node.js application.

## Installation

```bash
npm install cache-redis-config
```

## Usage

```javascript
const config = require('cache-redis-config');

// Create a new Redis client with default options
const client = config.createClient();

// Or create a new Redis client with custom options
const client = config.createClient({
  host: 'localhost',
  port: 6379,
  password: 'your-password',
});
```

## Options

The following options can be used when creating a new Redis client:

* `host`: The Redis server host (default: `localhost`)
* `port`: The Redis server port (default: 6379)
* `password`: The Redis server password (default: `null`)
* `database`: The Redis database number (default: 0)
* `timeout`: The Redis client timeout in milliseconds (default: 10000)

## API

### createClient(options)

Create a new Redis client with the given options.

```javascript
const client = config.createClient(options);
```

### getOptions()

Get the default options used by the `createClient` method.

```javascript
const options = config.getOptions();
```