# Services and APIs

## Kinds of APIs

Each API defines the following:

1. *Protocol* - the control structure
2. *Format* - the content structure

Multiple API methods have developed from isolated machines to multitasking systems, to networked servers:

- Before networking, an API usually meant a very close connection like a function call to a library in the same language as your application - calculating square root in a math library
- *Remote Procedure Calls* (RPC) were invented to call functions in other processes, on the same machine or others, as though they were in the calling application - gRPC.
- Messaging sends small chunks of data in pipelines among processes. Messages may be verb-like commands or just noun-like events of interest. Current popular messagings - Apache Kafka, RabbitMQ, NATS, ZeroMQ. Communication can follow different patterns:\
    1. *Request-response* - one:one like a web browser calling a web server
    2. *Publish-subscribe, or pub-sub* - publisher emits messages, and subsribers act on each according to some data in the message
    3. *Queues* - like pub-subs, but only one of a pool of subscribers grabs the message and acts on it.


## HTTP
Berners-Lee proposed three components for his World Wide Web:\
- *HTML* - language for displaying data
- *HTTP* - client-server protocol
- *URL*s - addressing scheme for web resources

## REST(ful)
Roy Fielding's Ph.D. thesis defined *Representational State Transfer* (REST) - architectural style for HTTP use (style means a higher-level pattern, like client-server, rather than a specific design). It's been largely misunderstood.

A roughly shared adaptation has evolved and dominates modern web. It's called RESTful, with these characteristics:
- Uses HTTP and client-server protocol
- Stateless (each connection is independent)
- Cacheable
- Resource-based

A resource is data that you can distinguish and perform operations on. A web service provides an endpoint - a distinct URL and HTTP verb (action) - for each feature that it wants to expose. An endpoint is also called a route, because it routes the URL to a function.

Database users are familiar with the *CRUD* acronym of procedures: create, read, update, delete. The HTTP verbs are pretty CRUDdy:
- POST - create (write)
- PUT - modify completely (replace)
- PATCH - modify partially (update)
- GET - read, retrieve
- DELETE - delete

A client sends a request to RESTful endpoint with data in one of the following areas of an HTTP message:
- Headers
- The URL string
- Query parameters
- Body values

In turn, HTTP response returns these:
- Status code:
    1. *100*s - info, keep going
    2. *200*s - success
    3. *300*s - redirection
    4. *400*s - client error
    5. *500*s - server error
- Various headers
- Body - empty, single, or chunked (in successive pieces)

## JSON
The combination of RESTful design and JSON data formats is common now.

## GraphQL
Facebook (Meta) designed *Graph Query Language* (GraphQL) to specify more flexible service queries - used instead of RESTful design.

# Concurrency
Besides the growth of service orientation, the rapid expansion of the number of connections to web services requires ever better efficiency and scale. We want to reduce the following:
- Latency - the up-front wait time
- Throughput - the number of bytes per second between the service and its callers

The term *concurrency* doesn't mean full parallelism. Multiple processing isn't occuring in the same nanosecond, in a single CPU. Instead, concurrency mostly avoids *busy* waiting (idling the CPU until a response is delivered). 

Normal Python execution is *synchronous*: one thing at a time, in the order specified by the code. But we want to be *asynchronous*: do a little of one thing, then a little of another thing, back to the first thing, and so on. If all our code uses the CPU to calculate things (*CPU bound*), there's really no spare time to be asynchronous. But if we perform something that makes the CPU wait for an external thing to complete (I/O bound), we can be asynchronous.

Asynchronous systems provide an event loop: requests for slow operations are sent and noted, but we don't hold up the CPU waiting for their responses. Instead, some immediate processing is done on each pass through the loop, and any responses that came in during that time are handled in the next pass.

Asynchronous processing isn't magic. You still have to be careful to avoid doing too much CPU-intensive work during the event loop, because that will slow down everything.

# Layers
To manage size and complexity, many applications have long used a so-called three-tier model (other interpretations: Model-View-Controller (MVC) and variations). For this book using the following simple separation of terms:
- Web - input/output layer over HTTP, which assembles client requests, calls the Service Layer, and returns responses
- Service - business logic, which calls the data layer when needed
- Data - access to data stores and other services
- Model - data definitions shared by all layers
- Web client - web browser or other HTTP client-side software