# Technical Roadmap

This document outlines the planned evolution of Noise Floor Oracle
from a simulated prototype to a production-ready runtime component.

## Phase 1 — Simulation and Validation (Current)

- Backend-agnostic oracle implementation
- Saturation detection via depth sweeps
- Mock and fake-backend based validation
- Visualization and demonstration tools

Status: Complete

## Phase 2 — Qiskit Backend Integration

- Integration with Qiskit Runtime primitives
- Collection of backend-reported noise metrics (T1, T2, gate errors)
- Execution of depth-swept circuits on IBM Quantum backends
- Empirical validation across multiple devices

Status: Planned

## Phase 3 — Runtime Service Exposure

- Packaging oracle as a callable runtime service
- Standardized API for noise floor queries
- Backend-agnostic interface with IBM-specific adapters
- Integration with scheduling and transpilation pipelines

Status: Planned

## Phase 4 — Optimization-Aware Decision Layer

- Compiler-level stopping criteria
- Cost-aware circuit depth selection
- Automated benchmarking workflows
- Enterprise-scale orchestration support

Status: Future
