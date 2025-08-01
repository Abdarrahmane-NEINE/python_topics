# MongoDB Cheat Sheet

## 1. Introduction: Why, What, When, and How

### Why Use MongoDB?
- **Flexible Schema**: Store data in BSON (binary JSON) documents, allowing each document to have its own structure.
- **Scalability**: Built for horizontal scaling with sharding and replica sets.
- **High Availability**: Replica sets provide redundancy and failover.
- **Agile Development**: Rapid prototyping without rigid schema design.
- **Performance**: Optimized for high read/write throughput.

### What is MongoDB?
- **Document-Oriented Database**: Data is stored as JSON-like documents (BSON) in collections (analogous to tables).
- **NoSQL**: Designed for unstructured or semi-structured data, differing from traditional SQL databases.
- **Rich Query Language**: Supports CRUD operations, aggregation pipelines, and secondary indexes.

### When to Use MongoDB?
- When your application requires a flexible, evolving schema.
- For projects that demand fast iteration or deal with varied data types.
- When you need to scale horizontally (across multiple servers).
- In real-time analytics, content management systems, or IoT applications.

### How to Use MongoDB?
- **Installation & Setup**: Run the `mongod` server and interact via the `mongo` shell or client libraries.
- **CRUD Operations**: Use built-in commands for creating, reading, updating, and deleting documents.
- **Advanced Operations**: Utilize aggregation pipelines, transactions, and indexing strategies.
- **Ecosystem Tools**: Manage deployments with MongoDB Atlas, Compass, and drivers for your programming language.

---

## 2. Beginner Level

### Installation & Setup

#### Starting the Server:
```bash
mongod --dbpath /path/to/data
```

#### Connecting via the Shell:
```bash
mongo
```

### Basic CRUD Operations

#### Create (Insert):
```js
db.users.insertOne({ name: "Alice", age: 30 });
```

#### Read (Find):
```js
db.users.find({ name: "Alice" });
```

#### Update:
```js
db.users.updateOne({ name: "Alice" }, { $set: { age: 31 } });
```

#### Delete:
```js
db.users.deleteOne({ name: "Alice" });
```

### Basic Query Operators
- **Comparison Operators**: `$eq`, `$gt`, `$lt`, etc.

```js
db.users.find({ age: { $gt: 25 } });
```

### Creating Indexes (Basic)

#### Single Field Index:
```js
db.users.createIndex({ name: 1 });
```
Indexes speed up query performance by allowing quick lookups.

### Simple Aggregation Pipeline

#### Aggregation Example:
```js
db.orders.aggregate([
  { $match: { status: "A" } },
  { $group: { _id: "$cust_id", total: { $sum: "$amount" } } }
]);
```
This pipeline filters orders with status "A" and groups them by customer, summing the order amounts.

---

## 3. Intermediate Level

### Advanced Querying

#### Complex Conditions:
```js
db.users.find({
  $or: [
    { age: { $lt: 25 } },
    { age: { $gt: 60 } }
  ]
});
```
Combines conditions using the `$or` operator.

### Enhanced Aggregation Pipelines

#### Joining Collections with `$lookup`:
```js
db.orders.aggregate([
  {
    $lookup: {
      from: "products",
      localField: "product_id",
      foreignField: "_id",
      as: "product_details"
    }
  },
  { $unwind: "$product_details" }
]);
```
The `$lookup` stage performs a left outer join between orders and products.

### Additional Pipeline Stages:
- `$project`: Reshape each document.
- `$sort`: Order the results.
- `$limit`: Limit the number of results.

### Update Operators

#### Increment a Field:
```js
db.users.updateOne({ name: "Bob" }, { $inc: { age: 1 } });
```

#### Modify Arrays:
```js
db.users.updateOne(
  { name: "Charlie" },
  { $push: { hobbies: "reading" } }
);
```

### Data Modeling Considerations
- **Embedding**: Use for closely related data (faster reads, fewer joins).
- **Referencing**: Use when data is large or shared across documents (reduces duplication).

### Indexing Strategies

#### Compound & Text Indexes:
```js
db.posts.createIndex({ title: "text", content: "text" });
```
Text indexes enable full-text search over multiple fields.

### Schema Validation

#### Enforce Document Structure:
```js
db.createCollection("products", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "price"],
      properties: {
        name: { bsonType: "string" },
        price: { bsonType: "number", minimum: 0 }
      }
    }
  }
});
```
Ensures that documents in the products collection meet specific criteria.

---

## 4. Advanced Level

### Performance Tuning & Scaling

#### Sharding (Horizontal Scaling)
```js
sh.enableSharding("myDatabase");
db.myCollection.createIndex({ shardKey: 1 });
sh.shardCollection("myDatabase.myCollection", { shardKey: 1 });
```
Sharding distributes data across multiple servers based on the shard key.

#### Replica Sets (High Availability)
- Configure multiple `mongod` instances.
- Create a replica set configuration.
- Use `rs.initiate()` in the `mongo` shell.

Replica sets provide redundancy and automatic failover.

### Transactions (ACID Compliance)

#### Multi-Document Transactions:
```js
const session = db.getMongo().startSession();
session.startTransaction();
try {
  session.getDatabase("myDatabase").accounts.updateOne(
    { account_id: 1 },
    { $inc: { balance: -100 } }
  );
  session.getDatabase("myDatabase").accounts.updateOne(
    { account_id: 2 },
    { $inc: { balance: 100 } }
  );
  session.commitTransaction();
} catch (e) {
  session.abortTransaction();
}
session.endSession();
```
Transactions ensure atomicity across multiple operations, similar to SQL transactions.

### Backup & Restore

#### Using `mongodump` & `mongorestore`:
```bash
mongodump --db myDatabase --out /backup/dir
mongorestore --db myDatabase /backup/dir/myDatabase
```
Regular backups are essential for data recovery and integrity.

---

## Ecosystem & Tools
- **MongoDB Atlas**: Managed cloud service for MongoDB deployments.
- **MongoDB Compass**: GUI for visualizing data and managing clusters.
- **Driver Libraries**: Official drivers available for Node.js, Python, Java, C#, etc.
- **Monitoring Tools**: Use Ops Manager or Atlas monitoring to track performance and issues.

---

## Final Thoughts
- **Beginners**: Focus on installation, basic CRUD, and simple queries.
- **Intermediate Developers**: Leverage deeper query features, aggregation, and data modeling strategies.
- **Advanced Users**: Dive into performance tuning, sharding, transactions, and real-time data handling.

