---
title: "In-Game Telemetry and Event Targets Reference"
tags: ["telemetry", "events", "testing", "gameplay-targets", "ed-models"]
created_at: "2026-11-02"
last_updated_at: "2026-11-02"
---

# In-Game Telemetry and Event Targets Reference

This document maps all 258+ Frontier Journal event models and cockpit telemetry bitfields defined in `ed-models` to their exact in-game triggers. It serves as the operational guide for harvesting real-world test logs in *Elite Dangerous* to test against domain hydration in `ed-integration-smoke`.

---

## 1. Cockpit Telemetry Targets (`Status.json`)

The cockpit status file updates continuously (up to 4 Hz) with flags and telemetry fields.

### 1.1. StatusFlags (Primary 32-Bit Bitfield)
| Flag | Target In-Game Action |
|:---|:---|
| `Docked` | Complete landing on a starport, planetary port, or fleet carrier pad. |
| `Landed` | Touch down surface landing gear on planetary terrain. |
| `LandingGearDown` | Toggle landing gear deploy/retract key. |
| `ShieldsUp` | Present while shields are active; drops when shields collapse or are powered down. |
| `Supercruise` | Engage frame shift drive into supercruise mode. |
| `FlightAssistOff` | Toggle flight assist off (`FA-Off`). |
| `HardpointsDeployed` | Deploy combat hardpoints. |
| `InWing` | Form or join a wing/team with another player. |
| `LightsOn` | Toggle ship headlights. |
| `CargoScoopDeployed` | Toggle cargo scoop deploy/retract. |
| `SilentRunning` | Engage silent running (heatsink closed). |
| `ScoopingFuel` | Approach a scoopable star (O, B, A, F, G, K, M) with an active fuel scoop. |
| `SrvHandbrake` | Engage handbrake while operating an SRV. |
| `SrvTurret` | Switch into SRV turret view mode. |
| `SrvUnderShip` | Drive SRV into the ship's boarding bay docking perimeter. |
| `SrvDriveAssist` | Toggle SRV drive assist mode. |
| `FsdMassLocked` | Enter gravity well of a station, ring, or planet. |
| `FsdCharging` | Initiate hyperspace jump or supercruise entry charge. |
| `FsdCooldown` | Immediate state upon dropping out of hyperspace/supercruise. |
| `LowFuel` | Deplete main fuel tank below 25% capacity. |
| `OverHeating` | Push ship heat above 100% (silent running or scooping). |
| `HasLatLong` | Fly in orbital cruise or surface proximity where coordinates appear. |
| `IsInDanger` | Enter hostile combat engagement. |
| `BeingInterdicted` | Undergo interdiction tether from NPC or player. |
| `InMainShip` | Helm main spaceship. |
| `InFighter` | Transfer control to launched Ship-Launched Fighter (SLF). |
| `InSrv` | Deploy and helm Surface Recon Vehicle (SRV). |
| `AnalysisMode` | Switch cockpit HUD from Combat to Analysis mode. |
| `NightVision` | Toggle night vision mode. |
| `AltReverse` | Reverse throttle in SRV driving mode. |

### 1.2. StatusFlags2 (Extended 32-Bit Bitfield)
| Flag | Target In-Game Action |
|:---|:---|
| `OnFoot` | Disembark from ship or vehicle onto a planet or station concussion. |
| `InTaxi` | Board and ride an Apex Interstellar shuttle. |
| `InMulticrew` | Join another commander's ship helm via multicrew. |
| `OnFootInStation` | Walk inside a starport or outpost social concourse. |
| `OnFootOnPlanet` | Walk on a planetary surface exterior. |
| `AimDownSight` | Aim weapon down sights (ADS) while on foot. |
| `LowOxygen` | Deplete suit oxygen reserves below critical threshold. |
| `LowHealth` | Take personal shield/health damage on foot. |
| `Cold` / `Hot` | Walk in extreme planetary temperature zones. |
| `GlideMode` | Enter orbital drop glide phase towards planetary surface. |
| `BreathableAtmosphere` | Step inside an atmospheric building or airlock. |

---

## 2. Frontier Journal Event Targets by Chapter

### 2.1. Chapter 2: Startup Events (`startup/`)
| Event Name | Target In-Game Action |
|:---|:---|
| `Fileheader` | Auto-written on game client launch. |
| `Commander` | Auto-written when selecting game mode (Open/Solo/Group). |
| `NewCommander` | Create a brand-new commander profile. |
| `ClearSavedGame` | Clear commander save from main menu. |
| `LoadGame` | Auto-written when loading into the cockpit. |
| `Materials` | Emitted upon session launch summarizing raw/manufactured/encoded inventories. |
| `Cargo` | Emitted upon session launch or cargo bay change summarizing inventory. |
| `Loadout` | Emitted on game load or when switching ships/outfitting loadouts. |
| `Missions` | Emitted on session launch summarizing active missions. |
| `Progress` | Emitted on game load showing combat/trade/exploration/soldier/exobiologist rank %. |
| `Rank` | Emitted on game load reporting current rank tiers. |
| `Reputation` | Emitted on game load reporting superpower reputations (Federation, Empire, Alliance). |
| `Statistics` | Emitted on game load detailing lifetime statistics. |
| `Passengers` | Emitted on game load if passenger cabins have manifest occupants. |
| `Powerplay` | Emitted on game load if pledged to a Galactic Power. |

### 2.2. Chapter 3: Travel Events (`travel/`)
| Event Name | Target In-Game Action |
|:---|:---|
| `Location` | Emitted on session start or respawn reporting current location. |
| `StartJump` | Charge frame shift drive for Hyperspace or Supercruise. |
| `FSDJump` | Hyperspace tunnel breakout into target star system. |
| `FSDTarget` | Select a destination star system in GalMap or navigation panel. |
| `SupercruiseEntry` | Drop into supercruise from normal space. |
| `SupercruiseExit` | Drop out of supercruise into normal space (station/ring/signal). |
| `ApproachBody` | Approach a planet or moon into orbital flight. |
| `LeaveBody` | Fly away from planetary gravity well. |
| `DockingRequested` | Request docking permission from contact panel. |
| `DockingGranted` | Docking request approved and pad assigned. |
| `DockingDenied` | Docking request denied (full pads or hostile). |
| `DockingTimeout` | Docking clearance expires before landing. |
| `DockingCancelled` | Cancel active docking request. |
| `Docked` | Ship clamps onto landing pad. |
| `Undocked` | Ship releases from landing pad clamps. |
| `Touchdown` | Land ship on planetary surface. |
| `Liftoff` | Thrusters lift ship off planetary terrain. |
| `NavRoute` | Calculate multi-jump route on GalMap. |
| `NavRouteClear` | Clear active plotted navigation route. |

### 2.3. Chapter 4: Combat Events (`combat/`)
| Event Name | Target In-Game Action |
|:---|:---|
| `UnderAttack` | Targeted and fired upon by hostile vessel. |
| `ShipTargeted` | Target a ship with HUD target lock. |
| `ShieldState` | Shields drop to 0% or recharge back to 100%. |
| `HullDamage` | Hull integrity takes damage through shields. |
| `HeatWarning` | Internal temperature exceeds 100%. |
| `HeatDamage` | Internal temperature causes module damage (>140%). |
| `Interdiction` | Successfully interdict an NPC or player with FSD Interdictor. |
| `Interdicted` | Submit to or evade incoming interdiction. |
| `EscapeInterdiction` | Successfully win interdiction escape vector minigame. |
| `Bounty` | Destroy wanted ship and claim bounty voucher. |
| `CapShipBond` | Destroy capital ship heat relays in a combat zone. |
| `FactionKillBond` | Destroy enemy combatant in conflict zone. |
| `PVPKill` | Destroy another player's vessel. |
| `Died` | Ship destroyed; respawn screen triggered. |
| `FighterDestroyed` | Launched SLF is destroyed. |
| `SRVDestroyed` | Deployed SRV is destroyed on surface. |

### 2.4. Chapter 5: Exploration Events (`exploration/`)
| Event Name | Target In-Game Action |
|:---|:---|
| `DiscoveryScan` | Fire discovery scanner ("Honk") in unexplored system. |
| `FSSDiscoveryScan` | Open Full Spectrum System Scanner (FSS) and scan system plane. |
| `FSSSignalDiscovered` | Tune FSS frequency to identify non-body radio signal. |
| `FSSBodySignals` | Scan planet with FSS revealing geological/biological signals. |
| `FSSAllBodiesFound` | 100% scan completion of all stellar/planetary bodies in system. |
| `Scan` | Perform basic or detailed surface scan on star or planet. |
| `ScanBaryCentre` | Scan orbital barycentre of binary body pair. |
| `SAAScanComplete` | Map 100% of a planetary body using Detailed Surface Scanner (DSS) probes. |
| `SAASignalsFound` | DSS probes reveal surface points of interest (POIs). |
| `NavBeaconScan` | Target and scan physical navigation beacon nav point. |
| `CodexEntry` | Discover and scan a new organic, geological, or stellar phenomenon. |
| `MaterialDiscovered` | Discover a raw/manufactured/data material tier for the first time. |
| `MaterialCollected` | Scoop or limpet-collect floating material chunk. |
| `MaterialDiscarded` | Jettison raw/manufactured material from inventory. |
| `BuyExplorationData` | Purchase navigation data for a system from Galaxy Map. |
| `SellExplorationData` | Sell cartographic data at Universal Cartographics contact. |
| `MultiSellExplorationData`| Bulk-sell pages of cartographic data at starport. |
| `Screenshot` | Capture high-resolution screenshot (F10 / Alt-F10). |

### 2.5. Chapter 6: Trade Events (`trade/`)
| Event Name | Target In-Game Action |
|:---|:---|
| `MarketBuy` | Purchase cargo commodity from Starport Commodities Market. |
| `MarketSell` | Sell cargo commodity to Starport Commodities Market. |
| `BuyTradeData` | Purchase market trade route data for a star system. |
| `CollectCargo` | Scoop or limpet-retrieve floating cargo canister. |
| `EjectCargo` | Jettison or abandon cargo canister into space. |
| `MiningRefined` | Refinery completes processing 100% mineral ore chunk into cargo. |
| `AsteroidCracked` | Detonate seismic charges to fissure a deep core asteroid. |

### 2.6. Chapter 7: Station Services Events (`station/`)
| Event Name | Target In-Game Action |
|:---|:---|
| `Market` | Open Commodities Market interface at station. |
| `Shipyard` | Open Shipyard interface at station. |
| `Outfitting` | Open Outfitting interface at station. |
| `ModuleBuy` | Purchase and fit new module to ship. |
| `ModuleSell` | Sell equipped module for credits. |
| `ModuleStore` | Store module in station storage. |
| `ModuleSwap` | Swap module between two ship slots. |
| `ModuleRetrieve` | Install stored module into ship slot. |
| `ModuleBuyAndStore` | Buy module directly into station storage. |
| `ModuleSellRemote` | Sell module stored at another station. |
| `FetchRemoteModule` | Order transfer of stored module from remote station. |
| `MassModuleStore` | Store multiple modules simultaneously (e.g. stripped ship). |
| `ShipyardBuy` | Purchase a new ship at shipyard. |
| `ShipyardSell` | Sell current or stored ship at shipyard. |
| `ShipyardSwap` | Switch active ship to another stored ship. |
| `ShipyardTransfer` | Order transfer of stored ship to current station. |
| `ShipyardNew` | Deploy newly purchased ship hull. |
| `ShipyardRedeem` | Redeem reward ship. |
| `StoredShips` | Open stored ship manifest list. |
| `StoredModules` | Open stored module manifest list. |
| `Repair` / `RepairAll` | Repair module or complete hull damage at maintenance contact. |
| `RefuelAll` / `RefuelPartial` | Purchase fuel at starport contact. |
| `BuyAmmo` | Restock ammunition at munitions contact. |
| `BuyDrones` / `SellDrones` | Restock or sell limpets from munitions contact. |
| `RestockVehicle` | Restock destroyed SRV or SLF hangar bays. |
| `SetUserShipName` | Rename ship or change ship ID plate in outfitting livery. |
| `MissionAccepted` | Accept mission from starport mission board. |
| `MissionCompleted` | Turn in mission objectives and claim mission rewards. |
| `MissionAbandoned` | Abandon active mission in transactions panel. |
| `MissionFailed` | Fail mission due to death, timer expiry, or cargo loss. |
| `MissionRedirected` | Mission objectives update with new delivery destination. |
| `CommunityGoal` | Open Community Goal mission board. |
| `CommunityGoalJoin` | Sign up to participate in active Community Goal. |
| `CommunityGoalReward` | Claim completed tier rewards for Community Goal. |
| `CommunityGoalDiscard` | Opt out of Community Goal. |
| `EngineerProgress` | Unlock, meet, or level up rank with an Engineer. |
| `EngineerApply` | Apply engineering modification blueprint to module. |
| `EngineerCraft` | Roll engineering modification tier progress. |
| `EngineerContribution` | Deliver requested unlock commodities/materials to engineer. |
| `EngineerLegacyConvert`| Convert pre-3.0 legacy engineering module. |
| `PayFines` / `PayBounties`| Pay off fines or legal bounties at station Authority/Interstellar Factors. |
| `PayLegacyFines` | Clear legacy fines. |
| `RedeemVoucher` | Redeem combat bonds or bounty vouchers at contacts. |
| `MaterialTrade` | Exchange materials with Raw/Manufactured/Encoded material trader. |
| `TechnologyBroker` | Unlock tech broker modules (Guardian FSD Booster, etc.). |
| `SearchAndRescue` | Hand in black boxes, escape pods, or personal effects to S&R contact. |
| `CargoDepot` | Collect or deliver partial cargo for wing cargo mission. |
| `CrewHire` / `CrewFire` / `CrewAssign` | Manage NPC crew members in Crew Lounge. |

### 2.7. Chapter 8: Powerplay Events (`powerplay/`)
| Event Name | Target In-Game Action |
|:---|:---|
| `PowerplayJoin` | Pledge allegiance to a Galactic Power. |
| `PowerplayLeave` | Renounce pledge to current Galactic Power. |
| `PowerplayDefect` | Defect directly from one Galactic Power to another. |
| `PowerplayCollect` | Collect preparation, expansion, or fortification materials from power contact. |
| `PowerplayDeliver` | Deliver power materials to target control or expansion system. |
| `PowerplayFastTrack` | Pay credits to skip wait time for power commodities. |
| `PowerplayVoucher` | Claim powerplay combat merits for undermining enemy systems. |
| `PowerplaySalary` | Claim weekly rating credit salary from power contact. |
| `PowerplayVote` | Cast weekly consolidation or preparation votes. |
| `PowerplayMerits` | Weekly rank recalculation and merit decay. |
| `PowerplayRank` | Notification of rank advancement or demotion. |
| `DeliverPowerMicroResources` | Deliver on-foot Powerplay materials (Powerplay 2.0). |

### 2.8. Chapter 9: Squadrons Events (`squadrons/`)
| Event Name | Target In-Game Action |
|:---|:---|
| `SquadronCreated` | Establish a new player squadron. |
| `AppliedToSquadron` | Submit application to join a squadron. |
| `JoinedSquadron` | Application approved and inducted into squadron. |
| `LeftSquadron` | Voluntarily leave or resign from squadron. |
| `InvitedToSquadron` | Receive invitation to join squadron. |
| `SquadronPromotion` | Promoted to higher squadron rank. |
| `SquadronDemotion` | Demoted to lower squadron rank. |
| `SquadronStartup` | Emitted on game load detailing squadron affiliation. |
| `SharedBookmarkToSquadron`| Share personal map bookmark to squadron bookmarks. |

### 2.9. Chapter 10: Fleet Carriers Events (`carrier/`)
| Event Name | Target In-Game Action |
|:---|:---|
| `CarrierBuy` | Purchase a Drake-Class Fleet Carrier from Carrier Vendor. |
| `CarrierStats` | Open Fleet Carrier management UI. |
| `CarrierFinance` | Deposit or withdraw credits from carrier balance; set tariff rates. |
| `CarrierDepositFuel` | Donate Tritium into carrier fuel depot tank. |
| `CarrierJumpRequest` | Schedule a carrier hyperspace jump to destination system/body. |
| `CarrierJump` | Carrier hyperspace transit completes. |
| `CarrierJumpCancelled`| Abort scheduled carrier hyperspace jump during lockdown window. |
| `CarrierCrewServices` | Install or suspend carrier shipyard/outfitting/bar services. |
| `CarrierDockingPermission`| Set carrier access permissions (All, Friends, Squadron, Not Notorious). |
| `CarrierBankTransfer` | Transfer funds between commander wallet and carrier bank. |
| `CarrierNameChange` | Rename fleet carrier or change carrier callsign. |
| `CarrierTradeOrder` | Place buy/sell order for commodities in carrier market. |
| `CarrierShipPack` | Purchase shipyard ship package for carrier. |
| `CarrierModulePack` | Purchase outfitting module package for carrier. |
| `CarrierLocation` | Emitted when carrier changes system or orbit. |

### 2.10. Chapter 11: Odyssey On-Foot Events (`odyssey/`)
| Event Name | Target In-Game Action |
|:---|:---|
| `Disembark` | Step out of ship or SRV onto concourse or planetary surface. |
| `Embark` | Board ship or SRV from on-foot. |
| `BuySuit` / `SellSuit` | Purchase or sell on-foot suit at Pioneer Supplies. |
| `UpgradeSuit` | Upgrade suit tier (G1 to G5) at Pioneer Supplies. |
| `BuyWeapon` / `SellWeapon` | Purchase or sell on-foot weapon at Pioneer Supplies. |
| `UpgradeWeapon` | Upgrade weapon tier (G1 to G5) at Pioneer Supplies. |
| `SuitLoadout` | Open suit loadout management screen. |
| `CreateSuitLoadout` / `DeleteSuitLoadout` / `RenameSuitLoadout` / `SwitchSuitLoadout` | Manage personal on-foot equipment configurations. |
| `LoadoutEquipModule` | Equip modification or weapon to suit loadout. |
| `BookTaxi` / `CancelTaxi` | Book or cancel Apex Interstellar shuttle transport. |
| `BookDropship` / `CancelDropship` | Book or cancel Frontline Solutions combat dropship. |
| `DropshipDeploy` | Deploy into planetary conflict zone via dropship. |
| `ScanOrganic` | Take genetic sampling of plant life using Genetic Sampler. |
| `SellOrganicData` | Sell genetic data at Vista Genomics concourse counter. |
| `CollectItems` / `DropItems` | Pick up or drop physical items into on-foot backpack. |
| `UseConsumable` | Use medkit, energy cell, or bypass e-breach. |
| `Backpack` / `BackpackChange` | Backpack inventory updates or changes. |
| `ShipLocker` | Access ship locker cargo storage on foot. |
| `BuyMicroResources` / `SellMicroResources` / `TradeMicroResources` / `TransferMicroResources` | Trade micro-resources at bartender or transfer between locker/backpack. |
| `FCMaterials` | Manage carrier bartender micro-resource sales. |

### 2.11. Chapters 12 & 13: Other & Social Events (`other/`)
| Event Name | Target In-Game Action |
|:---|:---|
| `FuelScoop` | Scoop fuel continuously from star corona. |
| `ReservoirReplenished` | Main fuel tank transfers fuel to active reservoir tank. |
| `Friends` | Friend requests, status changes, or player connection updates. |
| `Music` | Game background music track transitions (Supercruise, Combat, Station, etc.). |
| `SendText` / `ReceiveText` | Transmit or receive chat messages across local, wing, or direct channels. |
| `DatalinkScan` | Scan target datalink beacon on megaship, outpost, or installation. |
| `DataScanned` | Download data packet from scanned data point. |
| `DatalinkVoucher` | Claim encoded data voucher at station. |
| `Scanned` | Ship scanned by police, pirate, or station security. |
| `CommitCrime` / `CrimeVictim` | Commit illegal act (speeding, assault, trespass) or get victimized. |
| `RebootRepair` | Execute Reboot/Repair sequence from ship right-hand panel. |
| `AfmuRepairs` | Use Auto Field-Maintenance Unit (AFMU) to repair an internal module. |
| `Synthesis` | Craft ammo, FSD boosts, or SRV fuel via synthesis panel. |
| `LaunchSRV` / `DockSRV` | Deploy or recover SRV from planetary hangar bay. |
| `LaunchFighter` / `DockFighter` | Deploy or recover Ship-Launched Fighter from fighter bay. |
| `FighterRebuilt` | Hangar finishes assembling replacement fighter hull. |
| `LaunchDrone` / `RepairDrone` | Fire limpet drone (collector, prospector, repair, hatch breaker). |
| `ProspectedAsteroid` | Prospector limpet impacts asteroid and analyzes composition. |
| `VehicleSwitch` | Switch control between mothership, fighter, and SRV. |
| `WingInvite` / `WingJoin` / `WingLeave` / `WingAdd` | Manage wing/team memberships. |
| `JoinACrew` / `QuitACrew` / `ChangeCrewRole` / `KickCrewMember` / `EndCrewSession` | Multicrew helm and gunner session events. |
| `JetConeBoost` | Supercharge FSD in neutron star or white dwarf jet cone. |
| `JetConeDamage` | Take FSD integrity damage from jet cone turbulence. |
| `CockpitBreached` | Canopy glass blows out under sustained hull damage. |
| `SelfDestruct` | Trigger ship or SRV self-destruct countdown. |
| `Resurrect` | Pay rebuy insurance cost after ship destruction. |
| `Promotion` | Achieve higher rank in Combat, Trade, Exploration, CQC, Soldier, or Exobiologist. |
| `ModuleInfo` | Game writes detailed internal module states. |
| `NpcCrewPaidWage` | NPC copilot draws percentage wage deduction from earnings. |
| `NpcCrewRank` | NPC copilot advances combat rank. |
| `SupercruiseDestinationDrop`| Drop out of supercruise at targeted waypoint. |
| `USSDrop` | Drop out of supercruise into an Unidentified Signal Source (USS). |
| `SystemsShutdown` / `Shutdown` | Thargoid EMP pulse causes complete system shutdown. |
| `ApproachSettlement` | Enter proximity of surface settlement or planetary port. |
| `CargoTransfer` | Transfer cargo canisters between ship and SRV. |
| `Resupply` | Full resupply completed at landing pad. |
| `ColonisationContribution` / `ColonisationConstructionDepot` | Deliver construction supplies to colonisation outpost depots. |
