The Analytics Data Pipeline ::
Storage -> Ingest -> Processing -> Storage -> Delivery

Data Lake ::
A data lake consists of two parts: storage and processing. Data lake storage requires an infinitely scalable, fault-tolerant, 
storage repository designed to handle massive volumes of data with varying shapes, sizes, and ingest velocities. Data lake 
processing requires a processing engine that can successfully operate on the data at this scale.

In reality, a data lake includes not just a single processing engine, but multiple processing engines, and because it 
represents the enterprise-wide, centralized repository of source and processed data (after all, it champions a “store all” 
approach to data management), it has other requirements such as metadata management, discovery, and governance.

the data lake concept as it is used today is intended for batch processing, where high latency (time until results ready) is 
appropriate.

two different architectures that can be used to act on the data managed by a data lake: lambda and kappa architecture ::
1) Lambda Architecture ::
a pipeline architecture that aims to reduce the com‐ plexity seen in real-time analytics pipelines by constraining any 
incremental computation to only a small portion of this architecture.

In lambda architecture, there are two paths for data to flow in the pipeline :
• A “hot” path where latency-sensitive data (e.g., the results need to be ready in seconds or less) flows for rapid consumption
by analytics clients. This data is mutable in nature.

the hot path places a latency constraint on the data. The impact of this latency constraint is that the types of calculations 
that can be performed are limited to those that can happen quickly enough. This might mean switching from an algorithm that 
provides perfect accuracy to one that provides an approximation.

• A “cold” path where all data goes and is processed in batches that can tolerate greater latencies (e.g., the results can take
minutes or even hours) until results are ready. This is immutable in nature. Any changes in any already existing data would end
up appending another row with a timestamp alongside the previous values. 

Because the “cold” path can tolerate a greater latency until the results are ready, the computation can afford to run across 
large data sets and the types of calculation performed can be time-intensive.



2) Kappa Architecture ::
The only difference between Lambda and Kappa architecture is that Kappa eliminates the cold path and makes all processing 
happen in a near–real-time streaming mode.
It arises from the disadvantage that keeping in sync the logic that does the computation in the hot path with the logic that 
is doing the same calculation in the cold path.
Kappa architecture centers on a unified log (think of it as a highly scalable queue), which ingests all data (which are 
considered events in this architecture). There is a single deployment of this log in the architecture, whereby each event 
datum collected is immutable, the events are ordered, and the current state of an event is changed only by a new event being 
appended.

The Azure data analytics Pipeline and different services provided by Azure on each component ::
=============================================================================================================================
Source :: 
    Database and Flat Files (pulled);
    Streaming sources (pushed to ingestor).
    
Ingest :: 
    Batch Ingest :: Azure import/export services; Azure Data factory; Azure HDInsight Sqoop
        
    Streaming Ingest :: Azure Event Hubs, Azure IoT Hub, Azure HDInsight(Kafka)
    
    
Storage :: components that are used to store the ingested, intermediate, and final data.
    Transient storage :: This can take the form of multiconsumer queues with a duration-based expiry to their content.
                         Basically for streaming storage ie - Event Hubs and IoT Hub.
    
    Persistent storage :: These components are capable of storing their content indefinitely and at scale.
                         ie - Azure Blob Storage, HDFS, and Azure Data Lake Store. Basically storage for Batch processing.
          
          
    Serving storage :: To store the final output be it batch processing or stream output. These datas are served to the client.
                       ie - Azure Document DB, Azure SQL Database, Azure SQL Data Warehouse, Azure Redis Cache, Azure Search,
                       and HDInsight running HBase.
            
    



    

