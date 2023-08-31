# AWs
## Terms

|Term| Definition|
|---|---|
|11 9’s guarantee|99.999999999% durability of objects over a given year. This durability level corresponds to an average annual expected loss of 0.000000001% of objects|
|Availability Zones|A logical data center in an AWS region with redundant and separate power, networking and connectivity reducing the likelihood of two zones failing simultaneously|
|AWS CloudFront|Fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency|
|AWS Local Zones|A type of AWS infrastructure deployment that places AWS compute, storage, database, and other select services closer to large population, industry, and IT centers where no AWS Region exists today|
|AWS Regions|A geographical location with a collection of availability zones physically isolated from and independent of every other region|
|AWS Support|Paid support plans offering AWS customers access to AWS technical experts and professional guidance|
|Durability|The probability that the object will remain intact and accessible after a period of one year|
|Edge Location|A physical site that CloudFront uses to cache copies of your content for faster delivery to users at any location|
|Fault Tolerance|The property that enables a system to continue operating properly in the event of the failure of (or one or more faults within) some of its components|
|High Availability|Refers to systems that are durable and likely to operate continuously without failure for a long time|
|Memory-Optimized|The R3 instance class recommended for applications that require high memory performance|
|Points of Presence|AWS Edge Locations and Regional Edge Caches used for both AWS CloudFront and Lambda@Edge to deliver content to end users at high speeds|
|Storage-Optimized|Instances are designed for workloads that require high, sequential read and write access to very large data sets on local storage. They are optimized to deliver tens of thousands of low-latency, random I/O operations per second (IOPS) to applications|
|VPC Peering|A networking connection between two AWS VPCs that allows you to route traffic between them using private IP addresses|
|VPC Sharing|allows you to share subnets with other AWS accounts in your organization|


## Pricing for EC2 Instances in AWS
AWS EC2 instance pricing is straightforward, but it can quickly become complex when you take up the task of optimizing your environment to achieve the ideal cost/performance balance.

- Explore OS licensing pricing and options
- Limit the users and roles that can launch production instances
- Choose the best instance for your workload
- Save by moving to new generation instances when available


### Purchasing Options

|Option| How it Works|
|---|---|
|Capacity Reservations|Reserve capacity for your EC2 instances in a specific Availability Zone for any duration.|
|Dedicated Hosts|Pay for a physical host that is fully dedicated to running your instances, and bring your existing per-socket, per-core, or per-VM software licenses to reduce costs.|
|Dedicated Instances|Pay, by the hour, for instances that run on single-tenant hardware.|
|On-Demand Instances|An AWS service or technology that can be acquired at any time for a predetermined standard cos|
|Reserved Instances|An AWS service or technology that can be reserved for a period of time at a discount in exchange for a payment commitment|
|Savings Plans|Reduces your Amazon EC2 costs by making a commitment to a consistent amount of usage, in USD per hour, for a term of 1 or 3 years.|
|Scheduled Instances|Purchase instances that are always available on the specified recurring schedule, for a one-year term.|
|Spot Instances|an EC2 instance that can be acquired by bidding for a low price in exchange for the understanding that AWS can reclaim it at any time|

- https://www.youtube.com/watch?v=px2Iko_Ezao&t=269s

### Reserved and Spot Instances
Reserved instances are a 1 or 3 year commitment and multiple payment options also save money,
Spot instances can be terminated by AWS at any time with a 2 minute notification that you might not see
On demand instances are the most expensive option and should only be used in short-term or urgent situations.

- https://www.youtube.com/watch?v=rlQjQ9XKs2o&t=181s

## Storage Pricing
- Storage costs vary considerably depending on usage and requirements.
- Applications require different types of optimized storage depending on their primary function.

- https://www.youtube.com/watch?v=855-ZH2W7C0

|Term|	Definition|
|---|---|
|Edge Cache|	A high-speed data storage layer which stores a subset of data, typically transient in nature, close to the end user so that future requests for that data are served up faster
|EBS|	Elastic Block Store - cloud-based and pre-allocated linux-based block storage system provided by Amazon Web Services (AWS) that is best used for storing persistent data
|EFS|	Elastic File System - a simple, scalable, elastic, and encrypted file storage system that can be used by concurrent compute resources in the AWS cloud and on-premises
|HDD|	Category of EBS hard disk drive. Can be throughput optimized (workhorse) or cold (infrequently scanned)
|Lifecycle Policies|	Automate the actions you want to take on an object in an S3 bucket over its lifetime, for example, move them to another storage class, archive them after a number of days or years, or delete them.
|S3|	Amazon Simple Storage Service is general purpose object storage used for frequently accessed files
|S3 Endpoints|	A private connection between your VPC and S3 that doesn’t require internet access, potentially reducing NAT gateway costs
|SSD|	Category of EBS solid-state drive. Can be IOPS optimized for databases (fast) or general-purpose for boot volumes and dev/test systems
|Storage Cache|	A high-speed data storage layer that stores a subset of typically transient data
|Tagging|	Allows you to name and classify S3 buckets. AWS can provide a usage and cost report based on tags

