# os.   
Process synchronization is crucial in concurrent programming, ensuring that multiple processes or threads access shared resources safely and efficiently. This project implements the following synchronization primitives:

- Mutexes (Mutual Exclusion)
- Semaphores

Examples
The project includes 7 examples that demonstrate the application of these synchronization primitives:

1. Producer-Consumer Problem: Illustrates the use of semaphores to synchronize producer and consumer threads.
2. Race Condition: Demonstrates the consequences of inadequate synchronization and provides a solution using mutexes.
3. Priority Inversion: Shows how to address priority inversion using priority inheritance or ceiling protocols.
4. Bounded Buffer: Implements a bounded buffer using semaphores and mutexes to manage producer-consumer synchronization.
5. Dining Philosophers: Solves the classic dining philosophers problem using semaphores and mutexes to ensure deadlock-free synchronization.
6. Reader-Writer Problem: Demonstrates a solution to the reader-writer problem using semaphores and mutexes to balance reader and writer access.

Features
- Implementations of mutexes, semaphores
- 7 examples illustrating synchronization techniques
- Well-structured and readable code

Requirements
- [Language : Python, libraries used : Time, Threading] used : Time, Threading]
