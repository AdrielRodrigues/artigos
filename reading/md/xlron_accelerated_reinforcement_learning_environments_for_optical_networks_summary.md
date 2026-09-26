---
index_terms:
  - reinforcement learning
  - optical networks
  - GPU acceleration
  - resource allocation
  - JAX framework
  - network simulation
---

# XLRON: Accelerated Reinforcement Learning Environments for Optical Networks

## Abstract
XLRON is an open-source project that introduces GPU-accelerated reinforcement learning (RL) for optical network problems. The authors report a training speed-up of 100x to 1000x compared to existing tools, facilitating new research opportunities in the field.

## 1. Introduction and Motivation
While RL has shown potential in optimizing resource allocation—such as routing modulation and spectrum assignment (RMSA) and virtual optical network embedding (VONE)—several barriers hinder its deployment in production networks: scalability, robustness, interpretability, and overall performance.

The authors identify three primary obstacles slowing progress in the research community:
1. **Compute Intensity:** Traditional training requires costly CPU clusters for simulations paired with GPU servers for inference/updates, complicating setup and debugging.
2. **Lack of Standardization:** The absence of standard benchmarks and environments necessitates frequent reimplementation, slowing reproduction and comparison of results.
3. **Reliability Issues:** Closed-source code and a lack of comprehensive unit testing limit the verifiable reliability of current simulations.

XLRON is designed to address these issues by implementing GPU-compatible simulation and training code that allows for massive parallelization. Developed with test-driven development and modularity, it provides configurable environments for RMSA, routing and spectrum assignment (RSA), routing and wavelength assignment (RWA), and VONE.

## 2. Methodology
XLRON achieves its speed-ups by adopting RL architectures from Google DeepMind and utilizing the JAX numerical computing framework. By implementing both the simulation environment and the training algorithm in JAX, the entire training loop is compiled as a single program and executed on GPU or TPU hardware via Just-In-Time (JIT) compilation.

To enable this acceleration, XLRON adheres to specific technical constraints:
* **Data Constraints:** All data must be scalars or arrays with static dimensions known at compile time. The network state (FSU occupancy, node resources, service durations, topology, and shortest paths) is therefore represented as a series of arrays.
* **Program Constraints:** The system follows a functional programming paradigm required by JAX.

To ensure correctness and reproducibility, the project includes over 800 unit tests and leverages JAX's sophisticated pseudo-random number generation.

## 3. Case Studies
The authors compare XLRON against a baseline consisting of the Stable-Baselines3 (SB3) library and the `optical-rl-gym` environment.

### Comparison on RMSA
Using the NSFNET topology with 100 FSU per link and 150 Erlang traffic load, both systems were tested using the PPO algorithm for $10^7$ total timesteps (across $10^4$ episodes). XLRON was run on an Nvidia A100 GPU, while SB3 ran on an Apple M1 Pro CPU.
* **Performance:** XLRON matched the performance of the K-shortest path first-fit (KSP-FF) heuristic within the training budget.
* **Speed-up:** XLRON achieved a speed-up of over 100x with 250 parallel environments and approximately 500x with 2000 parallel environments compared to SB3.

### Comparison on VONE
The second study evaluated the time required to complete one million environment steps for VONE across two topologies (NSFNET and CONUS) and different FSU capacities (100 and 320).
* **CPU Performance:** On CPU, XLRON is consistently ~10x faster than SB3.
* **GPU Performance:** With 2000 parallel environments on GPU, the speed-up can exceed 1000x.
* **Specific Result:** For the CONUS topology with 320 FSUs per link, XLRON completed one million samples in 14 seconds, whereas SB3 required 2 hours and 10 minutes (a ~560x speed-up).

## 4. Conclusions
XLRON demonstrates significant efficiency gains over existing RL frameworks: roughly 10x on CPU and 100-1000x on GPU. The authors conclude that by enabling a "high-data regime," XLRON will likely facilitate breakthroughs in solving resource allocation problems within optical networks.