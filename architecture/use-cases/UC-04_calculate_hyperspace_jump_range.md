---
title: "Use-Case Specification: UC-04 Calculate Hyperspace Jump Range"
use_case_id: "UC-04"
status: "approved"
version: "1.0.0"
level: "sea_level"
primary_actor: "Route Planning Engine (ed-router)"
created_at: "2026-11-01"
last_updated_at: "2026-11-01"
---

# Use-Case Specification: UC-04 Calculate Hyperspace Jump Range

## 1. Description & Goal
Computes the exact single-hop jump range for a ship based on hull mass, equipped modules, current fuel mass, and cargo mass using Frontier's nonlinear FSD formula.

## 2. Actors & Scope
* **Primary Actor:** Pathfinding router (`ed-router`).
* **System Boundary:** `ed-models` driving port facade (`EliteDomainFacade`).

## 3. Preconditions
* Ship loadout is instantiated with valid equipped Frame Shift Drive module specifications.

## 4. Postconditions
* Returns `JumpRangeProfile(unladen_range, laden_range, current_jump_range)`.

## 5. Main Success Scenario (Basic Flow)
1. Actor passes `ShipLoadout`, `cargo_mass_t`, and `fuel_mass_t` to `facade.calculate_jump_range(...)`.
2. The interactor sums base hull mass, module masses, and cargo mass to determine total mass $M$.
3. The interactor retrieves FSD rating parameters: optimal mass $m_{\text{opt}}$, fuel rating constant $a$, and power exponent $b$.
4. The interactor evaluates jump range: $\text{range} = \left(\frac{f_{\text{max}}}{a \times 10^{-3}}\right)^{1/b} \times \frac{m_{\text{opt}}}{M}$.
5. The interactor computes unladen (zero cargo), laden (full cargo), and current jump profiles.
6. The profile is returned to the actor.
