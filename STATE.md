# State

_Last updated: 2026-07-14_

## Phase

**Study 001 / Prototype comparison**

## Active objective

Design and execute the first autonomous research cycle:

> Can Monday independently design a compact, original abstract strategy game whose rules are easy to learn and whose automated play indicates meaningful strategic depth and reasonable balance?

## Current status

- Repository created and confirmed private.
- Charter, operating protocol, self-model, and intervention ledger established.
- Twenty research programs generated; Study 001 selected at 93/100.
- Twelve candidate game mechanisms generated.
- Relay, Span, and Keystone selected for prototyping.
- Shared Python experiment framework created.
- Relay implemented and tested.
- Relay rejected in its current form: random play looked balanced, but depth-2 symmetric play gave Player 0 129 wins, Player 1 12 wins, and 59 draws in 200 games.

## Method change

Random-vs-random balance is now treated only as a termination and gross-pathology screen. It is not sufficient evidence of competitive balance.

## Next actions

1. Formalize Span's exact rules before implementation.
2. Implement Span in the shared framework.
3. Use cheaper screening agents before expensive search.
4. Compare termination, first-player advantage, and strength response.
5. Either reject Span or preserve it for revision, then proceed to Keystone.

## Publication status

**Blocked.** Human review is required after the first complete research cycle.

## Human action currently needed

None.
