
mongo = the client,

mongos = MongoDB Shard Utility, the controller and query router for sharded clusters.
	Sharding partitions the data-set into discrete parts.

mongod = The primary daemon process for the MongoDB system.
	It handles data requests, manages data access, and performs background management operations.

MongoDB Atlas = a fully-managed cloud database developed by the same people that build MongoDB.
	Atlas handles all the complexity of deploying, managing, and healing your deployments
	on the cloud service provider of your choice (AWS, Azure, and GCP).


A Replica-Set
	means that you have multiple instances of MongoDB which each mirror all the data of each other.
	A replica-set consists of one Master(also called "Primary") and one or more Slaves(aka Secondary).

	Read-operations can be served by any slave, so you can increase read-performance by adding more slaves
	to the replica-set(provided that your client application is capable to actually use different set-members).

	But write-operations always take place on the master of the replica-set and are then propagated to
	the slaves, so writes won't get faster when you add more slaves.

	Replica-sets also offer fault-tolerance. When one of the members of the replica-set goes down,
	the others take over. When the master goes down, the slaves will elect a new master.
	For that reason it is suggested for productive deployment to always use MongoDB as a replica-set of
	at least three servers, two of them holding data (the third one is a data-less "arbiter"
	which is required for determining a new master when one of the slaves goes down).

A Sharded Cluster
	means that each shard of the cluster(which can also be a replica-set) takes care of a part of the data.
	Each request, both reads and writes, is served by the cluster where the data resides.
	This means that both read- and write performance can be increased by adding more shards to a cluster.
	Which document resides on which shard is determined by the shard key of each collection.
	It should be chosen in a way that the data can be evenly distributed on all clusters
	and so that it is clear for the most common queries where the shard-key resides
	(example:
	when you frequently query by user_name, your shard-key should include the field user_name
	so each query can be delegated to only the one shard which has that document).

	The drawback is that the fault-tolerance suffers.
	When one shard of the cluster goes down, any data on it is inaccessible.
	For that reason each member of the cluster should also be a replica-set. This is not required.
	When you don't care about high-availability, a shard can also be a single mongod instance
	without replication. But for production-use you should always use replication.


########################## Sharded Cluster ############################
          /                       |                      \
         /                        |                       \
      Shard A                  Shard B                  Shard C
        / \                      / \                      / \
+-------+ +---------+    +-------+ +---------+    +-------+ +---------+
|Primary| |Secondary|    |Primary| |Secondary|    |Primary| |Secondary|
|  25GB |=| 25GB    |    | 25 GB |=| 25 GB   |    | 25GB  |=| 25GB    |
+-------+ +---------+    +-------+ +---------+    +-------+ +---------+

When you want to split your data of 75GB into 3 shards of 25GB each,
you need at least 6 database servers organized in three replica-sets.
Each replica-set consists of two servers which have the same 25GB of data.

You also need servers for the arbiters of the three replica-sets as well as
the mongos router and the config server for the cluster.
The arbiters are very lightweight and are only needed when a replica-set member goes down,
so they can usually share the same hardware with something else.
But Mongos router and config-server should be redundant and on their own servers.



db.help()                    help on db methods
db.mycoll.help()             help on collection methods
sh.help()                    sharding helpers
rs.help()                    replica set helpers
help admin                   administrative help
help connect                 connecting to a db help
help keys                    key shortcuts
help misc                    misc things to know
help mr                      mapreduce

show dbs                     show database names
show collections             show collections in current database
show users                   show users in current database
show profile                 show most recent system.profile entries with time >= 1ms
show logs                    show the accessible logger names
show log [name]              prints out the last segment of log in memory, 'global' is default
use <db_name>                set current database
db.foo.find()                list objects in collection foo
db.foo.find( { a : 1 } )     list objects in foo where a == 1
it                           result of the last line evaluated; use to further iterate
DBQuery.shellBatchSize = x   set default number of items to display on shell
exit                         quit the mongo shell

> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
> use acme
switched to db acme
> db
acme
> db.createCollection('post')
{ "ok" : 1 }
> show collections
post
> show dbs
acme    0.000GB
admin   0.000GB
config  0.000GB
local   0.000GB
> show collections
post
> db.deleteCollection('post')
2019-10-22T18:00:07.279+0100 E  QUERY    [js] uncaught exception: TypeError: db.deleteCollection is not a function :
@(shell):1:1

> db.post.drop()
true
> db.createCollection('posts')
{ "ok" : 1 }
> show collections
posts

> db.posts.insert({
title: 'Post Three',
body: 'Body of post Three',
category: ['News', 'event'],
user: {
    name: 'Johney Doely',
    status: 'author3'
},
date: Date()
})

> db.posts.find().pretty()
> db.posts.find().limit(1).pretty()
> db.posts.find().sort({ title: -1}).pretty()

> db.posts.find().forEach(function(doc) { print('Blog Post: ' + doc.title) })
> db.posts.findOne({ category: 'News'})

> db.posts.update({_id: ObjectId("5daf3816967a0e9844dc43a1")},
{
	title: 'Post One',
	category: ['News', 'event one'],
	user: {
		name: 'Johney Doely',
		status: 'author1'
	},
date: Date()
})

> db.posts.update({_id: ObjectId("5daf3816967a0e9844dc43a1")},
{
	$set: {
		body: 'Body of post 1',
		category: 'Technology',
		likes: 4
	}
}
)

> db.posts.update({_id: ObjectId("5daf3816967a0e9844dc43a1")}, { $inc: { likes: 2} })
> db.posts.update({_id: ObjectId("5daf3816967a0e9844dc43a1")}, { $rename: { likes: 'views'} })

> db.posts.remove({_id: ObjectId("5daf3816967a0e9844dc43a2"})
> db.posts.remove({ title: 'Post Two'})

> db.posts.update({_id: ObjectId("5daf3816967a0e9844dc43a1")},
{
	$set: {
		comments: [
			{
			user: 'Mary Johns',
			body: 'Comment One',
			date: Date()
			},
			{
			user: 'Hary Johns',
			body: 'Comment Two',
			date: Date()
			}
		]
	}
}
)

> db.posts.find({
	comments: {
	$elemMatch: {
		user: 'Mary Johns'
	}
}
}).pretty()

> db.posts.createIndex({ title: 'text'})
> db.posts.find({
	$text: {
		$search: "\"Post O\""
	}
}).pretty()

> db.posts.update({ title: 'Post Two' }, { $set: { views: 10} })
> db.posts.find({ views: { $gt: 6 } })
> db.posts.find({ views: { $gte: 6 } }).pretty()
