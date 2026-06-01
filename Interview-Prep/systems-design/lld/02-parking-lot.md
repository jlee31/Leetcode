# LLD: Design a Parking Lot

A classic object-oriented design interview. No "right" answer — they're grading
your class decomposition, use of enums/inheritance, and how you handle change.

## Requirements to clarify

- Multiple **spot sizes** (motorcycle, compact, large) and **vehicle types**.
- A vehicle fits certain spots (a motorcycle fits any; a truck needs large).
- Multiple **levels/floors**, each with many spots.
- Park a vehicle (assign nearest suitable free spot), un-park (free the spot).
- Track availability; maybe issue a ticket and compute a fee on exit.

## Suggested class decomposition

```
ParkingLot
  - levels: List[Level]
  + park(vehicle) -> Ticket | None
  + leave(ticket) -> fee

Level
  - spots: List[ParkingSpot]
  + find_available_spot(vehicle) -> ParkingSpot | None

ParkingSpot
  - size: SpotSize
  - vehicle: Vehicle | None
  + can_fit(vehicle) -> bool
  + is_free() -> bool

Vehicle (abstract)  -> Motorcycle, Car, Truck
  - size: VehicleSize

enum SpotSize / VehicleSize { SMALL, MEDIUM, LARGE }

Ticket
  - spot, vehicle, entry_time
```

## Design decisions to discuss

1. **Enum vs subclass for sizes/types** — enums keep it simple; subclasses let
   each vehicle override `can_fit` logic. Justify your pick.
2. **Spot assignment strategy** — first-fit, best-fit (smallest spot that fits),
   nearest-to-entrance. This is a pluggable *Strategy*.
3. **Concurrency** — two cars racing for the last spot. Need atomic
   reserve-then-confirm or a lock per level. Mention it even if you don't code it.
4. **Extensibility (Open/Closed)** — adding an EV charging spot or handicapped
   spot shouldn't require rewriting `park()`. Where do you add the type?
5. **Fee calculation** — another Strategy (hourly, flat, tiered).

## Exercise

Sketch the classes (in Python or C++ — your interview language). Implement
`ParkingLot.park()` and `leave()` with a first-fit strategy and a simple hourly
fee. Then state how you'd swap in best-fit *without touching* `park()`.
