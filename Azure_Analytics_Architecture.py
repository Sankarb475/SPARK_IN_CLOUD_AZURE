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
• A “hot” path where latency-sensitive data (e.g., the results need to be ready in seconds or less) flows for rapid consumption by analytics clients. This data is mutable in nature.

• A “cold” path where all data goes and is processed in batches that can tolerate greater latencies (e.g., the results can take minutes or even hours) until results are ready. This is immutable in nature. Any changes in any already existing data would end
up appending another row with a timestamp and changes accomodated



2) Kappa Architecture ::

