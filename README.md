# ML Eventing Systems (Lightweight Simulation)

A lightweight event-driven architecture simulation for machine learning pipelines.

This project demonstrates how modern ML systems can be decoupled using event-driven design patterns to improve scalability, reliability, and fault tolerance.

## Overview

In large-scale machine learning systems, synchronous pipelines often become bottlenecks due to tight coupling between components.

Event-driven architectures solve this by decoupling producers and consumers through an asynchronous event bus, enabling better scalability and system resilience.

This project simulates a simplified version of such architecture.

## Key Features

- Event-based asynchronous processing
- Decoupled producer/consumer architecture
- Simple in-memory event bus
- Worker-based processing system
- Basic retry handling

## Architecture

Producer → Event Bus → Workers → Processor → Output

## Why Event-Driven Design Matters

Modern ML infrastructure often deals with:

- High-volume data ingestion
- Unpredictable workloads
- Independent processing pipelines

Event-driven systems allow components to scale independently and improve system robustness under load.

This pattern is widely used in production AI infrastructure systems.

## Run Locally

pip install -r requirements.txt  
bash run.sh

Then open:

http://127.0.0.1:8000/docs

## Example Flow

1. Send event to system
2. Event is pushed into event bus
3. Worker consumes event asynchronously
4. Processor handles computation
5. Result is returned

## Design Considerations

- Decoupling of system components
- Asynchronous processing model
- Scalability under load
- Fault isolation between workers

## Note

This project is a simplified simulation for architectural demonstration purposes and does not include production dependencies.