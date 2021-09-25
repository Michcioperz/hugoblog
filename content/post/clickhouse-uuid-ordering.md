---
title: "Falsehoods programmers believe about UUID ordering in ClickHouse"
date: 2021-09-25T17:21:00+0200
containsCode: true
---

This is another one of those posts where I accept that things just are the way they are, but write down things for others, so that the Google query "clickhouse uuid ordering" or "clickhouse uuid sorting" isn't completely devoid of relevant results.

Recently I got to tinker with a ClickHouse database. I'm still new to it, but I guess you can tell it's a good database cause the client prompt is a `:)` smiley.

I'm pretty sure we can all also agree that UUIDs are pretty cool, and much cooler than incrementing IDs.

### So, anyway,

Did you know that **ClickHouse's ordering of UUIDs is not lexicographic**?

A quick hopefully reproducible example:

```sql
CREATE TABLE uuids (uuid UUID) ENGINE = MergeTree() ORDER BY uuid;
INSERT INTO uuids SELECT generateUUIDv4();
INSERT INTO uuids SELECT generateUUIDv4();
INSERT INTO uuids SELECT generateUUIDv4();
INSERT INTO uuids SELECT generateUUIDv4();
INSERT INTO uuids SELECT generateUUIDv4();
INSERT INTO uuids SELECT generateUUIDv4();
INSERT INTO uuids SELECT generateUUIDv4();
INSERT INTO uuids SELECT generateUUIDv4();
INSERT INTO uuids SELECT generateUUIDv4();
INSERT INTO uuids SELECT generateUUIDv4();
INSERT INTO uuids SELECT generateUUIDv4();
INSERT INTO uuids SELECT generateUUIDv4();
INSERT INTO uuids SELECT generateUUIDv4();
INSERT INTO uuids SELECT generateUUIDv4();
INSERT INTO uuids SELECT generateUUIDv4();
```

This should be enough to get us some data to look at. Now, because of how we created the table, the data is already ordered by the `uuid` column, but let's still make sure:

```sql
SELECT * FROM uuids ORDER BY uuid;
```

And the result I get is:

```
2b01a395-d282-4647-89d9-c27555e0c8b5
811ba197-f29c-4d8b-8a74-3c2e7ee5fdcf
0acc6e01-4830-4763-8da7-78a18114d728
3d73ae42-c32f-4ccf-90d1-65853387e166
66fe2326-d376-414b-91d5-a271eaa460e6
81da6af2-3f52-4e80-9508-05653f689ec4
3506b5a0-b7e9-4b45-9556-1dfaba8612ce
74139452-3074-4fa2-98ee-52b18d1b6e94
890992ca-72b6-4a72-a131-b25c432c5009
c0f17764-c675-40af-ab03-ce7b13e253e4
3ee8fcbc-e062-4cf3-af0a-1c64910ff7c5
638117ba-6686-4ff3-b549-552735bc5939
545dc444-2fe7-4a0e-b976-62bc8a9ef0a8
429698d8-7145-45a3-bb57-96370ad5397a
c108587f-45e3-446c-be6d-c2c09462dead
```

Not particularly sorted to the human eye, is it? What we expected is probably more like this:

```sql
SELECT * FROM uuids ORDER BY toString(uuid);
```

```
0acc6e01-4830-4763-8da7-78a18114d728
2b01a395-d282-4647-89d9-c27555e0c8b5
3506b5a0-b7e9-4b45-9556-1dfaba8612ce
3d73ae42-c32f-4ccf-90d1-65853387e166
3ee8fcbc-e062-4cf3-af0a-1c64910ff7c5
429698d8-7145-45a3-bb57-96370ad5397a
545dc444-2fe7-4a0e-b976-62bc8a9ef0a8
638117ba-6686-4ff3-b549-552735bc5939
66fe2326-d376-414b-91d5-a271eaa460e6
74139452-3074-4fa2-98ee-52b18d1b6e94
811ba197-f29c-4d8b-8a74-3c2e7ee5fdcf
81da6af2-3f52-4e80-9508-05653f689ec4
890992ca-72b6-4a72-a131-b25c432c5009
c0f17764-c675-40af-ab03-ce7b13e253e4
c108587f-45e3-446c-be6d-c2c09462dead
```

But it's different! Hopefully this will never be useful to you, but if you or someone you know writes code where the ordering of UUIDs matters (this also applies to aggregate functions like min and max), you have to pay special attention to it unfortunately.

### Frequently screamed questions

#### What the hell? Is the ordering here stable? How are they ordered anyway?

Yeah, actually, if you look closely at the first result list, you should be able to spot the pattern. Which is, that you can split the digits of the UUID into two groups AAAAAAAA-AAAA-AAAA-BBBB-BBBBBBBBBBBB and then the data is ordered lexicographically by (B, A) tuple.

And I guess it makes sense to some extent. The UUID type in ClickHouse is [typedef'd to a 128-bit unsigned integer](https://github.com/ClickHouse/ClickHouse/blob/066d02dd2fdcd82bfd1b3e78d1ecfd9bfdd5e7d8/src/Core/Types.h#L73). Most of the machines people run ClickHouse on are 64-bit, and I imagine there are some shenaningans in the part that converts between the string representation and the integer value that cause the two halves of the number to be swapped.

#### How can this hurt me? How did you discover this?

I was looking into a bug where the affected feature paginated through a query. It would fetch certain items ordered by a (timestamp, uuid) tuple in batches of 10 at a time, and then get another batch by filtering items which were larger in ordering. This will work fine if you use the same ordering in both ORDER BY and WHERE parts of your solution.

In the affected application, stringified ordering was used. However, a query optimizer in the application saw `WHERE toString(uuid) < 'previous-best-uuid'`, and decided that stringification was unnecessary. It didn't touch the ORDER BY clause though. This caused the database to incorrectly filter rows, skipping some unprocessed rows as well as repeating some already processed rows.

I guess the bigger lesson here is that when you paginate by a cursor, you have to be confident that filtering and ordering compare elements the same way. Which is not easy when you have a behaviour like what ClickHouse does here.
